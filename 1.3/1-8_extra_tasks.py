def exponentiation(n,m):
    if m == 0:
        return 1
    return n * (exponentiation(n, m-1))

def sum_digit(s):
    if s < 0:
        return -sum_digit(-s)
    if s < 10:
        return s
    return s%10 + sum_digit(s//10)
 
def length_check_pop(r_list):
    if r_list == []:
        return 0
    r_list.pop(0)
    return 1 + length_check_pop(r_list)