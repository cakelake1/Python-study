def MisterRobot(N, data):
    arr = list(data)
    for i in range(N):
        while arr[i] != i + 1:
            p = i
            while p < N and arr[p] != i + 1:
                p += 1
            if p == N:
                return False
            if p - i >= 2:
                arr[p-2], arr[p-1], arr[p] = arr[p-1], arr[p], arr[p-2]
            elif i < N - 2:
                arr[i], arr[i+1], arr[i+2] = arr[i+1], arr[i+2], arr[i]
            else:
                return False
    return True