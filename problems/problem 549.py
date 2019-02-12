import useful as u
import math



maxVal = 10**8


primes = u.primesTo(maxVal+1)
primes1 = [p for p in filter(lambda k : k>=maxVal**(1/2),primes)]

primes2 = [p for p in filter(lambda k : k< maxVal**(1/2),primes)]


print("done getting primes")


def count(m,p):
    total = 0
    ind = 1
    while m >= p**ind:
        total += math.floor(m/p**ind)
        ind+=1
    return total

def getSmallestForPrime(p,k):
    ##prime p to the power k
    if k<p:
        return k*p
    answer = k*p
    lastAnswer = answer
    ind= 2
    while True:
        answer -= p
        c = count(answer,p)
        if c < k:
            break
        lastAnswer= answer
    return lastAnswer

    

flags = [False] * (maxVal+1)
flags[0] = flags[1] = True
answer = 0


for p in primes1:
    for i in range(p,maxVal,p):
        answer += p
        flags[i] = True

primes2

counters = []

for p in primes2:
    if p < 10:
        counters += [(p,i,getSmallestForPrime(p,i)) for i in range(1,math.ceil(math.log(maxVal,p)))]
    else:
        counters += [(p,i,i*p) for i in range(1,math.ceil(math.log(maxVal,p)))]



u.sortN(counters,2)
for cou in counters[::-1]:
    for i in range(cou[0]**cou[1],maxVal+1,cou[0]**cou[1]):
        if not flags[i]:
            answer +=  cou[2]
            flags[i] = True

print(answer)
