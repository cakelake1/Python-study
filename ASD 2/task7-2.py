
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



#8.* Добавьте метод удаления всех дубликатов из упорядоченного списка.
    def delete_duplicate(self):
        if self.head is None:
            return
        node = self.head
        while node is not None and node.next is not None:
            if self.compare(node.value, node.next.value) != 0:
                node = node.next
                continue
            duplicate = node.next
            node.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = node
            else:
                self.tail = node


#9.* Напишите алгоритм слияния двух упорядоченных списков в один, сохраняя порядок элементов. Подумайте, как это сделать наиболее эффективно.
# Уже было похожее ранее задание, я сравнивал сначала, чтобы списки были одинаково упорядоченные. Затем я сравнивал поэлементно значения в списке и добавлял наименьшее в новый список в цикле, а затем добавлял оставшиеся значения.
# так как нам нужен алгоритм, то я добавляю дополнитеоьный метод add_in_tail, который в свою очередь, добавляет значение в конец списка, и он выполняется при условии если наши списки упорядоченныые
    def add_in_tail(self, value):
        new_node = None(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
# и напишем сам метод слияния merge:
    def merge(self, list2):
        if self.__ascending != list2.__ascending:
            raise ValueError("списки не совпадают")
        result = OrderedList(self.__ascending)
        node1 = self.head
        node2 = list2.head
        while node1 and node2:
            compare = self.compare(node1.value, node2.value)
            if (self.__ascending and compare <= 0) or (not self.__ascending and compare >= 0):
                result.add_in_tail(node1.value)
                node1 = node1.next
            else:
                result.add_in_tail(node2.value)
                node2 = node2.next
        while node1:
            result.add_in_tail(node1.value)
            node1 = node1.next
        while node2:
            result.add_in_tail(node2.value)
            node2 = node2.next
        return result


#10.* Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.

#11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.

#12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).