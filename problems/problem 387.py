import useful as u
import math

expo=14

n=10**expo
sqrtN=int(math.sqrt(n))+1


primes = u.primesTo(sqrtN)

def isHar(n):
    digitSum = u.addDigits(n)
    return n%digitSum==0

def isStrong(n):
    digitSum = u.addDigits(n)
    return u.fastIsPrime(int(n/digitSum),primes,sqrtN)
                         
nextGenH = list(range(1,10))
nextGenHS=[]
primeTot = 0
for i in range(2,expo+1):
    print(i)
    nextGen = [10*x +y for y in range(10) for x in nextGenH]
    nextGenH = [x for x in filter(lambda k: isHar(k),nextGen)]

    nextGenP=[10*x +y for y in range(10) for x in nextGenHS]
    primeTot +=sum([x for x in filter(lambda k: u.fastIsPrime(k,primes,sqrtN),nextGenP)])
    
    
    nextGenHS=[x for x in filter(lambda k: isStrong(k),nextGenH)]


print(primeTot)
