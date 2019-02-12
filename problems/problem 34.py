print("Starting")

goodNums = []
total = 0

def fact(x):
    if x==0:
        return 1
    answer = 1
    for i in range(1,x+1):
        answer*=i
    return answer

def tokenNum(x):
    text = str(x)
    nums = []
    for i in range(0,len(text)):
        nums.append(int(text[i]))
    return nums

for i in range(10,100000):
    print(i)
    nums = tokenNum(i)
    sumForI = 0
    for x in nums:
        sumForI+=fact(x)
    if i == sumForI:
        goodNums.append(i)
        total += i

print(goodNums)
print(total)
input("press something")
