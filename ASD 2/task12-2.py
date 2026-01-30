# Рефлексия по предыдущим задачам:

# task10 4* Метод, реализующий декартово произведение множеств.
    # Если кратко, то я сделал декартово произведение для двух множеств, у нас же задача сделать просто для множеств(а их может быть больше двух) 
    # сделаем для всех множеств и с рекурсией:
from __future__ import annotations
from typing import Any

def cartesian(*many_sets):
    if len(many_sets)== 0:
        return []
    if len(many_sets) == 1:
        one_set = many_sets[0]
        one_list = list(one_set.storage)
        return [(i, ) for i in one_list]
    lists = [list(s.storage) for s in many_sets]
    return recursive_cartesian(lists)

def recursive_cartesian(lists):
    if len(lists) == 0:
        return []
    if len(lists) == 1:
        return [(i,) for i in lists[0]]
    result = []
    for i in lists[0]:
        for j in recursive_cartesian(lists[1:]):
            result.append((i, ) + j)
    return result
class PowerSet:
    def __init__(self) -> None:
        self.storage = {}
        self._size = 0

    def put(self, value: Any) -> None:
        if value not in self.storage:
            self.storage[value] = True
            self._size +=1

# 6* task10-2 *6 Реализуйте мульти-множество (Bag), в котором каждый элемент может присутствовать несколько раз.
    # В принципе выполнено верно, на всякий случай еще раз проверил и прошелся по всем механизмам.
    #1. Хранение частот: есть
    #2. Механизм добавления: есть
    #3. Механизм удаления: есть
    #4. Дополнительные операции: есть

# task 11-2 *2 Алгоритм слияния нескольких фильтров Блюма.
    # выполнил корректно, единственное, что понимал, что повышается вероятность ложного срабатывания, но не написал почему, а именно, то что биты объединенного филтра срабатывают чаще.

# task 11-2 *3 Фильтр Блюма, предусматривающий удаление элементов
    # Если рассматривать саму идею блюм фильтра, то он не должен хранить элементы, а я пересчитывал юитовый регистр при каждом удалении в сохраненных добавленных элементах, что не эффективно(требует больше помяти) к тому еще
    # тогда нужен блюм фильтр без хранения и со счетчиками
    # улаляем проверку на биты, удаляем список, добаляем счетчики.
class BloomFilter3:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.counters = [0] * f_len

    def hash1(self, str1):
        start_value = 0
        for c in str1:
            code = ord(c)
            start_value = (start_value * 17 + code) % self.filter_len
        return start_value

    def hash2(self, str1):
        start_value = 0
        for c in str1:
            code = ord(c)
            start_value = (start_value * 223 + code) % self.filter_len
        return start_value
    
    def add(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        self.counters[index_1] += 1
        self.counters[index_2] += 1
        return True     

    def is_value(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        bit_1 = self.counters[index_1] > 0
        bit_2 = self.counters[index_2] > 0
        return bit_1 and bit_2
    
    def remove(self, str1):
        if not self.is_value(str1):
            return False
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        if self.counters[index_1] > 0:
            self.counters[index_1] -= 1
        if self.counters[index_2] > 0:
            self.counters[index_2] -= 1
        return True    

# task 11-2 *4  Алгоритм, который анализирует конфигурацию фильтра Блюма и пытается, насколько возможно, восстановить исходное множество с учётом всех ограничений и искажений (например, коллизий, ложноположительных срабатываний...).
    # Что я смог проверить:
        # Все биты набора установлены в фильтре
        # оба хэша установлены в фильтре
    # Я считаю дальше корректно не реализовать сам код, а именно разобраться:
    # Что еще можно проверить:
        # Предметную область входных данных: emails, ip_addres, phone_number, ссылки.
        # Тематические словари : технические термины, имена рус и англ, слова на англ.
        