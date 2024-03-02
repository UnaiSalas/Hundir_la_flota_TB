from variables import *
import numpy as np
import random

class Tablero():
    def __init__(self, jugador, dicc_barcos = None):
        self.jugador = jugador #para saber de quién es el tablero.
        self.fila = ALTO_TABLERO
        self.columna = ANCHO_TABLERO

        self.dicc_barcos_usuario = np.array(list((dicc_barcos))) #duditas
        self.tablero_usuario = self.crear_tablero(self.fila, self.columna)
        self.tablero_oponente = self.crear_tablero(self.fila, self.columna)

    def crear_tablero(self, filas, columnas):
        return np.full((filas, columnas), " ")

    def __str__(self):
        return f"Tablero del jugador {self.jugador}\nUsuario: {self.tablero_usuario}\nMáquina: {self.tablero_oponente}"
    