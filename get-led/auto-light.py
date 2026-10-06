import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
foto = 6
GPIO.setup(foto, GPIO.IN)
state = 0
while True:
    state = not(GPIO.input(foto))
    GPIO.output(led,state)