import useful as u
import math

primeMax = 10**8

primes = u.primesTo(primeMax)
print("done Primes")

maxVal = 10**15

def gFunc(n,prev):
    return prev+u.GCD(n,prev)

n=4
g=13
atMax = False

currentLog = math.floor(math.log(n,10))
while not atMax:
    timer = math.floor(math.log(n,10))
    if timer >currentLog :
        currentLog=timer
        print(currentLog,n)
    n+=1
    g=gFunc(n,g)
    p = min(u.factorsFromPrimes(g-n-1,primes))
    temp = max(((-((n+1)%p))%p,0))
    if n+temp> maxVal:
        atMax = True
        temp= maxVal - n
    n += temp
    g += temp

print(n,g)
    
