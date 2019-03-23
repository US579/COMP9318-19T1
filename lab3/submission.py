
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

def signoid(inX):
    return 1.0 / (1 + np.exp(-inX))

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function

    print(data)

data_file='./asset/a'

## Read in the Data...
raw_data = pd.read_csv(data_file, sep=',')
labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)

print(raw_data.head())
print(data)
## Fixed Parameters. Please do not change values of these parameters...
weights = np.zeros(3) # We compute the weight for the intercept as well...
print(weights)
num_epochs = 50000
learning_rate = 50e-5