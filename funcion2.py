from variables import *
import numpy as np
import random

''' 
3. Una vez ya tienes modelizado tu tablero, hay que montar el programa que se ejecutara desde un **main.py**:
    * El programa no es más que el **típico `while true: `, con una serie de inputs del usuario**. Se está ejecutando constantemente y le pide al usuario coordenadas para comprobar si impacta.
    * Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
    * A continuación **inicializa los tableros de ambos jugadores** con los barcos. Estas dos primeras acciones solo se ejecutan una vez!! Que es el comienzo del juego.
    * Después de eso ya comienza el juego. Básicamente **se irá ejecutando iterativamente en el `while`, y le irá preguntando coordenadas al usuario.**
    * Recoges coordenadas, compruebas en el tablero de la máquina si habia barco.
        * Hay barco: marca en el tablero de la maquina el impacto y le vuelve a tocar al usuario
        * No hay barco: le toca a la maquina. O lo que es lo mismo, escoge una coordenada aleatoria, y comprueba en el tablero del usuario si habia barco.
    * **Así hasta que uno de los dos jugadores se quede sin barcos, y termina el juego.**
    * Cuando empiece tu turno deberías imprimir por pantalla tu tablero, para ver cuántos impactos te ha hecho la máquina, así como el tablero con los impactos que has hecho tu en el adversario, de manera que te sirva de ayuda para el siguiente disparo.
    * Todas aquellas funciones que puedas construir para la ejecución de este programa deberán estar definidas en un script que se llame **funciones.py**.
'''

def disparo_coordenada(tablero):
    if tablero.jugador == 1:
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
    else:
        fila = random.randint(0 , ALTO_TABLERO)
        columna = random.randint(0 , ANCHO_TABLERO)
    print(f"Intentando disparar a las coordenadas {fila} {columna}...")
    if tablero[fila, columna] == "O":
        print("¡Tocado!, Barco alcanzado")
        tablero[fila, columna] = "X"
    elif tablero[fila, columna] == " ":
        tablero[fila, columna] = "-"
        print("¡Agua!, Disparo en agua")
    else:
        print("Ya habias disparado en esas coordenadas")


turno = 0 #valores: 0 y 1. 0: turno usuario y 1: turno máquina


while True:
    if turno == 0:
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
        disparo_coordenada(tablero2)
        #cuando actualizas el tablero es cuando se actualiza el turno
    else:
        print(f'Es el turno del oponente')
        disparo_coordenada(tablero1)

