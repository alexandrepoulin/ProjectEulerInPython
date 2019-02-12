print("Starting")
from mpmath import *
mp.dps = 120
sigfigs = 120

numbers = [x for x in range(2,100)]
numbers = [x for x in filter(lambda k: sqrt(k) != int(sqrt(k)), numbers)]
numbers = [x for x in map(lambda k: sqrt(k), numbers)]

answer = 0
for num in numbers:
    for i in range(0,101):
        if str(num)[i] == ".":
            continue
        answer += int(str(num)[i])

print(answer)

