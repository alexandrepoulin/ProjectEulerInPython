print("Starting")

##smallest number = 100011222333444555
##Largest number = 999888777666555444
import useful

def inc(x):
    maxNum = 0
    temp = x.copy()
    changed = False
    for i in range(9,4,-1):
        if x.count(i) != 3:
            maxNum = i
            break
    for i in range(len(x)-1,-1,-1):
        if x[i] < maxNum:
            changed = True
            temp[i] = x[i]+1
            c0 = temp[:i+1].count(0)
            c1 = temp[:i+1].count(1)
            c2 = temp[:i+1].count(2)
            c3 = temp[:i+1].count(3)
            c4 = temp[:i+1].count(4)
            c5 = temp[:i+1].count(5)
            c6 = temp[:i+1].count(6)
            c7 = temp[:i+1].count(7)
            c8 = temp[:i+1].count(8)
            c9 = temp[:i+1].count(9)
            for j in range(i+1, len(x)):
                if c0 != 3:
                    temp[j] = 0
                    c0+=1
                    continue
                if c1 != 3:
                    temp[j] = 1
                    c1+=1
                    continue
                if c2 != 3:
                    temp[j] = 2
                    c2+=1
                    continue
                if c3 != 3:
                    temp[j] = 3
                    c3+=1
                    continue
                if c4 != 3:
                    temp[j] = 4
                    c4+=1
                    continue
                if c5 != 3:
                    temp[j] = 5
                    c5+=1
                    continue
                if c6 != 3:
                    temp[j] = 6
                    c6+=1
                    continue
                if c7 != 3:
                    temp[j] = 7
                    c7+=1
                    continue
                if c8 != 3:
                    temp[j] = 8
                    c8+=1
                    continue
                if c9 != 3:
                    temp[j] = 9
                    c9+=1
                    continue
            break
    if changed:
        return [True,temp]
    return [False]

val = [True,useful.intToList(100011222333444555)]
progress = val[1][:12]
counter = 1
while True:
    val = inc(val[1])
    if progress != val[1][:12]:
        progress = val[1][:12]
        print(progress)
    if not val[0]:
        break
    counter+=1

                
                
        
