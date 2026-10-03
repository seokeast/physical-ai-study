def calculate_speed(distance):
    if distance > 70:
        return 10
    elif 30 < distance <=70:
        return 5
    else : 
        return 0


distances = [100, 60, 25]

for distance in distances:
    result = calculate_speed(distance)
    print(f"거리 {distance}cm -> 속도 {result}")