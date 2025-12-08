class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        node = self.head
        while node is not None:
            if node.value == val:
                next_node = node.next
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                        node.next.prev = node.prev
                else:
                    self.tail = node.prev
                if not all:
                    return
                node = next_node
            else:
                node = node.next          

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
                newNode.prev = None
                newNode.next = None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                newNode.next = None
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            if newNode.next is not None:
                newNode.next.prev = newNode
            else:
                self.tail = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None  