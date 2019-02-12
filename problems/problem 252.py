#import matplotlib.pyplot as plt
#import numpy as np
#import math

s0=290797
nextS = 290797
xpoints=[]
ypoints=[]
while len(xpoints) <500:
    nextS = (nextS**2)%50515093
    nextT = (nextS%2000)-1000
    xpoints.append(nextT)
    nextS = (nextS**2)%50515093
    nextT = (nextS%2000)-1000
    ypoints.append(nextT)

print(xpoints[:3],ypoints[:3])
