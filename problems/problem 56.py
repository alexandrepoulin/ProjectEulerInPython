print("Starting")

def getSum(x):
    answer = 0
    for i in str(x):
        answer += int(i)
    return answer

maxSum = 0

for a in range(2,100):
    print(a)
    for b in range(2,100):
        s = getSum(a**b)
        if s>maxSum:
            maxSum = s

print(maxSum)
input("done")
