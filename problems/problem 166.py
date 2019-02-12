print("Starting")

#this problem has 10 equations and 2 unknowns which vary from 0 to 9 The equations are
#d_(4q)+d_(4q+1)+d_(4q+2)+d_(4q+3) = 12 for q = 0,1,2,3
#d_(q)+d_(q+4)d_(q+2*4)+d_(q+3*4) = 12 for q = 0,1,2,3
#d_0+d_5+d_10+d_15 =12
#d_3+d_6+d_9+d_12 = 12

#I need to make a matrix with these 12 variables (10 by 16)
#Then I need to reduce the matrix to RREF
#This will give me 10 equations in terms of 6 variables (turns out it gives 7 variables)
#which I can use to generate all of the other variables.

import useful

Matrix = []

for q in range(0,4):
    line1 = []
    line2 = []
    for i in range(0,16):
        if i == 4*q:
            line1.append(1)
        elif i == 4*q+1:
            line1.append(1)
        elif i == 4*q+2:
            line1.append(1)
        elif i == 4*q+3:
            line1.append(1)
        else:
            line1.append(0)
        if i == q:
            line2.append(1)
        elif i == q+4:
            line2.append(1)
        elif i == q+8:
            line2.append(1)
        elif i == q+12:
            line2.append(1)
        else:
            line2.append(0)
    line1.append(1)
    line2.append(1)
    Matrix.append(line1)
    Matrix.append(line2)
Matrix.append([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1]) ##first diagonal equation
Matrix.append([0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1]) ##second diagonal equation

temp = useful.RREF(Matrix)
RREF = useful.intMatrix(temp[0])
pivots = temp[1]
numPivots = len(pivots)
counter = 0

print("Matrix Solved")

for d in range(0,9*4+1):
    print("The current d is: ",d)
    for d1 in range(0,10):
        if d1 > d:
            continue
        if d1 < d-27:
            continue
        for d2 in range(0,10):
            if d2 > d:
                continue
            if d2 < d-27:
                continue
            for d3 in range(0,10):
                if d3 > d:
                    continue
                if d3 < d-27:
                    continue
                if -d1-d2-d3 +d <0:
                    continue
                if -d1-d2-d3 +d >9:
                    continue
                for d4 in range(0,10):
                    if d4 > d:
                        continue
                    if d4 < d-27:
                        continue
                    for d5 in range(0,10):
                        if d5 > d:
                            continue
                        if d5 < d-27:
                            continue
                        if d5+d2>d:
                            continue
                        if d5+d2<d-18:
                            continue
                        if d5+d1>d:
                            continue
                        if d5+d1<d-18:
                            continue
                        for d6 in range(0,10):
                            if d6 > d:
                                continue
                            if d6 < d-27:
                                continue
                            if -d6-d5-d4+d<0:
                                continue
                            if -d6-d5-d4+d>9:
                                continue
                            if d6+d3>d:
                                continue
                            if d6+d3<d-18:
                                continue
                            for d7 in range(0,10):
                                if d7 > d:
                                    continue
                                if d7 < d-27:
                                    continue
                                if -d7-d4-d1+d<0:
                                    continue
                                if -d7-d4-d1+d>9:
                                    continue
                                if d7-d6+d4+d3+d2+2*d1 -d < 0:
                                    continue
                                if d7-d6+d4+d3+d2+2*d1 -d > 9:
                                    continue
                                if -d7-d5-d4-d3-d2-2*d1+2*d <0:
                                    continue
                                if -d7-d5-d4-d3-d2-2*d1+2*d >9:
                                    continue
                                if -d7+d6+d5<0:
                                    continue
                                if -d7+d6+d5>9:
                                    continue
                                if -d7+d6-d5-d4-d3-2*d2-2*d1+2*d<0:
                                    continue
                                if -d7+d6-d5-d4-d3-2*d2-2*d1+2*d>9:
                                    continue
                                if d7-d6+d5+d4+d2+2*d1 -d <0:
                                    continue
                                if d7-d6+d5+d4+d2+2*d1 -d >9:
                                    continue
                                if d7+d4+d3+d2+d1-d <0:
                                    continue
                                if d7+d4+d3+d2+d1-d >9:
                                    continue
                                sol = [d7,d6,d5,d4,d3,d2,d1]
                                s = useful.solM(RREF,pivots,sol,d)
                                good = True
                                for i in s:
                                    if i < 0 or i > 9:
                                        good = False
                                if good:        
                                    counter += 1

print(counter)
input("Done")



