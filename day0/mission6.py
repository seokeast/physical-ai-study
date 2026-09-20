distances = [100, 75, 45, 25, 10]

for distance in distances:
    print(f"현재거리: {distance}cm")

    if distance > 70:
        print("전진")
        distance = + 10
    elif 30 < distance <= 70 :
         print("감속")
         distance = + 5
    else:
        print("정지")
        distance = + 0