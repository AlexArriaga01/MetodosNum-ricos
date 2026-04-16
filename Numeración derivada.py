import numpy as np

t_i=0.5
h=0.25

t_i1=t_i+h
t_i2=t_i1+h

def f(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

def df(t_i):
    return (4*f(t_i1)-3*f(t_i)-f(t_i2))/(2*h)

print(df(t_i))