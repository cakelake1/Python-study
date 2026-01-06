class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

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