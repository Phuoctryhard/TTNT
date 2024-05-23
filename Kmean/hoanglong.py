import numpy as np
import matplotlib.pyplot as plt
import csv

def data():
    X = []
    with open('D:\\nam3ki2\\onthipython\\Kmean\\Countries.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for line in reader:
            _, x, y = line
            x, y = map(float, [x, y])
            X.append([x, y])

    return np.array(X)


def plot(X, Y=[], centers=[]):
    colors = ['red', 'green', 'blue', 'purple', 'yellow']
    for idx, p in enumerate(X):
        if len(Y) < 1:
            plt.plot(p[0], p[1], marker="o", markersize=5, color='blue')
        else:
            plt.plot(p[0], p[1], marker="o", markersize=5,
                     color=colors[int(Y[idx])])

    if len(centers > 0):
        for idx, c in enumerate(centers):
            plt.plot(c[0], c[1], marker="x", markersize=10)
    plt.show()


def dist(a, b, norm=2):
    # print(a, b)
    return np.linalg.norm(a - b, norm)


def kmeans(X, k=5, norm=2, max_iter=10):
    centers = X[np.random.randint(0, X.shape[0], size=k)]
    labels = np.zeros(X.shape[0])

    last_labels = np.ones(X.shape[0])

    iter = 0
    while iter < max_iter or (last_labels != labels).all():
        last_labels = labels[:]
        for i in range(X.shape[0]):
            l = min(range(centers.shape[0]), key=lambda c: dist(X[i], centers[c],
                                                                norm))
            labels[i] = l

        dis = [[] for _ in range(k)]
        for i in range(X.shape[0]):
            dis[int(labels[i])].append(X[i])

        for c in range(k):
            if len(dis[c]) < 1:
                continue
            centers[c] = np.mean(dis[c], axis=0)

        iter += 1
    for i in range(X.shape[0]):
        l = min(range(centers.shape[0]),
                key=lambda c: dist(X[i], centers[c], norm))
        labels[i] = l
    return centers, labels


def accuracy(true_labels, predicted_labels):
    correct = np.sum(true_labels == predicted_labels)
    total = len(true_labels)
    return (correct / total) * 100


X = data()
centers, labels = kmeans(X)
print(centers)
plot(X, labels, centers)

# Assuming you have true labels available
