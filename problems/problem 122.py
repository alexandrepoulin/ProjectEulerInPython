print("Starting")

import math

def NextIterations(x,i): #x is a list of sets
    newList = []
    for s in x:
        for e1 in s:
            for e2 in s:
                if e1 > e2:
                    continue
                if (e1+e2) > 200:
                    continue
                if i >= 8:
                    if answer[e1+e2] != 20:
                        continue
                if answer[e1+e2] > i:
                    answer[e1+e2] = i
                newSet = s.copy()
                newSet.add(e1+e2)
                if newSet not in x and newSet not in newList:
                    newList.append(newSet)
    return newList

answer = [20]*201
answer[0] = 0
answer[1] = 0

first = set()
first.add(1)

iterations = [[first]]

for i in range(1,12):
    iterations.append(NextIterations(iterations[i-1],i))

total = 0
for i in range(0,201):
    print(i,answer[i])
    if answer[i] == 20:
        total+= 12
    else:
        total+=answer[i]

print(total)
input("Done")
