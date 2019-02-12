print("Starting")

file = open("words.txt")
import math

squares = [[]]
for i in range(1,15):
    currentSet = set()
    for k in range(int(math.ceil(10**((i-1)/2))),int(math.floor(10**(i/2)))):
        currentSet.add(k**2)
    squares.append(currentSet)


def sort(x):
    letters = list(x)
    numbers = [y for y in map(lambda k: ord(k),letters)]
    numbers.sort()
    word = ""
    for k in numbers:
        word += chr(k)
    return word
        
words = {}
for line in file:
    line = line.strip()
    tokens = line.split(',')
    for t in tokens:
        k = t.strip("\"")
        words.update({k:sort(k)})

bestSoFar = 0
bestWords = []
bestNumbers = []
bestLength = 0
bestSigma = {}

for i in words:
    print(i)
    if len(i) < bestLength:
        continue
    for j in words:
        if len(i) != len(j):
            continue
        if i != j and i!= j[::-1] and words[i] == words[j]:
            iLetters = list(i)
            jLetters = list(j)
            sigma = {}
            length = len(iLetters)
            for k in range(0,length):
                sigma.update({k:jLetters.index(iLetters[k])})
            for s in squares[length]:
                number = list(str(s))
                if len(set(number)) != len(set(iLetters)):
                    continue
                number2 = [""]*length
                for m in range(0,length):
                    number2[sigma[m]] = number[m]
                temp = ""
                for x in number2:
                    temp += x
                number2 = int(temp)
                if number2 in squares[length]:
                    if s > bestSoFar:
                        bestSoFar = s
                        bestNumbers = [s,number2]
                        bestWords = [i,j]
                        bestLength = length
                        bestSigma = sigma
                    if number2 > bestSoFar:
                        bestSoFar = number2
                        bestWords = [i,j]
                        bestNumbers = [s,number2]
                        bestLength = length
                        bestSigma = sigma

print(bestWords)
print(bestNumbers)
print(bestLength)
print(bestSoFar)
print(bestSigma)

input("Done")
                    
                    
            

