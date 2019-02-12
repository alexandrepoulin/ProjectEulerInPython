import useful as u
import math

primeMax = 5*10**7
primes = u.primesTo(primeMax)
primesSet= set(primes)
print("done primes")

factors = [1 for i in range(primeMax+2)]
for p in primes:
    for i in range(p,primeMax+2,p):
        factors[i] = max([p,factors[i]])

print("done doing factors")

##def h(x,y):
##    if y==1:
##        return x
##    tempx = x+1
##    tempy = y-1
##    while tempy%tempx != 0:
##        tempx = tempx+1
##        tempy = tempy-1
##        if tempy==1:
##            return tempx
##    tempx = 1
##    tempy = tempy//tempx
##    return f2(tempy)
##
##
##def f(n):
##    return h(1,n)

def findFactors(m):
    global factors
    if m <= primeMax+1:
        return factors[m]
    factor = 0
    x = m
    sqrt = math.sqrt(x)
    for p in primes:
        if p> sqrt:
            break
        if x%p==0:
            if p>factor:
                factor = p
            while x%p==0:
                x = x//p
            if x <= primeMax+1:
                return max((factors[x],factor))
            if x==1:
                break
    if x!=1:
        return max([x,factor])
    return factor
            
def f2(n):
    max1 = findFactors(n+1)
    max2 = findFactors((n**2-n+1))

    return max([max1-1,max2-1])

answer = 0
for i in range(1,2*10**6+1):
    if i%10000==0:
        print(i)
    answer += f2(i)
    
