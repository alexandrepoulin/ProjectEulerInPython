import useful as u

## 43!=2^39 * 3^19 * 5^9 * 7^6 *11^3 * 13^3 * 17^2 *19^2 * 23 * 29 * 31 * 37 * 41 * 43
## consider three groups, A, B ,C. The prime factors are put into these groups


def partitions(n,p):
    parts = []
    for i in range(n+1):
        for j in range(n+1-i):
            k=n-i-j
            parts.append((p**i,p**j,p**k))
    return parts

def comb(x):
    a = 1
    b = 1
    c = 1
    for p in x:
        a*=p[0]
        b*=p[1]
        c*=p[2]
    return (a,b,c)

sqrt=2.457951648494612589606740627196811*10**26
cbrt=3.9238785509833851387013767*10**17

p2 = partitions(39,2)
p3 = partitions(19,3)
p5 = partitions(9,5)
p7 = partitions(6,7)
p11 = partitions(3,11)
p13 = partitions(3,13)
p17 = partitions(2,17)
p19 = partitions(2,19)
p23 = partitions(1,23)
p29 = partitions(1,29)
p31 = partitions(1,31)
p37 = partitions(1,37)
p41 = partitions(1,41)
p43 = partitions(1,43)

parts1= []
for a in p2:
    for b in p3:
        for c in p5:
            for d in p43:
                temp = comb([a,b,c,d])
                if temp[0] < cbrt and temp[1]<sqrt:
                    parts1.append(temp)

parts2 = []

for a in p7:
    for b in p11:
        for c in p13:
            for d in p17:
                for e in p19:
                    for f in p23:
                        for g in p29:
                            for h in p31:
                                for i in p37:
                                    for j in p41:
                                        temp = comb([a,b,c,d,e,f,g,h,i,j])
                                        if temp[0] < cbrt and temp[1]<sqrt:
                                            parts1.append(temp)


print(len(parts1),len(parts2))
u.sortN(parts1,3)
u.sortN(parts2,3)





