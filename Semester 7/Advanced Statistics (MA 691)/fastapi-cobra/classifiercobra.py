# Licensed under the MIT License - https://opensource.org/licenses/MIT

from sklearn import neighbors, tree, svm
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.naive_bayes import GaussianNB

import math
import numpy as np
import random
import logging
import numbers

logger = logging.getLogger("pycobra.classifiercobra")


class ClassifierCobra(BaseEstimator):
    def __init__(self, random_state=None, machine_list="basic"):
        self.random_state = random_state
        self.machine_list = machine_list

    def fit(self, X, y, default=True, X_k=None, X_l=None, y_k=None, y_l=None):
        X, y = check_X_y(X, y)
        self.X_ = X
        self.y_ = y
        self.X_k_ = X_k
        self.X_l_ = X_l
        self.y_k_ = y_k
        self.y_l_ = y_l
        self.estimators_ = {}

        try:
            if default:
                self.split_data()
                self.load_default(machine_list=self.machine_list)
                self.load_machine_predictions()
        except ValueError:
            return self
        return self

    def pred(self, X, M, info=False):
        select = {}
        for machine in self.estimators_:
            label = self.estimators_[machine].predict(X)
            select[machine] = set()
            for count in range(0, len(self.X_l_)):
                if self.machine_predictions_[machine][count] == label:
                    select[machine].add(count)

        points = []

        for count in range(0, len(self.X_l_)):
            row_check = 0
            for machine in select:
                if count in select[machine]:
                    row_check += 1
            if row_check == M:
                points.append(count)

        # if no points are selected, return 0
        if len(points) == 0:
            if info:
                logger.info("No points were selected, prediction is 0")
                return (0, 0)
            logger.info("No points were selected, prediction is 0")
            return 0

        classes = {}
        for label in np.unique(self.y_l_):
            classes[label] = 0

        for point in points:
            classes[self.y_l_[point]] += 1

        result = int(max(classes, key=classes.get))
        if info:
            return result, points
        return result

    def predict(self, X, M=None, info=False):
        X = check_array(X)

        if M is None:
            M = len(self.estimators_)
        if X.ndim == 1:
            return self.pred(X.reshape(1, -1), M=M)

        result = np.zeros(len(X))
        avg_points = 0
        index = 0
        for vector in X:
            if info:
                result[index], points = self.pred(
                    vector.reshape(1, -1), M=M, info=info)
                avg_points += len(points)
            else:
                result[index] = self.pred(vector.reshape(1, -1), M=M)
            index += 1

        if info:
            avg_points = avg_points / len(X_array)
            return result, avg_points
        return result

    def predict_proba(self, X, kernel=None, metric=None, bandwidth=1, **kwargs):
        probs = []
        for machine in self.estimators_:
            try:
                probs.append(self.estimators_[machine].predict_proba(X))
            except AttributeError:
                continue
        prob = np.mean(probs, axis=0)
        return prob

    def split_data(self, k=None, l=None, shuffle_data=True):
        if shuffle_data:
            self.X_, self.y_ = shuffle(
                self.X_, self.y_, random_state=self.random_state)

        if k is None and l is None:
            k = int(len(self.X_) / 2)
            l = int(len(self.X_))

        if k is not None and l is None:
            l = len(self.X_) - k

        if l is not None and k is None:
            k = len(self.X_) - l

        self.X_k_ = self.X_[:k]
        self.X_l_ = self.X_[k:l]
        self.y_k_ = self.y_[:k]
        self.y_l_ = self.y_[k:l]
        return self

    """
    The following machines are to be used based on the analysis done on 
    Google Colab - (mapped to symbolic representation)
    - Decision Tree Classifier - tree
    - K Nearest Neighbors - knn
    - Naive Bayes - naive_bayes
    - Support Vector Machines - svm
    - Random Forest - random_forest
    - Gradient Boosting - gdb
    - Logistic Regression - logreg
    - MLP Classifier - mlp
    """

    def load_default(self, machine_list="basic"):
        if machine_list == "basic":
            machine_list = ["logreg", "svm", "knn", "mlp"]
        if machine_list == "advanced":
            machine_list = [
                "gdb",
                "svm",
                "random_forest",
                "tree",
                "mlp",
                "logreg",
                "naive_bayes",
                "knn",
            ]

        for machine in machine_list:
            try:
                if machine == "gdb":
                    self.estimators_["gdb"] = GradientBoostingClassifier(
                        learning_rate=0.05, max_depth=2, n_estimators=50, min_samples_leaf=30, max_features='auto').fit(self.X_k_, self.y_k_)

                if machine == "svm":
                    self.estimators_["svm"] = svm.SVC(
                        C=0.01, kernel='linear').fit(self.X_k_, self.y_k_)

                if machine == "random_forest":
                    self.estimators_["random_forest"] = RandomForestClassifier(
                        max_depth=2, n_estimators=10, min_samples_leaf=10, max_features='auto').fit(self.X_k_, self.y_k_)

                if machine == "tree":
                    self.estimators_["tree"] = tree.DecisionTreeClassifier(
                        class_weight='balanced', max_depth=None, max_leaf_nodes=None, min_samples_leaf=21, min_samples_split=2).fit(self.X_k_, self.y_k_)

                if machine == "mlp":
                    self.estimators_["mlp"] = MLPClassifier(
                        max_iter=1000, learning_rate='constant', activation='tanh', learning_rate_init=0.1, alpha=0.1).fit(self.X_k_, self.y_k_)

                if machine == "logreg":
                    self.estimators_["logreg"] = LogisticRegression(
                        penalty='l2', class_weight='balanced', C=0.5).fit(self.X_k_, self.y_k_)

                if machine == "naive_bayes":
                    self.estimators_["naive_bayes"] = GaussianNB().fit(
                        self.X_k_, self.y_k_)

                if machine == "knn":
                    self.estimators_["knn"] = neighbors.KNeighborsClassifier(
                        n_neighbors=20, weights='uniform').fit(self.X_k_, self.y_k_)

            except ValueError:
                continue
        return self

    def load_machine(self, machine_name, machine):
        self.estimators_[machine_name] = machine
        return self

    def load_machine_predictions(self, predictions=None):
        self.machine_predictions_ = {}
        if predictions is None:
            for machine in self.estimators_:
                self.machine_predictions_[machine] = self.estimators_[machine].predict(
                    self.X_l_
                )
        return self

    def load_machine_proba_predictions(self, predictions=None):
        self.machine_proba_predictions_ = {}
        if predictions is None:
            for machine in self.estimators_:
                try:
                    self.machine_proba_predictions_[machine] = self.estimators_[
                        machine
                    ].predict_proba(self.X_l_)
                except AttributeError:
                    self.machine_proba_predictions_[machine] = self.estimators_[
                        machine
                    ].decision_function(self.X_l_)
        return self
