import numpy as np

def F(X):
    return np.array([np.cos(X[1]),np.cos(X[0])])

def DF(X):
    return np.array([[0,-np.sin(X[1])],[-np.sin(X[0]),0]])

x,y=0,0
X=np.array([x,y])

for i in range(25):
    delta=np.linalg.solve(DF(X),F(X))
    X=X-delta
    print(X)