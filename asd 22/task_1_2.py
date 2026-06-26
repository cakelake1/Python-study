#Задания.

#1. Напишите метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
#Деревья очень "рекурсивны", наиболее удобно и правильно думать о них именно в парадигме рекурсивных вычислений [CS106B].
# Нужно добавить атрибут в наш класс, self.Level = 0

def GetLevelsNodes(self):
    def get_level(node,level):
        node.Level = level
        for i in node.Children:
            get_level(i, level + 1)
        get_level(self.Root)

#2. Придумайте, как лучше организовать поддержку уровня узлов без анализа всего дерева.
# Первое, что приходит в голову, это проаназилировать все дерово и узнать уровень узла, это нам запрещено, но не запрещено добавить рассчет уровня узла в каждый метод(который эти узлы затрагиватет)
# Это Addchild и MoveNode.
# Для этого добавим новый метод
# UpdateLevelNode
def UpdateLevelNode(self, node, New_level):
    node.Level = New_level
    for i in node.Children:
        self.UpdateLevelNode(i, New_level + 1)

# далее вызываем наш метод в Addchild и MoveNode.
def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        self.UpdateLevelNode(NewChild, ParentNode.Level + 1)
        return True 
# В метод MoveNode изменения вносить не нужно, так как там вызывается Addchild c методом UpdateLevelNode 


