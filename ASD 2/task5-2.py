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