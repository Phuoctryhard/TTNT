import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, adjusted_rand_score
from sklearn.preprocessing import LabelEncoder


def initialize_K_centroids(X, K):
    m, n = X.shape
    np.random.seed(123)
    k_rand = np.ones((K, n))
    k_rand = X[np.random.choice(range(len(X)), K, replace=False), :]
    return k_rand


def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        distance = np.linalg.norm(X[i] - centroids, axis=1)
        c[i] = np.argmin(distance)
    return c


def compute_means(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        points_belong_k = X[np.where(idx == k)]
        centroids[k] = np.mean(points_belong_k, axis=0, )
    return centroids


def find_k_means(X, K, max_iters=10):
    _, n = X.shape
    centroids = initialize_K_centroids(X, K)
    # centroid_history = np.zeros((max_iters, K, n))
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
    return centroids, idx


df = pd.read_csv(
    r'D:\\nam3ki2\\onthipython\\nguyenvanmanh\\input.csv', header=None)
X = np.array(df[[0, 1, 2, 3]])
K = 3


centroids, idx = find_k_means(X, K, max_iters=10)


# Khởi tạo một đối tượng LabelEncoder
label_encoder = LabelEncoder()


label_mapping = {"Iris-setosa": 2, "Iris-versicolor": 0, "Iris-virginica": 1}
labels_true = np.array(df[4].map(label_mapping))


print("Các điểm trọng tâm :", centroids)
print(centroids)
print(np.asarray(idx, int))


# Đánh giá độ chính xác bằng accuracy
accuracy = accuracy_score(labels_true, idx)
print("Tỷ lệ phân cụm đúng: {:.2%}".format(accuracy))


#  (2 điểm) Nếu sử dụng thuật toán k-means với k = 3 thì kết quả phân nhóm sẽ như thế nào?
# (Trọng tâm của các cụm, tỷ lệ phân cụm đúng, tiêu chí đánh giá việc phân cụm đúng là gì?).
