def WordSearch(width, s, subs):
    words = s.split(' ')
    lines = []
    current_line = []
    current_length = 0
    # 1. Шум п.4, убираем комментарий
    # Разбиваем на строки с учетом ширины 
    for word in words:
        # 2. Шум п.4, убираем комментарий
        # Разбиваем слово на части, если оно слишком длинное
        while len(word) > width:
            part = word[:width]
            lines.append(part)
            word = word[width:]
        # 3. Шум п.4, убираем комментарий
        # Пытаемся добавить слово в текущую строку
        new_length = current_length + (len(word) + 1 if current_length > 0 else len(word))
        can_fit = new_length <= width
        # 4. Шум п.4, убираем комментарий
        # Добавляем слово в текущую строку или начинаем новую
        current_line = (current_line + [word]) if can_fit else [word]
        current_length = new_length if can_fit else len(word)
        # 5. Шум п.4 и  Недостоверные комментарии п.3, убираем комментарий
        # Если строка заполнена, добавляем в lines
        line_full = current_length == width
        lines.append(' '.join(current_line)) if line_full else None
        current_line = [] if line_full else current_line
        current_length = 0 if line_full else current_length
    # 6. Шум п.4
    # Добавляем последнюю строку, если она не пустая
    lines.append(' '.join(current_line)) if current_line else None
    # 7. Шум п.4 и Недостоверные комментарии п.3
    # Проверяем наличие слова subs в каждой строке (без if)
    result = []
    for line in lines:
        words_in_line = line.split()
        found = subs in words_in_line
        result.append(1 * found)  # True → 1, False → 0
    return result

def odometer(oksana):
    full_speed = 0
    past_time = 0
    for i in range(len(oksana)):
        if i % 2 == 0:  # Если индекс чётный - это скорость
            speed = oksana[i]
            time = oksana[i + 1]
            full_speed = full_speed + speed * (time - past_time)
            past_time = time
    return full_speed