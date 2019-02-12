print("Starting")

import useful
MAX = 1000000
primes = useful.primesTo(MAX)
primes.sort()

answer = 0
## better idea is go make a phi array, go through all multiples of primes and multiply
## by p-1 and divide by p.

numbers = set(range(MAX,1,-1))

while numbers:
    i = numbers.pop()
    print(len(numbers))
    factors = useful.factorsFromPrimes(i,primes)
    factors = set(factors)
    phiValue = useful.phi(i,primes)
    multiples = set()
    for fact in factors:
        number = 0
        while i*fact**number <= MAX:
            multiples.add(i*fact**number)
            number+=1
    multiples.intersection_update(numbers)
    multiples.add(i)
    for mult in multiples:
        answer+= phiValue*mult/i
    numbers.difference_update(multiples)

print(answer)

input("Done")
