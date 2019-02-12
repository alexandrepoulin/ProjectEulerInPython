print("Starting")

import dioph, useful

##need 0=5b^2-4L^2+-8b+4

solutionNeg = [16,17]
solutionPlus =[272,305]
## P Q K R S L
## X_(n+1) = PX_n+QY_n+K
## Y_(n+1) = RX_n+SY_n+L

##These are from http://www.alpertron.com.ar/QUAD.HTM
##after inserting the equation
plusRecCoeff= [-9,-8,-8,-10,-9,-8]
negRecCoeff= [-9,-8,8,-10,-9,8]


def nextNeg(val):
    x = val[0]
    y = val[1]
    xnew = negRecCoeff[0]*x+negRecCoeff[1]*y+negRecCoeff[2]
    ynew = negRecCoeff[3]*x+negRecCoeff[4]*y+negRecCoeff[5]
    return [xnew,ynew]
def nextPlus(val):
    x = val[0]
    y = val[1]
    xnew = plusRecCoeff[0]*x+plusRecCoeff[1]*y+plusRecCoeff[2]
    ynew = plusRecCoeff[3]*x+plusRecCoeff[4]*y+plusRecCoeff[5]
    return [xnew,ynew]

currentNeg = solutionNeg
currentPlus = solutionPlus
answer = 17+305
for i in range(5):
    currentNeg = nextNeg(currentNeg)
    currentPlus = nextPlus(currentPlus)
    currentNeg = nextNeg(currentNeg)
    currentPlus = nextPlus(currentPlus)
    answer += currentNeg[1]
    answer += currentPlus[1]

print(answer)
    
