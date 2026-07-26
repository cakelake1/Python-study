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
        self.Root = self.rec_build(0, len(s_a) - 1,None, s_a)
    def rec_build(self,left,right,parent,s_a):
        if left > right:
            return None
        mid = (left + right) // 2
        idx_mid = s_a[mid]
        node = BSTNode(idx_mid, parent)
        if parent is None:
            node.Level = 0
        else:
            node.Level = parent.Level + 1
        node.LeftChild = self.rec_build(left, mid - 1, node,s_a)
        node.RightChild = self.rec_build(mid + 1, right, node, s_a)
        return node
        
    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        return self.rec_balance(root_node) != -1
    def rec_balance(self,node):
        if node  is None:
            return 0
        left_side = self.rec_balance(node.LeftChild)
        if left_side == -1:
            return -1
        right_side = self.rec_balance(node.RightChild)
        if right_side == -1:
            return -1
        if abs(left_side - right_side) > 1:
            return -1
        result = 1 + max(left_side, right_side)
        return result
        