import useful as u
import math

maxRange = 10000
numsToCheck = [i+1 for i in range(maxRange)]
del numsToCheck[9998]
  
counter = 0
##theres a special form for 9999 solution
answer = int(11112222222222222222/9999) ##get rid of cunt of a number 9999

log = 0


while len(numsToCheck) != 0:
    counter += 1
    base3 = u.baseConvertNumNum(counter,10,3)
    if math.floor(math.log(base3,10))!=log:
        log = math.floor(math.log(base3,10))
        print(log,base3, len(numsToCheck),counter)
    toRemove = []
    for i in range(len(numsToCheck)):
        if base3%numsToCheck[i] == 0:
            toRemove.append(i)
            answer += int(base3 / numsToCheck[i])
    toRemove.sort()
    toRemove=toRemove[::-1]
    for r in toRemove:
        del numsToCheck[r]
    
print(answer)
