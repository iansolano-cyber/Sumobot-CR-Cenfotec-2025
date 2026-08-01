# Lógica desarrollada

Durante el desarrollo se fue definiendo el comportamiento esperado.

Primero:

Leer sensores infrarrojos.

Si detectan blanco:

retroceder

girar

continuar

Si no detectan blanco:

medir distancia con HC-SR04.

Si la distancia es menor de 20 cm:

perseguir al oponente.

En caso contrario:

continuar buscando.

La intención fue integrar todas estas decisiones dentro de un único programa sin que una acción bloqueara a las demás.
