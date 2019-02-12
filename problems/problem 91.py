print("Starting")

solutions = []

def check(x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
        return False
    if y1!=0 and y2!= 0 and x2/y2 == x1/y1:
        return False
    if x2!=0 and x1!= 0 and y1/x1 == y2/x2:
        return False
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return False
    if (y1 == 0 and x2 == 0) or (y2 == 0 and x1 == 0):
        return True
    if (y1 == 0 and x1 == x2 and y2 > 0)  or (y2 == 0 and x1 == x2 and y1 > 0):
        return True
    if (x2 == 0 and y1 == y2 and x1 > 0) or (x1 == 0 and y1 == y2 and x2 > 0):
        return True
    if x1 == y1 and x1 - x2 == y2 - y1:
        return True
    if x2 == y2 and x2 - x1 == y1 - y2:
        return True
    if x1 != 0 and y1 != y2 and y1/x1 == -(x1-x2)/(y1-y2):
        return True
    if x2 != 0 and y1!= y2 and y2/x2 == -(x2-x1)/(y2-y1):
        return True
    return False
counter = 0
for i in range(0,51):
    print(i)
    for j in range(0,51):
        for k in range(0,51):
            for m in range(0,51):
                if check(i,j,k,m):
                    if [i,j,k,m] in solutions or [k,m,i,j] in solutions:
                        continue
                    else:
                        solutions.append([i,j,k,m])
                    

print(len(solutions))
input("Done")
