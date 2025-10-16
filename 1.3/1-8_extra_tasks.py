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
    return inner_even_numbers_list(r_list2, 1)

def inner_even_index_list(r_list3, start_index):
    if start_index >= len(r_list3):
        return 0
    print(r_list3[start_index], end='')
    return inner_even_index_list(r_list3, start_index + 2)
def print_even_index_list(r_list3):
    return inner_even_index_list(r_list3, 0)

def inner_second_max_list(r_list4, start_index, first_max, second_max):
    if start_index == len(r_list4):
        return second_max
    current = r_list4[start_index]
    new_first = first_max
    new_second = second_max
    if current > first_max:
        new_second = first_max
        new_first = current
    elif current > second_max:
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

import os

def all_files_finder(path, items, index):
    if index >= len(items):
        return []
    item = items[index]
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        current_files = [full_path]
    if os.path.isdir(full_path):
        subdir_items = os.listdir(full_path)
        current_files = all_files_finder(full_path, subdir_items, 0)
    rest_files = all_files_finder(path, items, index + 1)
    result = current_files + rest_files
    return result

def find_all_files(path):
    items = os.listdir(path)
    return all_files_finder(path, items, 0)

def bracket_comb(current_string, opened, closed, total_pairs, results):
    if opened == total_pairs and closed == total_pairs:
        results.append(current_string)
        return 
    if opened < total_pairs:
        new_string = current_string + '('
        bracket_comb(new_string, opened + 1, closed, total_pairs, results)
    if closed < opened:
        new_string = current_string + ')'
        bracket_comb(new_string, opened, closed + 1, total_pairs, results)
def bracket(n):
    combinations = []
    if n > 0:
        bracket_comb("", 0, 0, n, combinations)
    return combinations

def find_all_files(path):
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        print(item)
        if os.path.isdir(item_path):
            find_all_files(item_path)

def find_all_files(path):
    items = os.listdir(path)
    result = []
    for item in items:
        item_path = os.path.join(path, item)
        result.append(item)
        if os.path.isdir(item_path):
            result.extend(find_all_files(item_path))
    return result