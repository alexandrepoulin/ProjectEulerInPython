
import useful as u


m=[
            [1, 6, 0, 0, 0 ,0 ,0],
            [1, 1, 5, 0, 0, 0, 0],
            [1, 1, 1, 4, 0, 0, 0],
            [1, 1, 1, 1, 3, 0, 0],
            [1, 1, 1, 1, 1, 2, 0],
            [1, 1, 1, 1, 1, 1, 1],  
            [0, 0, 0, 0, 0, 0, 7],
        ]
v= [[7],[0],[0],[0],[0],[0],[0]]

finalM = u.expEffMat(m,10**12,10**9)
print(u.matMult(finalM,v,10**9)[0][0])

