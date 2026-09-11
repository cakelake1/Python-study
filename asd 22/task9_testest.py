class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val 
        self.Parent = parent 
        self.Children = [] 
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root 
	
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        return True 
    
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        result = []
        def GetAllNodesRec(node):
            result.append(node)
            for i in node.Children:
                GetAllNodesRec(i)
        GetAllNodesRec(self.Root)
        return result

    def FindNodesByValue(self, val):
        result = []
        def FindNodesByValueRec(node):
            if node.NodeValue == val:
                result.append(node)
            for i in node.Children:
                FindNodesByValueRec(i)
        FindNodesByValueRec(self.Root)
        return result
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode) 
   
    def Count(self):
        TreeNodes = self.GetAllNodes()
        return len(TreeNodes)

    def LeafCount(self):
        leaves = 0
        nodes = self.GetAllNodes()
        for node in nodes:
            if not node.Children:
                leaves += 1
        return leaves
    def EvenTrees(self):
        result = []
        even = self.CountTrees(self.Root, result)
        if even % 2 != 0:
               return []
        return result
    def CountTrees(self,node, result):
        count = 1 
        for child in node.Children:
            count += self.CountTrees(child, result)
        if count % 2 == 0 and node.Parent is not None:
               result.append(node.Parent)
               result.append(node)
        return count
# Дерево с 6 вершинами    
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
# Подсчёт вершин
print(tree.Count(), end=" ")
edges = tree.EvenTrees()
print(len(edges), end=" ")
if len(edges) >= 2:
    print(edges[0].NodeValue, end=" ")
    print(edges[1].NodeValue)

# граничные случаи, 1 вершина и 0 вершин
root = SimpleTreeNode(10, None)
tree = SimpleTree(root)
result = []
print(tree.CountTrees(root, result))
root = SimpleTreeNode(None, None)
tree = SimpleTree(root)
result = []
print(tree.CountTrees(root, result))
result = []
# дерево с 2 вершинами
root = SimpleTreeNode(1, None)
tree = SimpleTree(root)
node2 = SimpleTreeNode(2, root)
root.Children = [node2]




