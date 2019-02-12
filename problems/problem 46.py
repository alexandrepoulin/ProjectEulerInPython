print("starting")

import useful
import math

found = False

primes = []

smallest = 0

x = 1

while not found:
    x+=2
    if useful.isPrime(x):
        primes.append(x)
        continue
    else:
        isGood = False
        for i in primes:
            value = math.sqrt((x-i)/2)
            if abs(int(value) - value) < 0.0000001:
                isGood = True
                break
        if isGood:
            continue
        found = True
        smallest = x
        break

print(smallest)
input("Done")
