print("Starting")

import math

def isValuePrime(value):
    x = value
    if int(value**0.5)+1 > 3:
        x = int(math.pow(value,0.5))+1 
    for i in range(2,int(value**0.5)+1):
        if value%i == 0:
            return False
    return True

def isPrime(value, a, b, n):
    if value <2:
        return False
    if b !=0 and a+n%b == 0:
        return False
    return isValuePrime(value)
    

def answer(x,y):
    value = 0
    bestCounter = 0
    bestA = -1001
    bestB = -1001
    for a in range(-x,x+1):
        print(a)
        for b in range(0,y+1):
            if bestCounter > b:
                continue
            counter = 0;
            value = b
            while isPrime(value,a,b,counter):
                counter +=1
                value = counter**2+a*counter+b
            if counter > bestCounter:
                bestCounter = counter
                bestA=a
                bestB=b

    print("------------------")
    print(bestCounter -1 )
    print(bestA)
    print(bestB)
    return bestA*bestB


print(answer(1000,1000))
input("Press any button to exit")
