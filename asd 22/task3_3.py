#Тесты:
#1. Реализуйте дополнительный метод обхода дерева WideAllNodes() без параметров для класса из занятия по двоичным деревьям (этот же класс используйте и для последующих заданий), так, чтобы он реализовывал алгоритм поиска в ширину, начиная с корня.
tree = BST(BSTNode(10, "root", None))
tree.AddKeyValue(5, "l")
tree.AddKeyValue(15, "r")
tree.AddKeyValue(3, "ll")
tree.AddKeyValue(7, "lr")
tree.AddKeyValue(12, "rl")
tree.AddKeyValue(18, "rr")
wide_result = tree.WideAllNodes()
print("[10,5,15,3,7,12,18]?",[node.NodeKey for node in wide_result] == [10,5,15,3,7,12,18])
#2. Реализуйте дополнительный метод обхода дерева DeepAllNodes(), начиная с корня, которому задаётся один целый параметр, принимающий значения 0 (in-order), 1 (post-order) и 2 (pre-order). В зависимости от этого параметра метод DeepAllNodes() реализует соответствующую форму алгоритма поиска в глубину.
tree5 = BST(BSTNode(10, "root", None))
tree5.AddKeyValue(5, "l")
tree5.AddKeyValue(15, "r")
tree5.AddKeyValue(3, "ll")
tree5.AddKeyValue(7, "lr")
tree5.AddKeyValue(12, "rl")
tree5.AddKeyValue(18, "rr")
# order 0
deep_result0 = tree5.DeepAllNodes(0)
print("[3,5,7,10,12,15,18]",[node.NodeKey for node in deep_result0] == [3,5,7,10,12,15,18])
# order 2
deep_result2 = tree5.DeepAllNodes(2)
print("[10,5,3,7,15,12,18]",[node.NodeKey for node in deep_result2] == [10,5,3,7,15,12,18])
# order 1
deep_result1 = tree5.DeepAllNodes(1)
print("[3,7,5,12,18,15,10]?",[node.NodeKey for node in deep_result1] == [3,7,5,12,18,15,10])

#3*Реализуйте алгоритм инвертирования дерева: надо сделать так, чтобы слева от главного узла были значения больше него, а справа — меньше.
node1 = BSTNode(1, "Root", None)
node2 = BSTNode(2, "Left", node1)
node3 = BSTNode(3, "Right", node1)
node4 = BSTNode(4, "Left-Left", node2)
node5 = BSTNode(5, "Left-Right", node2)
node6 = BSTNode(6, "Right-Left", node3)
node7 = BSTNode(7, "Right-Right", node3)
node1.LeftChild = node2
node1.RightChild = node3
node2.LeftChild = node4
node2.RightChild = node5
node3.LeftChild = node6
node3.RightChild = node7
tree = BST(node1)
print([n.NodeKey for n in tree.WideAllNodes()]) 
tree.InvertTreeNode()
print([n.NodeKey for n in tree.WideAllNodes()])  

#4.* Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна. Подумайте, как оптимизировать решение, чтобы производительность была достаточной даже для больших деревьев.
node1 = BSTNode(1, 100, None)
node2 = BSTNode(2, 200, node1)
node3 = BSTNode(3, 300, node1)
node4 = BSTNode(4, 400, node2)
node5 = BSTNode(5, 500, node2)
node6 = BSTNode(6, 600, node3)
node7 = BSTNode(7, 700, node3)
node1.LeftChild = node2
node1.RightChild = node3
node2.LeftChild = node4
node2.RightChild = node5
node3.LeftChild = node6
node3.RightChild = node7
tree = BST(node1)
level, max_sum = tree.FindLevelMaxSum()
print(level)
print(level,max_sum) 

#5*Учитывая результаты обхода дерева в префиксном и инфиксном порядке, разработайте функцию для восстановления оригинального дерева.
#Например,
preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
root = CreateTreeinpreorder(preorder, inorder)
tree = BST(root)
preorder_result = [node.NodeKey for node in tree.DeepAllNodes(2)]
inorder_result = [node.NodeKey for node in tree.DeepAllNodes(0)]
postorder_result = [node.NodeKey for node in tree.DeepAllNodes(1)]
wideresult_result = [node.NodeKey for node in tree.WideAllNodes()]

print(preorder_result)
print(inorder_result)
print(postorder_result)
print(wideresult_result) 