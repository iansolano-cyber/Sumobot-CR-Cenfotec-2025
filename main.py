import time

import motors
import imu
import state_machine


def setup():

    print("Iniciando Sumobot...")

    imu.init()

    motors.stop()

    time.sleep(1)

    print("Sistema listo")


def loop():

    while True:

        state_machine.update()

        time.sleep_ms(20)


try:

    setup()

    loop()

except KeyboardInterrupt:

    motors.stop()

    print("Robot detenido")
