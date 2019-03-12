# COMP9318-19T1
## About

### LAB1

* Q1 Bisection method

* Q2 Newton method

* Q3 token = ['1', '[', '2', '[', '3', '4', '5', ']', '6', '[', '7', '8', '[', '9', ']', '10', '[', '11', '12', ']', ']', '13', ']']

Seen token as a tree and every number behind '[' is the parent of the number benhind next '[', so the main tree parent node is '1' and the second layer parent nodes is '2' '6' '10'

### LAB2
* Optimal binning algorithm using dynamic programming

Error Sum of Squares (SSE)

SSE is the sum of the squared differences between each observation and its group's mean. It can be used as a measure of variation within a cluster. If all cases within a cluster are identical the SSE would then be equal to 0.

The formula for SSE is:

<a href="https://www.codecogs.com/eqnedit.php?latex=SSE&space;=&space;\sum_{i=1}^{n}\left&space;(&space;x_{i}&space;\right&space;-\bar{x})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SSE&space;=&space;\sum_{i=1}^{n}\left&space;(&space;x_{i}&space;\right&space;-\bar{x})^2" title="SSE = \sum_{i=1}^{n}\left ( x_{i} \right -\bar{x})^2" /></a>

Where n is the number of observations xi is the value of the ith observation and 0 is the mean of all the observations. This can also be rearranged to be written as seen in J.H. Ward's paper.

Recurisive method will compute many times, although its space complicity is lower than dynamic programmaing.

`import numpy as np
 def sse(arr):
    if len(arr) == 0: # deal with arr == []
        return 0.0
    avg = np.average(arr)
    val = sum( [(x-avg)*(x-avg) for x in arr] )
    return val
LARGE_NUM = 1000000000.0
def v_opt_rec(xx, b):
    mincost = LARGE_NUM
    n = len(xx) 
    # check boundary condition:
    if n < b:
        return LARGE_NUM + 1
    elif b == 1:
        return sse(xx)
    else:  # the general case
        for t in range(n):
            prefix = xx[0 : t+1]
            suffix = xx[t+1 : ]
            cost = sse(prefix) + v_opt_rec(suffix, b - 1)
            print('  '*calc_depth(b),'mincost:',mincost,'cost:',cost)
            mincost = min(mincost, cost)
        return mincost`
