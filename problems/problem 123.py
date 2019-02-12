print("Starting")

import useful
MAX = 10**6
primes = useful.primesTo(MAX)

answer = 0

for i in range(0,len(primes)):
    if i%2 == 1:
        continue
    val = 2*(i+1)*primes[i]% primes[i]**2
    if val > 10**10:
        print(val)
        print(primes[i])
        answer = i+1
        break

print(answer)
input("Done")
    
