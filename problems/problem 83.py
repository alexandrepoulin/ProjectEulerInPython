print("Starting")

file = open("matrix.txt")

matrix = []
for line in file:
    line = line.strip()
    tokens = line.split(',')
    row = []
    for num in tokens:
        row.append(int(num))
    matrix.append(row)

sumMatrix = []




visited = []

for row in range(0,80):
    lineSum = []
    lineVis = []
    for col in range(0,80):
        lineSum.append(99999999999999)
        lineVis.append(False)
    sumMatrix.append(lineSum)
    visited.append(lineVis)
    
sumMatrix[0][0] = matrix[0][0]

current = [0,0]

while current != [79,79]:
    #print(current)
    if current[0]-1 >= 0 and current[0]-1 <= 79 and not visited[current[0]-1][current[1]]:
        value = sumMatrix[current[0]][current[1]]+matrix[current[0]-1][current[1]]
        if value < sumMatrix[current[0]-1][current[1]]:
            sumMatrix[current[0]-1][current[1]] = value
            
    if current[0]+1 >= 0 and current[0]+1 <= 79 and not visited[current[0]+1][current[1]]:
        value = sumMatrix[current[0]][current[1]]+matrix[current[0]+1][current[1]]
        if value < sumMatrix[current[0]+1][current[1]]:
            sumMatrix[current[0]+1][current[1]] = value
            
    if current[1]-1 >= 0 and current[1]-1 <= 79 and not visited[current[0]][current[1]-1]:
        value = sumMatrix[current[0]][current[1]]+matrix[current[0]][current[1]-1]
        if value < sumMatrix[current[0]][current[1]-1]:
            sumMatrix[current[0]][current[1]-1] = value
            
    if current[1]+1 >= 0 and current[1]+1 <= 79 and not visited[current[0]][current[1]+1]:
        value = sumMatrix[current[0]][current[1]]+matrix[current[0]][current[1]+1]
        if value < sumMatrix[current[0]][current[1]+1]:
            sumMatrix[current[0]][current[1]+1] = value

    visited[current[0]][current[1]] = True

    bestValue = 99999999999999
    bestCandidate = []
    for row in range(0,80):
        for col in range(0,80):
            if sumMatrix[row][col] < bestValue and not visited[row][col]:
                bestValue = sumMatrix[row][col]
                bestCandidate = [row,col]
    current = bestCandidate


print(sumMatrix[79][79])
input("Done")

    

    
    
            
        
        
