""" Шерлок Холмс и механическая шкатулка
Сама суть этой загадки и то возбужденное состояние, в котором пребывал клиент Холмса, придавали этому делу необычный характер. Да и, кроме предстоящего расследования, мастерство моего друга, его умение удивительно быстро овладевать ситуацией и на основании тщательных наблюдений и простой логики делать поразительные по своей точности выводы зачаровывали меня. Изучать систему его работы и приемы, с помощью которых он в два счета распутывал сложнейшие загадки, для меня было настоящим удовольствием.
Шерлок Холмс в свободное время упражняется в проверке валидных паролей к его новой механической шкатулке. Пароли строятся из латинских букв и считаются валидными, если в соответствующей строке пароля все буквы встречаются одинаковое количество раз. Кроме того, разрешается удалить одну любую букву, чтобы выполнилось условие равенства частоты всех букв.
Например, строка xyz будет валидна, и строка xyzaa будет валидна (можно удалить одну a), и строка xxyyz будет валидна (можно удалить z). А строка xyzzz, или строка xxyyza или строка xxyyzabc невалидны.
Напишите функцию, проверяющую строку на валидность.
Функция
boolean SherlockValidString(string s)
получает на вход исходную строку длиной 2 или более английских букв, и возвращает true, если строка валидна.
Рефлексируем:
    У нас латинские буквы, нам в первую очередь нужно проверить наличие латинских букв, и мы сразу приведем все к нижнему регистру, чтобы проверка на подсчет букв проводилась корректно. ДОбавим все буквы в словарь, также отдельно получимм все множества букв.
    На первый взгляд нам нужно посчитать одинаковое количество значений, если все значения одинаковы, то тру, если разные, то считаем выполняем проверку:
    1. Находим минимум и максимум повторящихся значений
    2. Считаем сколько раз повторяются значения
Дальше проверяем условия:
    -если одна буква лишняя
        Максимальная количество одинаковых значение на 1 больше минимальной
        Только одна буква имеет максимальную значение
        удаление одной буквы выравнивает все значения
    - Если одна буква редкая
        минимальное значение 1
        толдько одна буква повторяется 1 раз
        удаление одной буквы выравнивает все значения
    - граничные случаи
        разница в значениях буквы больще 1
        буквы имеют очень больгие разные значения
        Удаление одной буквы не решает проблему
        Наличие более двух различных значений букв """

def SherlockValidString(s):
    for i in s:
        if not (('a' <= i <= 'z') or ('A' <= i <= 'Z')):
            return False
    lower_s = s.lower()
    dict_chars = {}
    for i in lower_s:
        dict_chars[i] = dict_chars.get(i, 0) + 1
    chars_list = list(dict_chars.values())
    if all(j == chars_list[0] for j in chars_list):
        return True # все значения одинаковые
    min_chars = min(chars_list)
    max_chars = max(chars_list)
    min_count = sum(1 for j in chars_list if j == min_chars )
    max_count = sum(1 for j in chars_list if j == max_chars)
    if (max_chars - min_chars ==1) and (max_count ==1):
        return True
    if (min_chars == 1) and (min_count == 1):
        return True
    return False

""" # Смешанный регистр - все равно валидно
print(SherlockValidString("AaBbCc"))      # True (A:1, a:1, B:1, b:1, C:1, c:1)
print(SherlockValidString("AAAbbb"))      # True (A:3, b:3)
print(SherlockValidString("XXxYYyZZz"))   # True (X:2, x:1, Y:2, y:1, Z:2, z:1)

print(SherlockValidString("AAAbb"))       # False (A:3, b:2 - разница 1, но A:1 буква, b:1 буква)
print(SherlockValidString("XXxYYyy"))     # False (X:2, x:1, Y:2, y:2)
print(SherlockValidString("abc123"))      # False - содержит цифры
print(SherlockValidString("hello!"))      # False - содержит специальный символ
print(SherlockValidString("test@test"))   # False - содержит @
print(SherlockValidString("space here"))  # False - содержит пробел
print(SherlockValidString("привет"))      # True (все буквы по 1 разу: п,р,и,в,е,т)
print(SherlockValidString("мама"))        # True (м:2, а:2)
print(SherlockValidString("папапа"))      # True (п:3, а:3)
print(SherlockValidString("хорошо"))      # True (х:1,о:2,р:1,ш:1) - ОШИБКА! Проверим:
# "хорошо" = х:1, о:2, р:1, ш:1 → невалидно! """


# Тест 1: Все буквы встречаются одинаковое количество раз
print(SherlockValidString("abc"))        # True (все по 1)
print(SherlockValidString("aabbcc"))     # True (все по 2)
print(SherlockValidString("xxyyzz"))     # True (все по 2)

# Тест 2: Можно удалить одну букву с максимальной частотой
print(SherlockValidString("xyzaa"))      # True (a:2, xyz:1 → удаляем a)
print(SherlockValidString("aabbb"))      # True (b:3, a:2 → удаляем b)

# Тест 3: Можно удалить одну букву с минимальной частотой (1)
print(SherlockValidString("xxyyz"))      # True (z:1, x,y:2 → удаляем z)
print(SherlockValidString("aabbc"))      # True (c:1, a,b:2 → удаляем c)

# Тест 4: Невалидные случаи
print(SherlockValidString("xyzzz"))      # False (z:3, x,y:1 → разница 2)
print(SherlockValidString("xxyyza"))     # False (x,y:2, z,a:1 → две буквы с частотой 1)
print(SherlockValidString("aabbccd"))    # True (a,b,c:2, d:1 → можно удалить d, но тогда все по 2? Проверим!)

print(SherlockValidString("aa"))         # True (все по 2)
print(SherlockValidString("ab"))         # True (все по 1)
print(SherlockValidString("aaa"))        # True (все по 3)
print(SherlockValidString("aab"))        # True (a:2, b:1 → удаляем b)
print(SherlockValidString("aabb"))       # True (все по 2)

