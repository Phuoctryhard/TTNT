import numpy as np
import pandas as pd
from numpy import genfromtxt
from sklearn.model_selection import train_test_split


def softmax(z):
    e_z = np.exp(z - np.max(z, axis=0))
    return e_z / np.sum(e_z, axis=0)


def logistic_softmax_regression(X, y, w_init, alpha, tol=1e-4, loop=10000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    K = len(np.unique(y))
    count = 0
    check_w = 20
    while count < loop:
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = np.eye(K)[:, y[i]].reshape(K, 1)
            zi = softmax(np.dot(w[-1].T, xi))
            w_new = w[-1] + alpha * np.dot(xi, (yi - zi).T)
            count += 1
            if count % check_w == 0:
                if np.linalg.norm(w_new - w[-check_w]) < tol:
                    return w
            w.append(w_new)
    return w


test = []
with open(r"D:\nam3ki2\onthipython\dehongngan\output.csv") as f:
    for val in f.readlines():
        l = val.strip()
        spl = l.split(",")
        if len(spl) > 1:
            test.append([float(i) for i in spl[:]])
test = np.array(test).T
test = np.vstack((np.ones((1, test.shape[1])), test))
x = []
y = []
with open(r"D:\nam3ki2\onthipython\dehongngan\input.csv") as f:
    for val in f.readlines():
        l = val.strip()
        spl = l.split(",")
        if len(spl) > 1:
            x.append([float(i) for i in spl[:-1]])
            if spl[-1] == "Iris-setosa":
                y.append(0)
            if spl[-1] == "Iris-versicolor":
                y.append(1)
            if spl[-1] == "Iris-virginica":
                y.append(2)
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=12, stratify=y)
x = np.array(x).T
y = np.array(y)
x = np.vstack((np.ones((1, x.shape[1])), x))
w = logistic_softmax_regression(x, y, np.zeros(
    (x.shape[0], len(np.unique(y)))), alpha=0.1)
y_train_pred = np.argmax(softmax(np.dot(w[-1].T, x)), axis=0)
y_train_pred
y_test_pred = np.argmax(softmax(np.dot(w[-1].T, test)), axis=0)
# print(y_test_pred)
for i in range(len(y_test_pred)):
    if y_test_pred[i] == 0:
        print('Iris-setosa')
    elif y_test_pred[i] == 1:
        print('Iris-versicolor')
    else:
        print('Iris-virginica')
