print("starting")

## the series has A_F(x)=xF1+x^2F2+x^3F_3 +...
## is A_F(x)=x/(1-x-x^2) and works for x< 1/phi = 0.61803398875

## if N=x/(1-x-x^2)
## -N+(N+1)x+Nx^2=0
## x = (-(N+1) +- sqrt(N^2+2N+1+4N^2))/2N
## x = (-(N+1) +- sqrt(5N^2+2N+1))/2N need +
## x = (sqrt(6N^2+2N+1)-(N+1))/2N

## a golden nuggest will occur when 5N^2+2N+1 =q^2 for some q
## need to solve diophantine equation 5N^2-q^2+2N+1 = 0
## find the recusion:
import dioph
rec = dioph.solveRecurrence(5,0,-1,2,0,1)

## the independent solutions are:
solutions = dioph.solve(5,0,-1,2,0,1)
##some issues, just fixing them
solutions = [x for x in filter(lambda k: (5*k[0]**2-k[1]**2 +2*k[0]+1) == 0 ,solutions)]
nuggets = solutions.copy()

##the next generated solutions will be:

def nextSolTemp(s):
    return [rec[0]*s[0]+rec[1]*s[1]+rec[2],rec[3]*s[0]+rec[4]*s[1]+rec[5]]
def nextSol(s):
    return nextSolTemp(nextSolTemp(s))

for s in solutions:
    current = s
    for i in range(10): ##10 should be enough
        current = nextSolTemp(current)
        nuggets.append(current)

##need to sort the nuggets based on first index
sortedNuggets = set([x[0] for x in nuggets])
sortedNuggets = [x for x in filter(lambda k: k>0,sortedNuggets)]
sortedNuggets.sort()

    
print(sortedNuggets[14])
