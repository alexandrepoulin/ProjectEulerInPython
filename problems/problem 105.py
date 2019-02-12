print("Starting")

file = open("sets.txt")
sets = []

for x in file:
    line = []
    x = x.strip()
    tokens = x.split(",")
    for i in tokens:
        line.append(int(i))
    sets.append(line)

pi = [[],[[0],[1]]] #pi[subsets strings of length i], pi[[subset strings]], pi[[[strings]]]
for i in range(1,12):
    newI = []
    for x in pi[i]:
        newp1 = x.copy()
        newp2 = x.copy()
        newp1.append(0)
        newp2.append(1)
        newI.append(newp1)
        newI.append(newp2)
    pi.append(newI)

answer = 0

for i in range(0,len(sets)):
    skip = False
    print(i+1)
    currentSet = sets[i]
    currentLength = len(currentSet)
    for x in pi[currentLength]:
        set1 = set()
        sum1 = 0
        for k in range(len(x)):
            if x[k] == 1:
                set1.add(currentSet[k])
        sum1 = sum(set1)
        for y in pi[currentLength]:
            set2 = set()
            sum2 = 0
            if x==y:
                continue
            for j in range(len(y)):
                if y[j]==1:
                    set2.add(currentSet[j])
            sum2 = sum(set2)
            if sum1 == sum2:
                skip = True
                break
            if len(set1)>len(set2) and sum2>sum1:
                skip = True
                break
        if skip:
            break
    if not skip:
        answer += sum(currentSet)

print(answer)
input("Done")

