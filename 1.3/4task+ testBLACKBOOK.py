#Бортовой софт Перехватчика генерирует телеметрический массив -- неповторяющиеся целые числа в диапазоне от 0 до 255, общим количеством N (длина массива), которое всегда нечётно. 
# В общем случае эти значения в массиве будут случайно перемешаны.
#1 <= N <= 127

#Для достижения максимального количества оборотов двигателю требуется корректный стартовый импульс. Он представляет собой массив, центральным элементом которого будет 
# максимальное его значение, все левые элементы упорядочены по возрастанию (причём первый левый элемент -- самый минимальный в массиве), а все правые -- по убыванию.

#Например, на входе массив из семи элементов, N=7:


#1 2 3 4 5 6 7 
#Эти элементы могут быть случайно перемешаны.

#На выходе должно быть:


#1 2 3 7 6 5 4
#Функция

#int [] MadMax(int N, int [] Tele)
#получает на вход массив Tele из N чисел, и возвращает результирующий массив-импульс.
import random
def MadMax(N, Tele):
    max_value = []
    left_part = []
    right_part = []
    N = max(1, min(N, 127))
    if N % 2 == 0:
        N = min(N+1, 127)
    randoms = random.sample(range(256), N )
    Tele.extend(randoms)
    print(Tele)
    max_value = max(Tele)
    max_index = Tele.index(max_value)
    Tele.pop(max_index)
    mid_index = len(Tele) // 2
    Tele.insert(mid_index, max_value)
    print(max_value)
    left_part = sorted(Tele[:mid_index])
    right_part = sorted(Tele[mid_index:], reverse=True)
    print(left_part)
    print(right_part)
    result = left_part + [max_value] + right_part   
    return result
arr = []
MadMax(9, arr)
#print(max_value)
print(arr)