import threading
import wiringpi as pi
import variableAndContrants as env
import led_traffic_controller as traffic
import led_lcd_controller as lcd
import database as api
import time

# Setting for wPi pin mod
pi.wiringPiSetup()

pi.pinMode(env.RED_1, pi.OUTPUT)
pi.pinMode(env.RED_2, pi.OUTPUT)
pi.pinMode(env.YELLOW_1, pi.OUTPUT)
pi.pinMode(env.YELLOW_2, pi.OUTPUT)
pi.pinMode(env.GREEN_1, pi.OUTPUT)
pi.pinMode(env.GREEN_2, pi.OUTPUT)
pi.pinMode(env.Button, pi.INPUT)

pi.pinMode(env.LED_PIN_A, pi.OUTPUT)
pi.pinMode(env.LED_PIN_B, pi.OUTPUT)
pi.pinMode(env.LED_PIN_C, pi.OUTPUT)
pi.pinMode(env.LED_PIN_D, pi.OUTPUT)
pi.pinMode(env.LED_PIN_E, pi.OUTPUT)
pi.pinMode(env.LED_PIN_F, pi.OUTPUT)
pi.pinMode(env.LED_PIN_G, pi.OUTPUT)

pi.pinMode(env.LED_PIN_DP, pi.OUTPUT)
pi.pinMode(env.LED_PIN_D1, pi.OUTPUT)
pi.pinMode(env.LED_PIN_D2, pi.OUTPUT)

# Setup envỉoment
api.call()

# Bật chế độ chờ ghi cho LCD
lcd.lcd_init()

# Bật chế độ đèn giao thông
traffic.HandleLED()

