def calculate_speed(distance):
    if distance > 70:
        return 10
    elif 30 < distance <=70:
        return 5
    else : 
        return 0


distances = [100, 60, 25, 90]

for distance in distances:
    speed = calculate_speed(distance)
    
    print(f"거리 {distance}cm -> {speed}")

    if speed == 0:
            print("장애물 발견! 정지")
            break
    