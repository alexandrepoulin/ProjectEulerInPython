print("Starting")

MAX = 10000

nums = set(range(10, MAX))

def isPal(x):
    return str(x) == str(x)[::-1]

def ite(x):
    return x+int(str(x)[::-1])

count = 0

while len(nums)>0:
    q = nums.pop()
    currentNum = q
    otherNums = [q]
    isLychrel = True
    for i in range(0, 50):
        currentNum = ite(currentNum)
        if isPal(currentNum):
            nums.difference_update(otherNums)
            isLychrel = False
            break
        if currentNum < 10000:
            otherNums.append(currentNum)
    if isLychrel:
        #print(q)
        count += 1

print(count)
input("done")
