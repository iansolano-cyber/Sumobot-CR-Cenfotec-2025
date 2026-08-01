# Sumobot ESP32

Proyecto de desarrollo de un robot sumo utilizando un ESP32 programado en MicroPython.

El objetivo del desarrollo fue integrar todos los sensores y actuadores necesarios para que el robot pudiera:

- moverse correctamente
- detectar el borde del dojo mediante sensores infrarrojos
- detectar un oponente utilizando un sensor ultrasónico HC-SR04
- utilizar un acelerómetro y giroscopio Qwiic (LSM6DS3TR-C)
- organizar todas las decisiones dentro de un único programa

Durante el desarrollo se realizaron numerosas pruebas para corregir errores relacionados con motores, sensores, direcciones I2C y registros del IMU.

---

## Hardware utilizado

ESP32

2 Motores DC

Driver de motores

HC-SR04

4 sensores infrarrojos

SparkFun Qwiic LSM6DS3TR-C

MicroPython

---

## Estado del proyecto

Durante este chat se consiguió:

- configurar motores
- configurar HC-SR04
- cambiar varias veces el pinout de los sensores
- corregir la dirección I2C del IMU
- comenzar la lectura correcta del acelerómetro
- integrar todas las partes dentro del mismo programa
- reorganizar la lógica principal del robot
