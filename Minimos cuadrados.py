import matplotlib.pyplot as plt
import numpy as np

Px=[0,.5,1,1.1,2,3,3.2,3.5,4,5]
Py=[.1,-.2,1,1.5,1.9,2,3,5,4.5,5]

Sx=0
Sy=0
for i in Px:
    Sx=Sx+i
    Sy=Sy+i
Sx=Sx/len(Px)
Sy=Sy/len(Py)

m1,m2=0,0
for i in range(len(Px)):
    m1=(Px[i]-Sx)*(Py[i]-Sy)
    m2=(Px[i]-Sx)**2

m=m1/m2
b=Sy-m*Sx

X=np.linspace(0,5,10)
Y=m*X+b

plt.scatter(Px,Py)
plt.plot(X,Y)
plt.show()