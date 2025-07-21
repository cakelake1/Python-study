def PatternUnlock(N, hits):
    dictionary_coordinate = {
            6: (0,0), 1: (0,1), 9: (0,2),
            5: (1,0), 2: (1,1), 8: (1,2),
            4: (2,0), 3: (2,1), 7: (2,2)
            }
    coordinates = []
    for numbers in hits:
        coordinates.append(dictionary_coordinate[numbers])
    not_formatted_result =  0.0
    for i in range(1,N):
        c0 = coordinates[i-1]
        c1 = coordinates[i]
        dx = c0[0] - c1[0]
        dy = c0[1] - c1[1]
        path_on_phone = (dx*dx + dy*dy) ** 0.5
        not_formatted_result = not_formatted_result + path_on_phone
    not_formatted_result = round(not_formatted_result,5)
    s = format(not_formatted_result, '.5f') 
    result = s.rstrip('0').rstrip('.') 
    return result

