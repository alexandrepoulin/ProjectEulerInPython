print("Starting...")

numbers = set(range(2000000,1,-1))

truncPrimes = []
primes = []

singles = [2,3,5,7]

notTrunc = []

sumSoFar = 0

while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, 2000000+1, p)))



primes.sort()

def filt(x):
    if len(str(x)) == 1:
        return False
    if x%10 == 9:
        return False
    if int(str(x)[0]) == 4 or int(str(x)[0]) == 6 or int(str(x)[0]) == 8 or int(str(x)[0])%10 == 9:
        return False
    return True

copy = [p for p in filter(lambda x: filt(x), primes)]

def isLeft(x):
    if x in notTrunc:
        return False
    if len(str(x)) == 1 and x in singles:
        return True
    if x in primes and isLeft(int(str(x)[0:len(str(x))-1])):
        return True
    notTrunc.append(x)
    return False

def isRight(x):
    if x in notTrunc:
        return False
    if len(str(x)) == 1 and x in singles:
        return True
    if x in primes and isRight(int(str(x)[1:])):
        return True
    notTrunc.append(x)
    return False

print(len(copy))
for p in copy:
    print(p)
    if p in singles:
        continue
    if isLeft(p) and isRight(p):
        truncPrimes.append(p)
        sumSoFar += p
        if len(truncPrimes) == 11:
            break

print(truncPrimes)
print(sumSoFar)
input("something")
    
