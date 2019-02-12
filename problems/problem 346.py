import math

MAX=10**12
##MAX=1000
maxB = int(math.sqrt(MAX))+1

def toBase10(b,x):
    answer = 0
    for i in range(len(x)):
        answer += int(x[-i-1])*b**i
    return answer

reps = set()

for b in range(2,maxB):
    numlist = ["1","1","1"]
    while True:
        num = toBase10(b,numlist)
        if num > MAX:
            break
        reps.add(num)
        numlist.append("1")

print(sum(reps)+1)
