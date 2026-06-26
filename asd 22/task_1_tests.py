class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val 
        self.Parent = parent 
        self.Children = [] 
        self.Level = 0
	
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
        #if self.Root is None:
            #return []
        result = []
        def GetAllNodesRec(node):
            result.append(node)
            for i in node.Children:
                GetAllNodesRec(i)
        GetAllNodesRec(self.Root)
        return result

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
    
    def UpdateLevelNode(self, node, New_level):
        node.Level = New_level
        for i in node.Children:
            self.UpdateLevelNode(i, New_level + 1)


    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        self.UpdateLevelNode(NewChild, ParentNode.Level + 1)
        return True 
# Создаю
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
node7 = SimpleTreeNode(7, None)
print([c.NodeValue for c in node2.Children]) #[4,5]
tree.AddChild(node2, node7) # Тест на добавление узла - добавляю узел 7 к узлу 2
print([c.NodeValue for c in node2.Children]) # [4,5,7] - успешный

tree.DeleteNode(node4) # удаляю 4 узел
print([c.NodeValue for c in node2.Children]) # [5,7]
print()

all_nodes = tree.GetAllNodes()
all_values = [n.NodeValue for n in all_nodes]
print(all_values)  # список всех узлов
print()
# найти список подходящих узлов по заданному значению
found5 = tree.FindNodesByValue(5)
print(len(found5)) # Есть
found10 = tree.FindNodesByValue(10)
print(len(found10)) # нету - 0

print([c.NodeValue for c in node2.Children])   # 5 7
print([c.NodeValue for c in node3.Children])   # [6]
tree.MoveNode(node5, node3)
print([c.NodeValue for c in node2.Children])   # [7]
print([c.NodeValue for c in node3.Children])   # [6,5]тест: проверяем, что узел отсутствует там где был исходно и появился в новом мест


track_nodes = tree.Count()
leaves = tree.LeafCount()
print(track_nodes) #6(1,2,3,5,6,7)
print("Количество листьев:", leaves) #5,6,7 
print()

# тесты по доп заданию
tree.UpdateLevelNode(root, 0) # проставил уровни
for node in tree.GetAllNodes():
    print(f"Узел {node.NodeValue}, уровень {node.Level}") # сходится

