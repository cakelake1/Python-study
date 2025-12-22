#main quest
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size()) # 3
print(q.dequeue()) # 10
print(q.dequeue()) # 20
print(q.size()) # 1
q.enqueue(40)
q.enqueue(50)
print(q.size()) # 3
print(q.dequeue()) # 30
print(q.dequeue()) # 40
print(q.dequeue()) # 50
print(q.size()) # 0
print(q.dequeue()) # None
print(q.dequeue()) # None
for i in range(5):
    q.enqueue(i*100)

for i in range(3):
    print(q.dequeue()) # 0, 100, 200

print(q.size()) # 2
q.enqueue(999)
print(q.dequeue()) # 300

#7.3*
print(is_palindrome("арозаупаланалапуазора"))  # True
print(is_palindrome("казак"))                   # True
print(is_palindrome("шалаш"))                   # True
print(is_palindrome("hello"))