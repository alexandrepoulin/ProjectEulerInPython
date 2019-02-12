print("Starting")

total = 0
alreadyFound =[]
factors = []

def skip(x,y): 
    for i in range(1,10):
        count = 0
        for k in range(0,len(str(x))):
            if str(x)[k] == str(i):
                count +=1
        for j in range(0,len(str(y))):
            if str(y)[j] == str(i):
                count +=1
        if count > 1:
            return True
        if "0" in str(y):
            return True
    return False

def shouldCount(x,y,z):
    for i in range(1,10):
        count = 0
        for k in range(0,len(str(x))):
            if str(x)[k] == str(i):
                count +=1
        for j in range(0,len(str(y))):
            if str(y)[j] == str(i):
                count +=1
        for l in range(0,len(str(z))):
            if str(z)[l] == str(i):
                count +=1
        if count != 1:
            return False
    if z in alreadyFound:
        return False
    factors.append([x,y])
    alreadyFound.append(z)
    return True

for i in range(1,100000):
    cont = False
    if "0" in str(i):
        continue
    for l in range(1,10):
        count = 0
        for k in range(0,len(str(i))):
            if str(i)[k] == str(l):
                count +=1
            if count > 1:
                cont = True
                break
        if cont:
            break
    if cont:
        continue
    print(i)
    for j in range(0,100000):
        if skip(i,j):
            continue
        if len(str(i))+len(str(j))+len(str(i*j)) > 9:
            break
        if shouldCount(i,j,i*j):
            total+=i*j



print(total)

input("press something")

            
