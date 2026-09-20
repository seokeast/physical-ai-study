batteries = [100, 80, 60, 40, 20, 10]

for battery in batteries:
    print(battery)

    if battery >= 50:
        print("운행 가능")
    elif 20 <= battery < 50:
        print("주의")
    else:
        print("충전 필요")
