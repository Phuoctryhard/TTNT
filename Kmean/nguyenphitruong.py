import numpy as np
import pandas as pd


def initialize_K_Centroids(X, K):
    m, n = X.shape
    k_rand = np.zeros((K, n))
    k_rand = X[np.random.choice(range(len(X)), K, replace=False), :]
    return k_rand


def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        distances = np.linalg.norm(X[i] - centroids, axis=1)
        c[i] = np.argmin(distances)
    return c


def compute_means(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        points_belong_k = X[np.where(idx == k)]
        centroids[k] = np.mean(points_belong_k, axis=0)
    return centroids


def find_k_mean(X, K, max_iters=100):
    _, n = X.shape
    centroids = initialize_K_Centroids(X, K)
    centroid_history = np.zeros((max_iters, K, n))
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        centroid_history[i] = centroids
    return centroids, idx


if __name__ == "__main__":
    df = pd.read_csv("D:\\nam3ki2\\onthipython\\Kmean\\input.csv")
    print(df.shape)
    X = df.iloc[:, :-1].values
    print(X.shape)
    centroids, idx = find_k_mean(X, 3, max_iters=50)
    print(idx)
    print("Centroids: ")
    print(centroids)
    data_with_clusters = df.copy()
    data_with_clusters['Clusters'] = idx
    print(data_with_clusters)
    # data_with_clusters.to_csv("output.csv", sep=',', header=False, index=True)


# kết quả
# (89, 5)
# (89, 4)
# [2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.
#  2. 2. 2. 2. 2. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
#  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 1. 1. 0. 0. 1. 1. 1. 1. 1.
#  0. 1. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 0.]
# Centroids:
# [[5.92368421 2.77894737 4.40789474 1.43157895]
#  [6.83636364 3.09090909 5.67727273 2.08181818]
#  [4.97241379 3.37586207 1.47586207 0.25172414]]
#     5.4  3.4  1.7  0.2     Iris-setosa  Clusters
# 0   5.1  3.7  1.5  0.4     Iris-setosa       2.0
# 1   4.6  3.6  1.0  0.2     Iris-setosa       2.0
# 2   5.1  3.3  1.7  0.5     Iris-setosa       2.0
# 3   4.8  3.4  1.9  0.2     Iris-setosa       2.0
# 4   5.0  3.0  1.6  0.2     Iris-setosa       2.0
# ..  ...  ...  ...  ...             ...       ...
# 84  6.7  3.0  5.2  2.3  Iris-virginica       1.0
# 85  6.3  2.5  5.0  1.9  Iris-virginica       0.0
# 86  6.5  3.0  5.2  2.0  Iris-virginica       1.0
# 87  6.2  3.4  5.4  2.3  Iris-virginica       1.0
# 88  5.9  3.0  5.1  1.8  Iris-virginica       0.0
