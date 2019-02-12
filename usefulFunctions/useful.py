#useful Stuff
import math
import itertools
from bigDouble import *

##factorial
def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

##efficient exponentiation
def expEff(base,power,mod=-1):
    moding = False
    if mod != -1:
        moding = True
        base %=mod 
    powers = [int(x) for x in (str(bin(power))[2:])]
    leng = len(powers)
    vals = [1]*leng
    vals[-1] = base
    for i in range(leng-2,-1,-1):
        vals[i] = vals[i+1]**2
        if moding:
            vals[i] = vals[i]%mod
    answer = 1
    for i in range(leng):
        if powers[i] == 1:
            answer *= vals[i]
            if moding:
                answer = answer%mod
    return answer

##efficient exponentiation for matrices
def expEffMat(base,power,mod=-1):
    moding = False
    if mod != -1:
        moding = True
        base = matMod(base,mod)
    powers = [int(x) for x in (str(bin(power))[2:])]
    leng = len(powers)
    vals = [1]*leng
    vals[-1] = base
    for i in range(leng-2,-1,-1):
        vals[i] = matMult(vals[i+1],vals[i+1])
        if moding:
            vals[i] = matMod(vals[i],mod)
    answer = identityMat(len(base))
    for i in range(leng):
        if powers[i] == 1:
            answer = matMult(answer,vals[i])
            if moding:
                answer = matMod(answer,mod)
    return answer

##Febonacci number
def Feb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    fnew = 1
    for m in range(2,n+1):
        fnew= f0+f1
        f0 = f1
        f1 = fnew
    return fnew

##Fermat's little theorem primality testing for p>= 5
def isPrimeFermat(p):
    a = expEff(2,p-1,p)
    if a != 1:
        return False
    a = expEff(4,p-1,p)
    if a != 1:
        return False
    a = expEff(5,p-1,p)
    if a != 1:
        return False
    a = expEff(6,p-1,p)
    if a != 1:
        return False
    return True

##convert from base n to m, takes a list of numbers less than n in the order of the powers
##i.e [1,3,1] in base 5 would be 1+3*5**2 + 1*5**3
def baseConvertListList(x,n,m):
    num = sum([x[i]*n**i for i in range(len(x))])
    answer = []
    counter = -1
    while num !=0:
        counter+=1
        temp = (num%m)
        answer.append(temp)
        num= int((num-temp)/m)
    return answer

##same as above, but takes a number in base 10
def baseConvert10NumList(x,n):
    num = x
    answer = []
    counter = -1
    while num !=0:
        counter+=1
        temp = (num%n)
        answer.append(temp)
        num= int((num-temp)/n)
    return answer

##this gives you another number in base m, but in the form of base 10, need m<=10
def baseConvertNumNum(x,n,m):
    digits = [int(k) for k in list(str(x))][::-1]
    num = sum([digits[i]*n**i for i in range(len(digits))])
    answer = 0
    counter = -1
    while num !=0:
        counter+=1
        temp = (num%m)
        answer+=10**counter * temp
        num= int((num-temp)/m)
    return answer

##same as above, but takes a number in base 10
def baseConvert10NumNum(x,n):
    num = x
    answer = 0
    counter = -1
    while num !=0:
        counter+=1
        temp = (num%n)
        answer+=10**counter * temp
        num= int((num-temp)/n)
    return answer

##adds the digits of x
def addDigits(x):
    return sum(map(lambda y: int(y),str(x)))

##checks if the number is 9 pandigital
def isPan(x):
    return set(str(x)) == {'1','2','3','4','5','6','7','8','9'}

##get the nth digit of an integer x
def getDigit(n,x):
    if n == 1:
        return x%10
    return ((x%10**n)-(x%10**(n-1)))//10**(n-1)

##increment the nth digit of an integer x by k (k can be negative)
def incDigit(n,x,k):
    return  x + k*10**(n-1)

##set a the nth digit of an integer x to k
def setDigit(n,x,k):
    return incDigit(n,x,k-getDigit(n,x))

##determine how many digits match two numbers in two numbers with the same amount of digits
def numOfMatchingDigits(x,y):
    length = len(str(x))
    counter = 0
    for i in range(length):
        if getDigit(length-i,x) == getDigit(length-i,y):
            counter+=1
    return counter

##turn a list of numbers into an integer
def listToInt(x):
    length = len(x)
    answer = 0
    for i in range(length):
        answer += x[length-1-i]*10**i
    return answer

##turn an int into a list
def intToList(x):
    answer = []
    length = len(str(x))
    for i in range(length):
        answer.append(getDigit(length-i,x))
    return answer

##turn a list of chars into a string:
def listToStr(x):
    answer = ""
    for i in x:
        answer += i
    return answer

##make a list of chars from a string
def strToList(x):
    return [i for i in x]

##determines if the number is a palindrom
def isPal(x):
    return str(x) == str(x)[::-1]

##determines if the number is prime
def isPrime(x):
    if x <= 1:
        return False
    MAX = int(x**0.5)+1
    nums = set(range(2,MAX))
    while len(nums)>0:
        p = nums.pop()
        if x%p == 0:
            return False
        nums.difference_update(set(range(p**2, MAX,p)))
    return True

##determines if the number is primes but take a premade sorted list of primes:
def fastIsPrime(x,primes, MAX):
    if x < MAX:
        return x in primes
    else:
        for i in primes:
            if i > x**0.5+1:
                break
            if x%i == 0:
                return False
    return True

##determines if the number is primes but take a premade sorted list of primes and a set of primes:
def fastIsPrime2(x,primes, MAX,primeSet):
    if x < MAX:
        return x in primeSet
    else:
        for i in primes:
            if i > x**0.5+1:
                break
            if x%i == 0:
                return False
    return True

##returns all the prime factors of x, ie for 12 it gives [2,2,3]
def primeFact(x):
    number = x
    answer = []
    while number > 1:
        for i in range(2,int(number)+1):
            if number%i == 0:
                answer.append(i)
                number = int(number/i)
                break
    return answer

##takes the prime factors and then returns puts the powers together
def compressFactors(x):
    factors = set(x)
    answer = []
    for y in factors:
        answer.append(y**(x.count(y)))
    return answer

##returns all the proper factors of x
def factors(x):
    factors = []
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            factors.append(i)
            if int(x/i) != i:
                factors.append(int(x/i))
    #factors.sort() ##uncomment if needed sort
    return factors

##if the factors of two numbers are know, the this returns the factors of their product
def factFromMult(fact1,fact2):
    factors = set(fact1+fact2)
    for i in fact1:
        for j in fact2:
            factors.add(i*j)
    return factors ##this is a set

##returns a sorted list of coprime numbers below x, takes the primes
def coprime(x,primes):
    pFactor = factorsFromPrimes(x,primes)
    nums = set(range(1,x))
    for p in pFactor:
        nums.difference_update(set(range(int(p),x,int(p))))
    group = list(nums)
    group.sort()
    return group

##return proper prime factors using a premade list of primes (faster than primeFact) ie for 12 it gives [2,2,3]
def factorsFromPrimes(x,primes):
    factors = []
    lastFact = 0
    square = x**0.5
    while x > 1:
        currentX = x
        for p in primes:
            if p < lastFact:
                continue
            if p > square:
                factors.append(int(x))
                x = 1
                break
            if x % p == 0:
                factors.append(int(p))
                lastFact = p
                x = x/p
                break
        if x == currentX:
            return [-1]
    return factors

##return n choose k, or n!/(k!*(n-k)!)
def nChooseK(n,k):
    answer = 1
    lower = max(k, n-k)
    upper = min(k, n-k)
    for i in range(upper+1,n+1):
        answer*=i
    for i in range(2, lower+1):
        answer//=i
    integerAnswer = int(answer)
    #x - a >0.5 assume x-a=1 so need (x-1)=a
    if integerAnswer-answer > 0.5:
        integerAnswer-=1
    elif integerAnswer-answer < -0.5:
        integerAnswer += 1
    return integerAnswer

##return log( n choose k, 10) as a big double, or log(n!/(k!*(n-k)!),10) (end is cut)
def nChooseKLog(n,k):
    answer = bigDouble(1,0)
    lower = max(k, n-k)
    upper = min(k, n-k)
    upperLen = n-upper
    lowerLen = lower
    minLen = min(upperLen,lowerLen)
    upperLonger = minLen==upperLen
    
    counter = 1
    while counter <=minLen:
        answer = answer * logToBD(math.log((counter+upper)/counter,10))
        counter +=1
    if upperLonger:
        while counter <= upperLen:
            answer = answer* logToBD(math.log(counter+upper,10))
    else:
        while counter <= lower:
            answer = answer / logToBD(math.log(counter,10))
    return answer

def primesTo(MAX):
    flags = [True] * MAX
    primes = []
    flags[0] = flags[1] = 0
    for (i, isprime) in enumerate(flags):
        if isprime:
            primes.append(i)
            for n in range(i*i, MAX, i):
                flags[n] = False
    return primes

##call this function, store the result and pass it into phiFast
def primeTermsForPhi(primes):
    return {p: (1-1/p) for p in primes}
def phiFast(n, primeTerms):
    if n in primes:
        return n-1
    facts = factorsFromPrimes(n,primes)
    factors = set(facts)
    if len(factors) == 1:
        p = factors.pop()
        return p**(len(facts)-1)*(p-1)
    answer = n
    for i in factors:
        answer *= primeTerms[i]
    return int(answer)

##Calculater Euler's Totient function (requires a list of primes)
def phi(n, primes):
    if n in primes:
        return n-1
    facts = factorsFromPrimes(n,primes)
    factors = set(facts)
    if len(factors) == 1:
        p = factors.pop()
        return p**(len(facts)-1)*(p-1)
    answer = n
    for i in factors:
        answer *= (1-1/i)
    return int(answer)

##determines if one string is a permutation of the other:
def isPerm(x,y):
    if len(x) != len(y):
        return False
    a = list(y)
    for i in x:
        if i in a:
            a.remove(i)
        else:
            return False
    return True
        
##returns a list of all permutations of the ordered list y
def perm(y):
    x= list(y)
    l = len(x)
    if l == 1:
        return [x]
    answer = []
    used = []
    for i in range(0,l):
        if x[i] in used:
            continue
        used.append(x[i])
        currentX = x[0:i]+x[i+1:l+1]
        perms = perm(currentX)
        for k in perms:
            answer.append([x[i]]+k)
    return answer

##returns the roman numeral representations of x
def numToRoman(x):
    answer = ""
    for i in range(0,math.floor(x/1000)):
        answer+="M"      
    numberOfHundreds = math.floor((x%1000)/100)
    if numberOfHundreds < 4:
        for i in range(0, numberOfHundreds):
            answer+="C"
    if numberOfHundreds == 4:
        answer += "CD"
    if numberOfHundreds >=5 and numberOfHundreds<=8:
        answer+="D"
        for i in range(0, numberOfHundreds-5):
            answer += "C"
    if numberOfHundreds == 9:
        answer+="CM"       
    numberOfTens = math.floor((x%100)/10)
    if numberOfTens < 4:
        for i in range(0, numberOfTens):
            answer+="X"
    if numberOfTens == 4:
        answer += "XL"
    if numberOfTens >=5 and numberOfTens<=8:
        answer+="L"
        for i in range(0, numberOfTens-5):
            answer += "X"
    if numberOfTens == 9:
        answer+="XC"
    units = x % 10
    if units < 4:
        for i in range(0, units):
            answer+="I"
    if units == 4:
        answer += "IV"
    if units >=5 and units<=8:
        answer+="V"
        for i in range(0, units-5):
            answer += "I"
    if units == 9:
        answer+="IX"
    return answer

##returns the numerical value of the roman numeral string x
def romanToNum(x):
    total = 0
    values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(0,len(x)):
        currentValue = values[x[i]]
        if i+1<len(x) and values[x[i+1]] > currentValue:
            total -= currentValue
        else:
            total += currentValue
    return total

## returns the list [x,y] where a>b to solve xa+yb=1
def euclidAlg(a,b):
    if a%b == 1:
        return [1,-(a-1)//b]
    value = a%b
    x = -(a - value)//b
    prevPara = euclidAlg(b,value)
    return [prevPara[1],prevPara[1]*x+prevPara[0]]

## returns the GCD of a and b where a>b:
def GCD(a,b):
    if a%b == 0:
        return b
    value = a%b
    x = -(a - value)//b
    return GCD(b,value)

## row Operations for a matrix M, no checks are done, so don't fuck it up
## swap rows
def swapRows(M,row1,row2):
    temp = M[row1]
    M[row1] = M[row2]
    M[row2] = temp
    return M
##multiply a row by a constant k
def multRowByConst(M,row,k):
    for i in range(len(M[row])):
        M[row][i] *= k
    return M
##add a multiple of row1 to row2
def addRowMult(M,row1,row2,k):
    for i in range(len(M[row1])):
        M[row2][i] += k*M[row1][i]
    return M

## returns the RREF of a Matrix and the indices of the columns with pivots
def RREF(m):
    matrix = m
    numRows = len(matrix)
    numCols = len(matrix[0])
    minNum = min(numRows,numCols)
    currentRow = 0
    pivots = []
    for k in range(0,numCols):
        ##find row with non-zero entry in that column and swap
        for row in range(currentRow,numRows):
            if matrix[row][k] != 0:
                matrix = swapRows(matrix,currentRow,row)
                break
        if matrix[currentRow][k] == 0:
            continue
        pivots.append([currentRow,k])
        ##make the entry in the k-k position 1
        matrix = multRowByConst(matrix,currentRow,1.0/matrix[currentRow][k])
        ##remove the other entries on that column
        for row in range(0,numRows):
            if row == currentRow:
                continue
            matrix = addRowMult(matrix,currentRow,row,-matrix[row][k])
        currentRow+=1
    return [matrix,pivots]

##make every entry in a matrix integers
def intMatrix(m):
    matrix = []
    for i in range(len(m)):
        line = []
        for j in range(len(m[i])):
            line.append(int(m[i][j]))
        matrix.append(line)
    return matrix

##return the solution of an augmented matrix given an imput for the columns with no pivots
def solM(m,pivots,imp,d):
    pivotCols = [k[1] for k in pivots]
    solution = []
    nonpivots = []
    for col in range(len(m[0])-1):
        if col in pivotCols:
            solution.append(0)
        else:
            nonpivots.append(col)
            solution.append(imp[len(nonpivots)-1])
    for i in range(len(pivots)):
        solution[pivots[i][1]] = d*m[pivots[i][0]][len(m[0])-1]
        for np in range(len(nonpivots)):
            solution[pivots[i][1]] -= imp[np]*m[pivots[i][0]][nonpivots[np]]
    return solution

##returns m1.m2 in that order
def matMult(m1,m2,mod = -1):
    if len(m1[0]) !=len(m2):
        print("incompatible matrices")
    modding = False
    if mod!=-1:
        modding = True
    newMat = []
    for row1 in range(len(m1)):
        newRow = []
        for col2 in range(len(m2[0])):
            val = 0
            for i in range(len(m1[0])):
                val+=m1[row1][i]*m2[i][col2]
            if modding:
                val%=mod
            newRow.append(val)
        newMat.append(newRow)
    return newMat

##returns m.v in that order
def matMultV(m,v,mod = -1):
    if len(m[0]) !=len(v):
        print("incompatible matrix and vector")
    modding = False
    if mod!=-1:
        modding = True
    newV = []
    for row1 in range(len(m)):
        val = 0
        for i in range(len(v)):
            val+=m[row1][i]*v[i]
        if modding:
            val%=mod
        newV.append(val)
    return newV


##print a matrix by rows
def printMat(m):
    for row in m:
        print(row)


##take the mod of each element in a matrix
def matMod(m,mod):
    newMat = []
    for i in range(len(m)):
        newRow = [x%mod for x in m[i]]
        newMat.append(newRow)
    return newMat

##give an n by n identity matrix
def identityMat(n):
    mat = [[0]*n for i in range(n)]
    for i in range(n):
        mat[i][i]=1
    return mat
    


##returns are primitive pythagorian triplets with perimeter less than MAX
def pythagorianTriplets(MAX):
    ##the perimeter will be 3r+2s+2t
    answer = []
    for r in range(2,int(MAX/3),2):
        val = int(r**2/2.0)
        facts = factors(val)
        facts.append(val)
        facts.append(1)
        facts.sort()
        for i in range(len(facts)):
            s = facts[i]
            t = int(val/s)
            if t<s:
                break
            if 3*r+2*s+2*t>=MAX:
                continue
            if GCD(t, s) != 1:
                continue
            answer.append([r+s,r+t,r+s+t])
    return answer

##Delete the duplicates in a list or lists when list(set(x)) wont work
def deleteDups(x):
    return list(x for x,_ in itertools.groupby(x))

##sort by the nth element of a list counting from zero of course
def sortN(l,n):
    l.sort(key=lambda x: x[n])
