from variables import *
from clases import *
import numpy as np
import random

def disparo_coordenada(tablero):
    if tablero.jugador == 0:
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
        print(f"Intentando disparar a las coordenadas {fila} {columna}...")
        if tablero.tablero_oponente[fila, columna] == "O":
            print("¡Tocado!, Barco alcanzado")
            tablero.tablero_usuario[fila, columna] = "X"
        elif tablero.tablero_oponente[fila, columna] == " ":
            tablero.tablero_usuario[fila, columna] = "-"
            print("¡Agua!, Disparo en agua")
        else:
            print("Ya habias disparado en esas coordenadas")
    else:
        fila = random.randint(0 , ALTO_TABLERO)
        columna = random.randint(0 , ANCHO_TABLERO)
        print(f"Intentando disparar a las coordenadas {fila} {columna}...")
        if tablero.tablero_oponente[fila, columna] == "O":
            print("¡Tocado!, Barco alcanzado")
            tablero.tablero_usuario[fila, columna] = "X"
        elif tablero.tablero_oponente[fila, columna] == " ":
            tablero.tablero_usuario[fila, columna] = "-"
            print("¡Agua!, Disparo en agua")
        else:
            print("Ya habias disparado en esas coordenadas")
    