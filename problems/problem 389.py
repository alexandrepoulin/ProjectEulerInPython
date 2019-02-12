import useful as u
import math

maxT = 4
maxC=maxT*6
maxO=maxC*8
maxD=maxO*12
maxI=maxD*20


##s sided dice, n dice thrown, k is the result



def P(s,n,k):
    answer = u.bigDouble(0,0)
    for i in range(0,(k-n)//s+1):
        temp = u.nChooseKLog(n,i) * u.nChooseKLog(k-s*i-1,n-1)
        temp.scale((-1)**i)
        answer = answer +temp
    return answer


values4 = list(u.bigDouble(0,0) for i in range(1,maxT+1))
values6 = list(u.bigDouble(0,0) for i in range(1,maxC+1))
values8 = list(u.bigDouble(0,0) for i in range(1,maxO+1))
values12 = list(u.bigDouble(0,0) for i in range(1,maxD+1))
values20 = list(u.bigDouble(0,0) for i in range(1,maxI+1))

print("done making lists")


for i in range(1,5):
    values4[i-1] += (P(4,1,i))


print("done 4")

for c,v in enumerate(values4):
    for i in range(c+1,(c+1)*6+1):
        values6[i-1]+=v*P(6,c+1,i)


print("done 6")

for c,v in enumerate(values6):
    for i in range(c+1,(c+1)*8+1):
        values8[i-1]+=v*P(8,c+1,i)

print("done 8")

for c,v in enumerate(values8):
    print(c," of ", maxO)
    for i in range(c+1,(c+1)*12+1):
        if i%10==0:
            print(c," of ", maxO, "    ",i," of ", (c+1)*12)
        values12[i-1]+=v*P(12,c+1,i)

print("done 12")

for c,v in enumerate(values12):
    print(c," of ", maxD)
    for i in range(c+1,(c+1)*20+1):
        if i%10==0:
            print(c," of ", maxD, "    ", i, " of ", ((c+1)*20))
        values20[i-1]+=v*P(20,c+1,i)

print("done 20")


tot = u.sumBD([x[1] for x in values20])
exp1 = u.sumBD([x[0] for x in values20])/tot
exp2 = u.sumBD([x[0]**2 for x in values20])/tot
answer = exp2-exp1*exp1
print(answer)
print(answer.N())

