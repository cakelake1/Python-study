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
""" print(length_check_pop([1,2,3,4])) """
def poliandrom_check(r_word, start = 0, end = 0):
    if end == 0:
        r_word =r_word.lower().replace(' ','')
        end = len(r_word) - 1
    if start >= end:
        return True
    if r_word[start] != r_word[end]:
        return False
    return poliandrom_check(r_word, start + 1, end - 1)
""" print(poliandrom_check('a'))
print(poliandrom_check('ab'))
print(poliandrom_check('anna'))
print(poliandrom_check('Anna'))
print(poliandrom_check('acab'))
print(poliandrom_check(''))
print(poliandrom_check("?!@#"))  """
""" def print_even_numbers(r_num):
    if r_num == 0:
        return 0
    print_even_numbers(r_num//10)
    last_num = r_num % 10
    if last_num % 2 == 0:
        print(last_num, end='')
print_even_numbers(1234)
print_even_numbers(1203456789101112)
print_even_numbers([1,2,3,4]) """
def print_even_numbers_list(r_list2, start = 0):
    if start >= len(r_list2):
        return 0
    if r_list2[start] % 2 == 0:
        print(r_list2[start], end='')
    return print_even_numbers_list(r_list2, start + 1)
""" print_even_numbers_list([1,2,3,4]) """
def print_even_index_list(r_list3, start = 0):
    if start >= len(r_list3):
        return 0
    print(r_list3[start], end='')
    return print_even_index_list(r_list3, start + 2)
print_even_index_list([1,2,3,4])
print_even_index_list([1,2,0,3,4,5,6,7,8,9,1,0,1,1,1,2])