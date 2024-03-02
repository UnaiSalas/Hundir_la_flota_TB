from variables import *
import numpy as np
import random

def disparo_coordenada(tablero):
    if tablero.jugador == 1:
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
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
    