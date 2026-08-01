from machine import ADC, Pin
import config

front_left = ADC(Pin(config.IR_FRONT_LEFT))
front_right = ADC(Pin(config.IR_FRONT_RIGHT))
rear_left = ADC(Pin(config.IR_REAR_LEFT))
rear_right = ADC(Pin(config.IR_REAR_RIGHT))

for sensor in [front_left, front_right, rear_left, rear_right]:
    sensor.atten(ADC.ATTN_11DB)


def read():
    return {
        "front_left": front_left.read(),
        "front_right": front_right.read(),
        "rear_left": rear_left.read(),
        "rear_right": rear_right.read()
    }


def is_white(value):
    return value > config.BLACK_THRESHOLD


def is_black(value):
    return value <= config.BLACK_THRESHOLD


def white_detected():
    values = read()

    return (
        is_white(values["front_left"]) or
        is_white(values["front_right"]) or
        is_white(values["rear_left"]) or
        is_white(values["rear_right"])
    )


def black_detected():
    values = read()

    return (
        is_black(values["front_left"]) and
        is_black(values["front_right"]) and
        is_black(values["rear_left"]) and
        is_black(values["rear_right"])
    )


def front_white():
    values = read()

    return (
        is_white(values["front_left"]) or
        is_white(values["front_right"])
    )


def rear_white():
    values = read()

    return (
        is_white(values["rear_left"]) or
        is_white(values["rear_right"])
    )


def left_white():
    values = read()

    return (
        is_white(values["front_left"]) or
        is_white(values["rear_left"])
    )


def right_white():
    values = read()

    return (
        is_white(values["front_right"]) or
        is_white(values["rear_right"])
    )


def print_values():
    values = read()

    print(
        values["front_left"],
        values["front_right"],
        values["rear_left"],
        values["rear_right"]
    )
