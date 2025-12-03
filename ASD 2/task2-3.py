def get_all_values(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

def test_LinkedList2():
    lst = LinkedList2()
    print("1. Пустой список:", lst.get_all_values())
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(20))
    lst.add_in_tail(Node(30))
    print("2. После добавления 10,20,30:", lst.get_all_values())
    print("3. Поиск 20:", lst.find(20).value if lst.find(20) else "Не найден")
    print("4. Поиск 99:", "Не найден" if lst.find(99) is None else "Ошибка")
    lst.delete(20)
    print("5. После delete(20):", lst.get_all_values())
    lst.insert(lst.find(10), Node(15))
    print("6. insert(15 после 10):", lst.get_all_values())
    lst.insert(None, Node(40))
    print("7. insert(None, 40) - в конец:", lst.get_all_values())
    lst.add_in_head(Node(5))
    print("8. add_in_head(5):", lst.get_all_values())
    lst.delete(10, all=True)
    print("9. delete(10, all=True):", lst.get_all_values())
    lst.clean()
    print("10. После clean():", lst.get_all_values())
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    print("11. Добавили 1,1,2:", lst.get_all_values())
    print("12. find_all(1):", [n.value for n in lst.find_all(1)])
test_LinkedList2()