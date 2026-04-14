import numpy as np

def F(x,y):
    return np.cos(y),np.cos(x)

x,y=0,0

for i in range(25):
    x,y=F(x,y)
    print(x,"\t",y)