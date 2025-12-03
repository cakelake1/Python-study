2.10.*

 def reverse(self):
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = node.prev
            node.prev = next_node
            node = next_node
        temp_head = self.head
        self.head = self.tail
        self.tail = temp_head
2.11.*
def has_cycle(self):
        if self.head is None:
            return False
        first = self.head
        second = self.head
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False


2.12.*
def get_all_values(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
def sort(self):
        values = self.get_all_values()
        values.sort()
        self.clean()
        for value in values:
            self.add_in_tail(Node(value))

2.13.*
def merge_sorted_lists(list1, list2):
        values1 = list1.get_all_values()
        values2 = list2.get_all_values()
        result = LinkedList2()
        i, j = 0, 0
        while i < len(values1) and j < len(values2):
            if values1[i] <= values2[j]:
                result.add_in_tail(Node(values1[i]))
                i += 1
            else:
                result.add_in_tail(Node(values2[j]))
                j += 1
        while i < len(values1):
            result.add_in_tail(Node(values1[i]))
            i += 1
        while j < len(values2):
            result.add_in_tail(Node(values2[j]))
            j += 1
        return result 



2.14.*