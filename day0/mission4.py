battery = 100

for i in range(5):
    print(f"{i+1}회차 배터리: {battery}")
    battery -= 20
    if battery <= 20:
        print("충전 필요")
        break