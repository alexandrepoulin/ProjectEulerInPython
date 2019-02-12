print("Starting")

import useful
from mpmath import *

mp.dps = 1000100
sigfigs = 10001000

MAX =1000000
primes = useful.primesTo(2000000)

answer = 0
counter = 1000001
while True:
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
            print(factors[i],counter)
            if factors[i]>MAX:
                answer = counter
            break
    if answer != 0:
        break
    if (counter+2)%5 == 0:
        counter += 4
    else:
        counter += 2

print(answer)

input("Done")
    
