print("Starting")

N=5000
s = -6*10**11

from mpmath import *

mp.dps = 1000
sigfigs = 1000

def f(r):
    answer = 0
    currentR = 1
    for k in range(1,5001):
        answer+=(900-3*k)*currentR
        currentR*=r
    return answer - s

upper = 1.1
lower = 1


while (upper - lower)> 10**(-15):
    val = 0.5*(upper+lower)
    func = f(val)
    if func > 0:
        lower = val
    else:
        upper = val

print(0.5*(upper+lower))

