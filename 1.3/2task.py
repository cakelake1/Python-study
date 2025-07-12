def odometer(oksana):
    full_speed = 0
    past_time = 0
    for i in range(len(oksana)):
        if i % 2 == 0: 
            speed = oksana[i]
            time = oksana[i + 1]
            full_speed = full_speed + speed * (time - past_time)
            past_time = time
    return full_speed