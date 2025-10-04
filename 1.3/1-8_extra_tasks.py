def exponentiation(n,m):
    if m == 0:
        return 1
    else:
        return n * (exponentiation(n, m-1))
""" print(exponentiation(2,3)) # 8
print(exponentiation(2,10)) # 1024
print(exponentiation(3,10)) # 59049
print(exponentiation(3,0)) # 1
print(exponentiation(1.1414,2)) # 1.30279396 """

def sum_digit(s):
    if s < 0:
        return -sum_digit(-s)
    if s < 10:
        return s
    else:
        return s%10 + sum_digit(s//10) 
""" print(sum_digit(123))
print(sum_digit(1))
print(sum_digit(2))
print(sum_digit(-11))
print(sum_digit(-33))
print(sum_digit(10))
print(sum_digit(11))
print(sum_digit(0))
print(sum_digit(-1))
print(sum_digit(12))
print(sum_digit(344))
print(sum_digit(1024)) """
def length_check_pop(r_list):
    if r_list == []:
        return 0
    else:
        r_list.pop(0)
        return 1 + length_check_pop(r_list)
print(length_check_pop([1,2,3,4]))