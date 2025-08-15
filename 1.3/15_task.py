def TankRush(H1, W1, S1, H2, W2, S2):
    map1 = S1.split()
    map2 = S2.split()
    if H2 > H1 or W2 > W1:
        return False
    if H2 == 0 or W2 == 0:
        return True
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            match = True
            for k in range(H2):
                if map1[i+k][j:j + W2] != map2[k]:
                        match = False
                        break
            if match: 
                return True
    return False