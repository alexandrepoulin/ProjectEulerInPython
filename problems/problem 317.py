from math import pi
g= 9.81
h= 100
v=20

##consider the explosion at the origine. The envelope will be a parabola.
##We need to find 3 points to define the parabola in the x z plane
##The heigh is easy to find and is h'=v^2/(2g)
##shooting at a 45 degree angle, we find dr = v^2/g
##This gives the function f1(z)=(dr^2-r^2)h'/dr^2
##shifting by h upwards, we find z = (dr^2-r^2)h'/dr^2 +h = h+h'-r^2(h'/dr^2)
##we now need to integrate this, but we don't know the bounds of r since we added h (and this is really hard to find)
##so we integrate over z using the disk method (?)
##solving for r^2 = (h+h'-z)*dr^2/h'
##integrating: V=pi Int_0^(h'+h)r^2dz =pi * dr^2/h'((h'+h)^2-(h'+h)^2/2)=pi * dr^2 *(h'+h)^2/(2h')
##subbing in values: V = pi * (v^2/g)^2 * ( (v^2/(2g)) + h )^2 /(2(v^2/(2g)))
##Simplifying: V = pi * v^2 * ( v^2 + 2gh )^2 /(4*g^3)


print(pi*v**2*(2*h*g+v**2)**2/(4*g**3))
