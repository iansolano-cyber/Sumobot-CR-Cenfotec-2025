from machine import Pin
import config

# Pines de los motores
left_forward = Pin(config.MOTOR_LEFT_FORWARD, Pin.OUT)
left_backward = Pin(config.MOTOR_LEFT_BACKWARD, Pin.OUT)

right_forward = Pin(config.MOTOR_RIGHT_FORWARD, Pin.OUT)
right_backward = Pin(config.MOTOR_RIGHT_BACKWARD, Pin.OUT)


def stop():
    left_forward.off()
    left_backward.off()
    right_forward.off()
    right_backward.off()


def forward():
    left_forward.on()
    left_backward.off()

    right_forward.on()
    right_backward.off()


def backward():
    left_forward.off()
    left_backward.on()

    right_forward.off()
    right_backward.on()


def turn_left():
    left_forward.off()
    left_backward.on()

    right_forward.on()
    right_backward.off()


def turn_right():
    left_forward.on()
    left_backward.off()

    right_forward.off()
    right_backward.on()


def forward_left():
    left_forward.off()
    left_backward.off()

    right_forward.on()
    right_backward.off()


def forward_right():
    left_forward.on()
    left_backward.off()

    right_forward.off()
    right_backward.off()


def backward_left():
    left_forward.off()
    left_backward.on()

    right_forward.off()
    right_backward.off()


def backward_right():
    left_forward.off()
    left_backward.off()

    right_forward.off()
    right_backward.on()


def brake(ms=100):
    stop()
    import time
    time.sleep_ms(ms)


def test():
    import time

    print("Avanzando")
    forward()
    time.sleep(2)

    print("Retrocediendo")
    backward()
    time.sleep(2)

    print("Izquierda")
    turn_left()
    time.sleep(2)

    print("Derecha")
    turn_right()
    time.sleep(2)

    print("Detenido")
    stop()
