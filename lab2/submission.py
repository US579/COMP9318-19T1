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

def SSE(x):
    mean = np.average(x)
    sse = 0.0
    for i in x:
        rd = i - mean
        sse += rd**2
    return sse



def v_opt_dp(x, num_bins):# do not change the heading of the function
    cost_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]
    index_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]
    path_matrix  = [[-1 for _ in range(len(x))] for _ in range(num_bins)]

    for i in range(1,num_bins+1):
        for j in range(len(x)):
            if num_bins - i <= j and len(x) - j >= i:
                suffix = x[j:]
                if i == 1:
                    cost = SSE(suffix)
                    cost_matrix[i-1][j] = cost
                    index_matrix[i-1][j] = suffix
                    path_matrix[i-1][j] = suffix
                else:
                    set_path = []
                    if len(suffix) == i:
                        for ele in suffix:
                            set_path.append([ele])
                        index_matrix[i-1][j] = suffix
                        path_matrix[i-1][j] = set_path
                        cost_matrix[i-1][j] = 0
                    else:
                        lis_cost = []
                        for mid in range(1, len(suffix) -i + 2):
                            one_path = []
                            pre_suffix = suffix[:mid]
                            one_path.append(pre_suffix)
                            suf_suffix = suffix[mid:]
                            pre_cost = SSE(pre_suffix)
                            num = index_matrix[i-2].index(suf_suffix)
                            #print(path_matrix[i-2][num])
                            if i > 2:
                                one_path+=(path_matrix[i - 2][num])
                            else:
                                one_path.append(path_matrix[i-2][num])
                            cost = pre_cost + cost_matrix[i-2][num]
                            lis_cost.append(cost)
                            set_path.append(one_path)
                        cost_matrix[i-1][j] = min(lis_cost)
                        index_mincost_path = lis_cost.index(min(lis_cost))
                        path_matrix[i-1][j] = set_path[index_mincost_path]
                        index_matrix[i-1][j] = suffix

    bins = path_matrix[num_bins-1][0]
    return cost_matrix , bins



