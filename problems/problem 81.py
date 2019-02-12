print("Starting")

file = open("matrix.txt")

matrix = []
for x in file:
    line = []
    x = x.strip()
    tokens = x.split(",")
    for i in tokens:
        line.append(int(i))
    matrix.append(line)

sumMatrix = []
for row in range(0,80):
    line = []
    for col in range(0,80):
        if row == 0:
            entrie = 0
            for i in range(0,col+1):
                entrie += matrix[0][i]
            line.append(entrie)
        else:
            if col == 0:
                entrie = 0
                for i in range(0,row+1):
                    entrie += matrix[i][0]
                line.append(entrie)
            else:
                entrie = matrix[row][col] + min(line[len(line)-1],sumMatrix[row-1][col])
                line.append(entrie)
    sumMatrix.append(line)

print(sumMatrix[79][79])

input("Done")
