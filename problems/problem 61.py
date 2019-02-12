print("Starting")

def tri(n):
    return int(n*(n+1)/2)
def quad(n):
    return int(n**2)
def pent(n):
    return int(n*(3*n-1)/2)
def hexa(n):
    return int(n*(2*n-1))
def hep(n):
    return int(n*(5*n-3)/2)
def octo(n):
    return int(n*(3*n-2))

triangles = [tri(x) for x in filter(lambda y: tri(y)>=1000 and tri(y)<10000, range(1,200))]
squares = [quad(x) for x in filter(lambda y: quad(y)>=1000 and quad(y)<10000, range(1,200))]
pentagons = [pent(x) for x in filter(lambda y: pent(y)>=1000 and pent(y)<10000, range(1,200))]
hexagons = [hexa(x) for x in filter(lambda y: hexa(y)>=1000 and hexa(y)<10000, range(1,200))]
heptagons = [hep(x) for x in filter(lambda y: hep(y)>=1000 and hep(y)<10000, range(1,200))]
octogons = [octo(x) for x in filter(lambda y: octo(y)>=1000 and octo(y)<10000, range(1,200))]
winningList = []

answer = -1
allNums = triangles+squares+pentagons+hexagons+heptagons+octogons
allNums.sort()
viewed = []
winning = False
for num1 in allNums:
    for num2 in allNums:
        if num1 == num2:
            continue
        if str(num1)[2:] ==  str(num2)[:2]:
            for num3 in allNums:
                if num3 == num1 or num3 == num1:
                    continue
                if  str(num2)[2:] ==  str(num3)[:2]:
                    for num4 in allNums:
                        if num4 == num3 or num4 == num2 or num4 == num1:
                            continue
                        if  str(num3)[2:] ==  str(num4)[:2]:
                            for num5 in allNums:
                                if num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                                    continue
                                if  str(num4)[2:] ==  str(num5)[:2]:
                                    for num6 in allNums:
                                        if num6 == num1 or num6 == num2 or num6 == num3  or num6 == num4 or num6 == num5:
                                            continue
                                        if  str(num5)[2:] ==  str(num6)[:2] and  str(num6)[2:] ==  str(num1)[:2]:
                                            allLists = [triangles,squares,pentagons,hexagons,heptagons,octogons]
                                            winningList = [num1,num2,num3,num4,num5,num6]
                                            winning = True
                                            for num in winningList:
                                                index = -1
                                                for i in range(0, len(allLists)):
                                                    if num in allLists[i]:
                                                        index = i
                                                        break
                                                if index == -1:
                                                    winning = False
                                                    break
                                                del allLists[i]
                                            if winning:
                                                answer = sum(winningList)
                                                break
                                if winning:
                                    break
                        if winning:
                            break
                if winning:
                    break
        if winning:
            break
    if winning:
        break


print(winningList)
print(answer)
input("done")








            
