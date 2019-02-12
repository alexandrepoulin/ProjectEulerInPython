print("Starting")

#28433*2^7830457+1

exp = str(bin(7830457))[2:]

powers = [2]

for x in range(1,len(exp)):
    powers.append((powers[-1]**2)%10**10)

answer = 1
counter = 0 
for i in range(0,len(exp)):
    if exp[i] == "1":
        answer = (answer*powers[-i-1])%10**10
answer = (28433*answer+1) %10**10

print(answer)

