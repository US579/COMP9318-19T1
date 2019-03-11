## import modules here 
import pandas as pd
import numpy as np

x = [3, 1, 18, 11, 13, 17]
num_bins = 4

################# Question 1 #################


#SSE is the sum of the squared differences between each
# observation and its group's mean.
# It can be used as a measure of variation within a cluster.
# If all cases within a cluster are identical the SSE would then be equal to 0.

def sse(x):
    mean = np.average(x)
    sse = 0.0
    for i in x:
        rd = i - mean
        sse += rd**2
    return sse



def v_opt_dp(x, num_bins):# do not change the heading of the function
    cost_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]
    index_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]

    Matrix = [[0 for i in range(len(x))] for i in range(num_bins)]

    for i in range(1,num_bins+1):
        for j in range(len(x)):
            if num_bins - i <= j and len(x) - j >= i:
                suffix = x[j:]
                print(i)
                print('suffix',suffix)
                if i == 1:
                    cost = sse(suffix)
                    cost_matrix[i-1][j] = cost
                    index_matrix[i-1][j] = suffix

                else:
                    if len(suffix) == i:
                        lis_path = []
                        min_cost = 0
                        for ele in suffix:
                            lis_path.append([ele])
                        print('ele',lis_path)
                        index_matrix[i-1][j] = lis_path
                        print('inde',index_matrix)
                #print(cost_matrix)
                    else:
                        for first_half in range(1, len(suffix) - i + 2):
                            print('first_half',first_half)
                            pre_suffix = suffix[:first_half]
                            print('pre',pre_suffix)
                            suf_suffix = suffix[first_half:]
                            print('suf',suf_suffix)




a = [1]


#print(SSE(a))



    

v_opt_dp(x,num_bins)