class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        slot_index = 0
        for char in key:
            slot_index += ord(char)
        return slot_index % self.size 


    def is_key(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            slot_index = (start_index + i) % self.size
            if self.slots[slot_index] == key:
                return True
            if self.slots[slot_index] is None:
                return False
        return False

    

    def put(self, key, value):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            slot_index = (start_index + i) % self.size
            if self.slots[slot_index] is None:
                self.slots[slot_index] = key
                self.values[slot_index] = value
                return
            if self.slots[slot_index] == key:
                self.values[slot_index] = value
                return
        self.slots[slot_index] = key
        self.values[slot_index] = value


    def get(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            slot_index = (start_index + i) % self.size
            if self.slots[slot_index] == key:
                return self.values[slot_index]
            if self.slots[slot_index] is None:
                return None
        return None