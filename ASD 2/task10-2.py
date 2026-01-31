# main_quest
from __future__ import annotations
from typing import Any
import time


class PowerSet:

    def __init__(self) -> None:
        self.storage = {}
        self._size = 0

    def size(self) -> int:
        # количество элементов в множестве
        return self._size

    def put(self, value: Any) -> None:
        if value not in self.storage:
            self.storage[value] = True
            self._size +=1

    def get(self, value: Any) -> bool:
        if value in self.storage:
            return True
        return False

    def remove(self, value: Any) -> bool:
        if value in self.storage:
            self.storage.pop(value)
            self._size -= 1
            return True
        return False

    def intersection(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for i in self.storage:
            if set2.get(i):
                result.put(i)
        return result

    def union(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for i in self.storage:
            result.put(i)
        for j in set2.storage:
            result.put(j)
        return result

    def difference(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for i in self.storage:
            if not set2.get(i):
                result.put(i)
        return result

    def issubset(self, set2: PowerSet) -> bool:
        for i in set2.storage:
            if not self.get(i):
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != set2.size():
            return False
        for i in self.storage:
            if not set2.get(i):
                return False
        return True
#4.* Добавьте метод, реализующий декартово произведение множеств.
    def cartesian(self, set2:PowerSet) -> PowerSet:
        result = PowerSet()
        for i in self.storage:
            for j in set2.storage:
                result.put((i,j))
        return result

#5.* Напишите функцию, которая находит пересечение любых трёх и более множеств (принимает количество множеств >= 3 в качестве списка).
    def multiple_sets(sets: list[PowerSet]) -> PowerSet:
        if len(sets) < 3:
            raise ValueError('требуется три множества')
        min_size_set = sets[0]
        min_size = min_size_set.size()
        for i in sets[1:]:
            cur_size = i.size()
            if cur_size < min_size:
                min_size = cur_size
                min_size_set = i
        result = PowerSet()
        for i in min_size_set.storage:
            cross_all = True
            for j in sets:
                if j is not min_size_set and not j.get(i):
                    cross_all = False
                    break
            if cross_all:
                result.put(i)
        return result


#6.* Реализуйте мульти-множество (Bag), в котором каждый элемент может присутствовать несколько раз. Добавьте методы добавления элементов, удаления одного экземпляра элемента и получения списка всех элементов с их частотами (сколько раз встречаются).
class Bag:
    def __init__(self):
        self.storage = {}

    def put(self, value):
        if value in self.storage:
            self.storage[value] += 1
        else:
            self.storage[value] = 1

    def remove(self, value):
        if value not in self.storage:
            return False
        self.storage[value] -= 1
        if self.storage[value] == 0:
            self.storage.pop(value)
        return True

    def get_elements(self):
        result = []
        for value, count in self.storage.items():
            result.append((value, count))
        return result
    
    def count(self, value):
        return self.storage.get(value,0)
    
    def total_values(self):
        total = 0
        for count in self.storage.values():
            total += count
        return total
    
    def unique_items(self):
        return len(self.storage)
    
#Рефлексия по решению задач задания 8.
# 3* Решение у меня правильно. В подсказке рекомендуется расширение на 80%, я сделал на 75%
# 4* У меня правильно решение, но сначала я сделал статическую соль, но потом изменил на динамическую с борльшими случайными значениями.