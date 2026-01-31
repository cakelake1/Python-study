#4. Сделайте тесты, проверяющие, как работают put(), is_key() и get():
#- добавление значения по новому ключу и добавление значения по уже существующему ключу с проверками что записалось, проверка присутствующего и отсутствующего ключей, извлечение значения по существующему и отсутствующему ключу.
# добавил 4 задание в тесты 9-3.py

#5.* Реализуйте словарь с использованием упорядоченного списка по ключу для оптимизации производительности поиска. Оцените временную сложность операций вставки, удаления и поиска в таком словаре.

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = []
        self.values = []
        self.keys = []

    def hash_fun(self, key):
        slot_index = 0
        for char in key:
            slot_index += ord(char)
        return slot_index % self.size 

    def is_key(self, key):
        for i in self.keys:
            if i == key:
                return True
        return False

    def put(self, key, value):
        if key in self.keys:
            key_index = self.keys.index(key)
            value_index = self.slots[key_index][1]
            self.values[value_index] = value
        else:
            self.values.append(value)
            value_index = len(self.values) - 1
            new_pair = [key, value_index]
            pos = 0
            for i,k in enumerate(self.keys):
                if k > key:
                    break
                pos = i + 1
            self.keys.insert(pos, key)
            self.slots.insert(pos, new_pair)

    def get(self, key):
        for i in range(len(self.slots)):
            slot_index = i
            if self.slots[slot_index][0] == key:
                return self.values[self.slots[slot_index][1]]
        return None

#6.* Создайте словарь, в котором ключи представлены битовыми строками фиксированной длины. Реализуйте методы добавления, удаления и поиска элементов, используя битовые операции для ускорения работы.
class BitNativeDictionary:
    def __init__(self, bit_length):
        bit_length=32
        self.bit_length = bit_length
        self.mask = (1 << bit_length) - 1
        self.keys = []
        self.values = []
    
    def add(self, key, value):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = value
                return
        self.keys.append(key & self.mask)
        self.values.append(value)
    
    def remove(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                remove_value = self.values.pop(i)
                self.keys.pop(i)
                return remove_value
        return None
    
    def get(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]
        return None
    
    def find(self, key):
        for i in self.keys:
            if i == key:
                return True
        return False
# Рефлексия по решению задач задания 7
 # 9* мое решение корректное
 # 10* Мое решение правильно
 # 11* Решение соответствует заданию и подсказкам
 # 12 * Решение корректное