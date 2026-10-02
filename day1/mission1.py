def robot_status(speed):

    if speed == 0:
        print("정지")

    elif 1 <= speed <= 5:
        print("저속")

    else:
        print("주행중")


robot_status(10)