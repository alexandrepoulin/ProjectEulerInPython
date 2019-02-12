print("Starting")
import useful

def f(n,r,s,t):
    val = useful.nChooseK(n-1,r)*useful.nChooseK(n-1-r,s)*useful.nChooseK(n-1-r-s,t)
    val += useful.nChooseK(n-1,r-1)*useful.nChooseK(n-r,s)*useful.nChooseK(n-r-s,t)
    val += useful.nChooseK(n-1,r)*useful.nChooseK(n-1-r,s-1)*useful.nChooseK(n-r-s,t)
    val *= 13**(n-r-s-t)
    return val

answer = 0
for n in range(3,17):
    for r in range(1,n-1):
        for s in range(1,n-1):
            for t in range(1,n-1):
                if r+s+t > n:
                    continue
                answer += f(n,r,s,t)

temp = useful.strToList(str(hex(answer))[2:])
for i in range(len(temp)):
    l = temp[i]
    if l == 'a':
        temp[i] = 'A'
    elif l == 'b':
        temp[i] = 'B'
    elif l == 'c':
        temp[i] = 'C'
    elif l == 'd':
        temp[i] = 'D'
    elif l == 'e':
        temp[i] = 'E'
    elif l == 'f':
        temp[i] = 'F'
temp = useful.listToStr(temp)
print(temp)
