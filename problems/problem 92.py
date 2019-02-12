print("Starting")

import useful

def f(x):
    return sum(map(lambda x: int(x)**2, list(str(x))))

def expand(x):
    q = useful.perm(str(x))
    answer = []
    for perm in q:
        number = ""
        for inte in perm:
            number += inte
        answer.append(int(number))
    return answer

MAX = 10**7
numbers = set(range(1,MAX))
goodRemoved = set()
removed = set()

count = 0

while numbers:
    print(len(numbers))
    x = numbers.pop()
    nums = set()
    nums.add(x)
    currentNum = x
    while currentNum != 1 and currentNum != 89 and len(nums.intersection(removed))==0:
        expandedNums = expand(currentNum)
        expandedNums = set(expandedNums)
        for y in expandedNums:
            if y < MAX:
                nums.add(y)
        currentNum = f(currentNum)
    if currentNum == 89 or len(nums.intersection(goodRemoved))>0:
        nums.difference_update(removed)
        count+=len(nums)
        goodRemoved.update(nums)
    removed.update(nums)
    numbers.difference_update(nums)

print(count)
input("Done")
    
