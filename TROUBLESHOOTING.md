# Problemas encontrados

## Problema

El robot solamente retrocedía.

Causa

La condición principal impedía evaluar el resto de sensores.

---

## Problema

El robot solamente giraba.

Causa

La lógica del borde estaba mal organizada.

---

## Problema

No detectaba correctamente el IMU.

Causa

Se utilizaban registros correspondientes a otro acelerómetro.

---

## Problema

ImportError:

No module named qwiic_imu

Causa

El proyecto no utiliza esa librería.

Se trabaja directamente mediante I2C.

---

## Problema

OSError:

ENODEV

Causa

La dirección I2C o la configuración del dispositivo era incorrecta.

---

## Problema

Los sensores infrarrojos estaban conectados a pines incorrectos.

Corrección

Se reemplazó:

GPIO18

GPIO19

por

GPIO36

GPIO39
