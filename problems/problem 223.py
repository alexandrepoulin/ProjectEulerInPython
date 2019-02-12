print("Starting")
MAX = 10**4
counter = (MAX-1)//2

done = set()

for a in range(2,MAX//3):
    if a in done:
        continue
    asquared = a**2
    print(a)
    for b in range(a,(MAX-a)//2):
        if 2*b > asquared:
            break
        val =(asquared+b**2-1.0)**0.5
        if (int(val)-val) < 0.00001:
            if a+b+val < MAX:
                for i in range(1,MAX//(a+b+int(val))):
                    if i*a not in done:
                        counter +=1
                        done.add(i*a)
                break

print(counter)
input("Done")
