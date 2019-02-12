from mpmath import *
mp.dps = 2000
sigfigs = 2000
import fractions
import useful
import math

class quadTerm:
    def __init__(self,denom,nom,root):
        if denom == 0:
            raise ZeroDivisionError
        self.denom = denom
        self.nom = nom
        self.root = root
        self.simp()

    def simp(self):
        x = math.sqrt(self.root)
        if int(x) == x:
            self.root = 0
            self.nom += x
        if self.root == 0:
            g = fractions.gcd(self.denom,self.nom)
            self.nom = int(self.nom/g)
            self.denom = int(self.denom/g)
            return self
        fact = useful.primeFact(self.root)
        factor = 1
        countedFact = []
        for i in fact:
            count = fact.count(i)
            if count == 1 or i in countedFact:
                continue
            if count % 2 == 0:
                factor *= i**int(count/2)
                countedFact.append(i)
                continue
            else:
                factor *= i**int((count-1)/2)
                countedFact.append(i)
        if self.nom == 0:
            g = fractions.gcd(self.denom,factor)
            self.root = int(self.root/g**2)
            self.denom = int(self.denom/g)
            return self
        g = fractions.gcd(self.denom,self.nom)
        g = fractions.gcd(g,factor)
        self.denom = int(self.denom/g)
        self.nom = int(self.nom/g)
        self.root = int(self.root/g**2)
        
    def inv(self):
        tempDenom = self.denom
        tempNom = self.nom
        tempRoot = self.root
        if tempNom == 0:
            newDenom = tempRoot
            newRoot = tempRoot*tempDenom**2
            return quadTerm(newDenom,0,newRoot)
        elif tempNom > 0:
            newDenom = tempRoot - tempNom**2
            newRoot = tempRoot*tempDenom**2
            newNom = -tempDenom*tempNom
            return quadTerm(newDenom,newNom,newRoot)
        newDenom = (tempRoot - tempNom**2)*tempDenom/abs(tempDenom)
        newRoot = tempRoot*tempDenom**2
        newNom = -abs(tempDenom)*tempNom
        return quadTerm(newDenom,newNom,newRoot)

    def value(self):
        return (self.nom+math.sqrt(self.root))/self.denom

    def __str__(self):
        return str(self.denom) + " ," + str(self.nom) + " ," + str(self.root)

    def __repr__(self):
        return str(self.denom) + " ," + str(self.nom) + " ," + str(self.root)

    def __add__(self,x):
        return quadTerm(self.denom,self.nom + self.denom*x,self.root)

    def __sub__(self,x):
        return quadTerm(self.denom,self.nom - self.denom*x,self.root)

    def __mul__(self,x):
        sign = x/abs(x)
        return quadTerm(sign*self.denom,self.nom*abs(x),self.root*abs(x)**2)

    def floor(self):
        return math.floor(self.value())

    def __lt__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.value() < other.value()
        else:
            return self.value() < other
        
    def __le__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.value() <= other.value()
        else:
            return self.value() <= other
        
    def __eq__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.nom == other.nom and self.denom == other.denom and self.root == other.root
        else:
            return self.value() == other
        
    def __ne__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.nom != other.nom or self.denom != other.denom or self.root != denom.root
        else:
            return self.value() != other
        
    def __gt__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.value() > other.value()
        else:
            return self.value() > other
        
    def __ge__(self, other):
        if other.__class__.__name__ == 'quad':
            return self.value() >= other.value()
        else:
            return self.value() >= other

    def contFrac(self):
        x = self
        values = []
        answer = []
        index = -1
        sign = 1
        while True:
            if x in values:
                index = values.index(x)
                break
            values.append(x)
            ai = x.floor()
            answer.append(ai)
            x -= ai
            x = x.inv()
        return [answer,index]

