print("Starting")

import quadratic
from mpmath import *
mp.dps = 100
sigfigs = 100

MAX = 10000

nums = set(range(2,MAX+1))
squares  = set([x for x in map(lambda k: k**2, range(2,int(sqrt(MAX)+1)))])
nums.difference_update(squares)
nums = list(nums)
nums.sort()

counter = 0

for x in nums:
    print(x)
    y = quadratic.quadTerm(1,0,x)
    frac = y.contFrac()
    length = len(frac[0])-1
    if length % 2 == 1:
        counter +=1

print(counter)
input("Done")
