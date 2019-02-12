## should be x = d(1+-sqrt(2-n))

import dioph
## use dioph like print(solve(4,0,-1,0,0,-27))

##requiring that 4d^2-q^2-n=0 for some n.
##loop through n, take the solutions with possitive q and d
##that will be the number of solutions.

## (x+2d)^2-(x+d)^2-x^2=n
## x^2+4dx+4d^2-x^2-2dx-d^2-x^2-n=0
## x^2-2dx-3d^2+n=0
## x= d +- sqrt(d^2+3d^2-n)
## x= d +- sqrt(4d^2-n)
## need 4d^2-n = q^2
## 4d^2 - q^2 - n = 0


print("Starting")

answer = 0

def test(solution,n):
    counter = 0
    x = solution[0]-solution[1]
    if x>0:
        if ((x+2*solution[0])**2-(x+solution[0])**2-x**2) == n:
            counter+=1
    if solution[1] != 0:
        x = solution[0]+solution[1]
        if x>0:
            if ((x+2*solution[0])**2-(x+solution[0])**2-x**2) == n:
                counter+=1
    return counter

for i in range(1154,10**6):
    if (i%10000)==0:
        print(i)
    solutions = dioph.solve(4,0,-1,0,0,-i) ##4d^2-q^2-n=0
    solutions = list(filter(lambda k: k[0]>0 and k[1]>=0, solutions))
    reducedSolutions = []
    for x in solutions:
        if x not in reducedSolutions:
            reducedSolutions.append(x)
    counter = 0
    for x in reducedSolutions:
        if x[1] == 0:
            counter+=1
        elif x[1]< x[0]:
            counter += 2
        else:
            counter+=1
        ##counter+=test(x,i)
        if counter >=11:
            break
    if counter == 10:
        answer+=1

print(answer)
input("done")
