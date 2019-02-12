print("starting")

import useful
import math

##the next prime after sqrt(999966663334) is 1000003
MAX = 999966663334
missingPrime = 1000003
##MAX = 1000
##missingPrime = 37
sqrtMAX = math.ceil(math.sqrt(MAX))
primes = useful.primesTo(sqrtMAX)
primes.append(missingPrime)
primes.sort()

p0 = 0
val0 = 0
p1 = 2
val1 = 4
answer = 0
counter = 0
for i in range(1,len(primes)):
    if i %1000 == 0:
        print(i, " of ", len(primes))
    p0 = p1
    p1 = primes[i]
    val0 = val1
    val1 = p1**2
    for j in range(val0+p0,val1,p0):
        if j > MAX:
            break
        if (j%p1)!= 0:
            answer += j
            counter += 1
    for j in range(val1-p1,val0,-p1):
        if j > MAX:
            continue
        if (j%p0)!= 0:
            answer += j
            counter += 1

print(answer,counter)
input("Done")
