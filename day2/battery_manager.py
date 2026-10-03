def check_battery(battery):
    if battery >= 50:
        print(f"배터리{battery} -> 정상")
    elif 20 <= battery < 50:
        print(f"배터리{battery} -> 주의")
    else:
        print(f"배터리{battery} -> 충전필요")

def show_summary(batteries):
    print(f"측정 횟수: {len(batteries)}")
    print(f"최고 배터리: {max(batteries)}")
    print(f"최저 배터리: {min(batteries)}")
    print(f"평균 배터리: {(sum(batteries))/(len(batteries)):.1f}")


batteries = [80, 45, 15]

for battery in batteries:
    check_battery(battery)

show_summary(batteries)

