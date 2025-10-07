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

def is_palindrom(s):
    s = s.lower().replace(' ','')
    if len(s) < 2 :
        return True
    if s[0] != s[-1]:
        return False
    chars = list(s)
    chars.pop(0)
    chars.pop()
    s = ''.join(chars)
    return is_palindrom(s)

def print_even_numbers_list(r_list2):
    if len(r_list2) == 0:
        return 0
    if r_list2[0] % 2 == 0:
        print(r_list2[0], end='')
    r_list2.pop(0)
    return print_even_numbers_list(r_list2)

def print_even_index_list(r_list3):
    if len(r_list3) == 0:
        return 0
    print(r_list3[0], end='')
    r_list3.pop(0)
    if len(r_list3) > 0 :
        r_list3.pop(0)
    return print_even_index_list(r_list3)

