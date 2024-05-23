import numpy as np
import pandas as pd
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


# Load data from input.csv
x = []
y = []
with open(r"D:\nam3ki2\onthipython\dehongngan\input.csv", 'r', encoding='utf-8') as f:
    for val in f.readlines():
        l = val.strip()
        spl = l.split(",")
        if len(spl) > 1:
            x.append([float(i) for i in spl[:-1]])
            if spl[-1] == "Iris-setosa":
                y.append(0)
            elif spl[-1] == "Iris-versicolor":
                y.append(1)
            elif spl[-1] == "Iris-virginica":
                y.append(2)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=12, stratify=y)

# Convert data to numpy arrays and add bias term
x_train = np.array(X_train).T
y_train = np.array(y_train)
x_train = np.vstack((np.ones((1, x_train.shape[1])), x_train))

# Initialize weights and train the model
w_init = np.zeros((x_train.shape[0], len(np.unique(y_train))))
alpha = 0.1
w = logistic_softmax_regression(x_train, y_train, w_init, alpha)

# Make predictions on training set
y_train_pred = np.argmax(softmax(np.dot(w[-1].T, x_train)), axis=0)

# Make predictions on test set
x_test = np.array(X_test).T
x_test = np.vstack((np.ones((1, x_test.shape[1])), x_test))
y_test_pred = np.argmax(softmax(np.dot(w[-1].T, x_test)), axis=0)

# Convert predictions to labels
pred_labels = []
for i in range(len(y_test_pred)):
    if y_test_pred[i] == 0:
        pred_labels.append('Iris-setosa')
    elif y_test_pred[i] == 1:
        pred_labels.append('Iris-versicolor')
    else:
        pred_labels.append('Iris-virginica')

# Write predictions to output.csv
output_data = {"Predictions": pred_labels}
output_df = pd.DataFrame(output_data)
output_df.to_csv("output.csv", index=False)
