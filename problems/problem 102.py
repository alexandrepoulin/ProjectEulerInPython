print("Starting")

def check(x):
    if x[:2] == [0,0] or x[2:4] == [0,0] or x[4:] == [0,0]:
        return False
    if (x[1] == 0 and x[3] == 0) or (x[3] == 0 and x[5] == 0) or (x[1] == 0 and x[5] == 0):
        return False
        
    if x[0] != x[2]:
        slopeAB = (x[1] - x[3])/(x[0]-x[2])
    if x[4] != x[2]:
        slopeBC = (x[3] - x[5])/(x[2]-x[4])
    if x[0] != x[4]:
        slopeCA = (x[5] - x[1])/(x[4]-x[0])

    if x[0] != x[2]:
        interAB = x[1]-slopeAB*x[0]
    if x[4] != x[2]:
        interBC = x[3]-slopeBC*x[2]
    if x[0] != x[4]:
        interCA = x[5]-slopeCA*x[4]
    intercepts = []

    if x[0] != x[2]:
        if 0 in range(min(x[0],x[2]),max(x[0],x[2])+1):
            intercepts.append(interAB)
    if x[4] != x[2]:
        if 0 in range(min(x[2],x[4]),max(x[2],x[4])+1):
            intercepts.append(interBC)
    if x[0] != x[4]:
        if 0 in range(min(x[0],x[4]),max(x[0],x[4])+1):
            intercepts.append(interCA)
    
    if len(intercepts)<2:
        return False

    if min(intercepts[0],intercepts[1])<0 and 0<max(intercepts[0],intercepts[1]):
        return True
    else:
        return False

file = open("triangles.txt")
counter = 0

for line in file:
    line = line.strip()
    tokens = line.split(',')
    triangle = []
    for x in tokens:
        triangle.append(int(x))
    if check(triangle):
        counter += 1

print(counter)
input("Done")
    
