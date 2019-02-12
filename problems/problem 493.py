print("starting")

def p(results,i,sumSoFar):
    return (10-results[i])/(70-sumSoFar)

def pnew(results,sumSoFar):
    return (70-len(results)*10)/(70-sumSoFar)

def getNewDict(sumSoFar,prev):
    newDict= dict()
    for x in prev:
        prob=prev[x]
        if type(x) is int:
            tempx=[x]
            if x <=9: 
                newtuple = (x+1)
                if newtuple in newDict:
                    newDict[newtuple]+=p(tempx,0,sumSoFar)*prob
                else:
                    newDict[newtuple]=p(tempx,0,sumSoFar)*prob
            newtuple = (x,1)
            if newtuple in newDict:
                newDict[newtuple]+=pnew(tempx,sumSoFar)*prob
            else:
                newDict[newtuple]=pnew(tempx,sumSoFar)*prob
            
        else:
            for i in range(len(x)):
                if x[i] <=9:
                    newtuple = list(x)
                    newtuple[i]+=1
                    newtuple.sort()
                    newtuple.reverse()
                    newtuple=tuple(newtuple)
                    if newtuple in newDict:
                        newDict[newtuple]+=p(x,i,sumSoFar)*prob
                    else:
                        newDict[newtuple]=p(x,i,sumSoFar)*prob
            if len(x)<=6:
                newtuple = list(x)
                newtuple.append(1)
                newtuple.sort()
                newtuple.reverse()
                newtuple=tuple(newtuple)
                if newtuple in newDict:
                    newDict[newtuple]+=pnew(x,sumSoFar)*prob
                else:
                    newDict[newtuple]=pnew(x,sumSoFar)*prob
    return newDict

def call(stuff,n):
    if n == 20:
        return stuff
    newStuff = getNewDict(n,stuff)
    return call(getNewDict(n,stuff),n+1)

start={(1):1}
sumSoFar=1
lastDict = call(start,sumSoFar)

answer = 0
for i in lastDict:
    if type(i) is int:
        answer +=lastDict[i]
    else:
        answer += len(i)*lastDict[i]

print(answer)
    
    

