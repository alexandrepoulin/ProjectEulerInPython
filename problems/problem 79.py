print("Starting")

file = open("keylog.txt")

entries = []

numsUsed = set()

for line in file:
    line = line.strip()
    entries.append(line)
    for i in str(line):
        numsUsed.add(i)
file.close()

removed = set()
answer = ""

while numsUsed:
    currentBest = ""
    for x in entries:
        x = x.strip()
        if x[0] in removed and x[1] in removed and x[2] in removed:
            continue
        elif x[0] in removed and x[1] in removed:
            currentVal = x[2]
        elif x[0] in removed:
            currentVal = x[1]
        else:
            currentVal = x[0]
        bestFound = True
        for y in entries:
            y = y.strip()
            if currentVal not in y:
                continue
            indexY = y.index(currentVal)
            if indexY == 0:
                continue
            if indexY == 1 and y[0] in removed:
                continue
            if indexY == 2 and y[0] in removed and y[1] in removed:
                continue
            if y[0] in removed and y[1] in removed and [2] in removed:
                continue
            bestFound = False
            break
        if bestFound:
            currentBest = currentVal
            break
    answer += currentBest
    removed.add(str(currentBest))
    numsUsed.difference_update(removed)

print(answer)
input("Done")
            
                
    
