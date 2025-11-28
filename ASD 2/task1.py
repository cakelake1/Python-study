class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result
    def delete(self, val, all=False):
        prev = None
        current = self.head
        while current is not None:
            if current.value == val:
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current.next is None:
                        self.tail = prev
                if not all:
                    return
            else:
                prev = current
            current = current.next
    def clean(self):
        self.head = None
        self.tail = None
    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count
    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode
    def get_all_values(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
def test_Linked_list():
    lst = LinkedList()
    print("Тест 1: Добавление элементов")
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(20))
    lst.add_in_tail(Node(30))
    print("Список:", lst.get_all_values())
    print("Тест 2: Поиск")
    print("Найти 20:", lst.find(20).value if lst.find(20) else "Не найден")
    print("Найти 99:", lst.find(99) if lst.find(99) else "Не найден")
    print("Тест 3: Удаление одного")
    lst.delete(20)
    print("После удаления 20:", lst.get_all_values())
    print("Тест 4: Вставка")
    lst.insert(lst.find(10), Node(15))
    print("После встаcвки 15 после 10:", lst.get_all_values())
test_Linked_list()