def TreeOfLife(H, W, N, tree):
    tree_matrix = [[0]*W for _ in range(H)] 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
            boom_matrix = [[False]*W for _ in range(H)] 
            for i in range(H):
                for j in range(W):
                    if tree_matrix[i][j] >= 3:
                        boom_matrix[i][j] = True
                        for dx, dy in directions:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < H and 0 <= nj < W:
                                boom_matrix[ni][nj] = True
            for i in range(H):
                for j in range(W):
                    if boom_matrix[i][j]:
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

