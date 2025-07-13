def ConquestCampaign(N, M, L, battalion):
    captured = [] 
    today_capture = [] 
    for i in range(0, 2 * L, 2):
        x = battalion[i] - 1
        y = battalion[i + 1] - 1
        if 0 <= x < N and 0 <= y < M and (x, y) not in captured:
            captured.append((x, y))
            today_capture.append((x, y))
    
    days = 0
    
    while today_capture:
        days = days + 1
        nextday_capture = []

        for x, y in today_capture:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in captured:
                    captured.append((nx, ny))
                    nextday_capture.append((nx, ny))

        today_capture = nextday_capture

    return days