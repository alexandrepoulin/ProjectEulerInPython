print("Starting")

import useful
from mpmath import *

mp.dps = 1000100
sigfigs = 10001000

MAX =1000000
primes = useful.primesTo(MAX)

answer = 0
counter = 91
hitCounter = 0
while True:
    if useful.fastIsPrime(counter,primes,MAX):
        if (counter+2)%5 == 0:
            counter += 4
        else:
            counter += 2
        continue
    GCD =useful.GCD(counter,9)
    mult = 1
    if GCD != 1:
        mult = 9
    phi = useful.phi(counter*mult,primes) ## this is to compensate the dividing by 9
    factors = useful.factors(phi)
    factors.sort()
    factors.append(phi)
    for i in range(len(factors)):
        if fmod(power(10,factors[i]),counter*mult) == 1:
            if (counter-1) % (factors[i]) == 0:
                answer += counter
                hitCounter+=1
                print(counter, hitCounter)
            break
    if hitCounter == 25:
        break
    if (counter+2)%5 == 0:
        counter += 4
    else:
        counter += 2



print(answer)

input("Done")
    
