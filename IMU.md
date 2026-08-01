# IMU

El módulo utilizado corresponde al SparkFun Qwiic LSM6DS3TR-C.

Durante el desarrollo se produjeron varios errores debido a que inicialmente se estaba utilizando la configuración de otro IMU.

Esto ocasionó:

- giroscopio siempre en cero
- acelerómetro incorrecto
- errores ENODEV
- registros incompatibles

Posteriormente se confirmó que:

La dirección correcta era:

0x6B

El módulo se conecta únicamente mediante Qwiic utilizando I2C.

No utiliza pines independientes para acelerómetro o giroscopio.

También se aclaró que no debía utilizarse ninguna librería externa llamada qwiic_imu ya que el proyecto trabaja directamente utilizando I2C desde MicroPython.
