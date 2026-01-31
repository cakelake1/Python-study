
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
# Чтобы избавится от цикла внутри цикла я добавил еще два метода на проверку длины от начала отсчета до конца списка и проверку с заданного элемента со всем элементами подсписка попарно

    def len_node(self, start_node):
        count = 0
        node = start_node
        while node is not None:
            count +=1
            node = node.next
        return count
    
    def check_sublist(self, start_node, sublist):
        node = start_node
        sub_node = sublist.head
        while node is not None and sub_node is not None:
            if self.compare(node.value, sub_node.value) != 0:
                return False
            node = node.next
            sub_node = sub_node.next
        return sub_node is None
    
    def sublist_contain(self, sublist):
        if sublist.head is None:
            return True
        if self.head is None:
            return False
        if sublist.len() > self.len():
            return False
        node = self.head
        sub_node = sublist.head
        while node is not None:
            check_node_len = self.len_node(node)
            if check_node_len < sublist.len():
                break
            if self.compare(node.value, sub_node.value) == 0:
                start_match = self.check_sublist(node, sublist)
                if start_match:
                    return True
                if node.next is not None and sub_node.next is not None:
                    compare_result = self.compare(sub_node.next.value, node.next.value)
                    if self.__ascending and compare_result < 0:
                        return False
                    if not self.__ascending and compare_result > 0:
                        return False
            node = node.next
        return False

#11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.
    def hits_num(self):
        if self.head is None:
            return None
        hits_value = self.head.value
        max_count = 1
        cur_value = self.head.value
        cur_count = 1
        node = self.head.next
        while node is not None:
            if self.compare(node.value, cur_value) == 0:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                    hits_value = cur_value
                cur_value = node.value
                cur_count = 1
            node = node.next
        if cur_count > max_count:
            hits_value = cur_value
        return hits_value
#12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).
# для бинарного поиска необходимо добавить массив, чтобы пользоваться индексами элементов
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList3:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.array = []

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
            self.array.append(new_node)
            return
        node = self.head
        slot_index = 0
        while node is not None:
            compare_result = self.compare(node.value,value)
            if self.__ascending and compare_result >= 0 :
                break
            if not self.__ascending and compare_result <= 0:
                break
            node = node.next
            slot_index += 1
        if node is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.array.append(new_node)
        elif node.prev is None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.array.insert(0, new_node)
        else:
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            self.array.insert(slot_index, new_node)

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
        slot_index = 0
        while node is not None:
            if self.compare(node.value, val) == 0:
                self.array.pop(slot_index)
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            return
        node = node.next
        slot_index += 1

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.array = []

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
    
    def find_index_bin(self, value):
        if not self.array:
            return None
        left = 0
        right = len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = self.array[mid].value
            result = self.compare(mid_value, value)
            if result == 0:
                return mid
            if (self.__ascending and result > 0) or (not self.__ascending and result < 0):
                    right = mid - 1
            else:
                left = mid + 1
        return None


class OrderedStringList(OrderedList3):
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
    
# Рефлексия по task5-2
# 3* Вращение очереди по кругу на N элементов.
    # Сделал аналогично подсказке.
# 4* Очередь с помощью двух стеков.
    # Я сделал за сложность О(n^2), В подсказке можно сделать за О(1), реализуем:
class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def size(self):
        return len(self.stack_in) + len(self.stack_out)
    
    def spin_circle(self, N):
        if self.size() == 0:
            return
        N = N % self.size()
        for _ in range(N):
            item = self.dequeue()
            self.enqueue(item)

# 5*. Обращение всех элементов в очереди в обратном порядке.
    # я использовал читерный прием, как я понимаю он не совсем поддходим, сделаю разворот с использованием стека:
    def reverse(self):
        if self.size() == 0:
            return
        array = []
        while self.size() > 0:
            item = self.dequeue()
            array.append(item)
        while array:
            item = array.pop()
            self.enqueue(item)
# 6* Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера
    # у меня в принципе правильно, но с подсказкой можно немного оптимизировать:
class CircleQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Очередь полна")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.front =(self.front + 1) % self.capacity
        return item
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def size(self):
        if self.rear >= self.front:
            return self.rear - self.front
        else:
            return self.capacity - self.front + self.rear
    
    def is_empty(self):
        return self.front == self.rear