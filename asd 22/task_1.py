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
        self.UpdateLevelNode(NewChild, ParentNode.Level + 1)
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