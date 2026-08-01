from machine import Pin
from time import sleep_us, ticks_us, ticks_diff
import config

trig = Pin(config.TRIG_PIN, Pin.OUT)
echo = Pin(config.ECHO_PIN, Pin.IN)


def distance():

    trig.off()
    sleep_us(2)

    trig.on()
    sleep_us(10)
    trig.off()

    timeout = ticks_us()

    while echo.value() == 0:
        if ticks_diff(ticks_us(), timeout) > 30000:
            return None

    start = ticks_us()

    while echo.value() == 1:
        if ticks_diff(ticks_us(), start) > 30000:
            return None

    end = ticks_us()

    duration = ticks_diff(end, start)

    return (duration * 0.0343) / 2


def enemy_detected():

    d = distance()

    if d is None:
        return False

    return d <= config.ATTACK_DISTANCE


def enemy_far():

    d = distance()

    if d is None:
        return True

    return d > config.ATTACK_DISTANCE


def print_distance():

    d = distance()

    if d is None:
        print("Sin lectura")

    else:
        print(round(d, 2), "cm")
