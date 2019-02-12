import useful as u
import math



maxVal = 10**8
mod = 1000000009

primes = u.primesTo(maxVal+1)


print("done getting primes", len(primes))


def count(m,p):
    total = 0
    ind = 1
    while m >= p**ind:
        total += m//p**ind
        ind+=1
    return total

answer = 1
for c, p in enumerate(primes):
    ##these are large exponents so we need to use efficient exponentiation
    answer *= (1 + u.expEff(p,2*count(maxVal,p),mod))
    answer %= mod
print(answer)
