# Hardware utilizado

## ESP32

Todo el proyecto fue desarrollado utilizando un ESP32.

Se utilizaron:

- GPIO digitales
- ADC
- I2C
- PWM (en varias pruebas)

---

## Motores

Durante el desarrollo se utilizaron dos motores DC controlados mediante cuatro señales digitales.

Configuración utilizada:

IN1 -> GPIO12

IN2 -> GPIO14

IN3 -> GPIO13

IN4 -> GPIO15

Durante varias pruebas también se utilizaron los pines 32 y 33 como Enable utilizando PWM.

Posteriormente se hicieron pruebas eliminando el uso del PWM para simplificar el control.

---

## Sensor ultrasónico

HC-SR04

Configuración utilizada:

TRIG -> GPIO26

ECHO -> GPIO23

El sensor se utilizó para detectar objetos a menos de 20 cm.

---

## Sensores infrarrojos

Durante el desarrollo hubo varios cambios.

Inicialmente se utilizaron:

GPIO34

GPIO35

GPIO18

GPIO19

Posteriormente se corrigió el hardware utilizado y finalmente quedaron:

GPIO34

GPIO35

GPIO36

GPIO39

Estos sensores son los encargados de detectar el borde del dojo.

---

## IMU

El acelerómetro y giroscopio utilizado corresponde al módulo:

SparkFun Qwiic LSM6DS3TR-C

No utiliza conexiones individuales para cada función.

Se conecta mediante el puerto Qwiic utilizando I2C.

La dirección utilizada es:

0x6B
