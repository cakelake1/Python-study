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

#5.* Напишите функцию, которая находит пересечение любых трёх и более множеств (принимает количество множеств >= 3 в качестве списка).

#6.* Реализуйте мульти-множество (Bag), в котором каждый элемент может присутствовать несколько раз. Добавьте методы добавления элементов, удаления одного экземпляра элемента и получения списка всех элементов с их частотами (сколько раз встречаются).

#сделаю 19 -22.02