""" Белые Ходоки
Белые Ходоки снова готовят свою армию мертвецов для очередного штурма Стены. Но они подкрадываются к ней хитростью, стараясь незаметно затесаться среди мирных жителей окрестных деревень.
Для этого Ходоки принимают обличье крестьян, однако становятся различимыми, когда группируются в тройки -- температура вокруг них при этом понижается на 10 градусов.
Вы возглавляете Железный Трон Семи Королевств и посылаете разведчиков выявить всех врагов.
Дайте им подробные инструкции по определению вражеских сил в каждой деревне.
Каждая деревня задаётся ASCII-строкой (возможно, пустой).
В ней могут быть числа (жители, разбредшиется по полям), но только из одного символа (цифры от 0 до 9). То есть подряд несколько цифр не могут следовать.
Если в такой строке между каждой парой чисел (цифр), сумма которых равна 10, насчитываются ровно три Ходока (символ "="), значит, Ходоки успешно выявлены.
Функция
bool white_walkers(string village) 
получает параметром village строку, описывающую одну деревню, и возвращает true, если в ней выявляются все Ходоки.
Например:
"axxb6===4xaf5===eee5" => true
"5==ooooooo=5=5" => false
"abc=7==hdjs=3gg1=======5" => true
"aaS=8" => false
"9===1===9===1===9" => true
 Рефлексируем:
задача у нас небольшая, что я вижу
1. обязательно проверка на пустую строку - фолс
2. Надо перевести строку в список - найти все цифры, сделать проверку на сумму каждый пары, если равно 10, то проверить на количество знаков = В подстроке, .
3. немного смущает ascii 
4. делаем проверку на количество цифр меньше двух
5. избавляемся от цикла через списковое исключение
6. немного меняем логику, если у нас в цикле пара цифр не равна десяти, то пропускаем следующий блок. с подсчетом количества символов равно, е"""
""" def white_walkers(village):
    if not any(char.isdigit() for char in village):
        return False
    list_digits = []
    for i, char in enumerate(village):
        if char.isdigit():
            list_digits.append((i, int(char)))
    if len(list_digits) < 2:
        return False """
def white_walkers(village):
    list_digits = [(i, int(char)) for i, char in enumerate(village) if char.isdigit()]
    if len(list_digits) < 2:
        return False
    correct_pairs = []
    for i in range(len(list_digits) - 1):
        index_1, number_1 = list_digits[i]
        index_2, number_2 = list_digits[i+1]
        if number_1 + number_2 != 10:
            continue
        between = village[index_1 + 1:index_2].count('=')
        correct_pairs.append(between == 3)
    return bool(correct_pairs) and all(correct_pairs)

test_cases = [
    ("axxb6===4xaf5===eee5", True),
    ("5==ooooooo=5=5", False),
    ("abc=7==hdjs=3gg1=======5", True),
    ("aaS=8", False),
    ("9===1===9===1===9", True),
    ("", False),
    ("abc", False),
    ("1=2", False),
    ("5====5", False),
    ("5==5", False)
]

for village, expected in test_cases:
    result = white_walkers(village)
    print(f'"{village}" -> {result} (expected: {expected}) {"✓" if result == expected else "✗"}')
        