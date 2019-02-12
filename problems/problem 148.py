print("Starting")

## the nth row has n entries
## the number of factors of 7 in the numerator goes up every 7 rows starting from the first row.
## need at least 1 extra factor of 7, it is easier to find the number which are not divisible

## (number of factors of 7 in nominator of row n) = (n-1)//7, ex row 9 has 1
## (number of entries that are not divisible in a row):(n//7+1)((n+1)%7)
## 1+2+3+4+5+6=21
## note that 999999994=142857142*7, so 10**9-999999994=6 and the case where 10**9+1 gives no contribution
## since (10**9+1)%7 =0. So we can consider the sum up to row 10**9+1.
## thus get sum up to 142857142+1 gives up to 142857143*21
## the sum is thus 21*142857143*142857144/2
## =21*142857143*71428572


#print(21*71428571*142857143)

##blasts, i'm missing some factors of 7 because of squares like 49

