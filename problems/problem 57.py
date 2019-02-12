print("starting")

from mpmath import *
mp.dps = 100
sigfigs = 100

from dioph import findContinuedFraction as cont
from dioph import findNextConvergent as nconv

counter = 0

data = cont(sqrt(2))
nums = data[0]
periodic = data[0][data[1]:]
for i in range(0,int(ceil((1000-len(nums))/len(periodic)))):
    nums.extend(periodic)
nums = nums[:1000]

secondLast = [1,0]
last = [nums[0],1]
for i in range(2,1001):
    print(i)
    current = nconv(nums[counter-1],last,secondLast)
    values = [x for x in map(lambda k: int(k),current)]
    if len(str(values[0])) > len(str(values[1])):
        counter += 1
    secondLast = last
    last = current

print(counter)
input("Done")



