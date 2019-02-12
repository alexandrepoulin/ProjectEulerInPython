print("Starting")

import useful
from mpmath import *

mp.dps = 1000100
sigfigs = 1000100

primes = useful.primesTo(100000)
primes.sort()
def computeMod(p):
    phi = p-1
    factors = useful.factors(p-1)
    factors.sort()
    factors.append(p-1)
    for i in range(len(factors)):
        tempFactors = useful.factorsFromPrimes(factors[i],primes)
        #for i in range(len(tempFactors)):
        #    tempFactors[i] = int(tempFactors[i])
        #print(set(tempFactors),set(tempFactors).issubset({2,5}))
        if not set(tempFactors).issubset({2,5}):
            continue
        if fmod(power(10,factors[i]),p) == 1:
            return True
    return False

##this shit is so abstract yo, number theory is weird
##these numbers are so fucking big, I'm baffled that this is working
answer = 2+3+5
for i in range(3,len(primes)):
    if i%1000 == 0:
        print(i, "out of", len(primes))
    if not computeMod(primes[i]):
        answer +=primes[i]
    else:
        print(primes[i])
print(answer)

input("Done")
