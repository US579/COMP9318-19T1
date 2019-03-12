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

Recurisive method will compute many times, although its space complicity is lower than dynamic programming.

In this case we apply dynamic programming, like Fibonacci sequence , we use privious consequence to compute the next by storing it in the mermory.

this lab2 also implement this strategy 

the first row ,represent from that block divide into one bin

[  ] [  ] [  ] [3, 1, 18, 11, 13, 17]    -1

[  ] [  ] [  ] [1, 18, 11, 13, 17]       -1

[  ] [  ] [  ] [18, 11, 13, 17]          -1

[  ] [  ] [  ] [11, 13, 17]              18.666

[  ] [  ] [  ] [13, 17]                   8.0

[  ] [  ] [  ] [17]                       0

the second row ,represent from that block divide into two bin

[  ] [  ] [[3, 1, 18, 11, 13, 17]]        -1

[  ] [  ] [[1, 18, 11, 13, 17]]           -1

[  ] [  ] [[18, 11, 13, 17]]              18.666

[  ] [  ] [[11, 13, 17]]                   2

[  ] [  ] [[13, 17]]                       0

[  ] [  ] [[17]]                          -1

etc......

Divding the problem into sub-problem , store the first row because it is the best optimal solution [11, 13, 17]:             

18.666, [13, 17]:8.0,[17]:0, after that when we are going to the second row,it will divide into two bins from the first number 

in the list, so [18, 11, 13, 17] can be split to prefix and suffix,which are [18] and [11,13,17],as we already know what the 

cost of [11,13,17] from the first row's data which is 18.666 and the cost of [18] is 0 , we are able to calculate the optimal 

cost that dividing [18, 11, 13, 17] into two bins is 0 + 18.999 == 18.999 ,this is the core thinking of the dynamic 

programming.





