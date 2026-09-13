from task_11 import SimpleGraph
from task_11_2 import (
    FindFarthestWay, FindAllresult,
    _first_vertex, _bfsFarthest, _bfsFarthestRec
)

SimpleGraph.FindFarthestWay = FindFarthestWay
SimpleGraph.FindAllresult = FindAllresult
SimpleGraph._first_vertex = _first_vertex
SimpleGraph._bfsFarthest = _bfsFarthest
SimpleGraph._bfsFarthestRec = _bfsFarthestRec


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
path = graph.BreadthFirstSearch(0, 5)
print("полный путь", end=" ")
if path:
    print(','.join(str(v.Value) for v in path))
else:
    print("[]")
print(graph.FindFarthestWay())
print(graph.FindAllresult())

# Граничные случаи
    # совпадение вершин
path = graph.BreadthFirstSearch(0, 0)
print("один путь", end=" ")
if path:
    print(','.join(str(v.Value) for v in path))
else:
    print("[]")
print(graph.FindFarthestWay())
print(graph.FindAllresult())

    # вершины не существуют
graph = SimpleGraph(5)
graph.AddVertex(10)
graph.AddVertex(20)
print(graph.BreadthFirstSearch(0, 2))
print(graph.BreadthFirstSearch(5, 0))
print(graph.FindFarthestWay())
print(graph.FindAllresult())

# тест связный граф
    # граничные случаи
        # пустой граф
graph = SimpleGraph(3)
print(graph.FindFarthestWay())
print(graph.FindAllresult())

        # граф с одной вершиной
graph = SimpleGraph(3)
graph.AddVertex(1)
print(graph.FindFarthestWay())
print(graph.FindAllresult())

        # граф с изолированной вершиной
graph = SimpleGraph(3)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddEdge(0, 1)
print(graph.FindFarthestWay())
print(graph.FindAllresult())

        # граф с вершинами, но без рёбер (все изолированы)
graph = SimpleGraph(4)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
print(graph.FindFarthestWay())
print(graph.FindAllresult())

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
print(graph.FindFarthestWay())
print(graph.FindAllresult())

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
print(graph.FindFarthestWay())
print(graph.FindAllresult())

    # несвязный граф
graph = SimpleGraph(5)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)
graph.AddEdge(0, 1)
graph.AddEdge(2, 3)
print(graph.FindFarthestWay())
print(graph.FindAllresult())