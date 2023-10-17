
def nb_digit(n) :
    if 0 < n < 9 :
        return 1
    else :
        return 1+nb_digit(n//10)




def convert(base,n,res) :
    if n == 1 :
        res += "1"
        return res
    else :
        quotient = n // base
        reste = n % base
        res += str(reste)
        return convert(base,quotient,res)

print(convert(2,19,""))




