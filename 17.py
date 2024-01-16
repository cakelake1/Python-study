
#Рефлексия:
# 3.1 : В принципе решение соответствует эталонному, только я еще использовал конвертацияю, чтобы исключить возможные ошибки.

# 3.2 : Мое решение также похоже на эталонное, основная сложность была в определении центрировании в картинке. Также я не использовал определенный шрифт, как в эталонном решении.



# Задания

# 1. Напишите небольшую программу, которая добавляет в словарь 100 случайных пар (предварительно в массив например ключи записываем)
# целый ключ + значение строка,
# затем считывает по ключам все значения и выводит, и затем удаляет все пары.


import random

my_keys = []    
my_dictionary = {}

for i in range(1,101):
    my_keys.append(i)
    
for i in range(1,101):
    key = int(i)
    my_dictionary[key] = 'random' + " " + str(random.randint(1,100))

for key in my_dictionary.keys():
    if my_dictionary.get(key):
        value = my_dictionary[key]
print(format(my_dictionary.items()))
my_dictionary.clear()
print(format(my_dictionary.items()))


# 2. Напишите функцию, которая получает список из 100 значений (сгенерируйте его заранее с числами в диапазоне от 1 до 10) и число N, и выдаёт список из тех значений в этом списке, которые повторяются не менее N раз. Используйте словарь для этого.


import random

a = [random.randint(1, 10) for _ in range(100)]

def one_hundred_values(r_value, N):
    my_dictionary = {}
    list_dict = []
    for i in r_value:
        if my_dictionary.get(i):
            my_dictionary[i] += 1
        else:
            my_dictionary[i] = 1

        if my_dictionary[i] == N:
            list_dict.append(i)
    return list_dict

print(one_hundred_values(a,12))
print(a)
