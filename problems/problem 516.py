import useful as u
import math

maxVal = 10**12
##maxVal = 10**2
mod = 2**32

maxValSqrt = int(math.sqrt(maxVal))

primes = u.primesTo(maxValSqrt)
primesSet= set(u.primesTo(maxValSqrt))
primes2 = primes[3:]

def isHamPrime(x):
    val=x
    while val%2 == 0:
        val = val//2
    while val%3 == 0:
        val = val//3
    while val%5 == 0:
        val = val//5
    return val == 1

hamNums = []
for i in range(0,math.ceil(math.log(maxVal,2))):
    tempi = 2**i
    for j in range(0,math.ceil(math.log(maxVal,3))):
        tempj = 3**j
        if tempj*tempi > maxVal:
            break
        for k in range(0,math.ceil(math.log(maxVal,5))):
            tempk = 5**k
            val = tempi*tempj*tempk
            if val > maxVal:
                break
            hamNums.append(val)
print(len(hamNums))
hamNums.sort()
hamPrimes = [1]+[x+1 for x in hamNums if (x+1 >=7 and u.fastIsPrime2(x+1,primes,maxValSqrt,primesSet))]
hamPrimes.sort()
print(len(hamPrimes))

multFact = [1]

def recursivelyDo(val,used):
    newVals = []
    maxUsed = max(used)
    for p in hamPrimes:
        if p <= maxUsed:
            continue
        temp = val*p
        if temp < maxVal:
            newVals.append([temp,used.union(set([p]))])
        else:
            break
    for v in newVals:
        multFact.append(v[0])
    [recursivelyDo(x[0],x[1]) for x in newVals]

print("starting recurse")
recursivelyDo(1,set([1]))
print("done Recurse")
multFact.sort()
print(len(multFact))

answer = 0
hamNums.sort()
for c,h in enumerate(hamNums):
    for p in multFact:
        val = h*p
        if val > maxVal:
            break
        answer += val
        answer %=mod
print(answer)
        
