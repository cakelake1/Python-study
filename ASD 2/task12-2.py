# Рефлексия по предыдущим задачам
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
        return [(i,) for i in one_list]
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
            result.append((i,) + j)
    return result
class PowerSet:
    def __init__(self) -> None:
        self.storage = {}
        self._size = 0

    def put(self, value: Any) -> None:
        if value not in self.storage:
            self.storage[value] = True
            self._size +=1
