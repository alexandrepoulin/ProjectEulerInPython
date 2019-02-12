import useful as u
import math

maxNum=100000000


primes = u.primesTo(maxNum)
print(len(primes))


def getNums():
    flags = [True] * maxNum
    numsToCheck = set()
    flags[0] = flags[1] = 0
    for p in primes:
        for n in range(p*p, maxNum, p*p):
            flags[n] = False
    for (i,f) in enumerate(flags):
        if i>maxNum/2:
            break
        if f:
            factors = len(set(u.factorsFromPrimes(i,primes)))
            yield (i,factors)

def coeff(n):
    return (-1)**(n+1)

def Tn(n):
    return int(n*(n+1)/2)

gen = getNums()

tot = maxNum-1
for (c,i) in enumerate(gen):
    if c%100000 == 0:
        print(c,i)
    tot += coeff(i[1])*Tn(math.floor((maxNum-i[0])/(i[0])))

tot*=6
print(tot)
