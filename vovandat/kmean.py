import numpy as np
import pandas as pd
from sklearn.metrics import davies_bouldin_score
class KMeans(object):
    def __init__(self, k, data, max_iter=10):
        self.cluster = k
        self.iter = max_iter
        self.data = np.array(data)
        self.centroids, self.idx = self.find_k_means(
            self.data, self.cluster, self.iter)

    def initialize_K_centroid(self, X, K):
        m, n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[np.random.choice(range(len(X)), K, replace=False), :]
        return k_rand

    def find_closest_centroid(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            if len(points_belong_k) > 0:
                centroids[k] = np.mean(points_belong_k, axis=0)
        return centroids

    def find_k_means(self, X, K, max_iters=10):
        n = X.shape[1]
        centroids = self.initialize_K_centroid(X, K)
        centroid_history = np.zeros((max_iters, K, n))
        for i in range(max_iters):
            idx = self.find_closest_centroid(X, centroids)
            centroids = self.compute_means(X, idx, K)
        return centroids, idx


# Load your data from 'Countries.csv'
df = pd.read_csv('D:\\nam3ki2\\onthipython\\vovandat\\Countries.csv')

# Instantiate your KMeans object and perform clustering
kmean = KMeans(5, np.array(df.iloc[:, 1:3]))

# Fetch the predicted clusters from your Kmean object
predicted_labels = kmean.idx

# Calculate the Davies-Bouldin Index
davies_bouldin = davies_bouldin_score(df.iloc[:, 1:3], predicted_labels) * 100

print("Tâm các cụm: ", kmean.centroids)
print("Các điểm phân cụm theo nhóm: ", kmean.idx)
print("Davies-Bouldin Index:", davies_bouldin)


# 3. Tiêu chí đánh giá việc phân cụm (viết bằng lời):
# Đánh giá tỷ lệ phân cụm bằng Index Davies-Bouldin Index Davies-Bouldin
# (Davies-Bouldin Index) là một độ đo được sử dụng để đánh giá hiệu suất của thuật toán phân cụm, như K-means. Độ đo này đo lường mức độ tách biệt giữa các cụm và đồng thời đo lường độ tương đồng bên trong mỗi cụm. Công thức tính Davies-Bouldin Index cho mỗi cụm được biểu diễn như sau:
# DB_i = (R_i + R_j) / D_i,j Trong đó: DB_i là giá trị Davies-Bouldin Index của cụm i. R_i là giá trị độ tương đồng trung bình của cụm i, được tính bằng cách tính trung bình khoảng cách từ mỗi điểm trong cụm i đến trung tâm của cụm i. R_j là giá trị độ tương đồng trung bình của cụm j, được tính bằng cách
# tính trung bình khoảng cách từ mỗi điểm trong cụm j đến trung tâm của cụm j. D_i,j là khoảng cách giữa trung tâm của cụm i và trung tâm của cụm j.
