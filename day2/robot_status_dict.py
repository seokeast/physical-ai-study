robot = {
    "name": "R1",
    "battery": 45,
    "speed": 5
}

print(f"로봇 이름: {robot['name']}")
print(f"배터리: {robot['battery']}")
print(f"속도: {robot['speed']}")

battery = robot['battery']

if battery >= 50:
    print("정상")
elif 20 <= battery < 50:
    print("주의")
else:
    print("충전 필요")
