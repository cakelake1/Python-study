#5.1 методы size, enqueue, dequeue
class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def size(self):
        return len(self.stack)
#5.2 Сложность enqueue О(1)- добавляем только элемент в коцен списка(простая операция), dequeue О(n), так как мы сдвигаем весь список.

#5.3 * Напишите функцию, которая "вращает" очередь по кругу на N элементов.
# Самое важное в этой задаче даже не отправить по кругу список, а сделать "нормализацию", так получим и нужное вращение и уменьшим количество итераций, а также нам достаточно будет поменять немного нормализацию, чтобы сделать отрицательное вращение.
def spin_circle(self, N):
        if self.size() == 0:
            return
        N = N % self.size() # нормализация
        for _ in range(N):
            item = self.dequeue()
            self.enqueue(item)

#5.4 Реализуйте очередь с помощью двух стеков.
# нужно добавить второй стек, внести в соответствие со стеками изменения и немного поменять логику enqueue
class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop(0))
        self.stack_in.append(item)
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop(0))

    def dequeue(self):
        if len(self.stack_in) == 0:
            return None
        return self.stack_in.pop(0) 

    def size(self):
        return len(self.stack_in)
    
    def spin_circle(self, N):
        if self.size() == 0:
            return
        N = N % self.size()
        for _ in range(N):
            item = self.dequeue()
            self.enqueue(item)

# 5.5 Добавьте функцию, которая обращает все элементы в очереди в обратном порядке.
# Все элементы хранятся в первой стеке(in), поэтому достаточно его развернуть(reverse)
def reverse(self):
        self.stack_in.reverse()

# 5.6 Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера. Добавьте ей метод проверки, полна ли она (при этом добавление новых элементов невозможно).Обеспечьте эффективное управление указателями начала и конца очереди в рамках массива, чтобы избежать неоправданных сдвигов данных.
# что нужно сделать: 
# 1.задать максимальный размер очереди(capacity)
# 2.Создать массив фиксированного размера
# 3. добавить указатель на начало ин а конец очереди
# 4. Доьавить счётчик элементов очереди
# 5. добавить метод проверки на полноту, если полна, то вывести ошибку.
class CircleQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.lenght = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Очередь полна")
        self.queue[self.rear] = item
        if self.rear == self.capacity - 1:
            self.rear = 0  
        else:
            self.rear += 1  
        self.lenght += 1

    def dequeue(self):
        if self.lenght == 0:
            return None
        item = self.queue[self.front]
        if self.front == self.capacity - 1:
            self.front = 0  
        else:
            self.front += 1  
        self.lenght -= 1
        return item
    
    def is_full(self):
        return self.lenght == self.capacity
    
    def size(self):
        return self.lenght

# Рефлексия из Задания 3(задача 5*)
# Динамический массив на основе банковского метода.
# При добавлении элемента например амортизационные 3 (1 реальные расходы + 2 кладем в банк).При удалении амортизационные 2 (1 + 1).При реаллокации (добавляем N элементов) - из банка списывается N.Когда надо выполнять реаллокацию, вопрос неоднозначный, можно по некоторому порогу в банке, но лучше когда внутренний массив весь заполнен. При уменьшении в реаллокации, в принципе, делать ничего не надо, или например 10% * N списать.
# Решение и логика верные . списал 10% * N при уменьшении реаллокации. Добвил в решение.
import ctypes

class DynArrayBank:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.bank = 0  

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        if new_capacity < self.capacity:
            self.bank -= int(self.count * 0.1)  # 10%* N
        else:
            self.bank -= self.count
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        self.bank += 3  
        if self.count == self.capacity:
            self.bank -= self.count  
            self.resize(2 * self.capacity)
        self.bank -= 1  
        self.array[self.count] = itm
        self.count += 1

# Рефлексия из Задания 3(задача 6*)
# Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое измерение может внутри масштабироваться по потребности. В конструкторе задаётся число измерений и размер по каждому из них. Обращаться к такому массиву надо как к обычному многомерному, например: myArr[1,2,3].
# Многомерный динамический массив
# Идея, что у нас есть интерфейс добавления элемента в некоторую многомерную позицию (i,j,k,...), а внутри это обычный одномерный динамический массив.Надо просто корректно реализовать операцию добавления элемента (отображение многомерной координаты в линию).Например входной размер массива 3x4x5, создаём одномерный массив длиной 60, и многомерная координата внутри него элементарно определяется.