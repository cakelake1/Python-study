class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False 
        self.ToLeft = False 

class BST:

    def __init__(self, node):
        self.Root = node 

    def FindNodeByKey(self, key):
        result = BSTFind()
        if self.Root is None:
            return result
        return self.recursive_find(self.Root, key)
    def recursive_find(self, node, key):
        if key == node.NodeKey:
            result = BSTFind()
            result.Node = node
            result.NodeHasKey = True
            return result
        if key < node.NodeKey:
            if node.LeftChild is not None:
                return self.recursive_find(node.LeftChild, key)
            result = BSTFind()
            result.Node = node
            result.NodeHasKey = False
            result.ToLeft = True
            return result
        if node.RightChild is not None:
            return self.recursive_find(node.RightChild, key)
        result = BSTFind()
        result.Node = node
        result.NodeHasKey = False
        result.ToLeft = False
        return result
      


    def AddKeyValue(self, key, val):
        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False
        new_node = BSTNode(key, val, result.Node)
        if result.Node is None:
            self.Root = new_node
            return True
        if result.ToLeft:
            result.Node.LeftChild = new_node
        else:
            result.Node.RightChild = new_node
        return True
  
    def FinMinMax(self, FromNode, FindMax):    
        cur_node = FromNode
        while True:
            if FindMax:
                next_node = cur_node.RightChild
            else:
                next_node = cur_node.LeftChild
            if next_node is None:
                break
            cur_node = next_node
        return cur_node
	
    def DeleteNodeByKey(self, key):
        result = self.FindNodeByKey(key)
        if not result.NodeHasKey:
            return False
        node = result.Node
        if node.LeftChild is None and node.RightChild is None:
            parent = node.Parent
            if parent is None:
                self.Root = None
            else:
                if parent.LeftChild is node:
                    parent.LeftChild = None
                else:
                    parent.RightChild = None
            return True
        if node.LeftChild is None or node.RightChild is None:
            if node.LeftChild is not None:
                child = node.LeftChild
            else:
                child = node.RightChild
            parent = node.Parent
            if parent is None:
                self.Root = child
                child.Parent = None
            else:
                if parent.LeftChild is node:
                    parent.LeftChild = child
                else:
                    parent.RightChild = child
                child.Parent = parent
            return True
        min_right_key = self.FinMinMax(node.RightChild, False)
        node.NodeKey = min_right_key.NodeKey
        node.NodeValue = min_right_key.NodeValue
        parent_succ =  min_right_key.Parent
        if  min_right_key.RightChild is not None:
            child =  min_right_key.RightChild
            child.Parent = parent_succ
        else:
            child = None

        if parent_succ is None:
            self.Root = child
        else:
            if parent_succ.LeftChild is  min_right_key:
                parent_succ.LeftChild = child
            else:
                parent_succ.RightChild = child
        return True
           
    def Count(self):
        def recursive_count(node):
            if node is None:
                return 0
            result = recursive_count(node.LeftChild) + recursive_count(node.RightChild) + 1
            return result
        return recursive_count(self.Root)
    
tree = BST(None)   # или BST(), если поправили конструктор

print("--- Проверка добавления первого узла ---")
res = tree.AddKeyValue(42, "answer")
print("AddKeyValue вернул True?", res == True)
print("Корень не None?", tree.Root is not None)
print("Ключ корня = 42?", tree.Root.NodeKey == 42)
print("Значение корня = 'answer'?", tree.Root.NodeValue == "answer")
print("Левый потомок None?", tree.Root.LeftChild is None)
print("Правый потомок None?", tree.Root.RightChild is None)

found = tree.FindNodeByKey(42)
print("Поиск 42: NodeHasKey =", found.NodeHasKey)   # должно быть True

print("\n--- Проверка добавления второго узла ---")
tree.AddKeyValue(20, "left")
found2 = tree.FindNodeByKey(20)
print("Поиск 20: NodeHasKey =", found2.NodeHasKey)  # True
print("20 — левый потомок 42?", tree.Root.LeftChild is not None and tree.Root.LeftChild.NodeKey == 20)    
tree = BST(None)   # создаём пустое дерево (Root = None)

print("--- Проверка добавления первого узла ---")
res = tree.AddKeyValue(42, "answer")
print("AddKeyValue вернул True?", res == True)          # должно быть True
print("Корень не равен None?", tree.Root is not None)   # True
print("Ключ корня = 42?", tree.Root.NodeKey == 42)      # True
print("Значение корня = 'answer'?", tree.Root.NodeValue == "answer")  # True
print("Левый потомок корня None?", tree.Root.LeftChild is None)       # True
print("Правый потомок корня None?", tree.Root.RightChild is None)     # True


# новое дерево
tree = BST(BSTNode(10, 10, None))
tree.AddKeyValue(5, 5)
tree.AddKeyValue(15, 15)
tree.AddKeyValue(3, 3)
tree.AddKeyValue(7, 7)
tree.AddKeyValue(12, 12)
tree.AddKeyValue(18, 18)


"""# Тест 1*
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
sym.Root.LeftChild.LeftChild = BSTNode(3, 3, sym.Root.LeftChild)
sym.Root.LeftChild.RightChild = BSTNode(7, 7, sym.Root.LeftChild)
sym.Root.RightChild.LeftChild = BSTNode(7, 7, sym.Root.RightChild)
sym.Root.RightChild.RightChild = BSTNode(3, 3, sym.Root.RightChild)
print("Симметричные деревья?", sym.SymmTrees() == True)

non_sym = BST(BSTNode(10, 10, None))
non_sym.AddKeyValue(5, 5)"""