print("Starting")

import useful
primes = useful.primesTo(20000)
primes.sort()

bestVal = 100000
bestN = 0

for p in primes:
##    print(p)
    for q in primes:
        val = p*q
        if val > 10000000:
            break
        func = (val-q-p+1)
        if useful.isPerm(str(val), str(int(func))):
            if val/func < bestVal:
                bestVal = val/func
                bestN = val


print(bestN)
input("Done")
    
