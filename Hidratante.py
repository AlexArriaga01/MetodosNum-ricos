import numpy as np

def f(x):
    return np.sin(x)-x**2+3*x-1

pm_1,pm=0,1

while abs(f(pm))>0.5*10**(-10):
    p=pm
    pm=pm_1-(((pm_1-pm)*f(pm_1))/(f(pm_1)-f(pm)))
    pm_1=p
    print(pm_1,pm)