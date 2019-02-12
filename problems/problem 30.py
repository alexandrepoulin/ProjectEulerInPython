print("Starting")

total = 0

def getNums(x):
    text = str(x)
    nums = []
    for i in range(0,len(text)):
        nums.append(int(text[i]))
    return nums

def add(x):
    sumSoFar = 0
    for i in range(0,len(x)):
        sumSoFar+=x[i]**5
    return sumSoFar


for i in range(10,1000000):
    print(i)
    if add(getNums(i)) == i:
        total+=i

print(total)

input("Press something to stop")
