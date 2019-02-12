import useful as u 
import math

def f(k,n):
    return math.exp(k/n)-1

def sumf(x,n):
    (a,b,c,d)=x
    return f(n,a)+f(n,b)+f(n,c)+f(n,d)

def err(x,n):
    return abs(sumf(x,n)-math.pi)

maxNum = 14210
N=10000
pi=3.14159265358979323846264338327950288419716939937510582097

bestErr = 100000
bestSoFar = []

list1 = []
list2 = []

##get 2 low ones, a mid one and a high one
cut11 = (1,4000)
cut12 = (1,4000)
cut21 =  (3000,6000)
cut22 =  (10000,13000)

for i in range(cut11[0],cut11[1]):
    val = f(i,N)
    for j in range(max(cut12[0],i+1),cut12[1]):
        list1.append([val+f(j,N),i,j])
print(len(list1))
for i in range(cut21[0],cut21[1]):
    val = f(i,N)
    for j in range(max(cut22[0],i+1),cut22[1]):
        list2.append([val+f(j,N),i,j])

print(len(list2))
u.sortN(list1,0)
u.sortN(list2,0)



def search(s):
    global bestErr
    global bestSoFar
    i=0
    f = len(list2)-1
    temp = s[0]+list2[-1][0]
    temperr = temp-pi
    if abs(temperr) < bestErr:
        bestErr = abs(temperr)
        bestSoFar = [s[1],s[2],list2[-1][1],list2[-1][2]]
    if temperr < 0:
        return
    while i+1<f:
        mid = (f+i)//2
        temp = s[0]+list2[mid][0]
        temperr = temp-pi
        if abs(temperr) <bestErr:
            bestErr = abs(temperr)
            bestSoFar = [s[1],s[2],list2[mid][1],list2[mid][2]]
        if temperr<0:
            i=mid
        else:
            f=mid

for s in list1:
    search(s)

print(bestErr,bestSoFar)
print(sum([x**2 for x in bestSoFar]))

##this works
