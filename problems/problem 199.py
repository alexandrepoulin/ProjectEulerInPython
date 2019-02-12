print("Starting")

import math, useful

iterations = 10

answer = 3*(2*math.sqrt(3)-3)**2

k1 = -1
k2 = 1/(2*math.sqrt(3)-3)
k3 = k2
k4 = k3

circles = [] ## [multiplicity, curvature, curvature of parents (3 times)]
circles.append([1, 13.928203230275514, 2.1547005383792524, 2.1547005383792524, 2.1547005383792524])
circles.append([3, 4.464101615137759, -1, 2.1547005383792524, 2.1547005383792524])
for c in circles:
        answer += c[0]/c[1]**2
circlesSimpl = []

def FindChildren(p1,p2,p3):
    return p1+p2+p3+2*math.sqrt(p1*p2+p1*p3+p2*p3)


for i in range(iterations-1):
    print(i+1)
    newCircles = []
    newCirclesSimpl = []
    for c in circles:
        for j in range(2,4):
            for k in range(j+1,5):
                temp1 = [c[1],c[j],c[k]]
                temp1.sort()
                temp2 = [FindChildren(c[1],c[j],c[k])]
                temp2.extend(temp1)
                mult = c[0]
                if temp2 in newCirclesSimpl:
                    newCircles[newCirclesSimpl.index(temp2)][0]+=mult
                else:
                    newCirclesSimpl.append(temp2)
                    temp3 = [mult]
                    temp3.extend(temp2)
                    newCircles.append(temp3)
    for c in newCircles:
        answer += c[0]/c[1]**2
    circles = newCircles
    circlesSimpl = newCirclesSimpl

print(1-answer)
        

