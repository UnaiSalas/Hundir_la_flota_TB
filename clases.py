from variables import *
import numpy as np
import random

class Tablero():
    def __init__(self, jugador, dicc_barcos_usuario = None):
        self.jugador = jugador #para saber de quién es el tablero.
        self.fila = ALTO_TABLERO
        self.columna = ANCHO_TABLERO

        self.dicc_barcos_usuario = dicc_barcos_usuario 
        self.tablero_usuario = self.crear_tablero(self.fila, self.columna)
        self.tablero_maquina = self.crear_tablero(self.fila, self.columna)

    def crear_tablero(self, filas, columnas):
        return np.full((filas, columnas), " ")

    def __str__(self):
        tablero_usuario_str = "Tablero del jugador {}\nUsuario:\n".format(self.jugador)
        for i, fila in enumerate(self.tablero_usuario):
            tablero_usuario_str += "{} ".format(i)
            for valor in fila:
                tablero_usuario_str += "{} ".format(valor)
            tablero_usuario_str += "\n"
        
        # Construir la representación del tablero de la máquina
        tablero_maquina_str = "Máquina:\n"
        for i, fila in enumerate(self.tablero_maquina):
            tablero_maquina_str += "{} ".format(i)
            for valor in fila:
                tablero_maquina_str += "{} ".format(valor)
            tablero_maquina_str += "\n"
        
        # Construir la representación del diccionario de barcos del usuario
        diccionario_str = "diccionario:{}".format(self.dicc_barcos_usuario)
        
        # Combinar las representaciones en una sola cadena
        return "{}\n{}".format(tablero_usuario_str, tablero_maquina_str, diccionario_str)
    #return f"Tablero del jugador {self.jugador}\nUsuario:\n {self.tablero_usuario}\nMáquina:\n {self.tablero_maquina}\n diccionario:{self.dicc_barcos_usuario}"

    def colocar_barcos(self):
        for barcos, eslora in self.dicc_barcos_usuario.items(): # Recorrer diccionario barcos con nombres y eslora
            orientacion = random.choice(["Horizontal", "Vertical"]) # Seleccion horientacion, aleatoria 
            intentos_restantes = 10 # Intentos restantes
            colocado = False
            while intentos_restantes > 0 and not colocado: # Mientras haya intentos y barco no colocado
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
                            self.tablero_usuario[fila, columna + i] = 'O'
                        colocado=True
                    else:
                        intentos_restantes -= 1
                else: 
                    fila = random.randint(0, self.fila - eslora)
                    columna = random.randint(0, self.columna - 1)
                    # Verificar si las posiciones están vacías antes de colocar el barco
                    posiciones_vacias = all(self.tablero_usuario[fila + i, columna] == ' ' for i in range(eslora))
                    if posiciones_vacias:
                        posiciones_barco = [(fila + i, columna) for i in range(eslora)]
                        self.dicc_barcos_usuario[barcos] = posiciones_barco
                        for i in range(eslora):
                            self.tablero_usuario[fila + i, columna] = 'O'
                            #self.dicc_barcos_usuario[barcos].append((fila + i, columna))
                        colocado=True
                    else:
                        intentos_restantes -= 1