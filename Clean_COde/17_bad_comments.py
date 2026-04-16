# def WordSearch(width, s, subs):
#     words = s.split(' ')
#     lines = []
#     current_line = []
#     current_length = 0
#     # 1. Шум п.4, убираем комментарий
#     # Разбиваем на строки с учетом ширины 
#     for word in words:
#         # 2. Шум п.4, убираем комментарий
#         # Разбиваем слово на части, если оно слишком длинное
#         while len(word) > width:
#             part = word[:width]
#             lines.append(part)
#             word = word[width:]
#         # 3. Шум п.4, убираем комментарий
#         # Пытаемся добавить слово в текущую строку
#         new_length = current_length + (len(word) + 1 if current_length > 0 else len(word))
#         can_fit = new_length <= width
#         # 4. Шум п.4, убираем комментарий
#         # Добавляем слово в текущую строку или начинаем новую
#         current_line = (current_line + [word]) if can_fit else [word]
#         current_length = new_length if can_fit else len(word)
#         # 5. Шум п.4 и  Недостоверные комментарии п.3, убираем комментарий
#         # Если строка заполнена, добавляем в lines
#         line_full = current_length == width
#         lines.append(' '.join(current_line)) if line_full else None
#         current_line = [] if line_full else current_line
#         current_length = 0 if line_full else current_length
#     # 6. Шум п.4
#     # Добавляем последнюю строку, если она не пустая
#     lines.append(' '.join(current_line)) if current_line else None
#     # 7. Шум п.4 и Недостоверные комментарии п.3 - удаляем комментарий
#     # Проверяем наличие слова subs в каждой строке (без if)
#     result = []
#     for line in lines:
#         words_in_line = line.split()
#         found = subs in words_in_line
#         result.append(1 * found)  # 8.  True - 1, False - 0 Избыточный комментарий п.7 - удаляем
#     return result

# def PatternUnlock(N, hits):
#     dictionary_coordinate = {
#             6: (0,0), 1: (0,1), 9: (0,2),
#             5: (1,0), 2: (1,1), 8: (1,2),
#             4: (2,0), 3: (2,1), 7: (2,2)
#             }
#     coordinates = []
#     for numbers in hits:
#         coordinates.append(dictionary_coordinate[numbers])
#     not_formatted_result =  0.0
#     for i in range(1,N):
#         c0 = coordinates[i-1]
#         c1 = coordinates[i]
#         dx = c0[0] - c1[0]
#         dy = c0[1] - c1[1]
#         path_on_phone = (dx*dx + dy*dy) ** 0.5 #9. Шум п.4 и п.2 бормотание, просто убираем комментарий -   Евклидово расстояние, в таких задачах использовать только его, меняется только расчет длины.
#         not_formatted_result = not_formatted_result + path_on_phone
#     not_formatted_result = round(not_formatted_result,5) #10. Избыточный комментарий п.7, просто удаляем комментарий-окрушляем до 5 знаков
#     s = format(not_formatted_result, '.5f') # 11. Избыточный комментарий п.7,форматируем в строку с 5 знаками - удаляем
#     result = s.replace('.', '').replace('0', '') #12. Недостоверныый комментарий п.3(сначала точка, потом ноль) - удалякм, обязательно сначала 0 убираем, потом только точку, разделять также нельзя
#     return result