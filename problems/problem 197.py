print("Starting")

import math
from mpmath import *

mp.dps = 100
sigfigs = 100
num = 30.403243784

def nextAn(an):
    return fmul(power(10,-9),math.floor(power(2,(fsub(num,power(an,2))))))

a0 = -1
anext = a0
for i in range(1000):
    anext = nextAn(anext)
    print(anext)
    
