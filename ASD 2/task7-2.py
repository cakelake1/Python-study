
#main_quest:
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node is not None:
            compare_result = self.compare(node.value,value)
            if self.__ascending and compare_result >= 0 :
                break
            if not self.__ascending and compare_result <= 0:
                break
            node = node.next
        if node is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        elif node.prev is None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node

    def find(self, val):
        node = self.head
        while node is not None:
            compare_result = self.compare(node.value, val)
            if compare_result == 0:
                return node
            if self.__ascending and compare_result > 0: 
                return None
            if not self.__ascending and compare_result < 0:
                return None
            node = node.next 
        return None 

    def delete(self, val):
        node = self.head
        while node is not None:
            if self.compare(node.value, val) != 0:
                node = node.next
                continue
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            return

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None


    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count +=1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = str(v1).strip()
        v2 = str(v2).strip()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

print("\nдобавление по убыванию:")
list2 = OrderedList(False)
list2.add(5)
list2.add(1)
list2.add(3)
list2.add(7)
list2.add(2)
print([node.value for node in list2.get_all()])  #  [7, 5, 3, 2, 1]

print("\nпоиск по возрастанию:")
list3 = OrderedList(True)
list3.add(1); list3.add(3); list3.add(5); list3.add(7); list3.add(9)
print("Найден 5:", list3.find(5).value if list3.find(5) else None)  #  5
print("Не найден 4:", list3.find(4))  #  None
print("Не найден 10:", list3.find(10))  #  None

print("\nПоиск по убыванию:")
list4 = OrderedList(False)
list4.add(9); list4.add(7); list4.add(5); list4.add(3); list4.add(1)
print("Найден 5:", list4.find(5).value if list4.find(5) else None)  #  5
print("Не найден 6:", list4.find(6))  #  None
print("Не найден 0:", list4.find(0))  #  None

print("\nУдаление по возрастанию:")
list5 = OrderedList(True)
list5.add(1); list5.add(2); list5.add(3); list5.add(3); list5.add(4)
print("До удаления:", [node.value for node in list5.get_all()])
list5.delete(3)
print("После удаления первой 3:", [node.value for node in list5.get_all()])  #  [1, 2, 3, 4]

print("\nУдаление по убыванию:")
list6 = OrderedList(False)
list6.add(4); list6.add(3); list6.add(3); list6.add(2); list6.add(1)
print("До удаления:", [node.value for node in list6.get_all()])
list6.delete(3)
print("После удаления первой 3:", [node.value for node in list6.get_all()])  #  [4, 3, 2, 1]

print("\nУдаление несуществующего элемента:")
list7 = OrderedList(True)
list7.add(1); list7.add(2); list7.add(3)
print("До удаления:", [node.value for node in list7.get_all()])
list7.delete(5)  # Не существует
print("После удаления 5:", [node.value for node in list7.get_all()])  #  [1, 2, 3]

print("\nУдаление из пустого списка:")
list8 = OrderedList(True)
list8.delete(1)  # Не должно быть ошибки
print("Пустой список:", [node.value for node in list8.get_all()])  #  []

# Задания 8-12 со звездочкой я сделаю чуть позже на новогодних каникулах
#8.* Добавьте метод удаления всех дубликатов из упорядоченного списка.

#9.* Напишите алгоритм слияния двух упорядоченных списков в один, сохраняя порядок элементов. Подумайте, как это сделать наиболее эффективно.

#10.* Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.

#11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.

#12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).