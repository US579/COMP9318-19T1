## import modules here
import math

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    if x < 2:
        return  x
    left , right = 0,x
    flag = 0
    while abs(flag - x) > 0.01:
        mid = left + (float(right -left))/2
        flag = mid * mid
        if flag < x:
            left = mid
        else:
            right = mid

    return  round(mid)



################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations 

## NOTE: you must use the default values of the above parameters, do not change them

def fprime(x):
    return 1.0 + math.log(x)

def f(x):
    return x * math.log(x) - 16.0


def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    root_lis = [x_0,x_0 - (f(x_0)/fprime(x_0))]
    while abs(root_lis[-1]-root_lis[-2]) >= EPSILON and len(root_lis) - 2  < MAX_ITER:
        root_lis.append(root_lis[-1] - (f(root_lis[-1])/fprime(root_lis[-1])))
    return root_lis[-1]


################# Question 3 #################
class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def make_tree(tokens): # do not change the heading of the function
    tree = Tree(tokens[0])
    child = tree
    parent = tree
    stack = []
    for i in range(1, len(tokens)):
        if tokens[i] == '[':
            stack.append(parent)
            parent = child
        elif tokens[i] == ']':
            parent = stack.pop()

        else:
            child = Tree(tokens[i])
            parent.add_child(child)
    return tree



def max_depth(root): # do not change the heading of the function
    if not root.children:
        return 1
    depth = 1
    for i in root.children:
        k = max_depth(i)
        if depth <= k + 1:
            depth = k + 1
    return depth
