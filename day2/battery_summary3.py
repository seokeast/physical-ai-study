def show_summary(batteries):
    print(f"측정 횟수: {len(batteries)}")
    print(f"최고 배터리: {max(batteries)}")
    print(f"최저 배터리: {min(batteries)}")
    print(f"평균 배터리: {(sum(batteries)/len(batteries)):.1f}")

batteries = [ 80, 45, 20]

show_summary(batteries)