# Тесты:
# Создаю дерево
root = SimpleTreeNode(1, None)
tree = SimpleTree(root)
node2 = SimpleTreeNode(2, root)
node3 = SimpleTreeNode(3, root)
root.Children = [node2, node3]
node4 = SimpleTreeNode(4, node2)
node5 = SimpleTreeNode(5, node2)
node2.Children = [node4, node5]
node6 = SimpleTreeNode(6, node3)
node3.Children = [node6]
node7 = SimpleTreeNode(7, None)
print([c.NodeValue for c in node2.Children]) #[4,5]
tree.AddChild(node2, node7) # Тест на добавление узла - добавляю узел 7 к узлу 2
print([c.NodeValue for c in node2.Children]) # [4,5,7] - успешный

tree.DeleteNode(node4) # удаляю 4 узел
print([c.NodeValue for c in node2.Children]) # [5,7]
print()

all_nodes = tree.GetAllNodes()
all_values = [n.NodeValue for n in all_nodes]
print(all_values)  # список всех узлов
print()
# найти список подходящих узлов по заданному значению
found5 = tree.FindNodesByValue(5)
print(len(found5)) # Есть
found10 = tree.FindNodesByValue(10)
print(len(found10)) # нету - 0

print([c.NodeValue for c in node2.Children])   # 5 7
print([c.NodeValue for c in node3.Children])   # [6]
tree.MoveNode(node5, node3)
print([c.NodeValue for c in node2.Children])   # [7]
print([c.NodeValue for c in node3.Children])   # [6,5]тест: проверяем, что узел отсутствует там где был исходно и появился в новом мест


track_nodes = tree.Count()
leaves = tree.LeafCount()
print(track_nodes) #6(1,2,3,5,6,7)
print("Количество листьев:", leaves) #5,6,7 
print()

# тесты по доп заданию
tree.UpdateLevelNode(root, 0) # проставил уровни
for node in tree.GetAllNodes():
    print(f"Узел {node.NodeValue}, уровень {node.Level}") # сходится