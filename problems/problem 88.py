print("Starting")

MAX = 12000+1
counters = [2]*15
kValues = [0]*MAX
going = True
while going:
    number = 1
    sumSoFar = 0
    going = False
    for i in range(0,15):
        number *= counters[i]
        sumSoFar += counters[i]
        if number >= 2*MAX:
            break
        k = number-sumSoFar+i+1
        if k >= MAX or k<= 1:
            continue
        if kValues[k] > number or kValues[k] == 0:
            kValues[k] = number
    for i in range(0,15):
        if counters[i] < 2*MAX:
            numb = counters[i]+1
            prod = 1
            for l in range(i+1,15):
                if counters[l] != 2:
                    prod *= counters[l]
            if numb**(i+1) <= 2*MAX/prod:
                for j in range(0,i+1):
                    counters[j] = numb
                going = True
                break
            else:
                continue

print(sum(set(kValues)))
input("Done")
        
    
