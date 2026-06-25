class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        #if ParentNode is None:
            #return False
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        return True # ваш код добавления нового дочернего узла существующему ParentNode
  
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        pass # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        #if self.Root is None:
            #return []
        result = []
        def GetAllNodesRec(node):
            result.append(node)
            for i in node.Children:
                GetAllNodesRec(i)
        GetAllNodesRec(self.Root)
        return result
        # ваш код выдачи всех узлов дерева в определённом порядке

    def FindNodesByValue(self, val):
        #if self.Root is None:
            #return []
        result = []
        def FindNodesByValueRec(node):
            if node.NodeValue == val:
                result.append(node)
            for i in node.Children:
                FindNodesByValueRec(i)
        FindNodesByValueRec(self.Root)
        # ваш код поиска узлов по значению
        return result
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode) 
        # в качестве дочернего для узла NewParent
        pass  
   
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