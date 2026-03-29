# 1.def checkPassword(password: str) -> bool:
#     upper, lower, digit = (False, False, False)
#     if len(password) >= 8:
#         for c in password:
#             if c.isupper():
#                 upper = True
#             elif c.islower():
#                 lower = True
#             elif c.isdigit():
#                 digit = True
#     if upper and lower and digit:
#         return True
#     else:
#         return False
    
# def checkPassword(password: str) -> bool:
#     has_upper = False  # Сделал переменную более понятной 1. было upper
#     has_lower = False  # Сделал переменную более понятной 2. было lower
#     has_digit = False  # Сделал переменную более понятной 3. было digit
#     if len(password) < 8:
#         return False  # Вынес сразу проверку длины пароля 4. Проверки не было.
#     for char in password:  # Сделал понятную переменную 5. было с 
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#     return has_upper and has_lower and has_digit  # избавился от if,else 6. Получаем сразу результат

# 2.def Capital(string: str) -> str:
#     marks = (".", "!", "?")
#     new_string = ""
#     first = True
#     for i, c in enumerate(string):
#         if c != " " and first is True:
#             first = False
#             new_string += c.capitalize()
#         elif c in marks:
#             new_string += c
#             first = True
#         elif c == 'i' and (string[i-1]) == ' ' and (string[i+1] == ' ' or string[i+1] in marks):
#             new_string += c.capitalize()
#         else:
#             new_string += c
    
#     return new_string

# def capitalize_sentences(text: str) -> str: # Сделал наименование функции более понятной, а также заменил string на text 7. было Capital
#     sentence_ends = (".", "!", "?") # Сделал переменную более понятной 8. было marks
#     capitalize_next = True # Сделал переменную более понятной 9. было first
#     result = [] # В коде была конкатенация строк, избавился от нее через список 10
#     for i, char in enumerate(text): #  # Сделал переменную более понятной 11. было с
#         if char != " " and capitalize_next: # Убрал "is True" 12
#             result.append(char.upper())  # добавил внесение в список заголовного символа вместо new_string += c.capitalize() 13
#             capitalize_next = False # флаг должен меняться в самом конце логики - перенес его 14 
#         elif char in sentence_ends:
#             result.append(char)  
#             capitalize_next = True  
#         elif char == 'i' and (text[i-1]) == ' ' and (text[i+1] == ' ' or text[i+1] in sentence_ends):
#             result.append('I')
#         else:
#             result.append(char)  
#     return ''.join(result) # заменил вывод целиковой строки из на основе конктанации на вывод из сборки строки из списка 15