# 4. Стеки
# 4.1:

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack.pop() 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[-1]
# Динамические массив "список" в ПИтоне.
# Cложность О(1) для методов push and pop
# тесты в файле 4-3

# 4.2, тесты добавил дополнительно в 4-3(аналогичные)
class Stack_head:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack.pop(0) 

    def push(self, value):
        self.stack.insert(0,value)

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[0]

    
# 4.3 
# Пока размер списка больше 0:
# Вывести на экран последний элемент в списке и удалить его, размер стека -1 - (х2)
# Когда мы попадаем на последний элемент, то получим вывод на экран None и цикл завершится.

# 4.4
# pop и push стали О(n), потому что требуется теперь сдвигать все элементы

# 4.5* тесты в task4_3
    def brackets_balance(value_string):
        stack = Stack()
        for i in value_string:
            if i == '(':
                stack.push(i)
            elif stack.size() ==0:
                return False
            else:
                stack.pop()
        return stack.size() == 0
# 4.6* тесты в task4_3
    def brackets_balance(value_string):
    stack = Stack()
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for i in value_string:
        if i in pairs:
            stack.push(i)
        elif stack.size() == 0:
            return False
        else:
            if pairs[stack.pop()] != i:
                return False
    return stack.size() == 0

# 4.7* тесты в task4_3

class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop() 

    def push(self, value):
        self.stack.append(value)
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[-1]
    
    def min_value(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]
    
# 4.8* Тесты в 4_3
class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.sum = 0
        self.count = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        pop_value = self.stack.pop()
        if pop_value == self.min_stack[-1]:
            self.min_stack.pop()
        self.sum -= pop_value
        self.count -= 1
        return pop_value 

    def push(self, value):
        self.stack.append(value)
        self.sum += value
        self.count += 1
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[-1]
    
    def min_value(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]
    
    def mid_summ(self):
        if self.count == 0:
            return None
        return self.sum / self.count
    
# 4.9 тест в task4_3
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack.pop() 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[-1]
    
    def postfix_calculator(self, value):
        stack = Stack()
        parts = value.split()
        
        for i in parts:
            if i.isdigit():
                stack.push(int(i))
            elif i == '+':
                b = stack.pop()
                a = stack.pop()
                stack.push(a + b)
            elif i == '*':
                b = stack.pop()
                a = stack.pop()
                stack.push(a * b)
            elif i == '=':
                return stack.pop()
        return stack.pop()