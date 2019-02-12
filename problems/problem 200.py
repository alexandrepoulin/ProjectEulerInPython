print("Starting")

import useful

primes = useful.primesTo(10**6)
print(len(primes))

def nextInd(x):
    if x[0] == (x[1]+1):
        return [x[0]+1,0]
    return [x[0],x[1]+1]

def sub(x):
    s = list(str(x))
    for i in range(len(s)-2):
        if s[i:i+3] == ['2','0','0']:
            return True
    return False

def checkPrimeProof(x):
    s = useful.intToList(x)
    for i in range(len(s)):
        for j in range(10):
            if s[i] == j:
                continue
            temp = s.copy()
            temp[i] = j
            val = useful.listToInt(temp)
            if useful.fastIsPrime(val,primes,10**6):
                return False
    return True

sqube = []
ind = [1,0]
current = 0

while len(sqube) < 210:
    if len(sqube) != current:
        print(len(sqube))
        current = len(sqube)
            
    val1 = primes[ind[0]]**3*primes[ind[1]]**2
    if sub(val1):
        if checkPrimeProof(val1):
            sqube.append(val1)
    val2 = primes[ind[1]]**3*primes[ind[0]]**2
    if sub(val2):
        if checkPrimeProof(val2):
            sqube.append(val2)
    ind = nextInd(ind)

sqube.sort()      
print(len(sqube))
print(sqube[199])
input("done")
