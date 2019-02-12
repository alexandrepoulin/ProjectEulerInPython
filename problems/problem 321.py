import math


## M(n) = n^2+2n
## T(m) = (m^2+m)/2
## this gives the diophantine equation
## 2n^2+4n - m^2-m=0
## letting x1= 4x+4, y1 = -8m-4
## inverse being x=x1/4-1 ; m=(y-4)/8
## this gives -8x^2 + y^2 +112 = 0
## we use x1=4, y1 = +-4 to generate the two family or solutions

##Xn+1 = P Xn + Q Yn 
##Yn+1 = R Xn + S Yn 

(P,Q,R,S) = (3,-1,-8,3)
def nextV(x,y):
    return ((P * x  + Q *y ), (R * x + S  * y ))

def xToN(x):
    return x/4-1

x=4
y=4

tri = []
while len(tri) !=40:
    tri.append(xToN(x))
    (x,y) = nextV(x,y)

x=4
y=-4
while len(tri) !=80:
    tri.append(xToN(x))
    (x,y) = nextV(x,y)

tri.sort()
tri=tri[2:42]

print(int(sum(tri)))


