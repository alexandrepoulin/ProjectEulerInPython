print("Starting")

diceRollCombs = []

diceRolled = 5
diceSides = 6
numWanted = 15

for i in range(3):
    newCombs = []
    made = set()
    for j in range(1,diceSides+1):
        if i == 0:
            newCombs.append([j,1])
        else:
            for k in diceRollCombs:
                temp = k[0] + j
                if temp in made:
                    for comb in newCombs:
                        if comb[0] == temp:
                            comb[1] += k[1]
                            break
                else:
                    newCombs.append([temp,1])
                    made.add(temp)
    #print(newCombs)
    diceRollCombs = newCombs

for comb in diceRollCombs:
    if comb[0] == numWanted:
        print(comb[1])
        break
    
    
                    
