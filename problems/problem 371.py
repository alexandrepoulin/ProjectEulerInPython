
import useful as u
import math

fiveTrack=[0]*500
nonFiveTrack=[0]*500

fiveTrack[499]=2
nonFiveTrack[499]=501/250

for i in range(498,-1,-1):
    fiveTrack[i]=(1000/(999-i))* (1+ (1-(i+1)/500)*fiveTrack[i+1])
    nonFiveTrack[i]=(1000/(999-i))* (1+ (1-(i+1)/500)*nonFiveTrack[i+1]+1/1000*fiveTrack[i])

print(nonFiveTrack[0])
