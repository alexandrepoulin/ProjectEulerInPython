print("Starting")

numbs = set()

length = 1

while True:
    length+=1
    value = 0
    for i in range(1,length+1):
        value+=i**2
    if value > 10**8:
        break
    counter = 0
    while value < 10**8:
        counter +=1
        numbs.add(value)
        value += (counter+length)**2-counter**2

print(sum(filter(lambda x: str(x)==str(x)[::-1],numbs)))
