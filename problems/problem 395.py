
##square will be defined by [[a,b],[c,d]]
##a will spawn the larger square
##b will spawn the smaller square
##c was attached to the previous big square
##d was attached the the brother square
##a,b,c,d are all pairs (x,y)

import math

def pairAdd(x,y):
    return (x[0]+y[0],x[1]+y[1])

def pairSub(x,y):
    return (x[0]-y[0],x[1]-y[1])

def matMult(mat,x):
    return (mat[0][0]*x[0]+mat[0][1]*x[1],mat[1][0]*x[0]+mat[1][1]*x[1])

def checkUp(square):
    spawners = square[0]
    return max([p[1] for p in spawners])

def checkDown(square):
    spawners = square[0]
    return  min([p[1] for p in spawners])

def checkRight(square):
    spawners = square[0]
    return  max([p[0] for p in spawners])

def checkLeft(square):
    spawners = square[0]
    return  min([p[0] for p in spawners])

def spawn(square):
    s = square[0]
    dx = s[1][0]-s[0][0]
    dy =s[1][1]-s[0][1]
    L=math.sqrt(dx**2+dy**2)
    mat = [[dx/L,-dy/L],[dy/L,dx/L]]
    newPoint = pairAdd(s[0], matMult(mat,(16/25*L,12/25*L)) )
    dx1 =newPoint[0] -s[0][0]
    dy1 =newPoint[1] -s[0][1]
    newSB = [[pairAdd(s[0],(-dy1,dx1)),pairAdd(newPoint,(-dy1,dx1))],[s[0],newPoint]]

    dx2 =s[1][0]-newPoint[0] 
    dy2 =newPoint[1] -s[1][1]
    
    newSS = [[pairAdd(newPoint,(dy2,dx2)),pairAdd(s[1],(dy2,dx2))],[newPoint,s[1]]]
    return [newSB,newSS]
    

current = 1

change=1

squares = [[[(0,1),(1,1)],[(0,0),(1,0)]]]
counter = 0

for i in range(10):
    newSquares = []
    for s in squares:
        s2 = spawn(s)
        newSquares.append(s2[0])
        newSquares.append(s2[1])
    squares = newSquares


while change > 10**(-11):
    upMost = []
    upness= 0
    downMost = []
    downness= 100
    leftMost = []
    leftness = 0
    rightMost = []
    rightness = 0
    
    for s in squares:
        s2 = spawn(s)
        up1 = checkUp(s2[0])
        up2 = checkUp(s2[1])
        down1 = checkDown(s2[0])
        down2 = checkDown(s2[1])
        right1 = checkRight(s2[0])
        right2 = checkRight(s2[1])
        left1 = checkLeft(s2[0])
        left2 = checkLeft(s2[1])
        if up1 > upness:
            upMost = s2[0]
            upness=up1
        if up2 > upness:
            upMost = s2[1]
            upness=up2
        if down1 < downness:
            downMost = s2[0]
            downness=down1
        if down2 < downness:
            downMost = s2[1]
            downness=down2
        if right1 > rightness:
            rightMost = s2[0]
            rightness=right1
        if right2 > rightness:
            rightMost = s2[1]
            rightness=right2
        if left1 < leftness:
            leftMost = s2[0]
            leftness=left1
        if left2 < leftness:
            leftMost = s2[1]
            leftness=left2
    squares = [upMost,downMost,leftMost,rightMost]

    area = (upness-min(0,downness))*(rightness-leftness)
    change = abs(area - current)
    current = area


print(current)
        
        
        
    
    
    
