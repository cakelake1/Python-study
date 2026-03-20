#3.1 Сделайте в своём коде три примера наглядных методов-фабрик. 
# class Queue:
#     def __init__(self):
#         self.stack = []
#     @classmethod
#     def from_list(cls, items): # Пример 1
#         q = cls()
#         for item in items:
#              q.enqueue(item)
#         return q
#     @classmethod
#     def empty(cls): # Пример 2
#         return cls()   
#     @classmethod 
#     def copy(cls, other): # ПРимер 3 
#         q = cls()
#         q.stack = other.stack.copy()
#         return q

#     def enqueue(self, item):
#         self.stack.append(item)

#     def dequeue(self):
#         if len(self.stack) == 0:
#             return None
#         return self.stack.pop(0)

#     def size(self):
#         return len(self.stack)
    
#     def __repr__(self):
#         return f"Queue({self.stack})"
    
# q1 = Queue.from_list([1, 2, 3])
# q2 = Queue.copy(q1)
# q3 = Queue.empty()
# print(q1)
# print(q2)
# print(q3)


#3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, напишите несколько примеров их правильного именования.
# Я интерфейсы или астрактные классы не использовал, но почему бы с ними не ознакомиться:
# В Питоне для создания и-ф и абстр. классов используется модуль abc. Abstract Base Classes. Нужно наловчится сразу использовать правильное именование, чтобы понимать назначение класса с ходу.
    # Абстрактные классы идентифицируются по словам BAse или Abstract, если они учавствуют в создании класса. Абстрактный класс может бьть без префикса.
    # Интерфейсы можно определить по суффискам er, able, ible