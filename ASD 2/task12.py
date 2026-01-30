# возьмем хэш и код из предудушей задачи, в методе put нажно добавить ключ.
# коллизии разрешим линейным пробированием и введем для них дополнительно счетчик(или шаг). Двигаемся по массиву с этим шагом, максимум это наш размер массива и начинаем массив заново. 
# если ключ есть в кэш - обновляем его
# если ключа нет и есть свободный слот - добавляем в свободный слот
# когда кэш заполнен - вытесняем элемент с наименьшим количеством обращений, для этого тоже заводим счетчик
#   

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 1

    def hash_fun(self, value):
        slot_index = 0
        for char in value:
            slot_index += ord(char)
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

    def put(self, key, value):
        slot_index = self.find(key)
        if slot_index is not None:
            self.values[slot_index] = value
            return slot_index
        slot_index = self.seek_slot(key)
        if slot_index is not None:
            self.slots[slot_index] = key
            self.values[slot_index] = value
            self.hits[slot_index] = 0
            return slot_index
        hits_index = 0
        for i in range(1, self.size):
            if self.hits[i] < self.hits[hits_index]:
                hits_index = i
        self.slots[hits_index] = key
        self.values[hits_index] = value
        self.hits[hits_index] = 0        
        return hits_index

    def find(self, value):
        start_index = self.hash_fun(value)
        slot_index = start_index
        for i in range(self.size):
            if self.slots[slot_index] == value:
                return slot_index
            if self.slots[slot_index] is None:
                return None
            slot_index += self.step
            slot_index = slot_index % self.size
        return None
    
    def get_key(self, key):
        slot_index = self.find(key)
        if slot_index is not None:
            self.hits[slot_index] += 1
            return self.values[slot_index]
        return None
    
    def get_hits(self, key):
        slot_index = self.find(key)
        if slot_index is None:
            return 0
        return self.hits[slot_index]
    
    def cash_key(self, key):
        if self.find(key) is None:
            return False
        return True