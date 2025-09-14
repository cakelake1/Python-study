""" Тренируем сборную России по футболу
Вы, тренер сборной России по футболу, ухитрились вывести её в финал чемпионата мира. Ваша задача -- определить, можно ли улучшить расстановку игроков на поле перед решающей встречей, или всё бесполезно и придётся использовать текущий вариант. Но у вас в распоряжении остались только два тренерских приёма, времени уже нету, и использовать можно только один из них.
На входе -- массив произвольных целых чисел (значения не повторяются).
Ваша задача -- попробовать упорядочить его по возрастанию с помощью однократного применения одного из двух приёмов:
1. Поменять местами два произвольных элемента массива.
2. Изменить на обратный порядок произвольной последовательной цепочки элементов в массиве.
Например, на входе
1) 1 3 2
Упорядочиваем правилом 1, меняем местами 3 и 2:
1 2 3
2) 3 2 1
Упорядочиваем правилом 2, меняем порядок с первого элемента до последнего:
1 2 3
3) 1 7 5 3 9
Упорядочиваем правилом 1, меняем местами 7 и 3:
1 3 5 7 9
4) 9 5 3 7 1
Нельзя упорядочить.
5) 1 4 3 2 5
Упорядочиваем правилом 2, меняем порядок с второго элемента до четвёртого:
1 2 3 4 5
Функция
boolean Football(int F[], int N)
получает на вход массив F из N (N >= 1) целых неповторяющихся чисел и возвращает true, если массив можно упорядочить однократным применением одного из двух правил.
Сортировку использовать запрещено.
как постить решение
Рефлексируем:
1. В перву. очередб нужно сделать проверку на количество чисел которые идут по порядку им меньше предыдущего, и записываем коэфициэнт если таких числе нет, значит у нас все числа отсортированы по порядку, если таких чисел = 2 , то мы используем первый прием.
2. прием мне пока не понятно в какой момент применять, возможно это тот же самый первый метод, но в обратном направлении, либо если у нас подряд несколько чисел
3. Сделаем простую проверку на сортировку, запишем ее в отдельную функцию
4. Сделаем функцию проверки на замену двух элементов
5. Напишем еще одну функцию на проверку разворота
 """
def Football(F,N):
    return check_swap(F) or check_reverse(F)

def check_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True
def check_swap(array):
    if check_sorted(array):
        return True
    number_1 = -1
    number_2 = -1
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            number_1 = i
            break
    if number_1 == -1:
        return True
    for i in range(number_1 + 1,len(array)):
        if array[i] < array[number_1]:
            number_2 = i
    if number_2 != -1:
        temp_array = array.copy()
        temp_array[number_1], temp_array[number_2] = temp_array[number_2], temp_array[number_1]
        return check_sorted(temp_array)
    return False
def check_reverse(array):
    if check_sorted(array):
        return True
    start_number = -1
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            start_number = i
            break
    if start_number == -1:
        return True
    end_number = start_number
    for i in range(start_number + 1, len(array)):
        if i < len(array) - 1 and array[i] < array[i+1]:
            end_number = i
            break
        end_number = i
    temp_array2 = array.copy()
    temp_array2[start_number:end_number+1] = temp_array2[start_number:end_number+1][::-1]
    return check_sorted(temp_array2)
print("Дополнительные тесты:")
print(Football([1], 1))                     # True - один элемент
print(Football([2, 1], 2))                  # True - обмен двух элементов
print(Football([1, 3, 2], 3))               # True - обмен 3 и 2
print(Football([2, 1, 3, 4], 4))            # True - обмен 2 и 1
print(Football([1, 2, 4, 3, 5], 5))         # True - обмен 4 и 3
print(Football([1, 5, 4, 3, 2, 6], 6))      # True - разворот [5,4,3,2]
print(Football([6, 5, 4, 3, 2, 1], 6))      # True - разворот всего массива
print(Football([1, 2, 5, 4, 3, 6], 6))      # True - разворот [5,4,3]
print(Football([1, 2, 3, 6, 5, 4], 6))      # True - разворот [6,5,4]

# Случаи, которые нельзя упорядочить
print(Football([3, 1, 2], 3))               # False 
print(Football([2, 3, 1], 3))               # False
print(Football([4, 2, 3, 1], 4))            # False
print(Football([1, 5, 2, 4, 3], 5))         # False
print(Football([3, 2, 4, 1, 5], 5))         # False

# Граничные случаи
print(Football([1, 2, 3, 2, 1], 5))         # False - повторяющиеся (но по условию значения не повторяются)
print(Football([5, 4, 3, 2, 1, 6], 6))      # True - разворот первых 5 элементов
print(Football([1, 7, 5, 3, 9], 5))         # True - обмен 7 и 3 (из примера)
print(Football([9, 5, 3, 7, 1], 5))         # False (из примера)

# Большие массивы
print(Football([1, 2, 3, 10, 5, 6, 7, 8, 9, 4], 10))  # True - обмен 10 и 4
print(Football([1, 2, 3, 10, 9, 8, 7, 6, 5, 4], 10))  # True - разворот [10,9,8,7,6,5,4]
