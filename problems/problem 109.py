print("Starting")

#total[1dart, 2dart, 3darts]
#dart = [multiplyer, number]
#dart combo will have [ dart1, dart2 ]


total = [] ##keep track of how many 1 dart, 2 dart and 3 dart solutions per index+1
total.append([[],[],[]]) # no ways to end with a score of 1
total.append([[[2,1]],[],[]]) # one way to end with a score of 2

for i in range(3,171):
    current = [[],[],[]]
    for d1 in range(1,21):
        if 2*d1 == i:
            current[0].append([2,d1])
        for m in range(1,4):
            if m*d1 < i:
                for d2 in range(0,len(total[i-m*d1-1][0])):
                    current[1].append([[m,d1],total[i-m*d1-1][0][d2]])
                    #print(d1,total[i-m*d1-1][0][d2])
                for d3 in range(0,len(total[i-m*d1-1][1])):
                    #print("here",[m,d1],total[i-m*d1-1][1][d3][0])
                    if m*d1 < total[i-m*d1-1][1][d3][0][0]*total[i-m*d1-1][1][d3][0][1] or (m*d1 == total[i-m*d1-1][1][d3][0][0]*total[i-m*d1-1][1][d3][0][1] and d1 < total[i-m*d1-1][1][d3][0][1]):
                        #print("if")
                        if [[m,d1],total[i-m*d1-1][1][d3][0],total[i-m*d1-1][1][d3][1]] not in current[2]:
                            current[2].append([[m,d1],total[i-m*d1-1][1][d3][0],total[i-m*d1-1][1][d3][1]])
                    else:
                        #print("else")
                        if [total[i-m*d1-1][1][d3][0],[m,d1],total[i-m*d1-1][1][d3][1]] not in current[2]:
                            current[2].append([total[i-m*d1-1][1][d3][0],[m,d1],total[i-m*d1-1][1][d3][1]])
    bull = 25
    if 2*bull == i:
        current[0].append([2,bull])
    for m in range(1,3):
        if m*bull < i:
            for d2 in range(0,len(total[i-m*bull-1][0])):
                current[1].append([[m,bull],total[i-m*bull-1][0][d2]])
            for d3 in range(0,len(total[i-m*bull-1][1])):
                if m*bull < total[i-m*bull-1][1][d3][0][0]*total[i-m*bull-1][1][d3][0][1] or (m*bull == total[i-m*bull-1][1][d3][0][0]*total[i-m*bull-1][1][d3][0][1] and bull < total[i-m*bull-1][1][d3][0][1]):
                    if [[m,bull],total[i-m*bull-1][1][d3][0],total[i-m*bull-1][1][d3][1]] not in current[2]:
                        current[2].append([[m,bull],total[i-m*bull-1][1][d3][0],total[i-m*bull-1][1][d3][1]])
                else:
                    if [total[i-m*bull-1][1][d3][0],[m,bull],total[i-m*bull-1][1][d3][1]] not in current[2]:
                        current[2].append([total[i-m*bull-1][1][d3][0],[m,bull],total[i-m*bull-1][1][d3][1]])
    total.append(current)
    #print(i, current)

answer1 = 0
answer2 = 0
answer3 = 0

for k in range(0,99):
    answer1 += len(total[k][0])
    answer2 += len(total[k][1])
    answer3 += len(total[k][2])

print(answer1, answer2, answer3)
print(answer1+answer2+answer3)



##need to remove doubles like s1s1d2, s1d2d2
