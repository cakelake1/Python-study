# # Внесите 12 правок в свой код, в которых улучшите работу с константами, и напишите по каждой, что конкретно вы улучшили.
# # У меня есть код:
# def white_walkers(village):
#     cu_sum_prefix = [0] * (len(village) + 1)
#     list_digits = []
#     for i, char in enumerate(village):
#         cu_sum_prefix[i+1] = cu_sum_prefix[i] + (char == '=')
#         if char.isdigit():
#             list_digits.append((i, int(char)))
#     if len(list_digits) < 2:
#         return False
#     correct_pairs = []
#     for i in range(len(list_digits) - 1):
#         index_1, number_1 = list_digits[i]
#         index_2, number_2 = list_digits[i+1]
#         count = cu_sum_prefix[index_2] - cu_sum_prefix[index_1 + 1]
#         if number_1 + number_2 == 10:
#             correct_pairs.append(count == 3)
#     return bool(correct_pairs) and all(correct_pairs)

# Я могу его улучшить и избавиться от магических чисел (10 и 3) и от магического символа ('=')
# def white_walkers(village):
#     WALKER_SYMBOL = '='
#     SUM_TARGET = 10
#     COLLECT_WALKERS = 3
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

# В следующем коде:
# def army_communication_matrix(n, matrix):
#     max_row = 0
#     max_sum = None
#     max_col = 0
#     max_size = 2
#     new_matrix = sum_elements(n, matrix)
#     for size in range(2, n):
#         for row in range(n - size + 1):
#             for col in range(n - size + 1):
#                 current_sum = sum_matrix(new_matrix, row, col, size)
#                 if max_sum is None or current_sum > max_sum:
#                     max_sum = current_sum
#                     max_row, max_col, max_size = row, col, size
#     return str(max_col) + " " + str(max_row) + " " + str(max_size)
# Убираю магические числа, обавляю константы, заменяю стартовые значения константами.
# def army_communication_matrix(n, matrix):
#     MIN_SIZE = 2 # Задаю стартовое значение в виде константы 1 
#     DEFAULT_START = 0 # Задаю стартовое значение в виде константы 2
#     NO_RESULT = None # Задаю стартовое значение в виде константы 3 
#     max_row = DEFAULT_START # Заменяю стартовое значение константой
#     max_sum = NO_RESULT # Заменяю стартовое значение константой
#     max_col = DEFAULT_START # Заменяю стартовое значение константой
#     max_size = MIN_SIZE # убираю магическое число
#     new_matrix = sum_elements(n, matrix)
#     for size in range(MIN_SIZE, n): # убираю магическое число
#         for row in range(n - size + 1):
#             for col in range(n - size + 1):
#                 current_sum = sum_matrix(new_matrix, row, col, size)
#                 if max_sum is NO_RESULT or current_sum > max_sum: # заменяю None стартовым значением(константой)
#                     max_sum = current_sum
#                     max_row, max_col, max_size = row, col, size
#     return str(max_col) + " " + str(max_row) + " " + str(max_size)