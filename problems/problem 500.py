import useful as u

neededNumer = 7376508 ## this is the number we need so that we get 500500 primes

primes = u.primesTo(neededNumer)

nonZeroExp = dict()

counter = 0

while True:
    counter += 1
    if counter%100 == 0:
        print(len(nonZeroExp), len(primes))
    num = primes[-1]
    ditchPrime = False
    bestKV = []
    for k, v in nonZeroExp.items():
        if not ditchPrime:
            if k**(v+1) < num:
                ditchPrime = True
                bestKV = [k,v]
        else:
            if k**(v+1) < bestKV[0]**(bestKV[1]+1):
                bestKV = [k,v]
    
                
    if not ditchPrime:
        if primes[len(nonZeroExp)]**2 < num:
            ditchPrime = True
            bestKV = [primes[len(nonZeroExp)],1]
    if ditchPrime:
        if primes[len(nonZeroExp)]**2 < bestKV[0]**(bestKV[1]+1):
            bestKV = [primes[len(nonZeroExp)],1]
    if not ditchPrime:
        break
    else:
        nonZeroExp[bestKV[0]]=2*bestKV[1]+1
        del primes[-1]

answer = 1
for p in primes:
    if p in nonZeroExp.keys():
        answer*= p**nonZeroExp[p]
    else:
        answer*=p
    answer %= 500500507

print(answer)

