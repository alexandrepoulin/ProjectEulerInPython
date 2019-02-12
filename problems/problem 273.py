print("Starting")

import useful
import dioph

primes = useful.primesTo(150)

primes = [p for p in filter(lambda k: ((k-1)%4)==0,primes)]
primes.sort()
print(len(primes))

nums = set([1])
for i in range(len(primes)):
    p = primes[i]
    print(i+1, "of ", len(primes), "; length: ", len(nums))
    toBeAdded = set()
    for j in nums:
        toBeAdded.add(j*p)
    nums = nums.union(toBeAdded)
nums.difference_update(set([1]))
nums = list(nums)
nums.sort()
answer = 0
for j in range(len(nums)):
    i = nums[j]
    if (j%100) == 0:
        print(j, "of", len(nums),i)
    sol = dioph.solve(1,0,1,0,0,-i,True,True)
    sol = [x for x in filter(lambda k: k[0] <= k[1], sol)]
    for x in sol:
        answer += x[0]

    
