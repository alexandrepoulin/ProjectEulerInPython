print("Starting")

import useful

factors = useful.factors(250)
factors.append(1)
factors.append(250)
factors.sort()

numbers = list(range(1,251))
powers = []
for i in numbers:
    case = -1
    fac = 0
    for f in factors:
        val = (i**f)%250
        if val == 0:
            case = 0
            fac = f
            break
        if val == 1:
            case = 1
            fac = f
            break
    powers.append([f,case])

numbers = list(range(1,250251))
repeatedNums = [0 for x in range(250)]
numberOfZeros = 0
for i in numbers:
    current = i%250
    if current == 0:
        numberOfZeros +=1
        continue
    if powers[current-1][0] >= i and powers[current-1][1] == 0:
        numberOfZeros +=1
        continue
    currentpow = i%powers[current-1][0]
    repeatedNums[(current**currentpow)%250]+=1

reducedList = []


print(len(reducedList))
combTo250 = []
    
    
