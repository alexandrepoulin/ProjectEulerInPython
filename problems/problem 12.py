print("Starting...")

numberCounter = 1
factorCounter = 0

previousNumber = 1
newNumber = 0

import math

while factorCounter < 500:
    numberCounter+=1
    newNumber = previousNumber + numberCounter
    for i in range(1,math.ceil(math.pow(newNumber+1,0.5))):
        if newNumber%i == 0:
            factorCounter+=2
    if factorCounter < 500:
        factorCounter = 0
    previousNumber = newNumber

print(previousNumber)
