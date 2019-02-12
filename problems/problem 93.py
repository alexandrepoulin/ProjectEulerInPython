print("Starting")

import useful

brackets = [[1,1,1,1],[2,1,1],[1,2,1],[1,1,2],[3,1],[1,3]]


def nextList(x):
    nums = []
    for i in x:
        nums.append(i)
    nums.sort()
    for i in range(0,4):
        if nums[-i-1] != 9 and nums[-i-1]+1 not in nums:
            nums[-i-1] += 1
            for k in range(0,i+1):
                nums[-i-1+k] = nums[-i-1]+k
            break
    return nums

def nextCounter(x):
    nums = []
    for i in x:
        nums.append(i)
    for i in range(0,4):
        if nums[-i-1] != 3:
            nums[-i-1] += 1
            for k in range(0,i):
                nums[-i+k] = 0
            break
    return nums

def check(x):
    perms = useful.perm(x)
    numbers = set()
    for p in perms:
        for b in brackets:
            counters = []
            nextCount = [0,0,0,0]
            while nextCount[0] != 3:
                counter = nextCount
                numbers.add(operate(p,b,counter))
                nextCount = nextCounter(counter)
    count = 0
    while True:
        count += 1
        if count not in numbers:
            break
    return count-1
        
        

def operate(abcd,bracket,counter):
    newCounter = []
    for i in counter:
        newCounter.append(i)
    newABCD = []
    for i in abcd:
        newABCD.append(i)
    finalAnswer = 0
    try:
        for k in range(0,len(bracket)):
            if bracket[-k-1] > 1:
                if bracket[-k-1] == 2:
                    if newCounter[-k-1] == 0:
                        newABCD[-k+bracket[-k-1]]+=newABCD[-k+bracket[-k-1]+1]
                        del newCounter[-k-1]
                    elif newCounter[-k-1] == 1:
                        newABCD[-k+bracket[-k-1]]-=newABCD[-k+bracket[-k-1]+1]
                        del newCounter[-k-1]
                    elif newCounter[-k-1] == 2:
                        newABCD[-k+bracket[-k-1]]*=newABCD[-k+bracket[-k-1]+1]
                        del newCounter[-k-1]
                    elif newCounter[-k-1] == 3:
                        newABCD[-k+bracket[-k-1]]/=newABCD[-k+bracket[-k-1]+1]
                        del newCounter[-k-1]
                    del newABCD[-k+bracket[-k-1]+1]
                if bracket[-k-1] == 3:
                    counts = 0
                    for j in range(1,3):
                        if counts < 2 and newCounter[-k-2+j] == 2:
                            newABCD[-k-2+j]*=newABCD[-k-1+j+counts]
                            del newCounter[-k-2+j]
                            del newABCD[-k-1+j+counts]
                            counts +=1
                        if counts < 2 and newCounter[-k-2+j] == 3:
                            newABCD[-k-2+j]/=newABCD[-k-1+j+counts]
                            del newCounter[-k-2+j]
                            del newABCD[-k-1+j+counts]
                            counts +=1
                    if counts < 2:
                        counts2 = 0
                        for j in range(1,bracket[-k-1]-counts):
                            if counts + counts2 <2 and newCounter[-k-2+j] == 0:
                                newABCD[-k-2+j]+=newABCD[-k-1+j-counts2]
                                del newCounter[-k-2+j]
                                del newABCD[-k-1+j-counts2]
                                counts2 += 1
                            if counts + counts2 <2 and newCounter[-k-2+j] == 1:
                                newABCD[-k-2+j]-=newABCD[-k-1+j-counts2]
                                del newCounter[-k-2+j]
                                del newABCD[-k-1+j-counts2]
                                counts2 += 1
        if counter[0] == 1:
            finalAnswer = -newABCD[0]
        else:
            finalAnswer = newABCD[0]
        for m in range(1,len(newABCD)):
            if newCounter[m] == 0:
                finalAnswer+=newABCD[m]
            if newCounter[m] == 1:
                finalAnswer-=newABCD[m]
            if newCounter[m] == 2:
                finalAnswer*=newABCD[m]
            if newCounter[m] == 3:
                finalAnswer/=newABCD[m]
    except ZeroDivisionError:
        pass
    return finalAnswer


abcd = []
nextABCD = [1,2,3,4]
bestSoFar = 0
bestABCD = [] 

while nextABCD != abcd:
    abcd = nextABCD
    number = check(abcd)
    print(abcd)
    if number > bestSoFar:
        bestSoFar = number
        bestABCD = abcd
    nextABCD = nextList(abcd)

print(bestSoFar)
print(bestABCD)
input("Done")
    
    
