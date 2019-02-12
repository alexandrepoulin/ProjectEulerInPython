print("Starting")

import useful
import math
MAX = 50000000
#MAX = 10000
val = math.ceil(math.sqrt(2*MAX**2-1))
primes = useful.primesTo(val)

def fastIsPrime(x):
    for i in primes:
        if i > x**0.5+1:
            break
        if x%i == 0:
            return False
    return True

##Fermat's little theorem primality testing for p>= 5

counter = 0
for n in range(2,MAX+1):
    temp= 2*n**2-1
    if (n%1000) == 0:
        print(n, " of ", MAX)
    if useful.isPrimeFermat(temp):
        if fastIsPrime(temp):
            counter += 1

print(counter)
input("Done")
