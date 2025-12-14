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

s1 = Stack()
print(s1.size()) 
print(s1.pop())   
print(s1.peek())  
print('Должно быть 0, None, None')
print()

s2 = Stack()
s2.push(10)
s2.push(20)
s2.push(30)
print(s2.size())
print(s2.peek())
print('Должно быть 3, 30')
print()

print("=== ТЕСТ 3: Удаление элементов ===")
s3 = Stack()
s3.push("A")
s3.push("B")
s3.push("C")
print(s3.size())
print(s3.pop())
print(s3.size())
print(s3.peek())
print(s3.pop())
print(s3.pop())  
print(s3.pop())
print(s3.size())
print('Должно быть 3, C, 2, B, B, A, None, 0 ')
print()

s4 = Stack()
s4.push(100)
s4.push(200)
print(s4.peek())
print(s4.size())
print('Должно быть 200, 2')
s4.pop()
print(s4.peek())
print(s4.size())
print('Должно быть 100, 1')
s4.push(300)
print(s4.peek())
print(s4.size())  
print('Должно быть 300, 2')
print()

s5 = Stack()
s5.push(42)
s5.push("строка")
s5.push([1, 2, 3])
s5.push(None)

print(s5.size())
print(s5.pop())
print(s5.pop())
print(s5.pop())
print(s5.pop())
print(s5.pop())
print('Должно быть 4, None, [1, 2, 3], "строка", 42, None ')
print()

s6 = Stack()
n = 1000
for i in range(n):
    s6.push(i)

print(s6.size())
print(s6.peek()) 
print('Должно быть 1000, 999 ')
print()
# Проверяем порядок LIFO
correct_order = True
for i in range(n-1, -1, -1):
    if s6.pop() != i:
        correct_order = False
        break
print(correct_order)
print(s6.size())
print('Должно быть True, 0 ')

# Тест 4.5
b1 = Stack.brackets_balance
print(b1("()"))
print(b1("(())"))
print(b1("()()"))
print(b1("(()())"))
print(b1(""))
print(b1("("))
print(b1(")"))
print(b1(")("))
print(b1("(()"))
print(b1("())"))
print(b1("((()()))"))
print(b1("(()(()"))

# Тест 4.6 b1 берем из теста 4.5
print()
print(b1("()[]{}"))
print(b1("([{}])"))
print(b1("({[]})"))
print(b1("{[()]}"))
print(b1(""))
print(b1("("))
print(b1(")"))
print(b1("([)]"))
print(b1("{{[(])}}"))
print(b1("({[}])"))
print(b1("((()))[[[]]]{{{{}}}}"))
print(b1("([{}])([{}])([{}])"))  

# Тест для 4.7
s = Stack()
print(s.min_value())
s.push(5)
print(s.min_value())
s.push(3)
print(s.min_value())
s.push(7)
print(s.min_value())
s.push(2)
print(s.min_value())
s.push(2)
print(s.min_value())
s.pop()
print(s.min_value())
s.pop()
print(s.min_value())
s.pop()
print(s.min_value())
s.pop()
print(s.min_value())
s.pop()
print(s.min_value())

# ТЕст для 4.8
print(s.mid_summ())
s.push(5)
print(s.mid_summ())
s.push(3)
print(s.mid_summ())
s.push(7)
print(s.mid_summ())
s.push(2)
print(s.mid_summ())
s.pop()
print(s.mid_summ())
s.pop()
print(s.mid_summ())
s.pop()
print(s.mid_summ())  

# Тест для 4.9
s = Stack()
result = s.postfix_calculator("8 2 + 5 * 9 + =")
print(result)  # → 59