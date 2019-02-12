print("Starting")
##the solution to 2x^2-y^2-2x+y=0 where x is the number of blue disks and y is the total
##number of disks is given by x_(n+1) = 3x_n+2y_n-2 and y_(n+1)=4x_n+3y_n-3


x = 85
y = 120
while y <= 10**12:
    x,y =3*x+2*y-2, 4*x+3*y-3
    print(2*x**2-y**2-2*x+y)
print(x,y)
input("Done")
