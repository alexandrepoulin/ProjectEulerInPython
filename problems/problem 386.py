import useful as u
import math

primes = u.primesTo(10**8)

answer = 0
for p in primes:
    answer += math.floor(10**8/p)



