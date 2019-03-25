
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
    lablMat = np.mat(labels).transpose()
    for i in range(num_epochs):
        theta = sigmoid(dataMat * weights)
        e = theta - lablMat
        new_weight = weights - learning_rate*dataMat.T*e
        weights = new_weight
        #print(weights)
    #print(weights)
    print(weights.A1)


logistic_regression(data,labels,weights,num_epochs,learning_rate)

