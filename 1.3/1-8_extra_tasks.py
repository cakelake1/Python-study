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
def poliandrom_check(r_word):
    r_word =r_word.lower().replace(' ','')
    if len(r_word) <= 1:
        return True
    if r_word[0] != r_word[-1]:
        return False
    return poliandrom_check(r_word[1:-1])
def print_even_numbers_list(r_list2):
    if not r_list2:
        return 0
    if r_list2[0] % 2 == 0:
        print(r_list2[0], end='')
    return print_even_numbers_list(r_list2[1:])
def print_even_index_list(r_list3):
    if not r_list3:
        return 0
    print(r_list3[0], end='')
    if len(r_list3) > 2:
        return print_even_index_list(r_list3[2:])

