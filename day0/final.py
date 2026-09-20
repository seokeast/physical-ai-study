robot_name = input("로봇 이름을 입력하세요: ")
distances = []
count = 0

while True:
    distance = int(input("현재 거리를 입력하세요: "))
    
    distances.append(distance)
    count += 1

    print(f"{count}회차 거리입력:{distance}")
        
    if distance > 70:
        print(f"{robot_name} 전진")

    elif 30 < distance <= 70:
        print(f"{robot_name} 감속")

    else:
        print(f"{robot_name} 정지")
        print("장애물 발견! 프로그램 종료")
        break

print(f"측정한 거리들: {distances}")

count = 1 

for i in distances:
    print(f"{count}번째 측정값: {i}")
    count +=1