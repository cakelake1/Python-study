def TankRush(H1, W1, S1, H2, W2, S2):
    # Создаем матрицы символов
    map1 = [list(s.strip()) for s in S1.split() if s.strip()]
    map2 = [list(s.strip()) for s in S2.split() if s.strip()]
    
    if len(map1) != H1 or any(len(row) != W1 for row in map1):
        return False
    if len(map2) != H2 or any(len(row) != W2 for row in map2):
        return False
        
    # Поиск шаблона
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            match = True
            for k in range(H2):
                for l in range(W2):
                    if map1[i+k][j+l] != map2[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    print(f"map1: {map1}")
    print(f"map2: {map2}")
    print(f"H1={H1}, W1={W1}, H2={H2}, W2={W2}")
    for row in map1:
        print(f"Row length: {len(row)}")
    return False
print(TankRush(4, 4, "1234 5678 9012 3456", 2, 2, "78 01")) # True (искомая карта с позиции (1,2))