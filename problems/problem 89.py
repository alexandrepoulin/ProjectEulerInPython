print("starting")
import useful



file = open("roman.txt")
counter = 0

for line in file:
    line = line.strip()
    counter+= len(line)-len(str(useful.numToRoman(useful.romanToNum(line))))


print(counter)
input("Done")
