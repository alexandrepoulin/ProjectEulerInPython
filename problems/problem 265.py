print("Starting")

start = [0,0,0,0,0,1]
startingLists = [0,1]
N = 5

##start = [0,0,0,1]
##startingLists = [0,1]
##N = 3

length = 2**N

def listToDec(x):
    answer = 0
    for i in range(len(x)-1,-1,-1):
        answer += 2**(len(x)-1-i)*x[i]
    return answer

def recur(current,currentLists):
    if len(current) == length:
        for i in range(1,N):
            test = current[len(current)-N+i:]
            test.extend(current[:i])
            if listToDec(test) in currentLists:
                return 0
            currentLists.append(listToDec(test))
        return listToDec(current)
    current1 = current.copy()
    currentLists1 = currentLists.copy()
    current2 = current.copy()
    currentLists2 = currentLists.copy()
    current1.append(0)
    current2.append(1)
    answer = 0
    if listToDec(current1[len(current1)-N:]) not in currentLists:
        currentLists1.append(listToDec(current1[len(current1)-N:]))
        answer += recur(current1,currentLists1)
    if listToDec(current2[len(current2)-N:]) not in currentLists:
        currentLists2.append(listToDec(current2[len(current2)-N:]))
        answer += recur(current2,currentLists2)
    return answer

print(recur(start,startingLists))
