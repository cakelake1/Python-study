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

def inner_is_palindrom(line, start_index, end_index):
    if line[start_index] != line[end_index]:
        return False
    if start_index >= end_index:
        return True
    return inner_is_palindrom(line, start_index + 1, end_index - 1)
def is_palindrom(s):
    if len(s) < 2 :
        return True
    return inner_is_palindrom(s, 0, len(s) - 1)

def inner_even_numbers_list(r_list2, start_index):
    if start_index > len(r_list2) - 1:
        return 0
    if r_list2[start_index] % 2 == 0:
        print(r_list2[start_index], end='')
    return inner_even_numbers_list(r_list2, start_index + 1)
def print_even_numbers_list(r_list2):
    inner_even_numbers_list(r_list2, 1)

def inner_even_index_list(r_list3, start_index):
    if start_index >= len(r_list3):
        return 0
    print(r_list3[start_index], end='')
    return inner_even_index_list(r_list3, start_index + 2)
def print_even_index_list(r_list3):
    inner_even_index_list(r_list3, 0)

