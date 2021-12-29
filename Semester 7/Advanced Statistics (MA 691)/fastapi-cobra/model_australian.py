# model and path libraries
from pathlib import Path
import joblib

# data analysis libraries
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
import numpy as np
import pandas as pd
import pickle

# cobra library
import classifiercobra

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# ignore warnings
import warnings

warnings.filterwarnings("ignore")
# ---------------------------------------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve(strict=True).parent

australian_credit_train_data = BASE_DIR.joinpath("data/australian.dat")


def train():
    # cleaning of tha data before training -----------------------------------------------------------------

    # Reading the data into python
    df = pd.read_table(australian_credit_train_data, sep='\s+', header=None)
    df.columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7',
                  'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'Y']

    # Data Pre-processing
    # Drop 'Y' column from df and then make a new DataFrame = y
    x = df.drop('Y', axis=1)
    y = df['Y']

    # Decide feature importance using DecisionTreeClassifier
    pohon = DecisionTreeClassifier(class_weight='balanced', random_state=15)
    pohom = pohon.fit(x, y)
    importances = pohon.feature_importances_

    # Meta-transformer for selecting features based on importance weights.
    # Transforms x to x_new, with attributes based on importance, using median as a thershold.
    fs = SelectFromModel(pohon, threshold='median', prefit=True)

    # Store fs for tranforming input data later on
    joblib.dump(fs, Path(BASE_DIR).joinpath("australian_fs.joblib"))

    x_new = fs.transform(x)
    x_new = pd.DataFrame(x_new)

    # Storing final data for future use
    joblib.dump(x_new, Path(BASE_DIR).joinpath("australian_x_new.joblib"))

    # Create dummies for categorial features.
    x_dummy = pd.get_dummies(x_new[[2, 3, 4]], columns=[2, 3, 4])

    # Perform a row normalization on the conitnuous data
    x_norm = pd.DataFrame(normalize(x_new[[0, 1, 5, 6]]))

    # Use PCA to make an orthogonal transformation that converts a set of correlated variables to a set of uncorrelated variables
    pca = PCA(n_components=2)
    pca.fit(x_norm)

    # Store pca for transforming input data later on
    joblib.dump(pca, Path(BASE_DIR).joinpath("australian_pca.joblib"))

    x_pca = pca.transform(x_norm)
    x_pca = pd.DataFrame(x_pca)
    x_pca = pd.concat([x_pca, x_dummy], axis=1)

    # Retraining the model using 100% data
    # Using the COBRA algorithm with advanced set of machine lists.
    cobra = classifiercobra.ClassifierCobra(machine_list="advanced")

    # Training the model on 100% Data available
    cobra_model = cobra.fit(x_pca, y)

    accuracy_values = cross_val_score(
        cobra_model, x_pca, y, cv=10, scoring="f1_weighted")
    print("\nAccuracy values for 10-fold Cross Validation:\n", accuracy_values)
    print("\nFinal Average Accuracy of the COBRA model:",
          round(accuracy_values.mean(), 4))

    # Dumping the trained model for future use
    joblib.dump(cobra, Path(BASE_DIR).joinpath("australian_cobra.joblib"))


def predict_australian(loan_details):
    # File paths for all joblib files
    model_file = Path(BASE_DIR).joinpath("australian_cobra.joblib")
    fs_file = Path(BASE_DIR).joinpath("australian_fs.joblib")
    pca_file = Path(BASE_DIR).joinpath("australian_pca.joblib")
    x_new_file = Path(BASE_DIR).joinpath("australian_x_new.joblib")

    # The model has not been trained - so train it
    if not model_file.exists():
        train()
        model_file = Path(BASE_DIR).joinpath("australian_cobra.joblib")

    # Assumning loan details is a dataframe with only 1 row ...
    # This is valid because the API will only accept 1 set of values at a time
    x = loan_details

    # Using fs to transform x
    fs = joblib.load(fs_file)
    x_new = fs.transform(x)
    x_new = pd.DataFrame(x_new)

    x_new_stored = joblib.load(x_new_file)
    x_new_stored.iloc[0] = x_new.values[0].tolist()

    # Create dummies for categorial features.
    x_dummy = pd.get_dummies(x_new_stored[[2, 3, 4]], columns=[2, 3, 4])
    x_dummy = x_dummy.head(1)

    # Perform a row normalization on the conitnuous data
    x_norm = pd.DataFrame(normalize(x_new[[0, 1, 5, 6]]))

    # Using pca to transform x_norm
    pca = joblib.load(pca_file)
    x_pca = pca.transform(x_norm)
    x_pca = pd.DataFrame(x_pca)
    x_pca = pd.concat([x_pca, x_dummy], axis=1)

    # Using trained model with COBRA to make a prediction
    cobra = joblib.load(model_file)
    prediction = cobra.predict(x_pca)

    return prediction


def predict_helper_australian(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12, param13, param14):
    new_loan_application = pd.DataFrame(
        data=[
            [param1, param2, param3, param4, param5, param6, param7,
                param8, param9, param10, param11, param12, param13, param14]
        ],
        columns=[
            "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14"
        ],
    )

    prediciton = predict_australian(new_loan_application)[0]
    return prediciton


'''
# How to use the predict function? --- code below.
new_loan_application = pd.DataFrame(
    data=[
        [0, 21.67, 11.5, 1, 5, 3, 0, 1, 1, 11, 1, 2, 0, 1]
    ],
    columns=[
        "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14"
    ],
)

print(new_loan_application)
print(predict_australian(loan_details=new_loan_application))
'''

'''
# How to use the predict_helper function? --- code below.

# get output of 1.0 - credit card application approved
print(predict_helper_australian(0, 21.67, 11.5, 1, 5, 3, 0, 1, 1, 11, 1, 2, 0, 1))

# get output of 0.0 - credit card application rejected
print(predict_helper_australian(1, 22.08, 11.46,
      2, 4, 4, 1.585, 0, 0, 0, 1, 2, 100, 1213))
'''
