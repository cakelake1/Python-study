from task_7 import Heap
from task_7_2 import(
    IsCorrectHeap,
    FindLess,
    FindMaxInRange,
    MergeHeap,
    _update

)
Heap.IsCorrectHeap = IsCorrectHeap
Heap.FindLess = FindLess
Heap.FindMaxInRange = FindMaxInRange
Heap.MergeHeap = MergeHeap
Heap._update = _update
# Тесты для основного задания
# сначала проверим граничные значения(пустое, один элемент, одинаковые элементы, отриц. значения и None)
# пустая куча
h = Heap()
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
h.Add(10)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
# один элемент
h = Heap()
h.MakeHeap([42], 2)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
# одинаковые элементы
h = Heap()
h.MakeHeap([5, 5, 5, 5, 5], 2)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
# отрицательные значения
h = Heap()
h.MakeHeap([-5, -1, -3, -2, -4], 2)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
# None
h = Heap()
h.MakeHeap([1, 2, 3], 1)
try:
    h.Add(None)
except TypeError:
    print("TypeError")
# множественное извлечение
h = Heap()
h.MakeHeap([50, 30, 40, 10, 20, 35, 45], 2)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
while h.size > 0:
    print(h.GetMax(), end=' ')
print()
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
# простые числа
h = Heap()
h.MakeHeap([10, 20, 5, 30, 15, 25], 2)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
h.Add(35)
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
print(h.GetMax())
print(h.HeapArray[:h.size])
print(h.IsCorrectHeap())
# FindMaxInRange
h = Heap()
h.MakeHeap([10, 20, 5, 30, 15, 25, 35, 40, 45], 3)
print(h.FindMaxInRange(20, 35))
print(h.FindMaxInRange(50, 60))
print(h.FindMaxInRange(-10, 10))
print(h.FindMaxInRange(25, 25))
# FindLess
h = Heap()
h.MakeHeap([10, 20, 5, 30, 15, 25, 35, 40, 45], 3)
print(h.FindLess(20))
print(h.FindLess(30))
print(h.FindLess(10))
print(h.FindLess(5))
print(h.FindLess(100))
# MergeHeap
h1 = Heap()
h1.MakeHeap([10, 20, 5, 30, 15, 25], 2)
h2 = Heap()
h2.MakeHeap([35, 40, 45, 50], 2)
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
print(h1.IsCorrectHeap())
print(h2.IsCorrectHeap())
h1.MergeHeap(h2)
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
print(h1.IsCorrectHeap())
print(h2.IsCorrectHeap())
while h1.size > 0:
    print(h1.GetMax(), end=' ')
print()
# граничные MergeHeap
#  с пустой кучей
h1 = Heap()
h1.MakeHeap([1, 2, 3], 1)
h2 = Heap()
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
h1.MergeHeap(h2)
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
print(h1.IsCorrectHeap())
# с пустой текущей кучей
h1 = Heap()
h2 = Heap()
h2.MakeHeap([5, 3, 7, 1, 9], 2)
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
h1.MergeHeap(h2)
print(h1.HeapArray[:h1.size])
print(h2.HeapArray[:h2.size])
print(h1.IsCorrectHeap())