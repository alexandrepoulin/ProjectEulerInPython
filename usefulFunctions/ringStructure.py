from math import sqrt

##objects of the form a+b*sqrt(c)
class ringObject:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.sqrtc=sqrt(c)

##    def getA(self):
##        return a
##    def getB(self):
##        return b
##    def getC(self):
##        return c
    def N(self):
        return a+b*sqrtc
    def __add__(self,x):
        if self.c != x.c:
            print("incompatible rings being added")
        return ringObject(self.a+x.a,self.b+x.b,self.c)
    def __sub__(self,x):
        if self.c != x.c:
            print("incompatible rings being added")
        return ringObject(self.a-x.a,self.b-x.b,self.c)
    def __mul__(self,x):
        if self.c != x.c:
            print("incompatible rings being added")
        return ringObject(self.a*x.a+self.b*x.b*self.c,self.b*x.a+self.a*x.b,self.c)
    def __imul__(self,x):
        if self.c != x.c:
            print("incompatible rings being added")
        return self*x

    ##this is not the (a+b*sqrt(c))%x, its  a%x +(b%x)*sqrt(c))   
    def __mod__(self,x):
        return ringObject(self.a%x,self.b%x,self.c)
    def Scale(self,x):
        return ringObject(self.a*x,self.b*x,self.c)
    def Square(self):
        return self*self

    ##only use the mod if in the final answer you discard the root
    def EffExp(self,power,mod=-1):
        moding = False
        base = self
        if mod != -1:
            moding = True
            base = base%mod
        powers = [int(x) for x in (str(bin(power))[2:])]
        leng = len(powers)
        vals = [1]*leng
        vals[-1] = base
        for i in range(leng-2,-1,-1):
            vals[i] = vals[i+1].Square()
            if moding:
                vals[i] = vals[i]%mod
        answer = ringObject(1,0,self.c)
        for i in range(leng):
            if powers[i] == 1:
                answer *= vals[i]
                if moding:
                    answer = answer%mod
        return answer
    def __repr__(self):
        return str(self.a)+"+("+str(self.b)+")*sqrt("+str(self.c)+")"

test = ringObject(1,1,2)


    
