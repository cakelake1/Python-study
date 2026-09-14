from itertools  import combinations
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
    def _vertex_unvisited(self):
        for v in self.vertex:
            if v is not None:
                v.Hit = False
    def WeakVertices(self):
        weak_vertices = []
        for i, node in enumerate(self.vertex):
            if not node:
                continue
            if self._is_vertice_weak(i):
                weak_vertices.append(node)
        return weak_vertices
    def _is_vertice_weak(self, weak):
        result = []
        for i, j in enumerate(self.m_adjacency[weak]):
            if i == weak:
                continue
            if j == 1:
                result.append(i)
        result_combinations = combinations(result, 2)
        for row, column in result_combinations:
            if self.m_adjacency[row][column]:
                return False
        return True    