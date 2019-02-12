print("Starting")

import useful

## only need to check subset pairs which have the same number of elements
## there are useful.nChooseK(n,s)*useful.nChooseK(n-s,s)*0.5 such pairs
## for a specific subset, we only need to look at pairs which have interweining elements
## such as (1,3)(2,4)
## number of times this doesn't happend is given by Catalan numbers given by c
## multiply that by the total number of ways to make two subsets of that size
## or useful.nChooseK(n,2*s)
## and you find how many pairs you need to check for a subset size
def c(s):
    return useful.nChooseK(2*s,s)/(s+1)

def x(n,s):
    return useful.nChooseK(n,s)*useful.nChooseK(n-s,s)*0.5-c(s)*useful.nChooseK(n,2*s)

answer = 0
N= 12
for s in range(2,7):
    answer += x(N,s)

print(answer)
