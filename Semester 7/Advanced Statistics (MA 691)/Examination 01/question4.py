import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris, load_breast_cancer, load_wine


def get_class_levels(data):
    return len(np.unique(data["target"]))


iris = load_iris()
class_levels = get_class_levels(iris)
kmeans = KMeans(n_clusters=class_levels, random_state=0).fit(iris["data"])
gmm = GaussianMixture(n_components=class_levels).fit(iris["data"])
print("GMM on Iris dataset")
print(gmm.means_, gmm.weights_)
print("KMeans on Iris dataset")
print(kmeans.labels_)

wine = load_wine()
class_levels = get_class_levels(wine)
kmeans = KMeans(n_clusters=class_levels, random_state=0).fit(wine["data"])
gmm = GaussianMixture(n_components=class_levels).fit(wine["data"])
print("GMM on wine dataset")
print(gmm.means_, gmm.weights_)
print("KMeans on Iris dataset")
print(kmeans.labels_)

breast_cancer = load_breast_cancer()
class_levels = get_class_levels(breast_cancer)
kmeans = KMeans(n_clusters=class_levels, random_state=0).fit(breast_cancer["data"])
gmm = GaussianMixture(n_components=class_levels).fit(breast_cancer["data"])
print("GMM on breast cancer dataset")
print(gmm.means_, gmm.weights_)
print("KMeans on Iris dataset")
print(kmeans.labels_)
