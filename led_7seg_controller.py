import variableAndContrants as env
import threading as cpu
import wiringpi as pi
import time

# bit 0 sẽ là bật dèn do chung Anote
# sap xem theo A B C D E F G
map_digital = [
    [0, 0, 0, 0, 0, 0, 1],  # hien thi so 0
    [1, 0, 0, 1, 1, 1, 1],  # hien thi so 1
    [0, 0, 1, 0, 0, 1, 0],  # hien thi so 2
    [0, 0, 0, 0, 1, 1, 0],  # hien thi so 3
    [1, 0, 0, 1, 1, 0, 0],  # hien thi so 4
    [0, 1, 0, 0, 1, 0, 0],  # hien thi so 5
    [0, 1, 0, 0, 0, 0, 0],  # hien thi so 6
    [0, 0, 0, 1, 1, 1, 1],  # hien thi so 7
    [0, 0, 0, 0, 0, 0, 0],  # hien thi so 8
    [0, 0, 0, 0, 1, 0, 0],  # hien thi so 9
]


# điều kiện gian ngắt process hiển thị led 7 thanh
# breakTime = False

def count_down(color):
    # quy ước thời gian đèn đỏ bằng tổng của đèn xan và đèn vàng.
    # xử lú đồng thời cả đèn xanh và đền đỏ thông qua tg của đèn xanh.

    if color == env.GREEN_1:
        time_down = env.TIME_GREEN[0]
        while time_down >= 0:
            handle_concurrent(time_down, time_down + env.TIME_YELLOW[0])
            time_down -= 1

    if color == env.YELLOW_1 or color == env.YELLOW_2:
        time_down = env.TIME_YELLOW[0]
        while time_down >= 0:
            handle_concurrent(time_down, time_down)
            time_down -= 1

    if color == env.GREEN_2:
        time_down = env.TIME_GREEN[0]
        while time_down >= 0:
            handle_concurrent(time_down + env.TIME_YELLOW[0], time_down)
            time_down -= 1


def handle_concurrent(time_led_1, time_led_2):
    # thời gian hiển thị, đồng thời sử dụng mảng đẻ truyền tham chiếu
    break_time = [1]
    theard_7seg = cpu.Thread(target=interup, args=(break_time,))
    theard_7seg.start()
    # print("waited ")
    while break_time[0]:
        push8bit(time_led_1)
        pi.digitalWrite(env.LED_PIN_D1, 1)
        time.sleep(0.005)
        pi.digitalWrite(env.LED_PIN_D1, 0)

        push8bit(time_led_2)
        pi.digitalWrite(env.LED_PIN_D2, 1)
        time.sleep(0.005)
        pi.digitalWrite(env.LED_PIN_D2, 0)


def interup(break_time):
    time.sleep(1)  # dặt tốc độ đếm 1s
    break_time[0] = 0
    # print("done !")


def push8bit(led_num):
    temp = map_digital[led_num]
    for index, val in enumerate(temp):
        pi.digitalWrite(env.LED_7segs[index], val)


def off_led():
    pi.digitalWrite(env.LED_PIN_D1, 0)
    pi.digitalWrite(env.LED_PIN_D2, 0)
