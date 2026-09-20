distances = [100, 75, 45, 25, 10]

for distance in distances:
    print(f"현재거리: {distance}cm")
    if distance <= 30:
        print("장애물 발견! 정지")
        break