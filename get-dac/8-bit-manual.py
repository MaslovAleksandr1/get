import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]

for pin in dac_pins:
    GPIO.setup(pin, GPIO.OUT)

dynamic_range = 3.17
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dymamic_range:.2f} B")
        print("Установливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)
def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
            a = number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
        GPIO.output(dac_pins, a)
finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()