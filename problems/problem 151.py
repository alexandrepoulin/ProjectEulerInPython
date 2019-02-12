print("Starting")

A2 = 8
A3 = 4
A4 = 2
A5 = 1
papers = [A2,A3,A4,A5]

##define F(batch)=n_2 * A2 + n_3 * A3 + n_4 * A4 + n_5 * A5
##where the n's are the number of sheets left before a batch
##then F(batch) is well defined and F(batch) = F(batch+1)-1

##we know F(16) = 1 only has the solution n_5 = 1
##and F(2) = 15 where all n's = 1
##need to find the possible combinations of n's for a

##finds all the combinations for batches of sum i
combs = [[] for x in range(16)]

def possibleDesendents(x):
    if sum(x) == 0:
        return
    if x in combs[sum(x)]:
        return
    combs[sum(x)].append(x)
    for i in range(len(x)):
        val =x[i]
        if val == A5:
            copy = x.copy()
            del copy[i]
            possibleDesendents(copy)
        if val == A4:
            copy = x.copy()
            del copy[i]
            copy.append(A5)
            copy.sort()
            possibleDesendents(copy)
        if val == A3:
            copy = x.copy()
            del copy[i]
            copy.append(A4)
            copy.append(A5)
            copy.sort()
            possibleDesendents(copy)
        if val == A2:
            copy = x.copy()
            del copy[i]
            copy.append(A3)
            copy.append(A4)
            copy.append(A5)
            copy.sort()
            possibleDesendents(copy)
possibleDesendents(papers)

realMult = [[] for x in range(15)]
realMult.append([[papers,1,0]])

##find the mults for 15 to 8
for i in range(15):
    for j in range(len(combs[i])):
        realMult[i].append([combs[i][j],0,0])
        
##mult will now be the probability, deal with it
for i in range(15,1,-1):
    for comb in combs[i]:
        currentMult = realMult[i][combs[i].index(comb)][1]
        for val in papers:
            if val not in comb:
                continue
            tempProb = currentMult*comb.count(val)/(len(comb))
            if val == A5:
                copy = comb.copy()
                del copy[comb.index(val)]
                realMult[i-1][combs[i-1].index(copy)][1] += tempProb
            if val == A4:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A5)
                copy.sort()
                realMult[i-1][combs[i-1].index(copy)][1] += tempProb
            if val == A3:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A4)
                copy.append(A5)
                copy.sort()
                realMult[i-1][combs[i-1].index(copy)][1] += tempProb
            if val == A2:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A3)
                copy.append(A4)
                copy.append(A5)
                copy.sort()
                realMult[i-1][combs[i-1].index(copy)][1] += tempProb
    for comb in combs[i]:
        currentMult = realMult[i][combs[i].index(comb)][1]
        current1PaperCount = realMult[i][combs[i].index(comb)][2]
        for val in papers:
            if val not in comb:
                continue
            tempProb = currentMult*comb.count(val)/(len(comb))
            if val == A5:
                copy = comb.copy()
                del copy[comb.index(val)]
                fracProp= tempProb/realMult[i-1][combs[i-1].index(copy)][1]
                if len(copy) == 1:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount+1
                else:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount
            if val == A4:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A5)
                copy.sort()
                fracProp= tempProb/realMult[i-1][combs[i-1].index(copy)][1]
                if len(copy) == 1:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount+1
                else:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount
            if val == A3:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A4)
                copy.append(A5)
                copy.sort()
                fracProp= tempProb/realMult[i-1][combs[i-1].index(copy)][1]
                if len(copy) == 1:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount+1
                else:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount
            if val == A2:
                copy = comb.copy()
                del copy[comb.index(val)]
                copy.append(A3)
                copy.append(A4)
                copy.append(A5)
                copy.sort()
                fracProp= tempProb/realMult[i-1][combs[i-1].index(copy)][1]
                if len(copy) == 1:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount+1
                else:
                    realMult[i-1][combs[i-1].index(copy)][2] += fracProp*current1PaperCount

answer = realMult[2][0][2]*realMult[2][0][1]+realMult[2][1][2]*realMult[2][1][1]
print(answer)
input("Done")
    
