#2.* На практике часто применяется сложение/слияние фильтров Блюма: в пиринговых сетях или распределённых базах данных, где на каждом узле ведутся локальные фильтры Блюма для проверки элементов (нередко в архитектуре MapReduce). Важная задача -- слияние этих локальных фильтров, чтобы любой узел мог эффективно проверять наличие элемента без необходимости обращаться к каждому отдельному фильтру.
#Напишите алгоритм слияния нескольких фильтров Блюма (одинакового размера и с одинаковым набором хэш-функций).
#Как изменится вероятность ложного срабатывания для итогового фильтра?
class BloomFilter2:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_reg32 = 0

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
        self.bit_reg32 |= (1 << index_1)
        self.bit_reg32|= (1 << index_2)     

    def is_value(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        bit_1 = (self.bit_reg32 & (1 << index_1)) != 0
        bit_2 = (self.bit_reg32 & (1 << index_2)) != 0
        return bit_1 and bit_2
    
    def merge(self, bloom_filters):
        for bloom_filter in bloom_filters:
            self.bit_reg32 |= bloom_filter.bit_reg32
        return self
# Вероятность ложного срабатывания в итоговом фильтре станет выше

#3.* Реализуйте фильтр Блюма, предусматривающий удаление элементов (стандартный фильтр Блюма удаление не поддерживает). Учтите, что при удалении несуществующих элементов (с ложноположительным результатом проверки их наличия) структура фильтра нарушается и могут удаляться другие входные значения.
class BloomFilter3:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_reg32 = 0
        self.new_items = []

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
        self.bit_reg32 |= (1 << index_1)
        self.bit_reg32|= (1 << index_2)
        self.new_items.append(str1)     

    def is_value(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        bit_1 = (self.bit_reg32 & (1 << index_1)) != 0
        bit_2 = (self.bit_reg32 & (1 << index_2)) != 0
        return bit_1 and bit_2
    
    def remove(self, str1):
        if str1 in self.new_items:
            self.new_items.remove(str1)
            self.bit_reg32_re()
            return True
        return False
    
    def bit_reg32_re(self):
        self.bit_reg32 = 0
        for i in self.new_items:
            index_1 = self.hash1(i)
            index_2 = self.hash2(i)
            self.bit_reg32 |= (1 << index_1)
            self.bit_reg32 |= (1 << index_2)
# Я думаю достаточно сбросить будет битовую маску после удаления элемента и проблем не будет


#4.* Подумайте (и попробуйте реализовать), каким может быть алгоритм, который анализирует конфигурацию фильтра Блюма и пытается, насколько возможно, восстановить исходное множество с учётом всех ограничений и искажений (например, коллизий, ложноположительных срабатываний...).
#Под исходным множеством понимаются исходные данные, оригинальное множество элементов, которые были добавлены в фильтр Блюма через метод Add.

# я предполагаю, что точного решения нет, но можно найти подходящие возможные варианты, что также есть хорошо.также у нас есть ограничения по размеру глубины поиска, так как размер и сложность поиска будет расти по экспоненте. В текущей реализации проверил элементы, которые могли бы быть добавлены и проверку на набор, который создаст фильтр.

class BloomFilter4:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_reg32 = 0
        self.new_items = []

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
        self.bit_reg32 |= (1 << index_1)
        self.bit_reg32|= (1 << index_2)
        self.new_items.append(str1)     

    def is_value(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        bit_1 = (self.bit_reg32 & (1 << index_1)) != 0
        bit_2 = (self.bit_reg32 & (1 << index_2)) != 0
        return bit_1 and bit_2
    
    def analize_check(self, check_list):
        new_bit_reg = 0
        for item in check_list:
            index_1 = self.hash1(item)
            index_2 = self.hash2(item)
            new_bit_reg |= (1 << index_1)
            new_bit_reg |= (1 << index_2)
        return (new_bit_reg & self.bit_reg32) == new_bit_reg
    
    def potential_elements(self, check_list):
        potential_list = []
        for item in check_list:
            index_1 = self.hash1(item)
            index_2 = self.hash2(item)
            new_bit_1 = (self.bit_reg32 & (1 << index_1)) != 0
            new_bit_2 = (self.bit_reg32 & (1 << index_2)) != 0
            if new_bit_1 and new_bit_2:
                potential_list.append(item)
        return potential_list
# также я вижу, что мой код не проверяет коллизии с одинаковыми битами и ложноположительные срабатывания не различает.

# Рефлексия по решению задач задания 9
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

# ничего нового я не добавлял, проверил еще код на корректность.
