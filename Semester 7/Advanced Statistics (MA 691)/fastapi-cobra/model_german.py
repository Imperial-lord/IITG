# model and path libraries
from pathlib import Path
import joblib

# data analysis libraries
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
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

german_credit_train_data = BASE_DIR.joinpath("data/german.csv")


def train():
    # cleaning of tha data before training -----------------------------------------------------------------

    # Reading the data into python
    df = pd.read_csv(german_credit_train_data)
    df = df.drop_duplicates()

    SelectedColumns = [
        "checkingstatus",
        "history",
        "purpose",
        "savings",
        "employ",
        "status",
        "others",
        "property",
        "otherplans",
        "housing",
        "foreign",
        "age",
        "amount",
        "duration",
    ]

    # Selecting final columns
    DataForML = df[SelectedColumns]

    # Saving this final data for reference during deployment
    joblib.dump(DataForML, Path(BASE_DIR).joinpath(
        "german_data_for_ml.joblib"))

    """# Data Pre-processing for Machine Learning
    ##### 1. Converting Ordinal variables to numeric using business mapping
    """

    # Treating the Ordinal variable first
    DataForML["employ"].replace(
        {"A71": 1, "A72": 2, "A73": 3, "A74": 4, "A75": 5}, inplace=True
    )

    # Converting the binary nominal variable to numeric using 1/0 mapping
    # Treating the binary nominal variable

    DataForML["foreign"].replace({"A201": 1, "A202": 0}, inplace=True)

    """##### 2. Converting nominal variables to numeric using get_dummies()"""

    # Treating all the nominal variables at once using dummy variables
    DataForML_Numeric = pd.get_dummies(DataForML)

    # Adding Target Variable to the data
    DataForML_Numeric["GoodCredit"] = df["GoodCredit"]

    # Separate Target Variable and Predictor Variables
    TargetVariable = "GoodCredit"
    Predictors = [
        "employ",
        "foreign",
        "age",
        "amount",
        "duration",
        "checkingstatus_A11",
        "checkingstatus_A12",
        "checkingstatus_A13",
        "checkingstatus_A14",
        "history_A30",
        "history_A31",
        "history_A32",
        "history_A33",
        "history_A34",
        "purpose_A40",
        "purpose_A41",
        "purpose_A410",
        "purpose_A42",
        "purpose_A43",
        "purpose_A44",
        "purpose_A45",
        "purpose_A46",
        "purpose_A48",
        "purpose_A49",
        "savings_A61",
        "savings_A62",
        "savings_A63",
        "savings_A64",
        "savings_A65",
        "status_A91",
        "status_A92",
        "status_A93",
        "status_A94",
        "others_A101",
        "others_A102",
        "others_A103",
        "property_A121",
        "property_A122",
        "property_A123",
        "property_A124",
        "otherplans_A141",
        "otherplans_A142",
        "otherplans_A143",
        "housing_A151",
        "housing_A152",
        "housing_A153",
    ]

    X = DataForML_Numeric[Predictors].values
    y = DataForML_Numeric[TargetVariable].values

    # Splitting the data into training and testing set

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=428
    )

    # Normalization of data
    PredictorScaler = MinMaxScaler()

    # Storing the fit object for later reference
    PredictorScalerFit = PredictorScaler.fit(X)

    # Generating the standardized values of X
    X = PredictorScalerFit.transform(X)

    # Split the data into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Separate Target Variable and Predictor Variables
    TargetVariable = "GoodCredit"

    # Selecting the final set of predictors for the deployment
    Predictors = [
        "employ",
        "age",
        "amount",
        "duration",
        "checkingstatus_A11",
        "checkingstatus_A12",
        "checkingstatus_A13",
        "checkingstatus_A14",
        "history_A30",
        "history_A31",
        "history_A32",
        "history_A33",
        "history_A34",
        "purpose_A40",
        "purpose_A41",
        "purpose_A410",
        "purpose_A42",
        "purpose_A43",
        "purpose_A44",
        "purpose_A45",
        "purpose_A46",
        "purpose_A48",
        "purpose_A49",
        "savings_A61",
        "savings_A62",
        "savings_A63",
        "savings_A64",
        "savings_A65",
        "status_A91",
        "status_A92",
        "status_A93",
        "status_A94",
    ]

    X = DataForML_Numeric[Predictors].values
    y = DataForML_Numeric[TargetVariable].values

    ### Normalization of data ###
    PredictorScaler = MinMaxScaler()
    PredictorScalerFit = PredictorScaler.fit(X)

    # Store predictor scaler fir for future use
    joblib.dump(PredictorScalerFit, Path(BASE_DIR).joinpath(
        "german_predictor_scaler_fit.joblib"))

    X = PredictorScalerFit.transform(X)

    # Retraining the model using 100% data
    # Using the COBRA algorithm with advanced set of machine lists.
    cobra = classifiercobra.ClassifierCobra(machine_list="advanced")

    # Training the model on 100% Data available
    cobra_model = cobra.fit(X, y)
    accuracy_Values = cross_val_score(
        cobra_model, X, y, cv=10, scoring="f1_weighted")
    print("\nAccuracy values for 10-fold Cross Validation:\n", accuracy_Values)
    print("\nFinal Average Accuracy of the model:",
          round(accuracy_Values.mean(), 4))

    # Dumping the trained model for future use
    joblib.dump(cobra, Path(BASE_DIR).joinpath("german_cobra.joblib"))


def predict_german(loan_details):
    model_file = Path(BASE_DIR).joinpath("german_cobra.joblib")
    data_for_ml_file = Path(BASE_DIR).joinpath("german_data_for_ml.joblib")
    predictor_scaler_fit_file = Path(BASE_DIR).joinpath(
        "german_predictor_scaler_fit.joblib")

    # the model has not been trained.
    if not model_file.exists():
        train()
        model_file = Path(BASE_DIR).joinpath("german_cobra.joblib")

    num_inputs = loan_details.shape[0]

    # Appending the new data with the Training data
    DataForML = joblib.load(data_for_ml_file)
    loan_details = loan_details.append(DataForML)

    # Treating the Ordinal variable first
    loan_details["employ"].replace(
        {"A71": 1, "A72": 2, "A73": 3, "A74": 4, "A75": 5}, inplace=True
    )

    # Generating dummy variables for rest of the nominal variables
    loan_details = pd.get_dummies(loan_details)

    # Maintaining the same order of columns as it was during the model training
    Predictors = [
        "employ",
        "age",
        "amount",
        "duration",
        "checkingstatus_A11",
        "checkingstatus_A12",
        "checkingstatus_A13",
        "checkingstatus_A14",
        "history_A30",
        "history_A31",
        "history_A32",
        "history_A33",
        "history_A34",
        "purpose_A40",
        "purpose_A41",
        "purpose_A410",
        "purpose_A42",
        "purpose_A43",
        "purpose_A44",
        "purpose_A45",
        "purpose_A46",
        "purpose_A48",
        "purpose_A49",
        "savings_A61",
        "savings_A62",
        "savings_A63",
        "savings_A64",
        "savings_A65",
        "status_A91",
        "status_A92",
        "status_A93",
        "status_A94",
    ]

    # Generating the input values to the model
    X = loan_details[Predictors].values[0:num_inputs]

    # Generating the standardized values of X since it was done while model training also
    PredictorScalerFit = joblib.load(predictor_scaler_fit_file)
    X = PredictorScalerFit.transform(X)

    cobra = joblib.load(model_file)

    # Genrating Predictions
    prediction = cobra.predict(X)
    predicted_status = pd.DataFrame(prediction, columns=["Predicted Status"])
    return predicted_status


def predict_helper_german(
    employ,
    age,
    amount,
    duration,
    checkingstatus,
    history,
    purpose,
    savings,
    status,
):
    new_loan_application = pd.DataFrame(
        data=[
            [
                employ,
                age,
                amount,
                duration,
                checkingstatus,
                history,
                purpose,
                savings,
                status,
            ]
        ],
        columns=[
            "employ",
            "age",
            "amount",
            "duration",
            "checkingstatus",
            "history",
            "purpose",
            "savings",
            "status",
        ],
    )

    predictions = predict_german(loan_details=new_loan_application)
    return predictions.to_json()


'''
# How to use the predict function? --- code below.
new_loan_application = pd.DataFrame(
    data=[
        ["A72", 40, 8951, 24, "A12", "A32", "A43", "A61", "A92"],
        ["A73", 53, 4870, 24, "A11", "A33", "A40", "A61", "A93"],
    ],
    columns=[
        "employ",
        "age",
        "amount",
        "duration",
        "checkingstatus",
        "history",
        "purpose",
        "savings",
        "status",
    ],
)

print(new_loan_application)
print(predict_german(loan_details=new_loan_application))
'''

'''
# How to use the predict_helper function? --- code below.

# get output of 1.0 - credit card application approved
print(predict_helper_german("A73", 53, 4870,
      24, "A11", "A33", "A40", "A61", "A93"))

# get output of 0.0 - credit card application rejected
print(predict_helper_german("A72", 40, 8951,
      24, "A12", "A32", "A43", "A61", "A92"))
'''
