# 3.1. Прокомментируйте 7 мест в своём коде там, где это явно уместно.
# def TankRush(H1, W1, S1, H2, W2, S2):
#     # 1.Задача проверяет наличие подматрицы S2 в матрице S1
#         # H1,W1 высота и ширина матрицы
#         # S1 строка с пробелами, например 1234 2345 0987
#         # S2, H2, W2 аналогичные значения для подматрицы
#     # 2. По условию задачи у нас строгий формат входных данных, но если это не так, алгоритм даст неверный результат или ошибку.
#     map1 = S1.split()
#     map2 = S2.split()
#     # 3.Подматрица не может поместиться в матрицу - ранний выход(оптимизация)
#     if H2 > H1 or W2 > W1:
#         return False
#     # 4.пустая подматрица всегда содержится в матрице(математическое определение)(оптимизация)
#     if H2 == 0 or W2 == 0:
#         return True
#     # 5.перебираем все возможные верхние левые углы (i, j), куда может встать подматриа.
#         # H1 - H2 + 1 — количество позиций по вертикали (индексы от 0 до H1-H2 включительно). 
#         # аналогично по горизонтали.
#     for i in range(H1 - H2 + 1):
#         for j in range(W1 - W2 + 1):
#             match = True
#             for k in range(H2):
#                 if map1[i+k][j:j + W2] != map2[k]: # 6.предполагаетcя, что все строки в map1 имеют ДЛИНУ НЕ МЕНЕЕ j+W2, стобы не получить indexError
#                         match = False # 7. Выжодим из цикла при любом несовпадении(оптимизация)
#                         break
#             if match: 
#                 return True
#     return False

# 3.2. Если вы раньше делали комментарии к коду, найдите 5 мест, где эти комментарии были излишни, удалите их и сделайте сам код более наглядным.
# было:
# def WordSearch(width, s, subs):
#     words = s.split(' ')
#     lines = []
#     current_line = []
#     current_length = 0

#     # Разбиваем на строки с учетом ширины
#     for word in words:
#         # Разбиваем слово на части, если оно слишком длинное
#         while len(word) > width:
#             part = word[:width]
#             lines.append(part)
#             word = word[width:]
        
#         # Пытаемся добавить слово в текущую строку
#         new_length = current_length + (len(word) + 1 if current_length > 0 else len(word))
#         can_fit = new_length <= width
        
#         # Добавляем слово в текущую строку или начинаем новую
#         current_line = (current_line + [word]) if can_fit else [word]
#         current_length = new_length if can_fit else len(word)
        
#         # Если строка заполнена, добавляем в lines
#         line_full = current_length == width
#         lines.append(' '.join(current_line)) if line_full else None
#         current_line = [] if line_full else current_line
#         current_length = 0 if line_full else current_length
    
#     # Добавляем последнюю строку, если она не пустая
#     lines.append(' '.join(current_line)) if current_line else None

#     # Проверяем наличие слова subs в каждой строке (без if)
#     result = []
#     for line in lines:
#         words_in_line = line.split()
#         found = subs in words_in_line
#         result.append(1 * found)  # True → 1, False → 0
    
#     return result

# Стало:
# def WordSearch(width, s, subs):
#     words = s.split(' ')
#     lines = []
#     current_line = []
#     current_length = 0
#     for word in words:
#         # Разбиваем слово на части принудительно, если оно слишком длинное(требование задачи)
#         while len(word) > width:
#             part = word[:width]
#             lines.append(part)
#             word = word[width:]
#         space_is_needed = 1 if current_length else 0
#         new_length = current_length + len(word) + space_is_needed 
#         if new_length <= width:
#             current_line.append(word)
#             current_length = new_length
#         else:
#             if current_length:
#                 lines.append(' '.join(current_line))
#             current_line = [word]
#             current_length = len(word)
#     if current_line:
#         lines.append(' '.join(current_line))
#     result = [int(subs in line.split()) for line in lines]
#     return result