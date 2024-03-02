from variables import *
from funciones import *
from clases import *
import numpy as np
import random


tablero1 = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero2 = Tablero(ID_MAQUINA, dicc_barcos_maquina)
disparo_coordenada(tablero1)


print(tablero1)