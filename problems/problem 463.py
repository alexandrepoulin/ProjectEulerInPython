tot = 58
##tot = 6

def triangle(n):
    return (n*(n+1))>>1
def toBase10(x):
    answer = 0
    for i in range(len(x)):
        answer += int(x[-i-1])*2**i
    return answer

total = sum((2*triangle(2**x-1)+2**x)%10**9 for x in range(0,tot))
print(total)

binform = list("11000111111101110101101001110100010101101010101010001110011")
##binform = list("1100100")

for i in range(1,len(binform)):
    if binform[i]=="0":
        continue
    prefactor = "".join(binform[:i])+"0"
    prefactor = toBase10(prefactor[::-1])
    divfactor = i+1
    total+=((triangle(2**(len(binform)-divfactor)-1)*2**divfactor+prefactor*2**(len(binform)-divfactor)))%10**9

total+=toBase10("".join(binform[::-1]))%10**9
print(total)
print(total%10**9)
