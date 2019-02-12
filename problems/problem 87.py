print("Starting")

import useful

primes = useful.primesTo(7100)
primes.sort()

counter = 0

numbers = set()

for i in primes:
    for j in primes:
        if i**2+j**3>50000000:
            break
        for k in primes:
            value = i**2+j**3+k**4
            if value < 50000000:
                if value not in numbers:
                    counter +=1
                    numbers.add(value)
            else:
                break
print(counter)
input("Done")
