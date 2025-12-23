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