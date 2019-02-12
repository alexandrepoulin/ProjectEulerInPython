from useful import GCD

maxNum=100

def getI(a,b,c,d):
    return ((a*b+b*c+c*d+d*a-GCD(a,b)-GCD(b,c)-GCD(c,d)-GCD(d,a))>>1)+1

squares = [i**2 for i in range(1,150)]

tot = 0
##for a in range(1,maxNum+1):
##    print(a)
##    for c in range(1,a+1):
##        for b in range(1,a+1):
##            for d in range(1,b+1):
##                num = getI(a,b,c,d)
##                if num in squares:
##                    if a==c and b==d and a==b:
##                        tot+=1
##                    elif a==c and b==d:
##                        tot+=2
##                    elif a==c and a==b and a!=d:
##                        tot+=2
##                    elif a==d and a==b and a!=c:
##                        tot+=2
##                    elif a==d and a==c and a!=b:
##                        tot+=2
##                    elif b==d and b==c and a!=b:
##                        tot+=2
##                    else:
##                        tot+=8

for a in range(1,maxNum+1):
    print(a)
    for c in range(1,maxNum+1):
        for b in range(1,maxNum+1):
            for d in range(1,maxNum+1):
                num = getI(a,b,c,d)
                if num in squares:
                    tot+=1
print(tot)
