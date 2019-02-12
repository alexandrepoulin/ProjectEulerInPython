import useful as u
import math

n=100000000

primesFull = u.primesTo(n)
primeSet =set(primesFull)

print("done getting primes")
print(len(primesFull))

def check(num):
    factors = [x for x in filter(lambda k: math.sqrt(num) > k, u.factors(num))]
    factors.sort()
    for f in factors:
        if not int(f+num/f) in primeSet:
            return False
    return True

def iniCheck(num):
    if num%4==0:
        return False
    if int(num/2+2) not in primeSet:
        return False
    sqrtVal = math.sqrt(num/2)
    for p in primesFull:
        if p > sqrtVal:
            break
        if not((num%p == 0 and int(num/p+p) in primeSet) or num%p != 0 ):
            return False
    return True
    
nums = dict()
for p in primesFull:
    if iniCheck(p-1):
        nums[p-1]=p-1

print("done removing obvious fakes")
print(len(nums))

numbers = [x for x in nums.keys()]
numbers.sort()
tot = 0
success=set()
failed=[]
for (i,val) in enumerate(numbers):
    if i%10000 == 0:
        print(i)
    if check(val):
        tot += val
        success.add(val)
    else:
        failed.append(val)
print(tot)




