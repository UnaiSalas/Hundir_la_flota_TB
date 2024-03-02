from variables import *
import numpy as np
import random

class Tablero():
    def __init__(self, jugador, dicc_barcos_usuario = None):
        self.jugador = jugador #para saber de quién es el tablero.
        self.fila = ALTO_TABLERO
        self.columna = ANCHO_TABLERO

        self.dicc_barcos_usuario = np.array(list((dicc_barcos_usuario))) #duditas
        self.tablero_usuario = self.crear_tablero(self.fila, self.columna)
        self.tablero_maquina = self.crear_tablero(self.fila, self.columna)

    def crear_tablero(self, filas, columnas):
        return np.full((filas, columnas), " ")

    def __str__(self):
        return f"Tablero del jugador {self.jugador}\nUsuario: {self.tablero_usuario}\nMáquina: {self.tablero_maquina}"
    
    def generador_disparo_maquina(self):
        fila = random.randrange(0 , ALTO_TABLERO)
        columna = random.randrange(0 , ANCHO_TABLERO)
        if self.tablero_usuario[fila, columna] == "X":
            print("¡Tocado!, Barco alcanzado")
        elif self.tablero_usuario[fila, columna] == "_":
            print("¡Agua!, Disparo en agua")
        else:
            print("Ya habias disparado en esas coordenadas")


