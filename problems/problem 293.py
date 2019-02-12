import useful as u
import math

maxVal = 10**9
maxPrimes = 10**8

smallPrimes = u.primesTo(25)
largePrimes = u.primesTo(maxPrimes)
largePrimesSet= set(largePrimes)
print(len(largePrimes))

def calcVal(x):
    answer = 1
    for i in range(len(x)):
        if x[i]==0:
            break
        answer *= smallPrimes[i]**x[i]
    return answer 

def inc(x):
    temp = calcVal(x)
    new = x.copy()
    for i in range(len(x)):
        if temp*smallPrimes[i] < maxVal:
            new[i]+=1
            return new
            
        else:
            new[i]=1
            temp = calcVal(new)
    return []

x=[0]*len(smallPrimes)
vals = []
while True:
    x = inc(x)
    if len(x)==0:
        break
    vals.append(calcVal(x))

print(len(vals))

answer = set()

for c,v in enumerate(vals):
    primeCan = v+3
    while not u.fastIsPrime2(primeCan,largePrimes,10**8,largePrimesSet):
        primeCan+=2
    answer.add(primeCan-v)

print(sum(answer))
    
