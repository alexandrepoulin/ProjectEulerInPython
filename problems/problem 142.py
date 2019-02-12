print("Starting")
import math
a= 0
parity = 0

def checkOthers(x,y,z):
    if int(math.sqrt(y+z)) != math.sqrt(y+z):
        return False
    if int(math.sqrt(x+z)) != math.sqrt(x+z):
        return False
    if int(math.sqrt(x-z)) != math.sqrt(x-z):
        return False
    return True
answer = []
found = False
while True:
    print(a)
    a += 1
    parity = a%2
    for b in range(2-parity,a,2):
        x = (a**2+b**2)/2.0
        y = (a**2-b**2)/2.0
        for d in range(1, math.ceil(math.sqrt(y))):
            z = y-d**2
            if checkOthers(x,y,z):
                answer = [x,y,z]
                found = True
                break
        if found:
            break
    if found:
        break
print(answer)
print(sum(answer))

input("Done")
