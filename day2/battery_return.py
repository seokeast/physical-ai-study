def check_battery(battery):
    if battery >= 50:
        return "정상"
    elif 20 <= battery < 50:
        return "주의"
    else:
        return "충전필요"


batteries = [80, 45, 15]

for battery in batteries:
    result = check_battery(battery)
    print(f"배터리 {battery} -> {result}")