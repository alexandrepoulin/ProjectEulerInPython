print("Starting")

MAXnum = 100000000
#MAXnum = 100
import useful
answer = 0

##the perimeter will be 3r+2s+2t
for r in range(2,int(MAXnum/3),2):
    if r%1000==0:
        print(r)
    val = int(r**2/2.0)
    facts = useful.factors(val)
    facts.append(val)
    facts.append(1)
    facts.sort()
    for i in range(len(facts)):
        s = facts[i]
        t = int(val/s)
        if t<s:
            break
        if 3*r+2*s+2*t>=MAXnum:
            continue
        if useful.GCD(t,s) !=1:
            continue
        ##want y-x to divide z
        ## y-x = t-s
        if ((r+t+s)%(t-s)) == 0:
            perimeter = 3*r+2*s+2*t
            answer += (MAXnum//perimeter)

print(answer)

