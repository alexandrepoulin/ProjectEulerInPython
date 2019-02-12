print("starting")

import useful

MAXPRIMES = 1000000
MAXLENGHT = 8

def filt(x,n):
    listX = list(str(x))
    for i in listX:
        if listX.count(i) >= 2:
            return True
    return False

primes = useful.primesTo(MAXPRIMES)
print("Done making primes")
primes2 = {i for i in filter(lambda p: filt(p,2),primes)}
print("Done making primes2")
primes3 = {i for i in filter(lambda p: filt(p,3),primes2)}
print("Done making primes3")
primes4 = {i for i in filter(lambda p: filt(p,4),primes3)}
print("Done making primes4")
primes5 = {i for i in filter(lambda p: filt(p,5),primes4)}
print("Done making primes5")


found = False
value = 0
value2 = 0
permForBest = []
currentLength = 0


def reformNumber(x):
    answer = ""
    for i in x:
        answer+=i
    return int(answer)

def check(perm,number):
    temp = number
    for i in range(0,len(perm)):
        if int(perm[i]) == 1:
            temp[i] = "*"
    answer = ""
    for k in temp:
        answer+=k
    return answer
    
for p in primes:
    print(p)
    length = len(str(p))    
    if length > currentLength:
        used = set()
        currentLength = length
        currentPrimes = {i for i in filter(lambda p: len(str(p)) == currentLength ,primes)}
        currentPrimes2 = {i for i in filter(lambda p: len(str(p)) == currentLength ,currentPrimes)}
        currentPrimes3 = {i for i in filter(lambda p: len(str(p)) == currentLength ,currentPrimes2)}
        currentPrimes4 = {i for i in filter(lambda p: len(str(p)) == currentLength ,currentPrimes3)}
        currentPrimes5 = {i for i in filter(lambda p: len(str(p)) == currentLength ,currentPrimes4)}
    if length == 1:
        continue
    for i in range(0,length-1):
        num = "1"
        for k in range(0,i):
            num += "1"
        while len(num)< length:
            num += "0"
        perms = useful.perm(num)
        for per in perms:
            counter = 0
            number = list(str(p))
            checking = check(per,number)
            if checking in used:
                continue
            else:
                used.add(checking)
            for ite in range(0,10):
                if per[0] == "1" and ite == 0:
                    continue
                for j in range(0,len(per)):
                    if per[j] == "1":
                        number[j] = str(ite)
                number2 = reformNumber(number)
                if i == 0 and number2 in currentPrimes:
                    counter+=1
                if i == 1 and number2 in currentPrimes2:
                    counter+=1
                if i == 2 and number2 in currentPrimes3:
                    counter+=1
                if i == 3 and number2 in currentPrimes4:
                    counter+=1
                if i == 4 and number2 in currentPrimes5:
                    counter+=1
            if counter == MAXLENGHT:
                found = True
                for ite in range(0,10):
                    for j in range(0,len(per)):
                        if per[j] == "1":
                            number[j] = str(ite)
                    number2 = reformNumber(number)
                    if i == 0 and number2 in currentPrimes:
                        break
                    if i == 1 and number2 in currentPrimes2:
                        break
                    if i == 2 and number2 in currentPrimes3:
                        break
                    if i == 3 and number2 in currentPrimes4:
                        break
                    if i == 4 and number2 in currentPrimes5:
                        break
                value = p
                value2 = number2
                permForBest = per
                break
        if found:
            break
    if found:
        break
            

print(value)
print(value2)
print(permForBest)
input("Done")
                    
                    
    

