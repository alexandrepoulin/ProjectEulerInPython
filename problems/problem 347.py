import useful as u
import math

maxVal = 10**7
maxPrime= int(maxVal/2)

primes=u.primesTo(maxPrime)

tot = 0

for p1 in primes:
    for p2 in primes:
        if p1 * p2 > maxVal:
            break
        if p1 >= p2 :
            continue
        bestSoFar = 0
        for x in range(1, math.floor(math.log(maxVal,p1)+1)):
            if p1**x*p2 >= maxVal:
                break
            for y in range(1,math.floor(math.log(maxVal,p2)+1)):
                temp=p1**x*p2**y
                if temp > maxVal:
                    break
                if temp > bestSoFar:
                    bestSoFar = temp
        tot += bestSoFar

print(tot)
