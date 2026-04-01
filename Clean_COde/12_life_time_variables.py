# Имеется код:
# # def SherlockValidString(s):
# #     for i in s:
# #         if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')):
# #             return False
# #     lower_s = s.lower()
# #     dict_chars = {}
# #     for i in lower_s:
# #         dict_chars[i] = dict_chars.get(i, 0) + 1
# #     chars_list = list(dict_chars.values())
# #     if all(j == chars_list[0] for j in chars_list):
# #         return True # все значения одинаковые
# #     min_chars = min(chars_list)
# #     max_chars = max(chars_list)
# #     min_count = sum(1 for j in chars_list if j == min_chars )
# #     max_count = sum(1 for j in chars_list if j == max_chars)
# #     if (max_chars - min_chars ==1) and (max_count ==1):
# #         return True
# #     if (min_chars == 1) and (min_count == 1):
# #         return True
# #     return False

# def is_valid_char(s): #1 добавил отдельную функицю проверки символов
#     LOWER = 'abcdefghijklmnopqrstuvwxyz'
#     UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in s:
#         if not (i in LOWER or i in UPPER):
#             return False
#     return True
        
# def count_char_freq(s): #2 добавил отдельную функицю подсчета частот
#     freq = {} #3 Переименовал переменную dict_chars на более понятную и вынес ее в отдельную функцию
#     lower_s = s.lower() #4 вынес локальную переменную в отдельную функцию
#     for i in lower_s:
#         freq[i] = freq.get(i, 0) + 1
#     return freq

# def all_equal(values): #5 добавил отдельную функицю проверки на равенство
#     if not values:
#         return True
#     return all(j == values[0] for j in values)

# def one_more_diff_freq(values): #6 добавил отдельную функцию проверки, что одна частота отличается на 1
#     min_chars = min(values)
#     max_chars = max(values)
#     if max_chars - min_chars != 1:
#         return False
#     max_count = sum(1 for j in values if j == max_chars)
#     return max_count == 1

# def one_one_freq(values): #7 добавил отдельную функцию проверки, что одна частота будет 1 , а остальные одинаковые
#     min_chars = min(values)
#     if min_chars != 1:
#         return False
#     min_count = sum(1 for j in values if j == min_chars )
#     if min_count != 1:
#         return False
#     list_values = [i for i in values if i != min_chars]
#     return all_equal(list_values)

# def SherlockValidString(s): #8 изменил основную функцию, удалил все локальные переменные, добавил две новые локальные переменные
#     if not is_valid_char(s): #9,10 вызываю отдельную функцию, вместо локальной проверки, также упростил выражение в функции if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')) через добавление констант
#         return False
#     freq_count = count_char_freq(s) #11 Вместо ручного подсчета вызываю отдельную функцию, куда спрятал локальные переменные
#     freq_values = list(freq_count.values())
#     if all_equal(freq_values): # 12, 13 вызываю отдельную функцию, вместо локальной проверки all(j == chars_list[0] for j in chars_list), a также добавил проверку на пустой список.
#         return True
#     if one_more_diff_freq(freq_values): #14 вызываю отдельную функцию, вместо локальной проверки (max_chars - min_chars ==1) and (max_count ==1)
#         return True
#     if one_one_freq(freq_values): #15 вызываю отдельную функцию, вместо локальной проверки (min_chars == 1) and (min_count == 1)
#         return True
#     return False

