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

    def disparo_coordenada(self):
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
        print(f"Intentando disparar a las coordenadas {fila} {columna}...")
        if self.tablero_maquina[fila, columna] == "O":
            print("¡Impacto! Barco alcanzado.")
            self.tablero_maquina[fila, columna] = "X"
        elif self.tablero_maquina[fila, columna] == " ":
            print("¡Agua! Disparo en el agua.")
            self.tablero_maquina[fila, columna] = "-"
        else:
            print("¡Ya habías disparado en esta posición!")

    def generador_disparo_maquina(self):
        fila = random.randint(0 , ALTO_TABLERO)
        columna = random.randint(0 , ANCHO_TABLERO)
        print(f"Intentando disparar a las coordenadas {fila} {columna}...")
        if self.tablero_usuario[fila, columna] == "O":
            print("¡Tocado!, Barco alcanzado")
            self.tablero_usuario[fila, columna] = "X"
        elif self.tablero_usuario[fila, columna] == " ":
            self.tablero_usuario[fila, columna] = "-"
            print("¡Agua!, Disparo en agua")
        else:
            print("Ya habias disparado en esas coordenadas")

tablero1 = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero2 = Tablero(ID_MAQUINA, dicc_barcos_maquina)
tablero1.disparo_coordenada()
tablero2.generador_disparo_maquina()

tablero2.generador_disparo_maquina()

print(tablero1)
print(tablero2)