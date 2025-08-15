def Unmanned(L, N, track):
    cur_time = 0 
    prev_time = 0 
    for position,r,g in track:
        if position > L:
            continue
        cur_time += position - prev_time 
        prev_time = position 
        traffic_lights = r + g
        if traffic_lights == 0:
            continue 
        time = cur_time % traffic_lights 
        if time < r: 
            cur_time += r - time 
    result = L - prev_time + cur_time   
    return result
