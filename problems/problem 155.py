print("starting")

maxNum = 10
C=1

vals = [[C]]
valset = set([C])

for i in range(maxNum-1):
    newlist = [] #size i+1
    for k in range(i+1):
        for j in vals[k]:
            for l in vals[i-k]:
                temp1 = round(l+j,4)
                temp2 = round(l*j/(l+j),4)
                if temp1 not in valset:
                    valset.add(temp1)
                    newlist.append(temp1)
                if temp2 not in valset:
                    valset.add(temp2)
                    newlist.append(temp2)
    vals.append(newlist)


print(len(valset))
