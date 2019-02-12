print("Starting")

Fn = [1,2]
MAX = 10**17
while Fn[-1] < MAX:
    Fn.append(Fn[-2]+Fn[-1])

combs = dict()
answer = 0

while MAX != 0:
    for i in range(len(Fn)-1):
        n = Fn[i]
        m = Fn[i+1]
        if m>MAX:
            m=MAX
        if n <=2 :
            combs[n] = 1
            answer += 1
            continue
        if not m == MAX:
            temp = m-n + sum(combs[x] for x in combs if x < (m-n))
            answer += temp
            combs[n] = temp
        else:
            answer+= m-n
            MAX = m-n
            break
        
print(answer)
