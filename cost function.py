import numpy as np
def computerCost(X,y,theta):
    m = len(y)
    J = 0
    J = (np.transpose(X*theta-y))*(X*theta-y)/(2*m) #计算代价J
    return J
