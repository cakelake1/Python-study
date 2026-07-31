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
	# создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 
        capacity = 2 ** ( depth + 1) - 1
        self.HeapArray = [None] * capacity
        count = min(len(a), capacity)
        for i in range(count):
            self.HeapArray[i] = a[i]
        self.size = count
        for i in range(self.size // 2 - 1, -1, -1):
             self.move_down(i)
# убрать count?

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
	    return -1 # если куча пуста

    def Add(self, key):
	# добавляем новый элемент key в кучу и перестраиваем её
	    return False # если куча вся заполнена