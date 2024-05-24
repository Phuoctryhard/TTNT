import numpy as np
import pandas as pd
import math
from sklearn import datasets

# Load input data
# Assuming space-separated values
input = pd.read_csv(
    "D:\\nam3ki2\\onthipython\\Regression\\input.csv", delim_whitespace=True)
Y = input.iloc[:, -1]  # Assuming the class labels are in the last column
X = input.iloc[:, :-1]

X = np.asarray(X)
Y = np.asarray(Y)
num_class = len(np.unique(Y))
classes = {value: idx for idx, value in enumerate(np.unique(Y))}


class LogisticReg:
    def __init__(self, lr, iters, num_class, classes):
        self.lr = lr
        self.num_class = num_class
        self.iters = iters
        self.classes = classes

    def sigmoid(self, Z):
        Z = Z.astype(float)
        return 1 / (1 + np.exp(-Z))

    def convert_labels(self, Y):
        res = np.zeros((Y.shape[0], self.num_class))
        for i, value in enumerate(Y):
            res[i][self.classes[value]] = 1
        return res

    def fit(self, X, Y):
        X = np.insert(X, 0, 1, axis=1)  # add Bias
        self.m, self.n = X.shape
        self.X = X
        self.Y = self.convert_labels(Y)

        limit = np.sqrt(2 / self.m)
        self.W = np.random.uniform(-limit, limit, (self.n, self.num_class))

        for _ in range(self.iters):
            y_preds = self.sigmoid(self.X.dot(self.W))
            gradients = self.X.T.dot(y_preds - self.Y)
            self.W -= self.lr * gradients

        return self

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        probas = self.sigmoid(X.dot(self.W))
        return np.argmax(probas, axis=1)


def accuracy(y_pred, y_actual, classes):
    right = 0
    for index in range(len(y_pred)):
        if y_pred[index] == classes[y_actual[index]]:
            right += 1
    return right / len(y_pred)


LR = LogisticReg(0.0001, 500, num_class, classes)
LR.fit(X, Y)
y_pred = LR.predict(X)

print("Accuracy:", accuracy(y_pred, Y, classes))
