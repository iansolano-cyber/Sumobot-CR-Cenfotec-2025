# Registro del desarrollo

## Primera etapa

Se construyó el programa inicial utilizando:

- motores
- HC-SR04
- sensores infrarrojos
- IMU

Posteriormente comenzaron las pruebas.

---

## Problemas encontrados

Los motores funcionaban correctamente de forma independiente.

Sin embargo, al integrar toda la lógica comenzaron distintos problemas.

Entre ellos:

- el robot solamente retrocedía
- el robot solamente giraba
- solamente ejecutaba una acción
- no reaccionaba cuando cambiaban los sensores

---

## Sensores infrarrojos

Durante las pruebas se aclaró que el dojo no utiliza una línea negra.

El piso completo es negro.

El borde únicamente es blanco.

Por lo tanto la lógica debía cambiar completamente.

Posteriormente también se corrigieron los pines utilizados.

Se eliminaron GPIO18 y GPIO19.

Los sensores correctos quedaron en:

GPIO34

GPIO35

GPIO36

GPIO39

---

## HC-SR04

Inicialmente la lógica detenía el robot cuando encontraba un objeto.

Posteriormente se corrigió.

El comportamiento esperado pasó a ser:

Si la distancia es menor de 20 cm

↓

Perseguir al oponente.

---

## IMU

Una de las etapas que presentó más problemas fue el acelerómetro.

Inicialmente se utilizaron registros pertenecientes a otro sensor.

Eso produjo lecturas como:

Giroscopio:

0

0

0

o valores completamente incorrectos.

Durante el desarrollo se confirmó que el sensor utilizado era un SparkFun Qwiic LSM6DS3TR-C.

También se corrigió la dirección I2C.

Inicialmente aparecía el error:

OSError: ENODEV

Posteriormente se configuró correctamente la dirección:

0x6B

Después comenzaron las primeras lecturas del acelerómetro.

Ejemplo obtenido durante las pruebas:

Acelerómetro (mg):

X=57.34

Y=-200.99

Z=1003.08

También comenzaron a aparecer lecturas del giroscopio.

---

## Organización del programa

Durante varias pruebas el programa solamente ejecutaba una condición.

Por ejemplo:

si detectaba blanco

nunca revisaba el HC-SR04

o solamente perseguía sin revisar el borde.

Por ello se reorganizó completamente la estructura del bucle principal para que todos los sensores fueran evaluados continuamente.
