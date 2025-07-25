# def WordSearch(width, s, subs):
#     words = s.split()
#     text_lines = []
#     result = []
#     current_text_line = ""

#     for word in words: # Если слово длинное
#         if len(word) > width:
#             if current_text_line: 
#                 text_lines.append(current_text_line)
#                 current_text_line = ""
#             start = 0
#             while start < len(word):
#                 part_word = word[start:start + width]
#                 text_lines.append(part_word)
#                 start = start + width
#         else: # во всех остальных случаях
#             if current_text_line == "":
#                 current_text_line = word
#             else:
#                 if len(current_text_line) + 1 + len(word) <= width:
#                     current_text_line = current_text_line + " " + word
#                 else:
#                     text_lines.append(current_text_line)
#                     current_text_line = word
                    
#     if current_text_line != "":
#         text_lines.append(current_text_line)
#     for line in text_lines:
#         wd = line.split()
#         correct = 0
#         for w in wd:
#             if w == subs:
#                 correct = 1
#                 break
#         result.append(correct)

#     return result


def WordSearch(width, s, subs):
    words = s.split(' ')
    lines = []
    current_line = []
    current_length = 0

    # Разбиваем на строки с учетом ширины
    for word in words:
        # Разбиваем слово на части, если оно слишком длинное
        while len(word) > width:
            part = word[:width]
            lines.append(part)
            word = word[width:]
        
        # Пытаемся добавить слово в текущую строку
        new_length = current_length + (len(word) + 1 if current_length > 0 else len(word))
        can_fit = new_length <= width
        
        # Добавляем слово в текущую строку или начинаем новую
        current_line = (current_line + [word]) if can_fit else [word]
        current_length = new_length if can_fit else len(word)
        
        # Если строка заполнена, добавляем в lines
        line_full = current_length == width
        lines.append(' '.join(current_line)) if line_full else None
        current_line = [] if line_full else current_line
        current_length = 0 if line_full else current_length
    
    # Добавляем последнюю строку, если она не пустая
    lines.append(' '.join(current_line)) if current_line else None

    # Проверяем наличие слова subs в каждой строке (без if)
    result = []
    for line in lines:
        words_in_line = line.split()
        found = subs in words_in_line
        result.append(1 * found)  # True → 1, False → 0
    
    return result

