import numpy as np
import pandas as pd

def f(x):
    return x**2-2

a,b=0,2

def bi(a,b):
    if f(a)*f(b)<0:
        p=(-f(a)*(b-a))/(f(b)-f(a))-a
        if f(a)*f(p)<0:
            a,b=a,p
        elif f(p)*f(b)<0:
            a,b=p,b
    else:
        raise ValueError("Intervalo inválido")
    print(a,b)
    return a,b

while abs(f(b))>0.5*10**(-10):
    a,b=bi(a,b)
    print(f(b))