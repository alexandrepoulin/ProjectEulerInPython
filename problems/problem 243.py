print("Starting")

import useful
from mpmath import *
mp.dps = 100
sigfigs = 100


primes = [2,3,5,7,11,13,17,19,23]
RATIO = 15499/94744
product = 1
for i in primes:
    product *= (1 - fdiv(1,i))

number = fprod(primes)


while True:
    print(number)
    if number*product/(number-1)<=RATIO:
        break
    number*=2


print(number)
input("done")
