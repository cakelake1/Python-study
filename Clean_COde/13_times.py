# На данном своем этапе обучения я технически понимаю когда переменная и ее значение связываются вместе, но пока пратических задач нет в моем решебнике, нужно боле глубокое понимание. Но пка я могу сделать на примере учебных задач:
# Пример 1 - раннее связывание. ПРоисходит при компиляции кода. Легко исправить значения в начале кода
# def white_walkers(village):
#     WALKER_SYMBOL = '=' # Пример 1
#     SUM_TARGET = 10 # Пример 2
#     COLLECT_WALKERS = 3 # ПРимер 3
#     cu_sum_prefix = [0] * (len(village) + 1)
#     list_digits = []
#     for i, char in enumerate(village):
#         cu_sum_prefix[i+1] = cu_sum_prefix[i] + (char == WALKER_SYMBOL) # убрал магический символ
#         if char.isdigit():
#             list_digits.append((i, int(char)))
#     if len(list_digits) < 2:
#         return False
#     correct_pairs = []
#     for i in range(len(list_digits) - 1):
#         index_1, number_1 = list_digits[i]
#         index_2, number_2 = list_digits[i+1]
#         count = cu_sum_prefix[index_2] - cu_sum_prefix[index_1 + 1]
#         if number_1 + number_2 == SUM_TARGET: # убрал магическое число 1
#             correct_pairs.append(count == COLLECT_WALKERS) # убрал магическое число 2
#     return bool(correct_pairs) and all(correct_pairs)

# # Пример 2 Связывания пни запуске программы, пользователь может перезапустить программу с новой процентной ставкой НДС 22%, которая поменялась по закону
# import os
# NDS = float(os.getenv('NDS_RATE', '0.2')) 
# def calculate_nds(price):
#     return price * NDS
# print(calculate_nds(100))

# # Пример 3 Позднее связывание. НАпример бухгалтер ведет черную\серую бухгалтерию и меняет значения в последний момент
# def calculate_ndfl(salary):
#     ndfl = float(input("Введите НДФЛ: "))  
#     return salary - (salary  * (ndfl/100))

# print(calculate_ndfl(40000))