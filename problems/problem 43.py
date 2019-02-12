print("Starting")

def addLast(x):
    nums = set("1234567890")
    nums.difference_update(set(x))
    return int(nums.pop()+x)

answer = 0

for i in range(6,59):
    value1 = str(i*17)
    if len(set(value1)) != len(value1):
        continue
    for j in range(0,10):
        if str(j) in value1:
            continue
        if int(str(j)+value1[:2])%13 == 0:
            value2 = str(j)+value1
            for k in range(0,10):
                if str(k) in value2:
                    continue
                if int(str(k)+value2[:2])%11 == 0:
                    value3 = str(k)+value2
                    for l in range(0,10):
                        if str(l) in value3:
                            continue
                        if int(str(l)+value3[:2])%7 == 0:
                            value4 = str(l)+value3
                            for m in range(0,10):
                                if str(m) in value4:
                                    continue
                                if int(str(m)+value4[:2])%5 == 0:
                                    value5 = str(m)+value4
                                    for n in range(0,10):
                                        if str(n) in value5:
                                            continue
                                        if int(str(n)+value5[:2])%3 == 0:
                                            value6 = str(n)+value5
                                            for p in range(0,10):
                                                if str(p) in value6:
                                                    continue
                                                if int(str(p)+value6[:2])%2 == 0:
                                                    value7 = str(p)+value6
                                                    answer += addLast(value7)

print(answer)
input("done")
                                            
                                            
            
