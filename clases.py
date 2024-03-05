from variables import *
import numpy as np
import random

class Tablero():
    def __init__(self, jugador, dicc_barcos_usuario = None):
        self.jugador = jugador #para saber de quién es el tablero.
        self.fila = ALTO_TABLERO
        self.columna = ANCHO_TABLERO

        self.dicc_barcos_usuario = dicc_barcos_usuario #duditas
        self.tablero_usuario = self.crear_tablero(self.fila, self.columna)
        self.tablero_maquina = self.crear_tablero(self.fila, self.columna)

    def crear_tablero(self, filas, columnas):
        return np.full((filas, columnas), " ")

    def __str__(self):
        return f"Tablero del jugador {self.jugador}\nUsuario: {self.tablero_usuario}\nMáquina: {self.tablero_maquina}\n diccionario:{self.dicc_barcos_usuario}"

    def colocar_barcos(self):
        for barcos, eslora in self.dicc_barcos_usuario.items(): # Recorrer diccionario barcos con nombres y eslora
            orientacion = random.choice(["Horizontal", "Vertical"]) # Seleccion horientacion, aleatoria 
            for _ in range(10): # Intentar colocar 10 barcos
                if orientacion == "Horizontal":
                    fila = random.randint(0, self.fila -1)
                    columna = random.randint(0, self.columna - eslora)
                    # Verificar si las posiciones están vacías antes de colocar el barco
                    posiciones_vacias = all(self.tablero_usuario[fila, columna + i] == ' ' for i in range(eslora))
                    if posiciones_vacias:
                        posiciones_barco = [(fila, columna + i) for i in range(eslora)]
                        self.dicc_barcos_usuario[barcos] = posiciones_barco
                        for i in range(eslora): # Colocacion en el tablero una vez seleccionada la orientacion 
                            #self.dicc_barcos_usuario[barcos].append((fila, columna + i))
                            self.tablero_usuario[fila, columna + i] = 'X'
                else: 
                    fila = random.randint(0, self.fila - eslora)
                    columna = random.randint(0, self.columna - 1)
                    # Verificar si las posiciones están vacías antes de colocar el barco
                    posiciones_vacias = all(self.tablero_usuario[fila + i, columna] == ' ' for i in range(eslora))
                    if posiciones_vacias:
                        posiciones_barco = [(fila + i, columna) for i in range(eslora)]
                        self.dicc_barcos_usuario[barcos] = posiciones_barco
                        for i in range(eslora):
                            self.tablero_usuario[fila + i, columna] = 'X'
                            #self.dicc_barcos_usuario[barcos].append((fila + i, columna))

tablero = Tablero(jugador = 1, dicc_barcos_usuario = dicc_barcos_usuario)
tablero.colocar_barcos()
print(tablero.tablero_usuario)