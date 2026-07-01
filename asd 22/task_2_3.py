#тест: проверяем поиск отсутствующего ключа в двух вариантах (запрошенный ключ добавляем либо левому, либо правому потомку) и поиск присутствующего ключа)
    #(тесты: проверяем исходное отсутствие узла по такому ключу в дереве и его наличие после добавления, в двух вариантах -- левым или правым узлом родителя, а также попытку добавления ключа, которое уже имеется в дереве, в таком случае ничего с деревом не делаем)
#(тест, 4 варианта: поиск начиная с корня и поиск начиная с поддерева, ищем максимальный и минимальный ключ)
#(тест: проверяем исходное наличие узла у родителя, его отсутствие после удаления, и результат работы метода)
tree = BST(BSTNode(10, "root", None))
tree.AddKeyValue(5, "l")
tree.AddKeyValue(15, "r")
tree.AddKeyValue(3, "ll")
tree.AddKeyValue(7, "lr")
tree.AddKeyValue(12, "rl")
tree.AddKeyValue(18, "rr")
r = tree.FindNodeByKey(2)
# Тест 1 поиск отсутствующего ключа слева и справа
print("2 есть??", r.NodeHasKey == False and r.ToLeft == True)
r = tree.FindNodeByKey(8)
print("8 есть??",r.NodeHasKey == False and r.ToLeft == False)
    # Поиск присутствующего ключа
g = tree.FindNodeByKey(3)
print("3 присутствует?", g.NodeHasKey == True)
g = tree.FindNodeByKey(7)
print("7 присутствует?",g.NodeHasKey == True)
# добавляю новый ключ, левый и правый

tree.AddKeyValue(2, "new_left")
r = tree.FindNodeByKey(2)  
print("2 есть?",r.NodeHasKey == True)
print("2 слева от 3",r.Node.Parent.NodeKey == 3 and r.Node.Parent.LeftChild == r.Node)
tree.AddKeyValue(8, "new_left")
r = tree.FindNodeByKey(8)  
print("8 есть?",r.NodeHasKey == True)
print("8 справа от 7",r.Node.Parent.NodeKey == 7 and r.Node.Parent.RightChild == r.Node)
# добавляю сушествующий ключ
tree.AddKeyValue(10, "check")
g = tree.FindNodeByKey(10)
print("10 корень?", g.Node.NodeValue == "root")
# поиск мин и макс 4 варианта
print("Мин от корня 2?", tree.FinMinMax(tree.Root, False).NodeKey == 2)
print("Макс от корня 18?", tree.FinMinMax(tree.Root, True).NodeKey == 18)
print("Мин от правого поддерева12?", tree.FinMinMax(tree.Root.RightChild, False).NodeKey == 12)
print("Макс от левого поддерева 8?", tree.FinMinMax(tree.Root.LeftChild, True).NodeKey == 8)

# удаление листа 2
tree.DeleteNodeByKey(2)
r = tree.FindNodeByKey(2)
print("2 удалён?", r.NodeHasKey == False)


tree.DeleteNodeByKey(12)
tree.DeleteNodeByKey(15)
r = tree.FindNodeByKey(15)
print("15 удалён?", r.NodeHasKey == False)
print("18 теперь прямо под корнем?", tree.Root.RightChild.NodeKey == 18 and tree.Root.RightChild.Parent == tree.Root)

tree.DeleteNodeByKey(5)
r = tree.FindNodeByKey(5)
print("5 удалён?", r.NodeHasKey == False)
# Проверяем, что на место 5 встал минимальный из правого поддерева 7
print("На месте 5 теперь 7?", tree.Root.LeftChild.NodeKey == 7)
print("Левый потомок 7 3?", tree.Root.LeftChild.LeftChild.NodeKey == 3)
print("Правый потомок 7 8?", tree.Root.LeftChild.RightChild.NodeKey == 8)
# новое дерево
tree = BST(BSTNode(10, 10, None))
tree.AddKeyValue(5, 5)
tree.AddKeyValue(15, 15)
tree.AddKeyValue(3, 3)
tree.AddKeyValue(7, 7)
tree.AddKeyValue(12, 12)
tree.AddKeyValue(18, 18)

# Тест 1*

tree_copy = BST(BSTNode(10, 10, None))
tree_copy.AddKeyValue(5, 5)
tree_copy.AddKeyValue(15, 15)
tree_copy.AddKeyValue(3, 3)
tree_copy.AddKeyValue(7, 7)
tree_copy.AddKeyValue(12, 12)
tree_copy.AddKeyValue(18, 18)
print("Одинаковые деревья?", tree.IsIdenticalTrees(tree_copy) == True)
tree_diff = BST(BSTNode(10, 10, None))
tree_diff.AddKeyValue(5, 5)
tree_diff.AddKeyValue(20, 20)
print("  Разные деревья?", tree.IsIdenticalTrees(tree_diff) == False)

# Тест 2*

paths1 = tree.Paths(1)
print("Путей длины 1?", len(paths1) == 0)
paths2 = tree.Paths(2)
print("Путей длины 2?", len(paths2) == 4)
paths3 = tree.Paths(3)
print("Путей длины 3?", len(paths3) == 0)
# 3. Тест 3*
print("количечство максимальных путей", tree.CountMaxSumPaths() == 1)
# Дерево с двумя максимальными путями
root2 = BSTNode(10, 10, None)
left = BSTNode(20, 20, root2)
root2.LeftChild = left
left.LeftChild = BSTNode(5, 5, left)
right = BSTNode(20, 20, root2)
root2.RightChild = right
right.RightChild = BSTNode(5, 5, right)
tree2 = BST(root2)
print("Два макс пути?", tree2.CountMaxSumPaths() == 2)

# 4. Тест 4*

sym = BST(BSTNode(10, 10, None))
sym.Root.LeftChild = BSTNode(5, 5, sym.Root)
sym.Root.RightChild = BSTNode(5, 5, sym.Root)
print("Симметричное?", sym.SymmTrees() == True)
# Несимметричное
non_sym = BST(BSTNode(10, 10, None))
non_sym.AddKeyValue(5, 5)
non_sym.AddKeyValue(15, 15)
print("Несимметричное?", non_sym.SymmTrees() == False)