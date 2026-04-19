import numpy as np
import pandas as pd

def F(X):
    return np.array([np.cos(X[1])-X[0],np.cos(X[0])-X[1])

def DF(X):
    return np.array([[-1,-np.sin(X[1])],[-np.sin(X[0]),-1]])

x,y=0,0
X=np.array([x,y])

L_X=[X]
L_FX=[F(X)]
for i in range(25):
    delta=np.linalg.solve(DF(X),F(X))
    X=X-delta
    L_X.append(X)
    L_FX.append(F(X))

D={"(x,y)":L_X,
   "F(x,y)":L_FX}

print(pd.DataFrame(D))
