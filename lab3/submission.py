
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file='./asset/a'

## Read in the Data...
raw_data = pd.read_csv(data_file, sep=',')
labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)
## Fixed Parameters. Please do not change values of these parameters...
weights = np.zeros(3) # We compute the weight for the intercept as well...
#print(weights)
num_epochs = 50000
learning_rate = 50e-5
print(weights)

def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
    dataMat = np.insert(data,0,1,axis=1)
    lablMat = np.mat(labels).T
    for i in range(num_epochs):
        error = sigmoid(dataMat*weights) - lablMat
        weights = weights - learning_rate * dataMat.T*error
    #print(np.array(for i in weights.T[0]))
    return np.array(weights.T.tolist()[0])


weights = logistic_regression(data,labels,weights,num_epochs,learning_rate)


def plotBestFit(weights,dataMat,labelMat):
    n=np.shape(dataMat)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if labelMat[i]==1:
            xcord1.append(dataMat[i][0])
            ycord1.append(dataMat[i][1])
        else:
            xcord2.append(dataMat[i][0])
            ycord2.append(dataMat[i][1])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=np.arange(-3,3,0.1)
    y=(-weights[0,0]-weights[1,0]*x)/weights[2,0] #matix
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

plotBestFit(weights,data,labels)