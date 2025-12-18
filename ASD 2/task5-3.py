#5.1 
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

#5.3
q = Queue()
for i in [1,2,3,4,5]:
    q.enqueue(i)
q.spin_circle(2)
print(q.stack)
q.spin_circle(44)
print(q.stack) # 23451
#5.4 тесты те же от 5.1 и 5.3
#5.5
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("Очередь до reverse:", q.stack_in)
q.reverse()
print("Очередь после reverse:", q.stack_in)
print("dequeue после reverse:", q.dequeue())
print("dequeue:", q.dequeue())
#5.6
cq = CircleQueue(3)
cq.enqueue("A")
cq.enqueue("B")
print("размер :", cq.size())
print("Полна?", cq.is_full())  
cq.enqueue("C")
print("размер ", cq.size())  # 3
print("Полна?", cq.is_full())  # True
try:
    cq.enqueue("D")
    print("D")
except Exception as e:
    print("Не удалось добавить D:", e)  # Очередь полна
print("удалил, cq.dequeue())  # A
print("размер ", cq.size())  # 2
cq.enqueue("D")
print("размер ", cq.size())  # 3
print("удалил, cq.dequeue()) 
print("удалил, cq.dequeue()) 
print("удалил, cq.dequeue())  
print("размер ", cq.size())  # 0
print("удалил из пустой:", cq.dequeue())  # None