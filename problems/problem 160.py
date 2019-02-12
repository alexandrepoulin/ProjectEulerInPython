import useful as u
import math

maxNumPrimes= 10**7
primes = u.primesTo(maxNumPrimes)

mod = 10**5

def countP(n,p):
    current = p
    total = 0
    while current <= n:
        total+= n//current
        current*=p
    return total

def findAnswer(n):
    total = 1
    for p in primes:
        if p>n:
            break
        if p==2:
            total*=u.expEff(2,countP(n,2)-countP(n,5),mod)
            total%=mod
        elif p==5:
            pass
        else:
            total*=u.expEff(p,countP(n,p),mod)
            total%=mod
    return total

print(findAnswer(10**5))
##print(findAnswer(10**7))

answer= 1
fact2 = False
for i in range(1,10**5):
    temp = i
    while temp%5==0:
        temp//=5
        fact2 +=1
    while fact2>0 and temp%2==0:
        fact2 -= 1
        temp //=2
    answer*= temp
    answer%=mod
print(answer)

print("")
print(findAnswer(10**6))

answer= 1
for i in range(1,10**5):
    temp = i
    while temp%5==0:
        temp//=5
        fact2 +=1
    while fact2>0 and temp%2==0:
        fact2 -= 1
        temp //=2
    if i==29:
        pass
    answer*= temp
    answer%=mod
print(answer)


def formula(n):
    r=1/5
    m=math.floor(math.log(n,5))
    answer = 10*(n*(1-r**(2*(m+1)))/(1-r**2) + 2*(1-r**(m+1))/(1-r)-10*(n+2))
    answer /=n*(1-2*r**(m+1))/(1-2*r)
    answer%=10**5
    return answer

print(formula(10**5))

##print(len(primes))

