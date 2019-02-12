print("Starting")
import math
answer = 50+49 ## edge

ballOrder= [50,48,46,44,42,40,38,36,34,32,30,31,33,35,37,39,41,43,45,47,49]
## need to minimize 4*L1L2-200(L1+L2) which happens if L1 is close to L2 

for i in range(len(ballOrder)-1):
    val1 = ballOrder[i]
    val2 = ballOrder[i+1]
    temp = math.sqrt((val1+val2)**2-(100-val1-val2)**2)
    answer+= temp

print(answer*1000)

