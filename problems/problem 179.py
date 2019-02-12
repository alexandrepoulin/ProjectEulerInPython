print("Starting")

import useful

primes = useful.primesTo(10000000)

prev1, cur1 = 1,1
prev2, cur2 = 1,1
counter = 1
answer = 0 

while counter <= 10**7:
    counter+=1
    print(counter)
    prev1 = cur1
    prev2 = cur2
    factors = useful.factorsFromPrimes(counter,primes)
    cur1 = len(factors)
    cur2 = len(set(factors))
    if prev1 == cur1 and prev2 == cur2:
        answer +=1

print(answer)
input("Done")

