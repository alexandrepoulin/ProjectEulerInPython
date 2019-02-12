print("Starting")

currentLen = 1
currentVal = -1

MAX = 10**9

nodes = dict()
nodes[0] = 1

while True:
    currentVal += 1
    temp = 0
    if nodes[currentVal]+currentLen > MAX:
        temp = (MAX-currentLen)
        if (currentVal+1) in nodes:   
            nodes[currentVal+1] += temp
        else:
            nodes[currentVal+1] = temp
        if (currentVal+4) in nodes:   
            nodes[currentVal+4] += temp
        else:
            nodes[currentVal+4] = temp
        currentLen += temp
        nodes[currentVal] -= temp
        break
    else:
        temp = nodes[currentVal]
        if (currentVal+1) in nodes:   
            nodes[currentVal+1] += temp
        else:
            nodes[currentVal+1] = temp
        if (currentVal+4) in nodes:   
            nodes[currentVal+4] += temp
        else:
            nodes[currentVal+4] = temp
        currentLen += temp
        del nodes[currentVal]

answer = 0
for c in nodes:
    answer += c*nodes[c]

print(answer)
