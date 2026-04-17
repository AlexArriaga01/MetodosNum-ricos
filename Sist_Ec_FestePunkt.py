import numpy as np
import pandas as pd

def F(x):
    return np.cos(X[1]),np.cos(X[0])

x,y=0,0
X=np.array([x,y])

L_X=[(x,y)]
L_FX=[F(X)]
for i in range(25):
    X=F(X)
    L_X.append(X)
    L_FX.append(F(X))

D={"(x,y)":L_X,
   "F(x,y)":L_FX}

print(pd.DataFrame(D))