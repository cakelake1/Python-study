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
""" def poliandrom_check(r_word):
    if not r_word:
        r_word =r_word.lower().replace(' ','')
        end = len(r_word) - 1
        start = r_word[0]
    if len(r_word[start]) >= len(r_word[end]):
        return True
    if r_word[start] != r_word[end]:
        return False
    r_word.pop(0)
    r_word.pop(end)
    return poliandrom_check(r_word) """
""" def is_palindrom1(s):
    s = s.lower().replace(' ','')
    if len(s) < 2 :
        return True
    if s[0] != s[-1]:
        return False
    chars = list(s)
    chars.pop(0)
    chars.pop()
    s = ''.join(chars)
    return is_palindrom(s) """
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
   

""" print(is_palindrom('a'))
print(is_palindrom('aba'))
print(is_palindrom('anna'))
print(is_palindrom('Anna'))
print(is_palindrom('acab'))
print(is_palindrom(''))
print(is_palindrom('An na'))
print(is_palindrom('aAbcbaa'))
print(is_palindrom('abca')) """
""" 
print(poliandrom_check('a'))
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
def inner_even_numbers_list(r_list2, start_index):
    if start_index >= len(r_list2):
        return 0
    if r_list2[start_index] % 2 == 0:
        print(r_list2[start_index], end='')
    return inner_even_numbers_list(r_list2, start_index + 1)
def print_even_numbers_list(r_list2):
    return inner_even_numbers_list(r_list2, 1)

""" print_even_numbers_list([1,2,3,4])
print_even_numbers_list([1,2,0,3,4,5,6,7,8,9,1,0,1,1,1,2]) """
def inner_even_index_list(r_list3, start_index):
    if start_index >= len(r_list3):
        return 0
    print(r_list3[start_index], end='')
    return inner_even_index_list(r_list3, start_index + 2)
def print_even_index_list(r_list3):
    return inner_even_index_list(r_list3, 0)
""" print_even_index_list([0,1,2,3,4])
print_even_index_list([0,1,2,3,4,5])
print_even_index_list([1,2,3,4])
print_even_index_list([1,2,0,3,4,5,6,7,8,9,1,0,1,1,1,2]) """
def inner_second_max_list(r_list4, start_index, first_max, second_max):
    if start_index == len(r_list4):
        return second_max
    current = r_list4[start_index]
    new_first = first_max
    new_second = second_max
    if current > first_max:
        new_second = first_max
        new_first = current
    if current > second_max:
        new_second = current
    return inner_second_max_list(r_list4, start_index + 1, new_first, new_second)
def second_max_list(r_list4):
    if len(r_list4) < 2:
        return None
    if r_list4[0] > r_list4[1]:
        first = r_list4[0]
        second = r_list4[1]
    else:
        first = r_list4[1]
        second = r_list4[0]
    return inner_second_max_list(r_list4, 2, first, second)
""" print(second_max_list([1,2,3,4,5,5,6,6]))  # 
print(second_max_list([1,2,3,4,5,5,6,6]))  #
print(second_max_list([1,2,3]))
print(second_max_list([1,2,3,3]))
print(second_max_list([1,2]))
print(second_max_list([1]))  """ 
import os

def all_files(path, items, index):
    if index >= len(items):
        return []
    item = items[index]
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        current_files = [full_path]
    elif os.path.isdir(full_path):
        subdir_items = os.listdir(full_path)
        current_files = all_files(full_path, subdir_items, 0)
    else:
        current_files = []
    rest_files = all_files(path, items, index + 1)
    return current_files + rest_files

def find_all_files(path):
    items = os.listdir(path)
    return all_files(path, items, 0)

def build_parentheses_combinations(current_string, opened, closed, total_pairs, results):
    if opened == total_pairs and closed == total_pairs:
        results.append(current_string)
        return
    if opened < total_pairs:
        new_string = current_string + '('
        build_parentheses_combinations(new_string, opened + 1, closed, total_pairs, results)
    if closed < opened:
        new_string = current_string + ')'
        build_parentheses_combinations(new_string, opened, closed + 1, total_pairs, results)
