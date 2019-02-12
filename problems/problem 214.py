print("Starting")

import useful

MAX = 40000000
#MAX = 20
primes = useful.primesTo(MAX)

primes.sort()
primeLen = len(primes)
chainLengths = {1:1}
answer = 0
print(len(primes))
primeTerms = {p: (1-1/p) for p in primes}

def phiFunc(n, primes):
    facts = useful.factorsFromPrimes(n,primes)
    factors = set(facts)
    if len(factors) == 1:
        p = factors.pop()
        return p**(len(facts)-1)*(p-1)
    answer = n
    for i in factors:
        answer *= primeTerms[i]
    return int(answer)

def addChainLenght(x, knownPrime):
    phi = 0
    if knownPrime:
        phi = x-1
    else:
        phi = phiFunc(x,primes)
    if phi in chainLengths:
        chainLengths[x] = chainLengths[phi]+1
    else:
        addChainLenght(phi, False)
        chainLengths[x] = chainLengths[phi]+1

for i in range(primeLen):
    if (i % 1000) == 0:
        print(i, " of ", primeLen)
    p = primes[i]
    addChainLenght(p,True)
    if chainLengths[p] == 25:
        answer += p

print(answer)
input("Done")

