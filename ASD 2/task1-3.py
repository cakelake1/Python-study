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