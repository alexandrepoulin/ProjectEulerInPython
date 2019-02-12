print("starting")

import random

for k in range(100,0,-1):
    for T in range(1,12):
        numberOfTurns = 0
        numberOfPoints = 0
        while numberOfPoints < k:
            good = True
            for i in range(T):
                if random.random() >0.5:
                    good = False
                    break
            if good:
                numberOfPoints+= 2**(T-1)
            numberOfTurns += 1
        print(k,T,numberOfTurns)

        
