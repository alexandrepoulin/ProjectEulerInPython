print("Starting")

MAX = 10**6
nums = list(0 for x in range(0,MAX+1))

def calTiles(hole,square):
    return (square-hole)*(square+hole)
print("Done making list")
holeSize = 1
squareSize = holeSize
changed = True
while changed:
    changed = False
    while True:
        squareSize+=2
        tiles = calTiles(holeSize,squareSize)
        if tiles > MAX:
            break
        nums[tiles]+=1
        changed = True
    holeSize+=1
    squareSize = holeSize
print("Done Calculating tiles")
answer = 0
for i in range(len(nums)):
    if nums[i]>=1 and nums[i]<=10:
        answer +=1

print(answer)
    
    
    
    
