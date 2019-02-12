print("Starting")

import useful

perms = useful.perm([1,2,3,4,5,6,7])

p=[]
for i in range(1,8):
    newPi = []
    for x in perms:
        newP = []
        for k in x:
            if k <= i:
                newP.append(1)
            else:
                newP.append(0)
        if newP not in newPi:
            newPi.append(newP)
    p.append(newPi)

start = [20,31,38,39,40,42,45]

def test(nums):
    for i in range(0,7):
        print(i+1)
        for x in p[i]:
            set1 = set()
            sum1 = 0
            for k in range(len(x)):
                if x[k] == 1:
                    set1.add(nums[k])
            sum1 = sum(set1)
            for n in range(0,7):
                for y in p[n]:
                    set2 = set()
                    sum2 = 0
                    if x==y:
                        continue
                    for j in range(len(y)):
                        if y[j]==1:
                            set2.add(nums[j])
                    sum2 = sum(set2)
                    if sum1 == sum2:
                        return False
                    if len(set1)>len(set2) and sum2>sum1:
                        return False
                    #print(i,x,y,set1,set2,sum1,sum2)
    return True
                
                
print(test(start))
