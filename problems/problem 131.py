print("Starting")

import useful

primes = useful.primesTo(10**6)

counter = 0

for i in range(1,2*10**6):
    p = (i+1)**3-i**3
    if p > 10**6:
        break
    if p in primes:
        counter+=1
    
print(counter)
input("done")
