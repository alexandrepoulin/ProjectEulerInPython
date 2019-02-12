print("Starting")

import useful

primes1 = useful.primesTo(10000000)
primes1.sort()
primes = set(primes1)

def primeTest(x):
    for i in primes1:
        if i > x**0.5+1:
            break
        if x%i == 0:
            return False
    return True

target = 0.10

primeCounter = 0
numberCounter = 1
counter = 0

while True:
    counter+=1
    val = (2*counter+1)**2
    if val < 10000000:
        if val-2*counter in primes:
            primeCounter += 1
        if val-4*counter in primes:
            primeCounter += 1
        if val-6*counter in primes:
            primeCounter += 1
    else:
        if primeTest(val-2*counter):
            primeCounter += 1
        if primeTest(val-4*counter):
            primeCounter += 1
        if primeTest(val-6*counter):
            primeCounter += 1
    numberCounter += 4
    print(primeCounter/numberCounter)
    if primeCounter/numberCounter < target:
        break
    
print(counter)
print(2*counter+1)

input("Done")
    
        
    
