# Рефлексия по задаче *8.2 Направленный граф, представленный матрицей смежности.
# что нужно сделать из рекомендаций:
# нужно сделать матрицу ассиметричной - оставить только верхнюю треугольную часть.
# обнулить диагональ и нижнюю часть
# инициализировать все вершины как непосещенные и проставить флаг боработана.
# добавить метод на проверку циклов
# добавить метод на выделение верхней треугольной части.
def get_up_part_triangle(self):
        for i in range(self.max_vertex):
            for j in range(self.max_vertex):
                if i >= j:
                    self.m_adjacency[i][j] = 0
def dfs(self, k, state):
        state[k] = 1
        for l in range(self.max_vertex):
            if self.m_adjacency[k][l] == 1 and self.vertex[l] is not None:
                if state[l] == 1:
                    return True
                if state[l] == 0 and self.dfs(l, state):
                    return True
        state[k] = 2
        return False
def has_cycles(self):
    state = [0] * self.max_vertex
    for k in range(self.max_vertex):
        if self.vertex[k] is not None and state[k] == 0:
            if self.dfs(k, state):
                return True
    return False

# *10.1 Добавьте метод, проверяющий, будет ли текущий неориентированный граф связным
# Если в задании подразумевается основной DFS, то у меня чуть чуть некорректно выполнено. Проверить смогу в последующих рекомендациях.
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


# *10.2 В ориентированном графе найдите длину самого длинного простого пути/

