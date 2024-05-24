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


data = pd.read_csv(r'D:\nam3ki2\onthipython\dehongngan\Countries.csv')

# Chuyển dữ liệu DataFrame thành mảng NumPy
X = data.iloc[:, 1:3].values
K = 5
centroids, idx = find_k_means(X, K, max_iters=10)
# in ra trọng tâm cụm
print(centroids)

data_with_clusters = data.copy()
data_with_clusters['Clusters'] = idx

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(data_with_clusters)

# in ra độ chính xác

# đo độ tương phản của mỗi cụm có phân tách tốt hay không
# Một Silhouette Score cao (gần 1) cho thấy mỗi điểm dữ liệu trong một cụm gần các điểm dữ liệu khác trong cùng cụm và xa các điểm dữ liệu trong các cụm khác.
silhouette_avg = silhouette_score(X, idx)
print("Silhouette Score:", silhouette_avg)
# Vẽ biểu đồ phân cụm
plt.figure(figsize=(8, 6))
plt.scatter(X[idx == 0, 0], X[idx == 0, 1], s=50, c='red', label='Cluster 0')
plt.scatter(X[idx == 1, 0], X[idx == 1, 1], s=50, c='blue', label='Cluster 1')
plt.scatter(X[idx == 2, 0], X[idx == 2, 1], s=50, c='green', label='Cluster 2')
plt.scatter(X[idx == 3, 0], X[idx == 3, 1],
            s=50, c='purple', label='Cluster 3')
plt.scatter(X[idx == 4, 0], X[idx == 4, 1],
            s=50, c='orange', label='Cluster 4')
plt.scatter(centroids[:, 0], centroids[:, 1], s=200,
            c='black', marker='X', label='Centroids')
plt.title('Clustering of Countries')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Hiển thị Silhouette Score trên biểu đồ
plt.text(plt.xlim()[0] + 0.05, plt.ylim()[1] - 0.1,
         'Silhouette Score: {:.2f}'.format(silhouette_avg), fontsize=12)
plt.show()


# 3. Tiêu chí đánh giá việc phân cụm (viết bằng lời):

# Tiêu chí đánh giá việc phân cụm bằng K-means bao gồm:
# Độ đo khoảng cách giữa các điểm dữ liệu trong cùng một cụm phải gần nhau nhất có thể.
# Độ đồng nhất của các điểm dữ liệu trong cùng một cụm. -
# Độ phân tách của các điểm dữ liệu giữa các cụm khác nhau.
# Số lượng cụm, phải đủ lớn để phân biệt đủ các cụm khác nhau nhưng cũng không quá lớn để
# tránh việc quá phân rã các cụm.
# Với các tiêu chí này, chúng ta có thể đánh giá hiệu quả của phương pháp phân cụm bằng K-means và
# điều chỉnh các tham số để đạt được kết quả phân cụm tốt nhất
