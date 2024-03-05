from variables import *
from funciones import *
from clases import *
import numpy as np
import random


tablero1 = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero2 = Tablero(ID_MAQUINA, dicc_barcos_maquina)

welcome = input('''¡Hola! ¡Bienvenido al juego de HUNDIR LA FLOTA!\n 
                
                Veamos las normas antes de comenzar:\n
                
                Objetivo del juego:\n 
                
                El objetivo principal del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos.\n

                Jugadas:\n

                Los jugadores se turnan para realizar una jugada.\n
                Una jugada consiste en seleccionar una coordenada en el tablero del oponente (por ejemplo, "A3" o "B4") para intentar hundir uno de sus barcos.\n
                El oponente informa si la jugada fue un "impacto" (tocó un barco) o un "agua" (no tocó ningún barco).\n
                
                Ganador:\n

                El jugador que hunde todos los barcos del oponente primero es el ganador.\n
                ''')
tablero1.colocar_barcos()

print(tablero1)
partida(tablero1)