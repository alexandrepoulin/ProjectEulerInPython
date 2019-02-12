print("Starting")

MAX_PRIME = 1000000

numbers = set(range(MAX_PRIME,1,-1))

circularP = []
primes = []
prime2 = []

def tokenNum(x):
    text = str(x)
    nums = []
    for i in range(0,len(text)):
        nums.append(text[i])
    return nums

while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, MAX_PRIME+1, p)))

print("Done Finding Primes, removing those with an even number")

primeSet = set(primes)

while primeSet:
    q = primeSet.pop()
    text = tokenNum(q)
    Keep = True
    for i in range(0,len(text)):
        if int(text[i])%2 == 0:
            Keep = False
            break
    if Keep or q == 2:
        prime2.append(q)

print("Done removing stuff")
print(len(prime2))


for q in prime2:
    nums = tokenNum(q)
    skip = False
    for k in range(0,len(nums)):
        newNums = nums[-1]
        for i in range(0,len(nums)-1):
            newNums+=nums[i]
        if not (int(newNums) in prime2):
            skip = True
            break
        nums = newNums
    if skip:
        continue
    print(q)
    circularP.append(q)

print(len(circularP))
input("Press something")
            
    

    

