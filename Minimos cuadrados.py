import matplotlib.pyplot as plt
import numpy as np

Px=[]
Py=[]

def Sxy(Px,Py):
    Sx=0
    Sy=0
    for i in Px:
        Sx=Sx+i
        Sy=Sy+i
    Sx=Sx/len(Px)
    Sy=Sy/len(Py)
    return Sx,Sy

    