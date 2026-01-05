#main quest
d = Deque()
d.addFront(1)
d.addFront(2)
print(d.removeFront())
print(d.removeFront())d.addTail(3)
d.addTail(4)
print(d.removeTail())
print(d.removeTail())
d.addFront(5)
d.addTail(6)
print(d.removeFront())
print(d.removeTail())
print(d.size())
d.addFront(7)
d.addTail(8)
print(d.size())
print(d.removeFront())
print(d.removeTail())

#7.3*
print(is_palindrome("арозаупаланалапуазора"))  # True
print(is_palindrome("казак"))                   # True
print(is_palindrome("шалаш"))                   # True
print(is_palindrome("hello"))

#7.4*
dq = Deque_Min()
dq.addFront(5)
dq.addTail(3)
dq.addFront(2)
print(dq.get_min())
dq.removeFront()
print(dq.get_min())
dq.removeTail()
print(dq.get_min())

#7.5*
dq = Deque75()
print(dq.size())
print(dq.removeFront())
print(dq.removeTail())
dq.addTail(10)
print(dq.size())
dq.addTail(20)
print(dq.size())
dq.addFront(5)
print(dq.size())
print(dq.removeTail())
print(dq.removeFront())
print(dq.size())
print(dq.removeTail())
print(dq.size())

#7.6*
print(balance_brackets("()"))
print(balance_brackets("(]"))
print(balance_brackets(""))
print(balance_brackets("[]"))
print(balance_brackets("{}"))
print(balance_brackets("()[]{}"))
print(balance_brackets("({[]})"))
print(balance_brackets("{[()()]}"))