def TankRush(H1, W1, S1, H2, W2, S2):
    map1 = [list(s) for s in S1.split()]
    map2 = [list(s) for s in S2.split()]
    
    print("Main map:")
    for row in map1:
        print(row)
    
    print("\nPattern map:")
    for row in map2:
        print(row)
    
    if H2 > H1 or W2 > W1:
        print("\nPattern larger than main map")
        return False
        
    if H2 == 0 or W2 == 0:
        print("\nEmpty pattern")
        return True
        
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            print(f"\nChecking position: ({i}, {j})")
            match = True
            
            for k in range(H2):
                substr = map1[i+k][j:j+W2]
                pattern = map2[k]
                
                print(f"  Row {k}:")
                print(f"    Substring: {substr}")
                print(f"    Pattern:   {pattern}")
                
                if substr != pattern:
                    match = False
                    print(f"    Mismatch at row {k}")
                    break
                    
            if match: 
                print("  FULL MATCH!")
                return True
                
    print("\nNo matches found")
    return False

# Тестовый вызов
print(TankRush(4, 4, "1234 5678 9012 3456", 2, 2, "78 01"))
print(TankRush(4, 4, "1234 5678 9012 3456", 2, 2, "78 01")) # True (искомая карта с позиции (1,2))
print(TankRush(4, 4, "1234 5678 9012 3456", 2, 2, "78 01"))  # True
print(TankRush(4, 4, "1234 5678 9012 3456", 2, 2, "78 01"))  # True