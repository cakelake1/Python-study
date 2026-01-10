# 3.* Реализуйте динамическую хэш-таблицу, которая автоматически удваивает свой размер, если уровень заполненности превышает заданный порог (например, 75%).
#Реализация должна корректно перераспределять все элементы в новую, более крупную хэш-таблицу с минимальными затратами по времени."""
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.count = 0
        self.overload = 0.75

    def hash_fun(self, value):
        slot_index = 0
        for char in value:
            slot_index += ord(char)
        return slot_index % self.size 
        
    def seek_slot(self, value):
        slot_index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[slot_index] is None:
                return slot_index
            slot_index += self.step
            slot_index = slot_index % self.size
        return None

    def put(self, value):
        if self.count / self.size >= self.overload:
            self.resize()
        slot_index = self.seek_slot(value)
        if slot_index is not None:
            self.slots[slot_index] = value
            self.count += 1
            return slot_index
        return None

    def find(self, value):
        slot_index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[slot_index] == value:
                return slot_index
            slot_index += self.step
            slot_index = slot_index % self.size
        return None
    
    def resize(self):
        items = []
        for item in self.slots:
            if item is not None:
                items.append(item)
        self.size = self.size * 2
        self.slots = [None] * self.size
        self.count = 0
        for item in items:
            slot_index = self.seek_slot(item)
            if slot_index is not None:
                self.slots[slot_index] = item
                self.count += 1         

 #4.* Реализуйте хэш-таблицу, которая использует несколько хэш-функций для каждой операции вставки, чтобы уменьшить вероятность коллизий. Проанализируйте, как это влияет на производительность и вероятность коллизий
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.count = 0
        self.overload = 0.75

    def hash_fun_1(self, value): # сумма кодов символов
        slot_index = 0
        for char in value:
            slot_index += ord(char)
        return slot_index % self.size 
    
    def hash_fun_2(self, value): # полиномиальная
        slot_index = 0
        for i, char in enumerate(value):
            slot_index += ord(char) * (31 ** i)
        return slot_index % self.size

    def hash_fun_3(self, value): # циклический сдвиг + XOR(исключаюшее или, ^)
        slot_index = 0
        for char in value:
            slot_index = (slot_index << 5) | (slot_index >> 27)
            slot_index ^= ord(char)
        return abs(slot_index) % self.size


    def put(self, value):
        if self.count / self.size >= self.overload:
            self.resize()
        slot_index = self.hash_fun_1(value)
        if self.slots[slot_index] is None:
            self.slots[slot_index] = value
            self.count += 1
            return slot_index
        slot_index = self.hash_fun_2(value)
        if  self.slots[slot_index] is None:
            self.slots[slot_index] = value
            self.count += 1
            return slot_index
        slot_index = self.hash_fun_3(value)
        if  self.slots[slot_index] is None:
            self.slots[slot_index] = value
            self.count += 1
            return slot_index
        start_index = self.hash_fun_1(value)
        for i in range(self.size):
            cur_index = (start_index + i * self.step) % self.size
            if self.slots[cur_index] is None:
                self.slots[cur_index] = value
                self.count += 1
                return cur_index
        return None

    def find(self, value):
        slot_index = self.hash_fun_1(value)
        if self.slots[slot_index] == value:
            return slot_index
        slot_index = self.hash_fun_2(value)
        if self.slots[slot_index] == value:
            return slot_index
        slot_index = self.hash_fun_3(value)
        if self.slots[slot_index] == value:
            return slot_index
        start_index = self.hash_fun_1(value)
        for i in range(self.size):
            cur_index = (start_index + i * self.step) % self.size
            if self.slots[cur_index] == value:
                return cur_index
            if self.slots[cur_index] is None:
                break
        return None
    
    def resize(self):
        items = []
        for item in self.slots:
            if item is not None:
                items.append(item)
        self.size = self.size * 2
        self.slots = [None] * self.size
        self.count = 0
        for item in items:
            self.put(item)  
# Проанализировав увеличение хэш таблиц, чтобы уменьшить вероятность коллизий я пришел к следующим выводам:
# во первых не случайно нам дали задание на увеличение размера наблица при заполнении на коэфициэнт 0.75, при заполнении талицы на больше чем на 75% вероятность коллизии становится НАМНОГО выше.
# далее если у нас таблица не большая, то хватает 1-2 хэщ функции, если таблица большая  лучше делать 2-3. большее количество хэш функций снижает количество коллизий незначительно, но значительно увеличивает производительность.
# Самой лучщей рекомендацией для себя: начинать с 1 хэш функции и тестировать на своих данных, но можно заметить, что 2 хэш функции будут чаще всего оптимальным вариантом.

#5.* Организуйте ddos-атаку на вашу исходную хэш-таблицу -- с помощью специально сгенерированных ключей, вызывающих большое число коллизий. Затем модифицируйте хэш-таблицу для защиты от таких атак (например, посолите).
import random
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.salt = random.randint(1, 1000000) # соль

    def hash_fun(self, value):
        slot_index = 0
        for char in value:
            slot_index += ord(char) + self.salt # добавил соль
        return slot_index % self.size 
        
    def seek_slot(self, value):
        start_index = self.hash_fun(value)
        slot_index = start_index
        for i in range(self.size):
            if self.slots[slot_index] is None:
                return slot_index
            slot_index += self.step
            slot_index = slot_index % self.size
        return None

    def put(self, value):
        slot_index = self.seek_slot(value)
        if slot_index is not None:
            self.slots[slot_index] = value
            return slot_index
        return None

    def find(self, value):
        start_index = self.hash_fun(value)
        slot_index = start_index
        for i in range(self.size):
            if self.slots[slot_index] == value:
                return slot_index
            slot_index += self.step
            slot_index = slot_index % self.size
        return None
# доделано 10.01.2026