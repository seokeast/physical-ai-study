def check_battery(battery):
    if battery >= 50:
        return "정상"
        
    elif 20 <= battery < 50:
        return "주의"
        
    else:
        return "충전 필요" 

while True:
    battery = int(input("배터리 값을 입력하세요: "))

    if battery == 0:
        print("프로그램 종료")
        break

    result = check_battery(battery)

    print(f"배터리 {battery} -> {result}")