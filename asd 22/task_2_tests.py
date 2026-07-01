class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        result = BSTFind()
        if self.Root is None:
            return result

        cur_node = self.Root
        while cur_node:
            if key == cur_node.NodeKey:
                result.Node = cur_node
                result.NodeHasKey = True
                return result
            elif key < cur_node.NodeKey:
                if cur_node.LeftChild:
                    cur_node = cur_node.LeftChild
                else:
                    result.Node = cur_node
                    result.NodeHasKey = False
                    result.ToLeft = True
                    return result
            else: 
                if cur_node.RightChild:
                    cur_node = cur_node.RightChild
                else:
                    result.Node = cur_node
                    return result
        return None   


    def AddKeyValue(self, key, val):
        #if self.Root is None:
            #self.Root = BSTNode(key, val, None)
            #return True

        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False
        new_node = BSTNode(key, val, result.Node)
        if result.ToLeft:
            result.Node.LeftChild = new_node
        else:
            result.Node.RightChild = new_node
        return True
  
    def FinMinMax(self, FromNode, FindMax):    
        # Поиск минимального (FindMax=False) или максимального (FindMax=True) ключа
        #в поддереве, начиная с узла FromNode.
        #Возвращает найденный узел.
            #if FromNode is None:
             #   return None
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
        # удаляем узел по ключу
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
print("Мин от корня -> 2?", tree.FinMinMax(tree.Root, False).NodeKey == 2)
print("Макс от корня -> 18?", tree.FinMinMax(tree.Root, True).NodeKey == 18)
print("Мин от правого поддерева (15) -> 12?", tree.FinMinMax(tree.Root.RightChild, False).NodeKey == 12)
print("Макс от левого поддерева (5) -> 8?", tree.FinMinMax(tree.Root.LeftChild, True).NodeKey == 8)

# Тест 8: удаление листа (2)
tree.DeleteNodeByKey(2)
r = tree.FindNodeByKey(2)
print("2 удалён?", r.NodeHasKey == False)

# Тест 9: удаление с одним потомком (сначала убьём 12, чтобы у 15 остался только 18)
tree.DeleteNodeByKey(12)
tree.DeleteNodeByKey(15)
r = tree.FindNodeByKey(15)
print("15 удалён?", r.NodeHasKey == False)
print("18 теперь прямо под корнем?", tree.Root.RightChild.NodeKey == 18 and tree.Root.RightChild.Parent == tree.Root)

tree.DeleteNodeByKey(5)
r = tree.FindNodeByKey(5)
print("5 удалён?", not r.NodeHasKey)
# Проверяем, что на место 5 встал минимальный из правого поддерева (7)
print("На месте 5 теперь 7?", tree.Root.LeftChild.NodeKey == 7)
print("Левый потомок 7 = 3?", tree.Root.LeftChild.LeftChild.NodeKey == 3)
print("Правый потомок 7 = 8?", tree.Root.LeftChild.RightChild.NodeKey == 8)

# Тест 11: удаление отсутствующего
print("Удаление 999 вернуло False?", tree.DeleteNodeByKey(999) == False)

# Тест 12: удаление из пустого
empty2 = BST(None)
print("Удаление из пустого вернуло False?", empty2.DeleteNodeByKey(42) == False)