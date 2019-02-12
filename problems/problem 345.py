print("Starting")

row1 = [  7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583]
row2 = [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913]
row3 = [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743]
row4 = [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350]
row5 = [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350]
row6 = [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803]
row7 = [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326]
row8 = [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973]
row9 = [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848]
row10 = [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198]
row11 = [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390]
row12 = [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574]
row13 = [ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699]
row14 = [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107]
row15 = [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]

MATRIX = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15]
MAXLENG = 15

##row1 =[  7,  53, 183, 439, 863,]
##row2 =[497, 383, 563,  79, 973,]
##row3 =[287,  63, 343, 169, 583,]
##row4 =[627, 343, 773, 959, 943,]
##row5 =[767, 473, 103, 699, 303,]
##MATRIX = [row1,row2,row3,row4,row5]
##MAXLENG = 5

#[3,4]

def inc(x):
    newX = []
    length = len(x)
    for i in range(length):
        currentMax = 0
        for j in range(MAXLENG-1,-1,-1):
            if j not in x[:length-i-1]:
                currentMax = j
                break
        if x[length-i-1] < currentMax:
            newX = x[:length-i-1]
            currentNum = x[length-i-1] 
            for j in range(currentNum+1,MAXLENG):
                if j not in newX:
                    newX.append(j)
                    break
        elif x[length-i-1] > x[length-i-2] and i != (length-1):
            newX = x[:length-i-2]
            currentNum = x[length-i-2]
            for j in range(currentNum+1,MAXLENG):
                if j not in newX:
                    newX.append(j)
                    break
        else:
            continue
        if len(newX)==length:
            break
        for j in range(MAXLENG):
            if j not in newX:
                newX.append(j)
                if len(newX)==length:
                    break
        break
    return newX

columnsForRow = [] ##selected column for each row
for i in range(MAXLENG):
    columnsForRow.append(i)

#numCycles = MAXLENG+1
numCycles = 5+1

for cycle1 in range(2,numCycles):
    print(cycle1)
    for cycle in range(2,cycle1+1):
        numbers = []
        for j in range(cycle):
            numbers.append(j)
        while True:
            val = 0
            for i in range(cycle):
                val -= MATRIX[numbers[i]][columnsForRow[numbers[i]]]
                if i != (cycle -1):
                    val += MATRIX[numbers[i]][columnsForRow[numbers[i+1]]]
                else:
                    val += MATRIX[numbers[i]][columnsForRow[numbers[0]]]
            if val > 0:
                temp = columnsForRow[numbers[0]]
                for i in range(cycle):
                    if i != (cycle -1):
                        columnsForRow[numbers[i]] = columnsForRow[numbers[i+1]]
                    else:
                        columnsForRow[numbers[i]] = temp
            nextNumbers = inc(numbers)
            if nextNumbers == []:
                break
            numbers = nextNumbers
        print(columnsForRow)
        sumVals = 0
        for i in range(MAXLENG):
            sumVals += MATRIX[i][columnsForRow[i]]
    print(sumVals)

answer = 0
for i in range(MAXLENG):
    answer += MATRIX[i][columnsForRow[i]]

print(answer)
    
