print("Start")

import math, random

iterations = 1
rings = 50

total = 0

for k in range(iterations):
    grid = []
    for i in range(30):
        line = []
        for j in range(30):
            line.append(1)
        grid.append(line)
    for i in range(rings):
        print(i)
        for row in range(30):
            for col in range(30):
                for j in range(grid[row][col]):
                    rand = random.random()
                    print(math.floor(2*rand))
                    if row == 0:
                        if col ==0:
                            temp = math.floor(2*rand)
                            if temp==0:
                                grid[row+1][col] += 1
                            else:
                                grid[row][col+1] += 1
                        elif col == 29:
                            temp = math.floor(2*rand)
                            if temp==0:
                                grid[row+1][col] += 1
                            else:
                                grid[row][col-1] += 1
                        else:
                            temp = math.floor(3*rand)
                            if temp==0:
                                grid[row+1][col] += 1
                            elif temp == 1:
                                grid[row][col-1] += 1
                            else:
                                grid[row][col+1] += 1
                    if row == 29:
                        if col ==0:
                            temp = math.floor(2*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            else:
                                grid[row][col+1] += 1
                        elif col == 29:
                            temp = math.floor(2*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            else:
                                grid[row][col-1] += 1
                        else:
                            temp = math.floor(3*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            elif temp == 1:
                                grid[row][col-1] += 1
                            else:
                                grid[row][col+1] += 1
                    else:
                        if col ==0:
                            temp = math.floor(3*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            elif temp == 1:
                                grid[row+1][col] += 1
                            else:
                                grid[row][col+1] += 1
                        elif col == 29:
                            temp = math.floor(2*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            elif temp == 1:
                                grid[row+1][col] += 1
                            else:
                                grid[row][col-1] += 1
                        else:
                            temp = math.floor(4*rand)
                            if temp==0:
                                grid[row-1][col] += 1
                            elif temp == 1:
                                grid[row+1][col] += 1
                            elif temp == 2:
                                grid[row][col-1] += 1
                            else:
                                grid[row][col+1] += 1
                    grid[row][col] = 0
        temp = 0
        for row in range(30):
            for col in range(30):
                if grid[row][col] == 0:
                    temp += 1
        print(temp)
            
    empty = 0
    for row in range(30):
        for col in range(30):
            if grid[row][col] == 0:
                empty += 1
    total += empty

print(total/iterations)



                    
                    
