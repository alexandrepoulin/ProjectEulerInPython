import useful as u
import math

maxVal = 10**6

primes = u.primesTo(maxVal)
primes = primes[1:]
answer =0

for p in primes:
    v = (p**2+13)//2
    answer +=2* (math.ceil((v-1)/3)-math.floor((v+1)/4))
print(answer)
