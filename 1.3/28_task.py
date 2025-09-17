def Keymaker(k):
    doors = ["0"] * k
    for i in range(1, k + 1):
        for j in range(i - 1, k , i):
            if doors[j] == '0':
                doors[j] = '1'
            else:
                doors[j] = '0'