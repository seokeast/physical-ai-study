def calculate_speed(distance):
    if distance > 70:
        return 10
    elif 30 < distance <=70:
        return 5
    else : 
        return 0


def show_summary(speeds):
     print(f"주행 횟수: {len(speeds)}")
     print(f"최고 속도: {max(speeds)}")
     print(f"최저 속도: {min(speeds)}")
     print(f"평균 속도: {(sum(speeds))/(len(speeds)):.1f}")


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

show_summary(speeds)