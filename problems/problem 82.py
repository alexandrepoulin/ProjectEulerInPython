print("Starting")

file = open("matrix2.txt")

matrix = []
for line in file:
    row = []
    line = line.strip()
    tokens = line.split(",")
    for x in tokens:
        row.append(int(x))
    matrix.append(row)

sumMatrix = []
## the sum matrix will be going up to down
for col in range(0,80):
    sumCol = []
    for row in range(0,80):
        if col == 0:
            sumCol.append(matrix[row][col])
        else:
            sumCol.append(sumMatrix[col-1][row]+matrix[row][col])
    if col == 0:
        sumMatrix.append(sumCol)
        continue
    for k in range(0,80):
        for i in range(0,80):
            if i == 0:
                sumCol[i] = min(sumCol[i], sumCol[i+1]+matrix[i][col])
            elif i == 79:
                sumCol[i] = min(sumCol[i], sumCol[i-1]+matrix[i][col])
            else:
                sumCol[i] = min(sumCol[i], sumCol[i-1]+matrix[i][col],sumCol[i+1]+matrix[i][col])
    sumMatrix.append(sumCol)

print(min(sumMatrix[79]))
input("Done")
