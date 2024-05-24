import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score


def initialize_K_centroids(X, K):
    m, n = X.shape
    k_rand = np.ones((K, n))
    k_rand = X[np.random.choice(range(len(X)), K, replace=False), :]
    return k_rand


def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        # compute distances
        distances = np.linalg.norm(X[i] - centroids, axis=1)
        c[i] = np.argmin(distances)
    return c


def compute_means(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        points_belong_k = X[np.where(idx == k)]
        centroids[k] = np.mean(points_belong_k, axis=0,)
    return centroids


def find_k_means(X, K, max_iters=10):
    _, n = X.shape
    centroids = initialize_K_centroids(X, K)
    centroid_history = np.zeros((max_iters, K, n))
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
    return centroids, idx


# data = pd.read_csv(r'D:\nam3ki2\onthipython\dehongngan\Countries.csv')
# Chuyển dữ liệu DataFrame thành mảng NumPy
# X = data.iloc[:, 1:3].values


XX = [[0, 4], [1, 3], [4, 0], [3, 1], [2, 1], [2, 3]]
X = np.array(XX)
K = 3
# tính idn

centroids, idx = find_k_means(X, K, max_iters=10)

print(centroids)
print(idx)


# data_with_clusters = data.copy()
# data_with_clusters['Clusters'] = idx

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

# print(data_with_clusters)
