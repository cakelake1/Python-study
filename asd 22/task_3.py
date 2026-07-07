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
        if self.Root is None:
            return BSTFind()
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
    
    def WideAllNodes(self):
        result = []
        list_que = [self.Root]
        index = 0
        while index < len(list_que):
            node = list_que[index]
            index += 1
            result.append(node)
            if node.LeftChild is not None:
                list_que.append(node.LeftChild)
            if node.RightChild is not None:
                list_que.append(node.RightChild)
        return result

    def DeepAllNodes(self, order):
        result = []
        self.recirsive_deep(self.Root, order, result)
        return result
    def recirsive_deep(self, node, order, result):
        if node is None:
            return
        if order == 2:
            result.append(node)
        self.recirsive_deep(node.LeftChild, order,result)
        if order ==0:
            result.append(node)
        self.recirsive_deep(node.RightChild, order, result)
        if order == 1:
            result.append(node)
        
