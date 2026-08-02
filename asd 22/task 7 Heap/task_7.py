class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.size = 0
        self.width = 0

    def _left(self, i):
        return 2 * i + 1
    def _right(self, i):
        return 2 *i + 2
    def _parent(self,i):
        return (i-1)//2
    
    def move_down(self,i):
        parent = i
        left = self._left(i)
        right = self._right(i)
        if left < self.size and self.HeapArray[left] > self.HeapArray[parent]:
            parent = left
        if right < self.size and self.HeapArray[right] > self.HeapArray[parent]:
            parent = right
        if parent != i:
            self.HeapArray[i], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[i]
            self.move_down(parent)
    
    def move_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.HeapArray[parent] < self.HeapArray[i]:
                self.HeapArray[parent], self.HeapArray[i] = self.HeapArray[i], self.HeapArray[parent]
                i = parent
            else:
                break
                                                                    
    def MakeHeap(self, a, depth):
        # размер массива выбираем на основе глубины depth 
        capacity = 2 ** ( depth + 1) - 1
        self.width = capacity
        self.HeapArray = [None] * capacity
        count = min(len(a), capacity)
        for i in range(count):
            self.HeapArray[i] = a[i]
        self.size = count
        for i in range(self.size // 2 - 1, -1, -1):
            self.move_down(i)

    def GetMax(self):
        if self.size == 0:
	        return -1 # если куча пуста
        max_value = self.HeapArray[0]
        self.size -= 1
        if self.size > 0:
            self.HeapArray[0] = self.HeapArray[self.size]
            self.HeapArray[self.size] = None
            self.move_down(0)
        else:
            self.HeapArray[0] = None
        return max_value
    
    def Add(self, key):
        if self.size >= self.width:
            return False
        self.HeapArray[self.size] = key
        self.size += 1
        self.move_up(self.size - 1)
        return True