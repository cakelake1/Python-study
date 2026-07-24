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
        self.Root = rec_build(0 len(s_a) - 1, None)
    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        def rec_balance(node):
            if node  is None:
                return -1
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
        return rec_balance(root_node) != -1 # сбалансировано ли дерево с корнем root_node