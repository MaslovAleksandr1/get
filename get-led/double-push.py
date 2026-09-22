import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
button = [9, 10]
GPIO.setup(button, GPIO.IN)
num = 0
sleep_time = 0.2
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(9) and GPIO.input(10):
        while True:
            GPIO.output(leds, 1)
            if GPIO.input(9) or GPIO.input(10):
                break
    if GPIO.input(9):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        if num > 255:
            num = 255
    if GPIO.input(10):
        num = num - 1
        if num < 0:
            num = 0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))