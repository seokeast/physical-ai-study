def calculate_speed(distance):
    if distance > 70:
        return 10
    elif 30 < distance <=70:
        return 5
    else : 
        return 0


distances = [100, 60, 40, 25, 90]
speeds = []

for distance in distances:
    speed = calculate_speed(distance)
    speeds.append(speed)
    
    print(f"거리 {distance}cm -> {speed}")

    if speed == 0:
            print("장애물 발견! 정지")
            break

print(f"주행 속도 기록: {speeds} ")
    