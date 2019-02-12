print("Starting")

import useful
from mpmath import *

mp.dps = 1000100
sigfigs = 1000100

primes = useful.primesTo(1000000)
primes.sort()
primes = primes[3:]
def computeMod(p):
    phi = p-1
    factors = useful.factors(p-1)
    factors.sort()
    factors.append(p-1)
    for i in range(len(factors)):
        if fmod(power(10,factors[i]),p) == 1:
            ## need to know if factors[i]|10**80
            ##i.e if 10**80 mod factors[i] == 0
            if fmod(power(10,9),factors[i]) == 0:
                return True
    return False

##this shit is so abstract yo, number theory is weird
counter = 0
answer = 0
for p in primes:
    if computeMod(p):
        counter +=1
        answer +=p
        print(p,counter)
    if counter == 40:
        break

print(answer)

input("Done")
