# Рефлексия по решению задач № 7
#   4. Поиск максимального элемента в заданном диапазоне значений.
# Выполнено корректно Цикл и прерывания присутствуют.
#5. Предикативный поиск.
# В моем коде поиск происходит по всей куче, в рекомендациях указано отсечение для оптимизациии,исправляем;
def FindLess(self, less):
    result = []
    stack = [0]
    while stack:
        i = stack.pop()
        if i >= self.size:
            continue
        val = self.HeapArray[i]
        if val >= less:
            continue
        result.append(val)
        left = self._left(i)
        right = self._right(i)
        if left < self.size:
            stack.append(left)
        if right < self.size:
            stack.append(right)
    return result

#6.Объединение текущей кучи с кучей-параметром.
# У меня куча разрушается/ Скопируем же нашу кучу в отдельном методе
def _update(self):
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
def MergeHeap(self, s_heap):
    temp_heap = self.copy_heap(s_heap)
    temp = []
    while temp_heap.size > 0:
        temp.append(temp_heap.GetMax())
    for i in temp:
        if self.size >= self.width:
            self._update()
def copy_heap(self, heap):
    new_copy_heap = Heap()
    new_copy_heap.width = heap.width
    new_copy_heap.size = heap.size
    new_copy_heap.HeapArray = heap.HeapArray.copy()
    return new_copy_heap
# Задание 9*
# 2.* Добавьте метод, который сбалансирует чётное двоичное дерево.
    # я предполагаю, что балансирую чётное двоичное дерево и не получаю нечетное и не двоичное дерево(просто не добавляю проверки)
from task_9 import SimpleTree, SimpleTreeNode
def EvenBinaryTreeBalance(self):
    values = []
    self.CheckOrder(self.Root, values)
    self.Root = self.BuildBalance(values, 0, len(values) - 1, None)


def CheckOrder(self, node, values):
    if len(node.Children) > 0:
        self.CheckOrder(node.Children[0], values)
    values.append(node.NodeValue)
    if len(node.Children) > 1:
        self.CheckOrder(node.Children[1], values)

def BuildBalance(self, values, start, end, parent):
    if start > end:
        return None
    mid = (start + end) // 2
    node = SimpleTreeNode(values[mid], parent)
    left = self.BuildBalance(values,start, mid - 1, node)
    right = self.BuildBalance(values, mid + 1, end, node)
    if left:
        node.Children.append(left)
    if right:
        node.Children.append(right)
    return node
# 3.* Добавьте метод, который для любого заданного подузла текущего дерева определит общее количество чётных поддеревьев.
# у нас уже есть метод подсчета узлов? можно его использовать частично, если узел поддерева будет неизвестен? то по умочанию корень? как параметр)
def CountEven(self, node = None):
    if node is None:
        node = self.Root
    return self.CountEvenRecursive(node)
def CountEvenRecursive(self, node):
    count = 0
    if self.CountTrees(node) % 2 == 0:
        count += 1
    for child in node.Children:
        count += self.CountEvenRecursive(child)
    return count