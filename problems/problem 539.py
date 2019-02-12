

def p(x):
    n=x
    m=1
    power = 0
    startingLeft = True
    while n!=m:
        if startingLeft:
            if (n-m)%(2**(power+1))==0:
                n-=2**power
            m+=2**power
            startingLeft = False
            power+=1
        else:
            if (n-m)%(2**(power+1))==0:
                m+=2**power
            n-=2**power
            startingLeft = True
            power+=1
##        print(m,n)
    return (m)

for i in range(1,50):
    print(i,p(i))
    
##print(p(1000))
