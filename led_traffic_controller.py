import variableAndContrants as env
import led_7seg_controller as seg
import led_lcd_controller as lcd
import threading as cpu
import wiringpi as pi
import time
from goto import with_goto

# Sử dụng mang đẻ chuyền tham chiếu tới biến
button_state = [0]
mod_led = ['light']  # Điều kiện chọn chế độ đèn light/night

# @with_goto
def HandleLED():
    theard_read_button = cpu.Thread(target=readButton, args=(button_state,))
    theard_read_button.start()
    while True:
        # if button_state[0] == 1:  # Bật chế độ emergency
        #     handelEmer()
        if mod_led == 'night':  # Bật chế độ ban đêm
            while mod_led == 'night':
                onEmer(env.Time_EMER)
        else:   # Bật chế độ giao thông bình thường
            handelEmer(button_state[0])
            onGreen(1)
            onRed(2)
            seg.count_down(env.GREEN_1)

            handelEmer(button_state[0])
            onYellow(1)
            seg.count_down(env.YELLOW_1)

            handelEmer(button_state[0])
            onRed(1)
            onGreen(2)
            seg.count_down(env.GREEN_2)

            handelEmer(button_state[0])
            onYellow(2)
            seg.count_down(env.YELLOW_2)


def onRed(index):
    if index == 1:
        pi.digitalWrite(env.YELLOW_1, 0)
        pi.digitalWrite(env.GREEN_2, 0)
        pi.digitalWrite(env.RED_1, 1)
    if index == 2:
        pi.digitalWrite(env.YELLOW_2, 0)
        pi.digitalWrite(env.GREEN_2, 0)
        pi.digitalWrite(env.RED_2, 1)


def onYellow(index):
    if index == 1:
        pi.digitalWrite(env.YELLOW_1, 1)
        pi.digitalWrite(env.GREEN_1, 0)
        pi.digitalWrite(env.RED_1, 0)
    if index == 2:
        pi.digitalWrite(env.YELLOW_2, 1)
        pi.digitalWrite(env.GREEN_2, 0)
        pi.digitalWrite(env.RED_2, 0)


def onGreen(index):
    if index == 1:
        pi.digitalWrite(env.YELLOW_1, 0)
        pi.digitalWrite(env.GREEN_1, 1)
        pi.digitalWrite(env.RED_1, 0)
    if index == 2:
        pi.digitalWrite(env.YELLOW_2, 0)
        pi.digitalWrite(env.GREEN_2, 1)
        pi.digitalWrite(env.RED_2, 0)


def onEmer(time_emer):
    timeDown = time_emer
    while timeDown >= 0:
        pi.digitalWrite(env.YELLOW_1, 1)
        pi.digitalWrite(env.YELLOW_2, 1)
        pi.digitalWrite(env.GREEN_1, 0)
        pi.digitalWrite(env.RED_1, 0)
        pi.digitalWrite(env.GREEN_2, 0)
        pi.digitalWrite(env.RED_2, 0)

        time.sleep(1)
        pi.digitalWrite(env.YELLOW_1, 0)
        pi.digitalWrite(env.YELLOW_2, 0)
        time.sleep(0.5)
        timeDown -= 1


def readButton(button_state):
    while True:
        state = pi.digitalRead(env.Button)
        button_state[0] = state
        print(state)

def handelEmer(state):
    if state:
        lcd.lcd_warning_emer()
        seg.off_led()
        onEmer(env.Time_EMER)
        lcd.lcd_init()