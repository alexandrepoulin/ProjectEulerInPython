print("Starting")

grid = []

def findMax(x):
    seq = []
    firstSign = 1 if x[0]>=0 else -1
    currentSign = firstSign
    currentTotal = 0
    for i in range(len(x)):
        if x[i]*currentSign >= 0:
            currentTotal += x[i]
        else:
            if currentSign == 1:
                currentSign = -1
                seq.append(currentTotal)
                currentTotal = x[i]
            else:
                currentSign = 1
                seq.append(currentTotal)
                currentTotal = x[i]
    if currentSign == 1:
        seq.append(currentTotal)
    if firstSign == -1:
        seq = seq[1:]
    changed = True
    lastChange = 1
    while changed:
        changed = False
        for i in range(0,len(seq)-2):
            if i%2 == 0:
                temp = seq[i]+seq[i+1]+seq[i+2]
                if temp >= seq[i] and temp > seq[i+2]:
                    seq = seq[:i] + [temp] + seq[i+3:]
                    changed = True
                    lastChange = i
                    break
            else:
                if abs(seq[i])>seq[i+1] and abs(seq[i+2])>seq[i+1]:
                    seq = seq[:i] + [seq[i]+seq[i+1]+seq[i+2]] + seq[i+3:]
                    changed = True
                    lastChange = i
                    break
    if len(seq) == 0:
        return 0
    return max(seq)    
            
for k1 in range(2000):
    row = []
    for k2 in range(1,2001):
        k = 2000*k1+k2
        if k <= 55:
            row.append((100003-200003*k+300007*k**3)%1000000 - 500000)
        elif k2 <= 24:
            row.append((grid[-1][2000+k2-25]+grid[-1][2000+k2-56]+1000000)%1000000 - 500000)
        elif k2 <= 55:
            row.append((row[k2-25]+grid[-1][2000+k2-56]+1000000)%1000000 - 500000)
        else:
            row.append((row[k2-25]+row[k2-56]+1000000)%1000000 - 500000)
    grid.append(row)

bestSum = 0
print("Done making grid")


##columns
for col in range(2000):
    temp1 = [j[col] for j in grid]
    temp2 = findMax(temp1)
    if temp2 > bestSum:
        bestSum = temp2
print("Done cols", bestSum)

##rows
for j in range(len(grid)):
    temp = findMax(grid[j])
    if temp > bestSum:
        bestSum = temp
print("Done Rows", bestSum)

##diagonals
for i in range(2000):
    temp1 = [grid[j][i-j] for j in range(i+1)]
    temp2 = findMax(temp1)
    if temp2 > bestSum:
        bestSum = temp2
for i in range(1,2000):
    temp1 = [grid[i+j][1999-j] for j in range(2000-i)]
    temp2 = findMax(temp1)
    if temp2 > bestSum:
        bestSum = temp2
print("Done dia", bestSum)

##antidiagonals
for i in range(2000):
    temp1 = [grid[i+j][j] for j in range(2000-i)]
    temp2 = findMax(temp1)
    if temp2 > bestSum:
        bestSum = temp2
for i in range(1,2000):
    temp1 = [grid[j][i+j] for j in range(2000-i)]
    temp2 = findMax(temp1)
    if temp2 > bestSum:
        bestSum = temp2
print("Done antidia", bestSum)

print(bestSum)

