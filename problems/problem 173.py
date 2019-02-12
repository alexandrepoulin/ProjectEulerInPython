print("Starting")

MAX_NUM = 1000000

MAXSIDELEN = (MAX_NUM-4)//4+2

answer = 0

for i in range(1,MAXSIDELEN-1):
    print(i)
    counter = 0
    total = 0
    while(True):
        total += 4+4*i+8*counter
        if total > MAX_NUM:
            break
        answer +=1
        counter += 1
print(answer)

input("Done")
