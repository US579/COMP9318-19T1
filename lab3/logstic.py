import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def parse_data():
    data = np.loadtxt('./asset/x')
    dataMat = data[:, 0:-1]
    print(dataMat)

    classLabels = data[:, -1]
    dataMat = np.insert(dataMat, 0, 1, axis=1)
    print(dataMat)
    return dataMat, classLabels


def loss_funtion(dataMat, classLabels, weights):
    m, n = np.shape(dataMat)
    loss = 0.0
    for i in range(m):
        sum_theta_x = 0.0
        for j in range(n):
            sum_theta_x += dataMat[i, j] * weights.T[0, j]
        propability = sigmoid(sum_theta_x)
        loss += -classLabels[i, 0] * np.log(propability) - (1 - classLabels[i, 0]) * np.log(1 - propability)
    return loss


def grad_descent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)  #(m,n)
    #print(dataMatrix)
    labelMat = np.mat(classLabels).T
    m, n = np.shape(dataMatrix)
    weights = np.ones((n, 1))
    #print(weights)
    alpha = 0.01
    maxstep = 10000
    eps = 0.0001
    count = 0
    loss_array = []

    for i in range(maxstep):
        loss = loss_funtion(dataMatrix, labelMat, weights)

        h_theta_x = sigmoid(dataMatrix * weights)
        e = h_theta_x - labelMat
        new_weights = weights - alpha * dataMatrix.T * e
        new_loss = loss_funtion(dataMatrix, labelMat, new_weights)
        loss_array.append(new_loss)
        if abs(new_loss - loss) < eps:
            break
        else:
            weights = new_weights
            count += 1

    print("weights is: ", weights)

    return weights, loss_array

def plotloss(loss_array):
    n = len(loss_array)
    plt.xlabel("iteration num")
    plt.ylabel("loss")
    plt.scatter(range(1, n+1), loss_array)
    plt.show()

data, labels = parse_data()
r, loss_array = grad_descent(data, labels)
r = np.mat(r).transpose()
plotloss(loss_array)
