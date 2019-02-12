##solves diophantine equations of the form Ax^2+Bxy+Cy^2+Dx+Ey+F=0
##returns [] is there are no solutions
##returns lowest form solutions

##Call solve(A,B,C,D,E,F,xNonNeg=False,yNonNeg=False,xZero=True,yZero=True)
##where you add NonNeg to the parameter if you want non-negative solutions
##and add zero if you want solutions with that parameter = 0
##Sometimes, you may want x>0 but y>=0 which is why this exists

##NOTE!!!!!!!!!!!!!!
##In the hyperbolic case, there is a case where there are infinitely many
##solutions, see note in the code

##mathematical source https://www.alpertron.com.ar/JQUAD.HTM
##Programmed by Alexandre Poulin



import fractions
import math
from mpmath import *
import quadratic
mp.pretty = True
mp.dps = 2000
sigfigs = 30

def euclidAlg(a,b):
    if b == 0:
        return [1,0]
    if a%b == 1:
        return [1,-(a-1)/b]
    value = a%b
    x = -(a - value)/b
    prevPara = euclidAlg(b,value)
    return [prevPara[1],prevPara[1]*x+prevPara[0]]

def findContinuedFraction(x):
    return x.contFrac()

def findNthConvergent(data,n):
    nums = data[0]
    periodic = data[0][data[1]:]
    if n > len(nums):
        for i in range(0,math.ceil((n-len(nums))/len(periodic))):
            nums.extend(periodic)
    nums = nums[:n]
    if len(nums) == 1:
        return [nums[0],1]
    nom0 = 1
    denom0 = 0
    nom1 = nums[0]
    denom1 = 1
    counter = 2
    secondLast = [nom0,denom0]
    last = [nom1, denom1]
    while counter <= n:
        current = findNextConvergent(nums[counter-1],last,secondLast)
        counter += 1
        secondLast = last
        last = current
    return last

def findNextConvergent(cn,t1,t2):
    return [fsum([fprod([cn,t1[0]]),t2[0]]),fsum([fprod([cn,t1[1]]),t2[1]])]

def solveQuad(a,b,c):
    return [quadratic.quadTerm(2*a,-b,b**2-4*a*c) ,quadratic.quadTerm(-2*a,b,b**2-4*a*c)]

def factors(x):
    factors = []
    for i in range(1,int(math.sqrt(x)+1)):
        if x % i == 0:
            factors.append(i)
            if int(x/i) != i:
                factors.append(int(x/i))
    factors.sort()
    return factors

def linearCase(D,E,F):
    if D == 0 and E == 0:
        if F == 0:
            return [[1,1]]
        else:
            return []
    elif D == 0 and E != 0:
        if F%E == 0:
            return [[1,int(-F/E)]]
        else:
            return []
    elif E == 0 and D != 0:
        if F%D == 0:
            return [[int(-F/D),1]]
        else:
            return []
    else:
        g = fractions.gcd(D,E)
        if F%g != 0:
            return []
        else:
            d = int(D/g)
            e = int(E/g)
            f = int(F/g)
            x = max(d,e)
            y = min(d,e)
            val = euclidAlg(x,y)
            val = [i for i in map(lambda k: -f*k, val)]
            if val[0]*d+val[1]*e + f == 0:
                return val
            else:
                return [[int(val[1]),int(val[0])]]

def simpleHyp(B,D,E,F):
    if D*E-B*F == 0:
        answer = []
        if E%B == 0:
            answer.append([-int(E/B),1])
        if D%B == 0:
            answer.append([1,-int(D%B)])
        return answer
    else:
        di = factors(D*E-B*F)
        answer = []
        for d in di:
            for i in [-1,1]:
                if (i*d-E)%B == 0 and ((D*E-B*F)/(d*i) -D)%B == 0:
                    answer.append([int((i*d-E)/B),int(((D*E-B*F)/(d*i) -D)/B)])
        return answer

def ellipticalCase(A,B,C,D,E,F):
    answer = []
    zeros = solveQuad(B**2-4*A*C, 2*(B*E-2*C*D),E**2-4*C*F)
    if int(zeros[0].value()) == zeros[0].value():
        answer.append([int(zeros[0].value()),0])
    if int(zeros[1].value()) == zeros[1].value():
        answer.append([int(zeros[1].value()),0])
    zeros = [math.ceil(min(zeros[0].value(),zeros[1].value())),math.ceil(max(zeros[0].value(),zeros[1].value()))]
    for x in range(zeros[0],zeros[1]):
        y = (-(B*x+E)+math.sqrt((B*x+E)**2-4*C*(A*x**2+D*x+F)))/(2*C)
        if int(y) == y:
            answer.append([int(x),int(y)])
        y = (-(B*x+E)-math.sqrt((B*x+E)**2-4*C*(A*x**2+D*x+F)))/(2*C)
        if int(y) == y:
            answer.append([int(x),int(y)])
    return answer

def parabolicCase(A,B,C,D,E,F):
    g = fractions.gcd(A,C)
    a = A/g
    b = B/g
    c = C/g
    sign = 0
    if A == 0 or B == 0:
        sign = 0
    else:
        sign = B/A*abs(A/B)
    value = sign*math.sqrt(c)*D-math.sqrt(a)*E
    if value == 0:
        roots = solveQuad(math.sqrt(a)*g,D,math.sqrt(a)*F)
        u1 = roots[0].value()
        u2 = roots[1].value()
        answer = []
        if int(u1) == u1:
            answer.extend(linearCase(math.sqrt(a),sign*math.sqrt(c),-u1))
        if int(u2) == u2:
            answer.extend(linearCase(math.sqrt(a),sign*math.sqrt(c),-u2))
        return answer
    ui = []
    for i in range(0,int(abs(value))):
        val = math.sqrt(a)*g*i**2+D*i+math.sqrt(a)*F
        if val % abs(value) == 0:
            ui.append(i)
    answer = []
    for j in ui:
        x = -(sign*math.sqrt(c)*g*j**2+E*j+sign*math.sqrt(c)*F)/value
        y = (math.sqrt(a)*g*j**2+D*j+math.sqrt(a)*F)/value
        answer.append([int(x),int(y)])
    return answer

def DandEareZero(A,B,C,F):
    value = math.sqrt(B**2-4*A*C)
    if int(value) == value:
        k = value
        divisors = factors(abs(A*F*4))
        divisors.extend([x for x in map(lambda y: -y, divisors)])
        answer = []
        for ui in divisors:
            y = (ui+4*A*F/ui)/(2*k)
            x = (ui-(B+k)*y)/(2*A)
            if int(y) == y and int(x) == x:
                answer.append([int(x),int(y)])
        return answer
    g = fractions.gcd(A,B)
    g = fractions.gcd(g,C)
    if F%g != 0:
        return []
    elif 4*F**2 < B**2-4*A*C:
        zeroes = solveQuad(A,B,C)
        answer = []
        for t in zeroes:
            nums = findContinuedFraction(t)
            for i in range(0,4*len(nums[0])): ##!!!!!!!! 4 is a value which usually works to get large solutions, but there are infinitely more
                nomAndDenom = findNthConvergent(nums,i+1)
                if A*nomAndDenom[0]**2+B*nomAndDenom[0]*nomAndDenom[1]+C*nomAndDenom[1]**2 +F == 0:
                    answer.append([x for x in map(lambda y: int(y), nomAndDenom)])
                    answer.append([x for x in map(lambda y: int(-y), nomAndDenom)])
        return answer
    else:
        answer = []
        g = fractions.gcd(A,B)
        g = abs(fractions.gcd(g,F))
        done = False
        if g == 1:
            vals = []
            done = True
            for l in range(0,abs(F)):
                if (A*l**2+B*l+C)%abs(F) == 0:
                    vals.append(l)
            for s in vals:
                zeroes = solveQuad(-(A*s**2+B*s+C)/F,2*A*s+B,-A*F)
                for t in zeroes:
                    nums = findContinuedFraction(t)
                    period = len(nums[0])-nums[1]
                    numberOfRepeats = 0
                    if (period%2) == 1:
                        numberOfRepeats+=1
                    for i in range(0,len(nums[0])+numberOfRepeats*period):
                        nomAndDenom = findNthConvergent(nums,i+1)
                        equation = -(A*s**2+B*s+C)/F*nomAndDenom[0]**2 + (2*A*s+B)*nomAndDenom[0]*nomAndDenom[1] - A*F*nomAndDenom[1]**2
                        if equation == 1:
                            y = nomAndDenom[0]
                            z = nomAndDenom[1]
                            x = s*y-F*z
                            answer.append([int(x),int(y)])
                            answer.append([int(-x),int(-y)])
        if g!=1:
            g = fractions.gcd(B,C)
            g = abs(fractions.gcd(g,F))
        else:
            g = 0
        if g == 1:
            done = True
            vals = []
            answer = []
            for l in range(0,abs(F)):
                if (C*l**2+B*l+A)%F == 0:
                    vals.append(s)
            for s in vals:
                zeroes = solveQuad(-(C*s**2+B*s+A)/F,2*C*s+B,-C*F)
                for t in zeroes:
                    nums = findContinuedFraction(t)
                    period = len(nums[0])-nums[1]
                    numberOfRepeats = 0
                    if (period%2) == 1:
                        numberOfRepeats+=1
                    for i in range(0,len(nums[0])+numberOfRepeats*period):
                        nomAndDenom = findNthConvergent(nums,i+1)
                        equation = -(C*s**2+B*s+A)/F*nomAndDenom[0]**2 + (2*C*s+B)*nomAndDenom[0]*nomAndDenom[1] - C*F*nomAndDenom[1]**2
                        if equation == 1:
                            x = nomAndDenom[0]
                            z = nomAndDenom[1]
                            y = s*x-F*z
                            answer.append([int(x),int(y)])
                            answer.append([int(-x),int(-y)])
        if not done:
            i = 0
            m = 0
            for someI in range(0,abs(F)):
                for someM in range(0,i+2):
                    a=A*someI**2+B*someI*someM+C*someM**2
                    G = abs(fractions.gcd(a,F))
                    if fractions.gcd(someI,someM) == 1 and G == 1:
                        i = someI
                        m = someM
                        break
                if i != 0 or m != 0:
                    break
            vals = linearCase(i,-m,-1)

            n = vals[0][0]
            j = vals[0][1]
            a = A*i**2+B*i*m+C*m**2
            b = 2*A*i*j+B*i*n+B*j*m+2*C*m*n
            c = A*j**2+B*j*n+C*n**2
            XYsolutions = DandEareZero(a,b,c,F)
            answer.extend([sol for sol in map(lambda k: [int(i*k[0]+j*k[1]),int(m*k[0]+n*k[1])],XYsolutions)])
        facts = factors(abs(F))
        facts = [x for x in filter(lambda k: int(math.sqrt(k))== math.sqrt(k) and k!=1,facts)]
        for f in facts:
            tempSol = DandEareZero(A,B,C,int(F/f))
            for t in tempSol:
                answer.append([int(t[0]*sqrt(f)),int(t[1]*sqrt(f))])
        return answer

def hyperbolicCase(A,B,C,D,E,F):
    if D == 0 and E == 0:
        answers = []
        if F == 0:
            value = math.sqrt(B**2-4*A*C)
            answers.append([0,0])
            if int(value) == value:
                answers.extend(linearCase(2*A,B+value,0))
                answers.extend(linearCase(2*A,B-value,0))
            return answer
        answers.extend(DandEareZero(A,B,C,F))
        return answers
    else:
        g = fractions.gcd(4*A*C-B**2,2*A*E-B*D)
        a = int((4*A*C-B**2)/g)
        f = int(4*A*(4*A*C*F-A*E**2-B**2*F+B*D*E-C*D**2)/g)
        solutionsNew = solve(a,0,g,0,0,f)
        solutionsReal = []
        for s in solutionsNew:
            y = int((g*s[1]+B*D-2*A*E)/(4*A*C-B**2))
            x = int((s[0]-D-B*y)/(2*A))
            solutionsReal.append([x,y])
        return solutionsReal
            

def clean(solutions, xNonNeg,yNonNeg,xZero,yZero):
    if xNonNeg and xZero:
        solutions = list(filter(lambda k: k[0]>=0, solutions))
    elif xNonNeg and not xZero:
        solutions = list(filter(lambda k: k[0]>0, solutions))
    elif not xNonNeg and not xZero:
        solutions = list(filter(lambda k: k[0]!=0, solutions))
    if yNonNeg and yZero:
        solutions = list(filter(lambda k: k[1]>=0, solutions))
    elif yNonNeg and not yZero:
        solutions = list(filter(lambda k: k[1]>0, solutions))
    elif not yNonNeg and not yZero:
        solutions = list(filter(lambda k: k[1]!=0, solutions))        
    reducedSolutions = []
    for x in solutions:
        if x not in reducedSolutions:
            reducedSolutions.append(x)
    return reducedSolutions

def solve(A,B,C,D,E,F,xNonNeg=False,yNonNeg=False,xZero=True,yZero=True):
    value = B**2-4*A*C
    if [A,B,C] == [0,0,0]:
        return clean(linearCase(D,E,F),xNonNeg,yNonNeg,xZero,yZero)
    elif [A,C] == [0,0]:
        return clean(simpleHyp(B,D,E,F),xNonNeg,yNonNeg,xZero,yZero)
    elif value < 0:
        return clean(ellipticalCase(A,B,C,D,E,F),xNonNeg,yNonNeg,xZero,yZero)
    elif value == 0:
        return clean(parabolicCase(A,B,C,D,E,F),xNonNeg,yNonNeg,xZero,yZero)
    else:
        return clean(hyperbolicCase(A,B,C,D,E,F),xNonNeg,yNonNeg,xZero,yZero)

def linearCaseRec(D,E,F):
    if D == 0 or E == 0:
        return []
    else:
        g = fractions.gcd(D,E)
        if F%g != 0:
            return []
        else:
            return [int(E/g),-int(D/g)]

def simpleHypRec(B,D,E,F):
    return (D*E-B*F == 0)

def ellipticalCaseRec(A,B,C,D,E,F):
    return []

def parabolicCaseRec(A,B,C,D,E,F):
    g = fractions.gcd(A,C)
    a = A/g
    b = B/g
    c = C/g
    sign = B/A*abs(A/B)
    value = sign*math.sqrt(c)*D-math.sqrt(a)*E
    if value == 0:
        roots = solveQuad(math.sqrt(a)*g,D,math.sqrt(a)*F)
        u1 = roots[0].value()
        u2 = roots[1].value()
        answer = []
        if int(u1) == u1:
            answer.extend(linearCase(math.sqrt(a),sign*math.sqrt(c),-u1))
        if int(u2) == u2:
            answer.extend(linearCase(math.sqrt(a),sign*math.sqrt(c),-u2))
        return answer
    ui = []
    for i in range(0,int(abs(value))):
        val = math.sqrt(a)*g*i**2+D*i+math.sqrt(a)*F
        if val % abs(value) == 0:
            ui.append(i)
    answer = []
    for j in ui:
        current = []
        val1 = -sign*math.sqrt(c)*g*value
        val2 = -(E+2*sign*math.sqrt(c)*g*j)
        val3 = -(sign*math.sqrt(c)*g*j**2+E*j+sign*math.sqrt(c)*F)/value
        val4 = math.sqrt(a)*g*value
        val5 = D+2*math.sqrt(a)*g*j
        val6 = (math.sqrt(a)*g*j**2+D*j+math.sqrt(a)*F)/value
        current = [int(val1),int(val2),int(val3),int(val4),int(val5),int(val6)]
        answer.append(current)
    return answer

def hyperbolicCaseRec(A,B,C,D,E,F):
    sol = solve(1,B,A*C,0,0,-1)
    sol = sol[:2]
    r=0
    s=0
    for s in sol:
        r=s[0]
        s=s[1]
        P=r
        Q=-C*s
        R=A*s
        S=r+B*s
        K = (C*D*(P+S-2)+E*(B-B*r-2*A*C*s))/(4*A*C-B**2)
        L = (D*(B-B*r-2*A*C*s)+A*E*(P+S-2))/(4*A*C-B**2)+D*s
        if int(K) == K and int(L) == L:
            return [P,Q,int(K),R,S,int(L)]
    
    P= r**2-A*C*s**2
    Q= -C*s*(2*r+B*s)
    K= -C*D*s**2-E*r*s
    R= A*s*(2*r+B*s)
    S= r**2+2*B*r*s+(B**2-A*C)*s**2
    L= D*s*(r+B*s)-A*E*s**2
    return [P,Q,K,R,S,L]
    

def solveRecurrence(A,B,C,D,E,F):
    ## the first parameter will be the case
    ##
    ## CASE 0:
    ## x_n = answer[0]*n+-x_0
    ## y_n = answer[1]*n+-y_0
    ##
    ## CASE 1:
    ## if answer !=0 then if the solution has a 1 in it, then it can be arbitrary
    ## will have the form [1,True] or [1,False]
    ##
    ## CASE 2:
    ## there is only a finite number of solutions given by solve. Returning [2,[]]
    ##
    ## CASE 3:
    ## will return a list for every solution
    ## x = answer[0]*n**2+answer[1]*n+answer[2]
    ## y = answer[3]*n**2+answer[4]*n+answer[5]
    value = B**2-4*A*C
    if [A,B,C] == [0,0,0]:                      ## CASE 0
        return [0,linearCaseRec(D,E,F)]
    elif [A,C] == [0,0]:                        ## CASE 1
        return [1,simpleHypRec(B,D,E,F)]
    elif value < 0:                             ## CASE 2
        return [2,ellipticalCaseRec(A,B,C,D,E,F)]
    elif value == 0:                            ## CASE 3
        return parabolicCaseRec(A,B,C,D,E,F)
    else:                                       ## CASE 4
        return hyperbolicCaseRec(A,B,C,D,E,F)
    


##Linear test (A=B=C=0):
##should give [-136,42]
#print(solve(0,0,0,10,84,16))
##should give [0,[42,-5]]
#print(solveRecurrence(0,0,0,10,84,16))

##Simple Hyperbolic Case Test(A=C=0, B!=0):
##should be [[-29, -69], [-27, 64], [-35, -12], [-21, 7], [-47, -6], [-9, 1], [-161, -3], [105, -2]]
#print(solve(0,2,0,5,56,7))
##should be [1,False]
#print(solveRecurrence(0,2,0,5,56,7))

##Elliptic Case test (B^2-4AC<0):
#print(solve(42,8,15,23,17,-4915)) ##should only be [-11,-1]
#print(solveRecurrence(42,8,15,23,17,-4915)) ##should be [2,[]]

##Parabolic Case test (B^2-4AC=0):
#print(solve(8,-24,18,5,7,16)) ##Should give [-2,-2] and [-4,-4]
#print(solveRecurrence(8,-24,18,5,8,16)) 
##Should give (close enough)
##x = - 174 u2 - 41 u - 4
##y = - 116 u2 - 37 u - 4

##Hyperbolic D=E=0 case (B^2-4AC>0)
##print(solve(18,41,19,0,0,-24)) ##good enough
##these works
##print(solveRecurrence(3,13,5,1,1,1))
##print(solveRecurrence(3,14,6,1,1,1))

##example
##print(solve(4,0,-1,0,0,-27))
