from variables import *
from funciones import *
from clases import *
import numpy as np
import os
import random



tablero_jugador = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero_maquina = Tablero(ID_MAQUINA, dicc_barcos_maquina)

tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

partida(tablero_jugador, tablero_maquina)

