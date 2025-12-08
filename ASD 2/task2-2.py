2.10.*
Надо понимать, что нам достаточно в логике поменять шаги. Следующий шаг сделать предыдущим, и предыдущий следующим. И в конце поменять начало и конец местами
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
Мы начинаем предполагать как вообще узнать есть ли цикл через функцию. На первый взгляд приходит в голову создать хэш талицу и вносить туду значения, заодно сравнивая их. Если немного погуглить то находим очень легкий и интересный алгоритм зайца и черепахи или "Алгоритм Флойда"/
Основной смысл у нас один указатель делает один шаг, а второй два шага и сравниваем их, главное условие правильно задать, чтобы дойти корректно до конца списка.
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
Тут я немного читерю, я написал функцию, которая выдает по шагам значения и просто их сортирует по питонски за О(n) и затем собирает в связанный список заново.
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
Получаю значения двух списков, сортирую их, результируюй список сортирвоать нельзя. Использую слияние двух отсортированных списков
функция сортироваки на основе функции получения значений:
def sort_list(self):
        if self.head is None or self.head.next is None:
            return
        values = self.get_all_values()
        values.sort()
        current = self.head
        for value in values:
            current.value = value
            current = current.next

def merge_sorted_lists_efficient(list1, list2):
    list1.sort_list()
    list2.sort_list()
    result = LinkedList2()
    node1 = list1.head
    node2 = list2.head
    while node1 is not None and node2 is not None:
        if node1.value <= node2.value:
            result.add_in_tail(node1)  
            node1 = node1.next
        else:
            result.add_in_tail(node2)  
            node2 = node2.next
    while node1 is not None:
        result.add_in_tail(node1)
        node1 = node1.next
    while node2 is not None:
        result.add_in_tail(node2)
        node2 = node2.next
    list1.head = list1.tail = None
    list2.head = list2.tail = None
    return result



2.14.*
Про dummy узел интересная информация, я поизучал.
В свободное время поприменяю на простых примерах, чтобы и наверное в свои решения посижу подабовляю фиктивный узел