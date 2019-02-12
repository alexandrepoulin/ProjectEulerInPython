print("Starting")

MAX = (10**6-1)**3

aVals = [0,1]
leng = [0,1]
for i in range(2,MAX+1):
    aVals.append(1+aVals[i-aVals[aVals[i-1]]])
    leng.append(leng[-1]+aVals[i])
    if leng[-1]>MAX:
        break
print(len(leng),leng[-1])

