name = input("로봇 이름을 입력하세요: ")

print(f"로봇 이름은 {name}입니다")

##########################################

distance = int(input("현재 거리를 입력하세요: "))

print(f"현재 거리: {distance}cm")

if distance > 70:
    print("전진")
elif 30 < distance <= 70:
    print("감속")
else:
    print("정지")
