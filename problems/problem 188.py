print("Starting")

base = 1777
tetra = -1+1855
current = base
exponent = 1
mod = 10**8

while current != 1:
    current *= base
    current = current%mod
    exponent +=1

print(exponent)

values = [base]

for i in range(exponent-1):
    values.append(base*values[-1]%exponent)

def calcExp(expo):
    return values[expo-1]

def calcLastExp(expo):
    val = 1
    for i in range(0,expo):
        val*=base
        val = val%mod
    return val

currentExponent = base
for i in range(0,tetra):
    print(i)
    if i == tetra-1:
        currentExponent = calcLastExp(currentExponent)
    else:
        currentExponent = calcExp(currentExponent)
    
print(currentExponent)

input("Done")
