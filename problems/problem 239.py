print("Starting")

import useful

a = [75,22]

def recurse(i,l,prevWasPrime):
    answer = 0
    if i == 22:
        answer += l[0]
        if prevWasPrime:
            answer += l[1]
        else:
            answer += (l[1]-1)
    else:
        answer += l[0]*recurse(i+1,[l[0]-1,l[1]],False)
        if prevWasPrime:
            answer += l[1]*recurse(i+1,[l[0],l[1]-1],True)
        else:
            answer += (l[1]-1)*recurse(i+1,[l[0],l[1]-1],True)
    return answer
recurseVal = recurse(1,a, False)
recurseVal *= useful.nChooseK(25,3)

for i in range(76,101):
    recurseVal/=i

print(recurseVal)
    
