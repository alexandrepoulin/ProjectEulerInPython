print("Starting")

maxNum = 9
maxLength = 20

## first number is the lenght LEFT, the second will be the number
## on the left and the third will be the number on the right.
## the fourth number will be the number of solutions for those numbers
Solutions = [[],[]] ##no need for chains of length 0 or 1

solutionArray2 = []
for i in range(10): ##the Left hand number
    iArray = []
    for j in range(0,10): ##the Right hand number
        if (i+j) >maxNum:
            break
        iArray.append(1)
    solutionArray2.append(iArray)
Solutions.append(solutionArray2)

for l in range(3,maxLength+1):
    solutionArray = [] ## solutions will have [i,j,# of solutions]
    minNum = 0
    if l == 20:
        minNum =1
    for i in range(minNum,10): ##the Left hand number (in the lth place)
        iArray = []
        for j in range(0,10): ##the Right hand number (in the (l-1)th place)
            if (i+j) >maxNum:
                break
            numberOfPoss = 0
            for k in range(0,maxNum-i-j+1):
                numberOfPoss += Solutions[l-1][j][k]
            iArray.append(numberOfPoss)
        solutionArray.append(iArray)
    Solutions.append(solutionArray)
                
answer = 0

for i in range(0,9):
    for j in Solutions[20][i]:
        answer += j
print(answer)
input("Done")
    
