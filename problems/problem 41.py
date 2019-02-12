print("Starting")

def isPrime(x):
    if x <= 1:
        return False
    MAX = int(x**0.5)+1
    nums = set(range(2, MAX))
    while len(nums)>0:
        p = nums.pop()
        if x%p == 0:
            return False
        nums.difference_update(set(range(p*2, MAX,p)))
    return True

def getNext(k,l):
    x = str(k)
    for i in range(2,len(x)+1):
        if x[-i+1] < x[-i]:
            answer = x[0:len(x)-i]
            numbers = set(answer)
            nextBest = 1
            for y in range(1,l+1):
                if str(y) not in numbers and int(y) > nextBest and int(y) < int(x[-i]):
                    nextBest = int(y)
            answer += str(nextBest)
            numbers.add(str(nextBest))
            for k in range(l,0,-1):
                if str(k) not in numbers:
                    answer += str(k)
            return [int(answer),l]
    answer = ""
    for i in range(l-1,0,-1):
        answer += str(i)
    return [int(answer),l-1]

current =7654321
currentLen = 7

found = False

while not found:
    print(current)
    if isPrime(current):
        found = True
    else:
        x = getNext(current,currentLen)
        current = x[0]
        currentLen = x[1]

print(current)
input("Done")
    
        
