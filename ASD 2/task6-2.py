#7.1 Почему и как будет различаться мера сложности для addHead/removeHead и addTail/removeTail?
# addTail/removeTail сложность О(1) мы добавляем\удаляем один элемент в конце списка.
# addHead/removeHead O(n) мы добавляем/удаляем в начале списка из за которого все элементы сдвигаются и сложность увеличивается

# 7.2. Добавьте для каждого из четырёх вышеупомянутых методов тесты: проверяйте изменившуюся длину очереди и наличие или отстутствие в ней добавляемого/удаляемого элемента.
class Queue:
    def __init__(self):
        self.queue = [] 

    def enqueue(self, item):
        self.queue.append(item)
        

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0) 

    def size(self):
        return len(self.queue) 
    
    def addHead(self, item):
        self.queue.insert(0, item)

    def removeHead(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)
    
    def addTail(self, item):
        self.queue.append(item)
    
    def removeTail(self):
        if self.size() == 0:
            return None
        return self.queue.pop()
    
    
    
q = Queue()
q.addHead(1)
print(q.size(), q.queue)
q.addHead(2)
print(q.size(), q.queue)
q.addTail(3)
print(q.size(), q.queue)
print(q.removeHead(), q.size(), q.queue)
print(q.removeTail(), q.size(), q.queue)
print(q.removeHead(), q.size(), q.queue)
print(q.removeHead(), q.size(), q.queue)
q.addTail(4)
q.addHead(5)
print(q.size(), q.queue)
print(q.removeTail(), q.size(), q.queue)
print(q.removeHead(), q.size(), q.queue)
print(q.removeHead(), q.size(), q.queue)

# 7.3. * Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
def is_palindrome(s):
    cleaned_list = s.replace(" ", "").lower()
    d = list(cleaned_list)
    while len(d) > 1:
        if d.pop(0) != d.pop():
            return False
    return True
# 7.4 *  Напишите метод, который возвращает минимальный элемент деки за O(1).
# Если мы говорим только о реализации метода, то:
def __init__(self):
        self.deque = []
        self.min_stack = []
    
def get_min(self):
    if not self.min_stack:
        return None
    return self.min_stack[-1]

# 7.5.* Реализуйте двустороннюю очередь с помощью динамического массива. Методы добавления и удаления элементов с обоих концов деки должны работать за амортизированное время o(1).

# 7.6.* Напишите автономную функцию, которая проверяет правильность расстановки (баланс) скобок в символьном (например, арифметическом) выражении. Оно подаётся на вход функции как строка, например "(())}{(" или "[]({})". Алгоритм должен обрабатывать и учитывать круглые (), квадратные [] и фигурные {} скобки. Строка всегда корректна: содержит только скобки указанных типов. Алгоритм должен работать за O(N), где N -- длина выражения.
#Внутри этой функции используйте стек.
# тут я не успеваю немного с двумя задачами, доделаю 23,24 декабря и дальнейшую рефлексию.