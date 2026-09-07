class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return i
        return -1
	
    def RemoveVertex(self, v):
        if not self.is_good_Vertex(v):
            return False
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0
        return True
        # ваш код удаления вершины со всеми её рёбрами
	
    def IsEdge(self, v1, v2):
        if not self.are_good_Vertics(v1, v2):
            return False
        if self.m_adjacency[v1][v2] == 1:
            return True
        return False
        # True если есть ребро между вершинами v1 и v2
	
    def AddEdge(self, v1, v2):
        if not self.are_good_Vertics(v1, v2):
                    return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True
        # добавление ребра между вершинами v1 и v2
	
    def RemoveEdge(self, v1, v2):
        if not self.are_good_Vertics(v1, v2):
                    return False        
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return True
        # удаление ребра между вершинами v1 и v2
    def is_good_Vertex(self, v):
        if v < 0 or v >= self.max_vertex or self.vertex[v] is None:
            return False
        return True
    def are_good_Vertics(self, v1, v2):
        return self.is_good_Vertex(v1) and self.is_good_Vertex(v2)
    def DepthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        if not self.is_good_Vertex(VFrom) or not self.is_good_Vertex(VTo):
            return []
        stack_vertex = []
        if self.dfs(VFrom, VTo, stack_vertex):
            return [self.vertex[idx] for idx in stack_vertex]
        return []
    def dfs(self, cur, tar, stack_vertex):
        self.vertex[cur].Hit = True
        stack_vertex.append(cur)
        if cur == tar:
            return True
        for i in range(self.max_vertex):
            if self.m_adjacency[cur][i] == 0:
                continue
            if self.vertex[i].Hit:
                continue
            if self.dfs(i, tar, stack_vertex):
                return True
        stack_vertex.pop()
        return False
    def dfs_connected(self, v):
            self.vertex[v].Hit = True
            for i in range(self.max_vertex):
                if self.m_adjacency[v][i] == 1 and not self.vertex[i].Hit:
                    self.dfs_connected(i)
    def IsConnected(self):
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        start = -1
        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                start = i
                break
        if start == -1:
            return True
        self.dfs_connected(start)
        for v in self.vertex:
            if v is not None and not v.Hit:
                return False
        return True

    def LongestPath(self):
        max_path = 0
        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                visited = [False] * self.max_vertex
                path_length = self.dfs_longest_path(i, visited)
                max_path = max(max_path, path_length)
        
        return max_path
    def dfs_longest_path(self, curr, visited):
        visited[curr] = True
        max_len = 0
        for nearby in range(self.max_vertex):
            if self.m_adjacency[curr][nearby] > 0 and not visited[nearby]:
                if self.vertex[nearby] is not None:
                    path_len = self.dfs_longest_path(nearby, visited)
                    max_len = max(max_len, path_len)
        visited[curr] = False
        return max_len + 1
#from task_10 import (SimpleGraph)
# тест *10.1 связный граф
    # граничные случаи
        #пустой граф
graph = SimpleGraph(6)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)
graph.AddVertex(6)
graph.AddEdge(0, 1)
graph.AddEdge(0, 2)
graph.AddEdge(1, 3)
graph.AddEdge(2, 3)
graph.AddEdge(3, 4)
graph.AddEdge(4, 5)  
path = graph.DepthFirstSearch(0, 5)
print("полный путь", end=" ")
if path:
    print(','.join(str(v.Value) for v in path))
else:
    print("[]")
print(graph.LongestPath())
# Граничные случаи
    # совпадение вершин
path = graph.DepthFirstSearch(0, 0)
print("один путь", end=" ")
if path:
    print(','.join(str(v.Value) for v in path))
else:
    print("[]")
print(graph.LongestPath())
    #вершины не существуют
graph = SimpleGraph(5)
graph.AddVertex(10)
graph.AddVertex(20)
print(graph.DepthFirstSearch(0, 2))
print(graph.DepthFirstSearch(5, 0))
print(graph.LongestPath())
# тест *10.1 связный граф
    # граничные случаи
        #пустой граф
graph = SimpleGraph(3)
print(graph.IsConnected())
print(graph.LongestPath())
        #граф с одной вершиной
graph = SimpleGraph(3)
graph.AddVertex(1)
print(graph.IsConnected())
print(graph.LongestPath())
        #граф с изолированной вершиной
graph = SimpleGraph(3)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddEdge(0, 1)
print(graph.IsConnected())
print(graph.LongestPath())
        #граф с вершинами, но без рёбер (все изолированы)
graph = SimpleGraph(4)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
print(graph.IsConnected())
print(graph.LongestPath())
# обычные тесты
    # связный граф
graph = SimpleGraph(4)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddEdge(0, 1)
graph.AddEdge(1, 2)
graph.AddEdge(2, 3)
print(graph.IsConnected())
print(graph.LongestPath())
    # связный граф с циклом
graph = SimpleGraph(4)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddEdge(0, 1)
graph.AddEdge(1, 2)
graph.AddEdge(2, 3)
graph.AddEdge(3, 0)
print(graph.IsConnected())
print(graph.LongestPath())
    # несвязный граф
graph = SimpleGraph(5)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)
graph.AddEdge(0, 1)   
graph.AddEdge(2, 3)   
print(graph.IsConnected())
print(graph.LongestPath())


