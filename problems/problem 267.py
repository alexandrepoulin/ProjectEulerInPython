##Start with M dollars, the next amounts will be:
##M_+=M(1+2f)
##M_-=M(1-f)
##Most probably, 
##M_f=(1+2f)^(1000-n) (1-f)^n
##〖10〗^9=(1+2f)^(1000-n) (1-f)^n
##9 ln⁡10=(1000-n)  ln⁡(1+2f)+n ln⁡(1-f)
##9 ln⁡10-1000 ln⁡(1+2f)=n ln⁡〖((1-f))/((1+2f) )〗
##(9 ln⁡10-1000 ln⁡(1+2f) ) (ln⁡〖((1-f))/((1+2f) )〗 )^(-1)=n
##
##dn/df=(((-2000)/((1+2f) )) (ln⁡〖((1-f))/((1+2f) )〗 )^(-1)-(9 ln⁡10-1000 ln⁡(1+2f) ) (ln⁡〖((1-f))/((1+2f) )〗 )^(-2)  ((1+2f))/((1-f) ) (-1/((1+2f) )-2(1-f)/(1+2f)^2 ) )
##0=(-2000(ln⁡〖((1-f))/((1+2f) )〗 )-(9 ln⁡10-1000 ln⁡(1+2f) )(-((1+2f))/((1-f) )-2) )
##0=(-2000(ln⁡〖((1-f))/((1+2f) )〗 )+(9 ln⁡10-1000 ln⁡(1+2f) )(3/((1-f) )) )
##2000/3 (1-f)(ln⁡〖((1-f))/((1+2f) )〗 )=(9 ln⁡10-1000 ln⁡(1+2f) )
##2/3 (1-f)(ln⁡〖((1-f))/((1+2f) )〗 )+ln⁡(1+2f)=9/1000  ln⁡10
##(1+2f)(((1-f))/((1+2f) ))^(2/3 (1-f) )-〖10〗^(9/1000)=0
##
##
##f= 0.146883922440940676575582401...
##
##1000-568=432
##P=1/2^1000  ∑_(n=432)^1000▒(█(1000@n)) 
##P=0.999992836186713594670702126004996978214851084651108957314045...
##
##

print(0.999992836187)