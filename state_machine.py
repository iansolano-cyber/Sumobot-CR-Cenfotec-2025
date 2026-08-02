import time

import config
import motors
import infrared
import ultrasonic
import imu


state = config.STATE_SEARCH


def escape():

    motors.backward()
    time.sleep_ms(config.BACK_TIME)

    motors.turn_right()

    start = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start) < 700:
        pass

    motors.stop()


def attack():

    motors.forward()


def search():

    motors.forward()
    time.sleep_ms(150)

    motors.turn_left()
    time.sleep_ms(config.SEARCH_TURN_TIME)


def update():

    global state

    # La prioridad siempre es evitar salir del dojo
    if infrared.white_detected():

        state = config.STATE_ESCAPE
        escape()
        return

    # Si encuentra un oponente, lo persigue
    if ultrasonic.enemy_detected():

        state = config.STATE_ATTACK
        attack()
        return

    # Si no encuentra nada, lo busca
    state = config.STATE_SEARCH
    search()


def current_state():

    if state == config.STATE_SEARCH:
        return "SEARCH"

    if state == config.STATE_ATTACK:
        return "ATTACK"

    if state == config.STATE_ESCAPE:
        return "ESCAPE"

    return "STOP"


def print_state():

    print(current_state())
