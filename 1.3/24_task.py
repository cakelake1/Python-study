def MatrixTurn(Matrix, M, N, T):
    matrix_list = [list(s) for s in Matrix]
    K = min(M, N) // 2
    for k in range(K):
        ring = []
        for j in range(k, N - k):
            ring.append(matrix_list[k][j])
        for i in range(k + 1, M - k - 1):
            ring.append(matrix_list[i][N - k - 1])
        for j in range(N - k - 1, k - 1, -1):
                ring.append(matrix_list[M - k - 1][j])
        for i in range(M - k - 2, k, -1):
                ring.append(matrix_list[i][k])
        L = len(ring)
        t = T % L
        if t == 0:
            continue
        new_ring = ring[L - t:] + ring[:L - t]
        index = 0
        for j in range(k, N - k):
            matrix_list[k][j] = new_ring[index]
            index += 1
        for i in range(k + 1, M - k - 1):
            matrix_list[i][N - k - 1] = new_ring[index]
            index += 1
        for j in range(N - k - 1, k - 1, -1):
                matrix_list[M - k - 1][j] = new_ring[index]
                index += 1
        for i in range(M - k - 2, k, -1):
                matrix_list[i][k] = new_ring[index]
                index += 1
    for i in range(M):
        Matrix[i] = ''.join(matrix_list[i])
