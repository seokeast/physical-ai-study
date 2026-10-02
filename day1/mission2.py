def check_battery(battery):

    if battery >= 50:
        return "정상"

    elif 20 <= battery < 50:
        return "주의"

    elif battery < 20:
        return "충전 필요"

result = check_battery(35)
print(result)