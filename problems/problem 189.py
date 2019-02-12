print("starting")

layer = 1
MAXLAYER = 8

answer = 3

while layer != MAXLAYER:
    layer += 1
    answer*=8*3**(layer-2)
    
    

print(answer)
        
