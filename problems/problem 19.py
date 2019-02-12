#tuesday for 1st Jan 1901

print("Starting...")

sep = 30
apr = 30
jun = 30
nov = 30
jan = 31
mar = 31
may = 31
jul = 31
aug = 31
octo = 31
dec = 31

def feb(year):
    if isLeapYear(year):
        return 29
    return 28

def isLeapYear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    return False



counter = 0
remainder = 0
for i in range(1901, 2001):
    months = [jan, feb(i), mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
    for k in range(0,12):
        if (months[k] + remainder) % 7 == 5:
            counter += 1;
        remainder = (months[k] + remainder) % 7




print(counter)

print("Done")
input("Press Something to exit")

