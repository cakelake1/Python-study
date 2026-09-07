from task_10 import (SimpleGraph)
from task_10_2 import dfs_connected, IsConnected, LongestPath, dfs_longest_path
SimpleGraph.dfs_connected = dfs_connected
SimpleGraph.IsConnected = IsConnected
SimpleGraph.dfs_longest_path = dfs_longest_path
SimpleGraph.LongestPath = LongestPath
# полный путь
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