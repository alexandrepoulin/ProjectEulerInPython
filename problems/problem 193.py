print("Starting")

import useful

MAX = 2**50
halfMAX = 2**25

primes = useful.primesTo(halfMAX)
primes.sort()
badNums = set()
print(len(primes))
for i in range(len(primes)):
    if (i%1000) == 0:
        print(i)
    p = primes[i]
    counter = 0
    badNums = badNums.union(set(range(p**2,MAX+1,p**2)))

answer = MAX - len(badNums) 
print(answer)
