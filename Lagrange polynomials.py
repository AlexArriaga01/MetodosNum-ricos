import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

X=np.array([2,2.5,4])
Y=1/X

x=sp.symbols('x')
if len(X)==len(Y):
    f=0
    for i in range(len(X)):
        f_i=1
        for j in range(len(X)):
            if j!=i:
                fac=(x-X[j])/(X[i]-X[j])
                f_i=f_i*(fac)
        f_i=sp.expand(f_i)
        f=f+Y[i]*f_i

    print(f"f(x)={f}")
    F=sp.lambdify(x,f,'numpy')
else:
    print("Error")

V=np.linspace(0.1,10,100)
plt.plot(V,1/V)
plt.plot(V,F(V))
plt.show()