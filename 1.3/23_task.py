def TreeOfLife(H, W, N, tree):
    tree_matrix = [[0]*W for _ in range(H)] # Заполняем матрицу нулями
    for i in range(H): 
        for j in range(W):
            if tree[i][j] == '+':
                tree_matrix[i][j] = 1
            else: tree_matrix[i][j] = 0
    for year in range(1, N+1):
        if year % 2 == 1:
            for i in range(H):
                for j in range(W):
                    if tree_matrix[i][j] == 0:
                        tree_matrix[i][j] = 1
                    else:
                        tree_matrix[i][j] +=1
        else: 
            for i in range(H):
                for j in range(W):
                    if tree_matrix[i][j] > 0:
                        tree_matrix[i][j] += 1
            boom_matrix = [[False]*W for _ in range(H)] # создаем матрицу на пометки для удаления
            for i in range(H):
                for j in range(W):
                    if tree_matrix[i][j] >= 3:
                        boom_matrix[i][j] = True
                        if i > 0:
                            boom_matrix[i-1][j] = True
                        if i < H - 1:
                            boom_matrix[i+1][j] = True
                        if j > 0:
                            boom_matrix[i][j-1] = True
                        if j < W - 1:
                            boom_matrix[i][j+1] = True
            for i in range(H):
                for j in range(W):
                    if boom_matrix[i][j]: # True or False
                        tree_matrix[i][j] = 0
    result = []
    for i in range(H):
        s = ''
        for j in range(W):
            if tree_matrix[i][j] == 0:
                s +='.'
            else:
                s +='+'
        result.append(s)
    return result

