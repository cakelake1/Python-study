#7.1 Почему и как будет различаться мера сложности для addHead/removeHead и addTail/removeTail?
# addTail/removeTail сложность О(1) мы добавляем\удаляем один элемент в конце списка.
# addHead/removeHead O(n) мы добавляем/удаляем в начале списка из за которого все элементы сдвигаются и сложность увеличивается

# 7.2. Добавьте для каждого из четырёх вышеупомянутых методов тесты: проверяйте изменившуюся длину очереди и наличие или отстутствие в ней добавляемого/удаляемого элемента.
class Deque:
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
class Deque_Min:
    def __init__(self):
        self.deque = []
        self.min_stack = []  

    def addFront(self, item):
        self.deque.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def addTail(self, item):
        self.deque.insert(0, item)
        if not self.min_stack  or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def removeFront(self):
        if self.size() > 0:
            item = self.deque.pop()
            if self.min_stack and item == self.min_stack[-1]:
                self.min_stack.pop()
            return item
        return None

    def removeTail(self):
        if self.size() > 0:
            item = self.deque.pop(0)
            if self.min_stack and item == self.min_stack[-1]:
                self.min_stack.pop()
            return item
        return None

    def size(self):
        return len(self.deque)
    
    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

# 7.5.* Реализуйте двустороннюю очередь с помощью динамического массива. Методы добавления и удаления элементов с обоих концов деки должны работать за амортизированное время o(1).
class Deque75:
    def __init__(self):
        self.stack = []
        self.start = 0
        self.count = 0
    
    def addFront(self, item):
        if self.count == len(self.stack):
            self._increase()
        if self.start == 0:
            self.start = len(self.stack) - 1
        else:
            self.start -= 1
        self.stack[self.start] = item
        self.count += 1
    
    def addTail(self, item):
        if self.count == len(self.stack):
            self._increase()
        index = (self.start + self.count) % len(self.stack)
        self.stack[index] = item
        self.count += 1
    
    def removeFront(self):
        if self.count == 0:
            return None
        item = self.stack[self.start]
        self.stack[self.start] = None
        self.start = (self.start + 1) % len(self.stack)
        self.count -= 1
        if self.count > 0 and self.count * 4 <= len(self.stack):
            self._decrease()
        return item
    
    def removeTail(self):
        if self.count == 0:
            return None
        index = (self.start + self.count - 1) % len(self.stack)
        item = self.stack[index]
        self.stack[index] = None
        self.count -= 1
        if self.count > 0 and self.count * 4 <= len(self.stack):
            self._decrease()
        return item
    
    def size(self):
        return self.count
    
    def _increase(self):
        old_size = len(self.stack)
        new_size = max(1, old_size * 2)
        new_stack = [None] * new_size
        for i in range(self.count):
            old_index = (self.start + i) % old_size
            new_stack[i] = self.stack[old_index]
        self.stack = new_stack
        self.start = 0
    
    def _decrease(self):
        old_size = len(self.stack)
        new_size = max(4, old_size // 2)
        new_stack = [None] * new_size
        for i in range(self.count):
            old_index = (self.start + i) % old_size
            new_stack[i] = self.stack[old_index]
        self.stack = new_stack
        self.start = 0

# 7.6.* Напишите автономную функцию, которая проверяет правильность расстановки (баланс) скобок в символьном (например, арифметическом) выражении. Оно подаётся на вход функции как строка, например "(())}{(" или "[]({})". Алгоритм должен обрабатывать и учитывать круглые (), квадратные [] и фигурные {} скобки. Строка всегда корректна: содержит только скобки указанных типов. Алгоритм должен работать за O(N), где N -- длина выражения.
#Внутри этой функции используйте стек.
def balance_brackets(stroke):
    stack = []
    open_chars = '([{'
    close_chars = ')]}'
    for char in stroke:
        if char in open_chars:
            stack.append(char)
        elif char in close_chars:
            if len(stack) == 0:
                return False
            close_char_index = close_chars.index(char)
            match_char = open_chars[close_char_index]
            if stack[-1] != match_char:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True
        
# тут я не успеваю немного с двумя задачами, доделаю 23,24 декабря и дальнейшую рефлексию.
# доделал только 5 января