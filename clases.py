from variables import *
import numpy as np

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

tablero1 = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero2 = Tablero(ID_MAQUINA, dicc_barcos_maquina)

print(tablero1)
print(tablero2)