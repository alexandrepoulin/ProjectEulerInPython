print("Starting")

length = 1 #length rectangle
heigth = 1 #heigth rectangle

found = False

def countRec(l,h):
    answer = 0 
    for i in range(0,l):
        for j in range(0,h):
            answer += (l-i)*(h-j)
    return answer

answer = 0

while not found:
    length += 1
    heigth = 1
    while True:
        heigth += 1
        val = countRec(length,heigth)
        if abs(2000000 - val) < 16:
            found = True
            answer = length*heigth
            break
        if val > 2000000:
            break 

print(answer)
input("Done")
    
