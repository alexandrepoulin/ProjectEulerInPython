print("Starting")

import useful

primes = useful.primesTo(1000000)
primes.sort()

bestSoFar = 0
bestN = 0

def phi(n):
    if n in primes:
        return n-1
    facts = useful.factorsFromPrimes(n,primes)
    factors = set(facts)
    if len(factors) == 1:
        p = factors.pop()
        return p**(len(facts)-1)*(p-1)
    answer = n
    for i in factors:
        answer *= (1-1/i)
    return int(answer)

nums = [x for x in filter(lambda y: y%6 == 0 and y%12 != 0, range(6,1000000))]
nums.sort()
for j in range(len(nums)):
    i = nums[j]
    if (j%1000) == 0:
        print(j, "of ", len(nums))
    val = i/phi(i)
    if val > bestSoFar:
        bestSoFar = val
        bestN = i

print(bestSoFar)
print(bestN)
input("Done")
