# batteries = [80, 45, 15]
# 각 배터리 값을 check_battery() 함수에 넣어서 아래처럼 출력해.
# 배터리 80 → 정상
# 배터리 45 → 주의
# 배터리 15 → 충전 필요
# 50 이상 → "정상"
# 20 이상 50 미만 → "주의"
# 20 미만 → "충전 필요"

def check_battery(battery):

    if battery >= 50:
        return "정상"

    elif 20 <= battery < 50:
        return "주의"

    else:
        return "충전 필요"

batteries = [80, 45, 15]

for battery in batteries:
    result = check_battery(battery)
    print(f"배터리 {battery} → {result}")