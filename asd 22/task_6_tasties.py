class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        if not a:
            self.Root = None
            return
        s_a = sorted(a)
        def rec_build(left,right,parent):
            if left > right:
                return None
            mid = (left + right) // 2
            idx_mid = s_a[mid]
            node = BSTNode(idx_mid, parent)
            if parent is None:
                node.Level = 0
            else:
                node.Level = parent.Level + 1
            node.LeftChild = rec_build(left, mid - 1, node)
            node.RightChild = rec_build(mid + 1, right, node)
            return node
        self.Root = rec_build(0, len(s_a) - 1, None)
    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        def rec_balance(node):
            if node  is None:
                return 0
            left_side = rec_balance(node.LeftChild)
            if left_side == -1:
                return -1
            right_side = rec_balance(node.RightChild)
            if right_side == -1:
                return -1
            if abs(left_side - right_side) > 1:
                return -1
            result = 1 + max(left_side, right_side)
            return result
        return rec_balance(root_node) != -1
    
    def IsCorrectTree(self, root_node):
        if root_node is None:
            return True
        def rec_check(node):
            if node is None:
                return True
            if node.LeftChild is not None and node.LeftChild.NodeKey > node.NodeKey:
                    return False
            if node.RightChild is not None and node.RightChild.NodeKey < node.NodeKey:
                    return False
            left_side = rec_check(node.LeftChild)
            right_side = rec_check(node.RightChild)
            return left_side and right_side
        return rec_check(root_node)
    
    def IsBalancdeCorrect(self, root_node):
        if root_node is None:
            return True
        def get_depthTree(node):
            if node is None:
                return 0
            left_side = get_depthTree(node.LeftChild)
            right_side = get_depthTree(node.RightChild)
            result = 1 + max(left_side, right_side)
            return result
        left_depth = get_depthTree(root_node.LeftChild)
        right_depth = get_depthTree(root_node.RightChild)
        if abs(left_depth - right_depth) > 1:
            return False
        if not self.IsBalanced(root_node.LeftChild):
            return False
        if not self.IsBalanced(root_node.RightChild):
            return False
        return True

tree = BalancedBST()
# граничные значения - пустой массив и отрицательные значения
tree.GenerateTree([])
print(tree.Root, end=" ")  
print(tree.IsBalanced(tree.Root)) 
tree.GenerateTree([0, -5, 5, -10, -3, 3, 10])
print(tree.Root.NodeKey, end=" ")  
print(tree.Root.LeftChild.NodeKey, end=" ")  
print(tree.Root.RightChild.NodeKey, end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey, end=" ")  
print(tree.Root.LeftChild.RightChild.NodeKey, end=" ")  
print(tree.Root.RightChild.LeftChild.NodeKey, end=" ")  
print(tree.Root.RightChild.RightChild.NodeKey, end=" ")  
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание   
# 0,1,2 глубина
tree.GenerateTree([42])
print(tree.Root.NodeKey,end=" ") 
print(tree.Root.Level, end=" ")
print(tree.Root.LeftChild, end=" ")
print(tree.Root.RightChild, end=" ")
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalanced(tree.Root))
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([10, 5, 15])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.Level,end=" ")
print(tree.Root.RightChild.Level,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([50, 25, 75, 12, 37, 62, 87])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание
# без сортировки
tree.GenerateTree([10, 5, 15, 3, 7, 12, 18])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание 
# дубликаты и одинаковые значения
tree.GenerateTree([3, 1, 3, 2, 1, 2, 3])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.LeftChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
tree.GenerateTree([5, 5, 5, 5, 5])
print(tree.Root.NodeKey,end=" ")
print(tree.Root.LeftChild.NodeKey,end=" ")
print(tree.Root.RightChild.NodeKey,end=" ")
print(tree.Root.LeftChild.RightChild.NodeKey,end=" ")
print(tree.Root.RightChild.RightChild.NodeKey,end=" ")
print(tree.IsBalanced(tree.Root))
print(tree.IsCorrectTree(tree.Root))  # 2* задание 
print(tree.IsBalancdeCorrect(tree.Root))  # 3* задание  
# проверка несбаланисрованного дерева
root = BSTNode(5, None)
root.LeftChild = BSTNode(3, root)
root.LeftChild.LeftChild = BSTNode(2, root.LeftChild)
root.LeftChild.LeftChild.LeftChild = BSTNode(1, root.LeftChild.LeftChild)
print(tree.IsBalanced(root))
print(tree.IsCorrectTree(root)) # 2* задание  
print(tree.IsBalancdeCorrect(root))  # 3* задание  