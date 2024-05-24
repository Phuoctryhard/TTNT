# Câu 2 (2 điểm): Cho không gian Oxyz với 10 điểm có tọa độ tương ứng (0,4,1), (4,1,0) (3,2,0),(2,3,2),(2,4,1) (2,3,4), (4,2,6), (4,1,2), (3,1,2) và (3,0,2)
import numpy as np


class KMeansClustering:
    def __init__(self, X, num_clusters=2):
        self.K = num_clusters
        self.max_iterations = 500
        self.num_examples, self.num_features = X.shape

    def distance(self, point, centroids):
        dist = np.sqrt(np.sum((point - centroids) ** 2, axis=1))
        return dist

    def initialize_random_centroids(self, X):
        centroids = np.zeros((self.K, self.num_features))
        for k in range(self.K):
            centroid = X[np.random.choice(range(self.num_examples))]
            centroids[k] = centroid
        return centroids

    def create_cluster(self, X, centroids):
        clusters = [[] for _ in range(self.K)]
        for point_idx, point in enumerate(X):
            closest_centroid = np.argmin(
                self.distance(point, centroids)
            )
            clusters[closest_centroid].append(point_idx)
        return clusters

    def calculate_new_centroids(self, cluster, X):
        centroids = np.zeros((self.K, self.num_features))
        for idx, cluster in enumerate(cluster):
            new_centroid = np.mean(X[cluster], axis=0)
            centroids[idx] = new_centroid
        return centroids

    def fit(self, X):
        centroids = self.initialize_random_centroids(X)
        for _ in range(self.max_iterations):
            clusters = self.create_cluster(X, centroids)
            previous_centroids = centroids
            centroids = self.calculate_new_centroids(clusters, X)
            diff = centroids - previous_centroids
            if not diff.any():
                break
        self.clusters = clusters
        self.centroids = centroids
        return centroids

    def predict(self, X):
        return self.clusters


X = [[0, 4, 1], [4, 1, 0], [3, 2, 0], [2, 3, 2], [2, 4, 1],
     [2, 3, 4], [4, 2, 6], [4, 1, 2], [3, 1, 2], [3, 0, 2]]


k = 2
kmean = KMeansClustering(X=np.asarray(X), num_clusters=k)
centroids = kmean.fit(np.asarray(X))
clusters = kmean.predict(np.asarray(X))
print(centroids)
print(clusters)
for i, cluster in enumerate(clusters):
    print("Cluster ", i + 1, ":")
    for value in cluster:
        print(X[value], " ")


# Kết quả

# (base) PS D:\nam3ki2\onthipython> python -u "d:\nam3ki2\onthipython\Kmean\phanvanhung.py"
# [[3.4 1.  1.2]
#  [2.  3.2 2.8]]

# phân nhóm
# [[1, 2, 7, 8, 9], [0, 3, 4, 5, 6]]
# Cluster  1 :
# [4, 1, 0]
# [3, 2, 0]
# [4, 1, 2]
# [3, 1, 2]
# [3, 0, 2]
# Cluster  2 :
# [0, 4, 1]
# [2, 3, 2]
# [2, 4, 1]
# [2, 3, 4]
# [4, 2, 6]
