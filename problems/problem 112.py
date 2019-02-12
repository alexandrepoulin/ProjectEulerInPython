print("Starting")

RATIO = 0.99

def isInc(x):
    stringOfNumber = str(x)
    for i in range(1,len(stringOfNumber)):
        if int(stringOfNumber[i]) < int(stringOfNumber[i-1]):
            return False
    return True

def isDec(x):
    stringOfNumber = str(x)
    for i in range(1,len(stringOfNumber)):
        if int(stringOfNumber[i]) > int(stringOfNumber[i-1]):
            return False
    return True

bouncyCount = 0
counter = 0
while True:
    counter += 1
    if not isInc(counter) and not isDec(counter):
        bouncyCount += 1
    rat = bouncyCount/(counter)
    print(rat)
    if rat >= RATIO:
        break

print(counter)
input("Done")
