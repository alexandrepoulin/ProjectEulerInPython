print("Starting")

import useful

##for an n by m wall

n = 32
m = 10

##the blocks are 2 by 1 and 3 by 1
##the possible combinations will be the following
comb = []

current = []
while sum(current) < n:
    current.append(2)
while 2 in current:
    if sum(current) == n:
        comb.append(current.copy())
        del current[0]
        current.append(3)
        del current[0]
        current.append(3)
        del current[0]
    elif sum(current) > n:
        del current[0]
    elif sum(current) < n:
        current.append(3)
if sum(current) == n and current not in comb:
    comb.append(current.copy())

print("Found base comb", len(comb))

allComb = []
for c in comb:
    allComb.extend(useful.perm(c))
    
print("Found All Comb", len(allComb))

##checks if allComb[i] works with allComb[j]
def check(i,j):
    if i == j:
        return False
    sumsI = set()
    sumsJ = set()
    runningTotalI=0
    runningTotalJ=0
    for k in range(len(allComb[i])):
        runningTotalI += allComb[i][k]
        sumsI.add(runningTotalI)
    for k in range(len(allComb[j])):
        runningTotalJ += allComb[j][k]
        sumsJ.add(runningTotalJ)
    if len(sumsI.intersection(sumsJ)) != 1:
        return False
    return True

compatible = []
for i in range(len(allComb)):
    currentComb = []
    if (i%50) == 0:
        print(i,"out of",len(allComb))
    for j in range(len(allComb)):
        if check(i,j):
            currentComb.append(j)
    compatible.append(currentComb)

print("Found compatible")

#want to keep that of each comb
#need array of m
#each entry of m is an array of len(allComb)
#each entry in those arrays will be the running total

layers = []
layer0 = []
for i in range(len(allComb)):
    layer0.append(1)
layers.append(layer0)
for i in range(1,m):
    layer = []
    if (i%50) == 0:
        print(i,"out of",len(allComb))
    for j in range(len(allComb)):
        runningTotal = 0
        for k in compatible[j]:
            runningTotal += layers[i-1][k]
        layer.append(runningTotal)
    layers.append(layer)

print("Found layers")

answer = 0
for i in range(len(allComb)):
    answer += layers[len(layers)-1][i]

print(answer)
input("Done")
