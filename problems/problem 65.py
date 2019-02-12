print("Starting")

import fractions
import useful
from mpmath import *

mp.dps = 100
sigfigs = 100

MAX = 100

nums = [2,1]
k = 1
while len(nums)< MAX:
    nums.append(2*k)
    k+=1
    if len(nums) == MAX:
        break
    nums.append(1)
    if len(nums) == MAX:
        break
    nums.append(1)

nom = 1
denom = nums[-1]
nums = nums[:-1]

while True:
    if len(nums) == 1:
        nom+=denom*nums[0]
        break
    new = nums[-1]
    temp = nom
    nom = denom
    denom = fadd(fmul(new,denom),temp)
    div = fractions.gcd(nom,denom)
    nom = fdiv(nom,div)
    denom = fdiv(denom,div)
    nums = nums[:-1]
    

print(int(nom))
print(int(denom))
nprint(fdiv(nom,denom))
print(useful.addDigits(int(nom)))
input("Done")
