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