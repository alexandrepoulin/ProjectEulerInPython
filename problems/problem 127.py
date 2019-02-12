print("Starting")

import useful
import math
MAX = 1000
MAX = 120000
primes = useful.primesTo(MAX)

def check(x):
    factors = useful.factorsFromPrimes(x,primes)
    leng = len(factors)
    factors = set(factors)
    leng2 = len(factors)
    #if leng > leng2:
    #    numFactors[x] = factors
    return leng > leng2

def rad(aFact,bFact,cFact):
    answer = 1
    factors = aFact.union(bFact.union(cFact))
    for f in factors:
        answer *= f
    return answer

def radInd(x):
    factors = useful.factorsFromPrimes(x,primes)
    factors = set(factors)
    answer = 1
    for f in factors:
        answer *= f
    rads[x] = answer

nums = list(range(1,MAX))
#numFactors = dict()
rads = [0]*(MAX+1)
for i in range(1,MAX+1):
    radInd(i)

nums = [x for x in filter(lambda k: check(k),nums)]
finalAnswer = 0
for k in range(len(nums)):
    c = nums[k]
    if k%1000 == 0:
        print(k, " out of " ,len(nums))
    for a in range(1,int(c/2)+1):
        b = c-a
        if b <= a:
            continue
        if useful.GCD(b,a) != 1:
            continue
##        aFact = set()
##        if a in numFactors:
##            aFact = numFactors[a]
##        else:
##            tempList = useful.factorsFromPrimes(a,primes)
##            aFact = set(tempList)
##            numFactors[a] = aFact
##        bFact = set()
##        if b in numFactors:
##            bFact = numFactors[b]
##        else:
##            tempList = useful.factorsFromPrimes(b,primes)
##            bFact = set(tempList)
##            numFactors[b] = bFact
        if rads[a]*rads[b]*rads[c] < c:
            finalAnswer +=c
        #if rad(aFact,bFact,numFactors[c]) < c:
            #finalAnswer+=c
            
print(finalAnswer)
input("done")
