print("Starting")

pyra = [0]*(37)
cube = [0]*(37)

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                for m in range(1,5):
                    for n in range(1,5):
                        for o in range(1,5):
                            for p in range(1,5):
                                for q in range(1,5):
                                    value = i+j+k+l+m+n+o+p+q
                                    pyra[value]+=1

for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                for m in range(1,7):
                    for n in range(1,7):
                        value = i+j+k+l+m+n
                        cube[value]+=1
pyraSum = sum(pyra)
cubeSum = sum(cube)

pyra = [x for x in map(lambda k: k/pyraSum, pyra)]
cube = [x for x in map(lambda k: k/cubeSum, cube)]

Sum = 0
for i in range(0,36):
    pyraProb = sum(pyra[i+1:])
    Sum += cube[i]*pyraProb

print(Sum)
