print("Starting")

from mpmath import *
mp.dps = 5000
sigfigs = 5000
MAX = -1
maxD = -1

import dioph


for D in range(2,1001):
    print(D)
    solution = dioph.solve(1,0,-D,0,0,-1)[0]
    if solution[0] > MAX:
        MAX = solution[0]
        maxD = D

print(maxD)
input("Done")
