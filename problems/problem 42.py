print("Starting")


#ord('A')=65
#ord("\"")=34
def stringNumber(x):
    total = 0
    for i in x:
        if ord(i)==34:
            continue
        total += (ord(i)-64)
    return total

def isTri(x):
    num = stringNumber(x)
    i = 0
    tn = 0
    while tn < num:
        i += 1
        tn = int(1/2*i*(i+1))
        if tn == num:
            return True
    return False
    
file = open("words.txt")

for line in file:
    tokens = line.split(",")

count = 0

for x in tokens:
    if isTri(x):
        count+=1

print(count)
input("Press something")






