import useful
import math


nums = set()
primes = useful.primesTo(51)

for i in range(1,51):
    for j in range(0, (i+1)//2+1):
        number = useful.nChooseK(i,j)
        good = True
        for p in primes:
            if number % p**2 == 0:
                good = False
                break
        if good:
            nums.add(useful.nChooseK(i,j))
print(sum(nums))

input("done")
