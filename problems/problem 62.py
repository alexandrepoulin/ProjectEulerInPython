print("Starting")

import useful
import math

foundCubes = set()

cubes = [x**3 for x in range(1,10000)]
cubes.sort()
perms = [x for x in map(lambda k: list(str(k)),cubes)]
for x in perms:
    x.sort()

answer = 0
bestCube = 0
for x in cubes:
    #print(x)
    perm = list(str(x))
    perm.sort()
    count = perms.count(perm)
    if count == 5:
        answer = math.pow(x,1/3)
        bestCube = x
        break
    for i in range(0,count):
        perms.remove(perm)



print(answer)
print(bestCube)
input("Done")
            
