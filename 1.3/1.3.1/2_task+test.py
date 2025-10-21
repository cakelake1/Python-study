""" def digital_rain(col):
    first = 0
    zero = 0
    m = len(col)
    prefix = [0] * (m+1)
    for i in range(m):
        if col[i] == '1':
            prefix[i+1] = prefix[i] + 1
        else:
            prefix[i+1] = prefix[i] - 1
    dictionary = {}
    max_length = 0
    start_pos = -1
    end_pos = -1
    for i in range(m + 1):
        current = prefix[i]
        if current in dictionary:
            start_index = dictionary[current]
            new_length = i - start_index
            if current > max_length:
                max_length = current
                start_pos = start_index
                end_pos = i
            elif current == max_length:
                if start_index > start_pos:
                    start_pos = start_index
                    end_pos = i
        else:
            dictionary[current] = i
    if max_length == 0:
        return ''
    result = ''
    for i in range(start_pos, end_pos):
    for i in col:
        if i =="1":
            first +=1
        elif i == '0':
            zero +=1
    return first,zero """
""" 
 """
        
def digital_rain_v2(col):
    zero = 0
    one = 0
    res = ''
    start = 0
    end = 0
    max_length = 0
    diff_index = {0:-1}
    for i,n in enumerate(col):
        if n =='0':
            zero += 1
        else:
            one += 1
        diff = one - zero
        if diff in  diff_index:
            start_index = diff_index[diff] + 1
            current_lenght = i - start_index + 1
            if current_lenght > max_length:
                max_length = current_lenght
                start = start_index
                end = i + 1
            elif current_lenght == max_length and current_lenght > 0:
                if start_index > start:
                    start = start_index
                    end = i + 1
        else:
            diff_index[diff] = i
    if max_length == 0 :
        return ''
    for i in range(start,end):
        res += col[i]
    return res
print(digital_rain_v2('1010101'))
test_cases = [
    "1111000",      # Ожидается: "111000"
    "11101000",     # Ожидается: "11101000" 
    "011111110",    # Ожидается: "10"
    "11111111",     # Ожидается: ""
    "1100",         # Ожидается: "1100"
]

for test in test_cases:
    result = digital_rain_v2(test)
    print(f"'{test}' => '{result}'")
# Расширенные тестовые примеры
test_cases = [
    # Базовые случаи из условия
    ("1111000", "111000"),
    ("11101000", "11101000"),
    ("011111110", "10"),
    ("11111111", ""),
    
    # Краевые случаи
    ("", ""),
    ("0", ""),
    ("1", ""),
    ("01", "01"),
    ("10", "10"),
    
    # Простые случаи
    ("1100", "1100"),
    ("0011", "0011"),
    ("1010", "1010"),
    ("0101", "0101"),
    
    # Случаи с несколькими валидными подстроками (выбираем правую)
    ("000111000111", "000111"),  # Две "000111", берем левую? Нет, проверяем!
    ("000111000111", "000111"),  # На самом деле: "000111" и "111000" - нужно уточнить
    
    # Сложные случаи
    ("110011001100", "11001100"),  # Или "10011001"?
    ("10101010", "10101010"),
    ("111000111000", "111000111000"),
    
    # Случаи где максимальная подстрока не с начала
    ("111000111000", "111000111000"),
    ("000111000", "000111"),
    
    # Случаи с вложенными подстроками
    ("111000111000111000", "111000111000111000"),
    ("1010101010", "1010101010"),
    
    # Специальные случаи для проверки выбора правой подстроки
    ("00110011", "00110011"),  # Две "0011", берем правую
    ("11001100", "11001100"),  # Две "1100", берем правую
    
    # Еще сложные случаи
    ("111000111000111", "111000111000"),
    ("000111000111000", "000111000111"),
    
    # Минимальные случаи
    ("00", ""),
    ("11", ""),
    ("0000", ""),
    ("1111", ""),
]

print("Тестирование алгоритма:")
print("=" * 50)

all_passed = True
for i, (test_input, expected) in enumerate(test_cases, 1):
    result = digital_rain_v2(test_input)
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    
    print(f"Тест {i:2d}: {status} '{test_input}' -> '{result}' (ожидалось: '{expected}')")

print("=" * 50)
print(f"Все тесты пройдены: {'ДА' if all_passed else 'НЕТ'}")

# Дополнительные тесты для отладки
print("\nДетальные тесты для отладки:")
debug_cases = [
    "000111000111",  # Интересный случай
    "00110011",      # Проверка выбора правой подстроки
    "11001100",      # Проверка выбора правой подстроки
]

for test in debug_cases:
    result = digital_rain_v2(test)
    print(f"'{test}' -> '{result}'")
    
    # Детальная отладка
    zero = 0
    one = 0
    diff_index = {0: -1}
    print("  Детали:")
    for i, n in enumerate(test):
        if n == '0': zero += 1
        else: one += 1
        diff = one - zero
        if diff in diff_index:
            start_idx = diff_index[diff] + 1
            length = i - start_idx + 1
            substr = test[start_idx:i+1]
            print(f"    i={i}, diff={diff}, подстрока: '{substr}' (длина={length})")
        diff_index[diff] = i
    print()