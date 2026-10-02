def check_battery(battery):

    if battery >= 50:
        return "정상"

    elif 20 <= battery < 50:
        return "주의"

    else:
        return "충전 필요"


batteries = []

while True:

    try:
        battery = int(input("배터리 값을 입력하세요: "))

    except:
        print("숫자를 입력해주세요.")
        continue

    if battery < 0 or battery > 100:
        print("0~100 사이 값을 입력해주세요.")
        continue

    if battery == 0:
        print("프로그램 종료")
        break

    batteries.append(battery)

    result = check_battery(battery)

    print(f"배터리 {battery} -> {result}")


if len(batteries) > 0:

    average = sum(batteries) / len(batteries)

    print(f"입력한 배터리: {batteries}")
    print(f"측정 횟수: {len(batteries)}")
    print(f"최고 배터리: {max(batteries)}")
    print(f"최저 배터리: {min(batteries)}")
    print(f"평균 배터리: {average:.1f}")

else:
    print("측정된 배터리 값이 없습니다.")