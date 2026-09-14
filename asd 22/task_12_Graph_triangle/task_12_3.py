from task_12 import SimpleGraph
from task_12_2 import CountTriangles, _count_triangles_recursive, NoOneWeakVertices
SimpleGraph.CountTriangles = CountTriangles
SimpleGraph._count_triangles_recursive = _count_triangles_recursive
SimpleGraph.NoOneWeakVertices = NoOneWeakVertices

#граничные случаи
    #пустой граф
g = SimpleGraph(5)
print(g.CountTriangles())
    #одна вершина
g = SimpleGraph(1)
g.AddVertex("A")
print(g.CountTriangles())
    #две вершины с ребром
g = SimpleGraph(2)
g.AddVertex("A")
g.AddVertex("B")
g.AddEdge(0, 1)
print(g.CountTriangles())
    #три вершины, нет ребра
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
print(g.CountTriangles())
    #удаление вершины у треугольника
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
g.RemoveVertex(2)
print(g.CountTriangles())
# один треугольник
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
print(g.CountTriangles())
# два треугольника
g = SimpleGraph(6)
for v in "ABCDEF":
    g.AddVertex(v)
g.AddEdge(0, 1); g.AddEdge(1, 2); g.AddEdge(0, 2)
g.AddEdge(3, 4); g.AddEdge(4, 5); g.AddEdge(3, 5)
print(g.CountTriangles())
# треугольников нет
g = SimpleGraph(4)
for v in "ABCD":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(2, 3)
print(g.CountTriangles())
# вершины в треуг.
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
weak = g.NoOneWeakVertices()
print(len(weak))
# треуг, своб.вершина 
g = SimpleGraph(4)
for v in "ABCD":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
g.AddEdge(2, 3)
weak = g.NoOneWeakVertices()
print([v.Value for v in weak])
# треуг и 2 из. вершины
g = SimpleGraph(5)
for v in "ABCDE":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
weak = g.NoOneWeakVertices()
print(sorted(v.Value for v in weak))
# *10.2 пустой граф
g = SimpleGraph(5)
weak = g.NoOneWeakVertices()
print(len(weak))
#одна вершина
g = SimpleGraph(1)
g.AddVertex("A")
weak = g.NoOneWeakVertices()
print(len(weak))
# три слабые вершины
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
weak = g.NoOneWeakVertices()
print(len(weak))
# удаление вершины
g = SimpleGraph(3)
for v in "ABC":
    g.AddVertex(v)
g.AddEdge(0, 1)
g.AddEdge(1, 2)
g.AddEdge(0, 2)
g.RemoveVertex(2)
weak = g.NoOneWeakVertices()
print(sorted(v.Value for v in weak))