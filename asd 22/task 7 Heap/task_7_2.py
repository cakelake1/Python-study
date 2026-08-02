#Рефлексия по 5 заданию:
#2. Эффективность поиска узла в дереве, представленном в виде массива.
#       ответил достаточно корректно, можно было добавить про кэш и память, получилось бы еще и грамотно.

# 3. Удаление узла из двоичного дерева, заданного в виде массива.
# У меня возникли сложности с данной задачей, я поставил себе время на ее решение дополнительно час в день. 

# 4. Сортировка двоичного дерева за O(1).
#       вот тут я немного не в ту сторону стал размышлять. Честно не увидел, что дерево уже отсортировано.

# Задания 7 Пирамиды
# 3. Добавьте метод проверки, что массив действительно содержит корректную кучу.
def IsCorrectHeap(self):
        for i in range(self.size):
            left = self._left(i)
            right = self._right(i)
            if left < self.size and self.HeapArray[left] > self.HeapArray[i]:
                return False
            if right < self.size and self.HeapArray[right] > self.HeapArray[i]:
                return False
        return True

# 4.* Добавьте метод поиска максимального элемента в заданном диапазоне значений.
def FindMaxInRange(self, first, last):
        if self.size == 0:
            return -1
        result = -1
        stack = [0]
        while stack:
            i = stack.pop()
            if i >= self.size:
                continue
            val = self.HeapArray[i]
            if first <= val <= last and val > result:
                result = val
            if val < first:
                continue
            left = self._left(i)
            right = self._right(i)
            if left < self.size:
                stack.append(left)
            if right < self.size:
                stack.append(right)
        return result

# 5 * Подумайте над эффективным алгоритмом поиска в куче элемента по заданному условию 
def FindLess(self, less):
        result = []
        stack = [0]
        while stack:
            i = stack.pop()
            if i >= self.size:
                continue
            val = self.HeapArray[i]
            if val < less:
                result.append(val)
            left = self._left(i)
            right = self._right(i)
            if left < self.size:
                stack.append(left)
            if right < self.size:
                stack.append(right)
        return result
# 6.Добавьте метод объединения текущей кучи с кучей-параметром.
def MergeHeap(self, s_heap):
        temp = []
        while s_heap.size > 0:
            temp.append(s_heap.GetMax())
        for i in temp:
            if self.size >= self.width:
                self._update()
            self.Add(i)
            
def _update(self): # по сути это внутренняя реализация, а не часть интерфейса
    if self.width == 0:
        self.width = 1
        self.HeapArray = [None]
        return
    new_width = self.width * 2 + 1
    new_array = [None] * new_width
    for i in range(self.size):
        new_array[i] = self.HeapArray[i]
    self.HeapArray = new_array
    self.width = new_width