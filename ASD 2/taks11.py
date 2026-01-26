class BloomFilter:

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
        self.bit_reg32 |= (1 << index_2)        

    def is_value(self, str1):
        index_1 = self.hash1(str1)
        index_2 = self.hash2(str1)
        bit_1 = (self.bit_reg32 & (1 << index_1)) != 0
        bit_2 = (self.bit_reg32 & (1 << index_2)) != 0
        return bit_1 and bit_2
