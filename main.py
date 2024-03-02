from variables import*
from funciones import*
from clases import*

tablero1 = Tablero(ID_JUGADOR, dicc_barcos_usuario)
tablero2 = Tablero(ID_MAQUINA, dicc_barcos_maquina)
tablero1.disparo_coordenada()
tablero2.generador_disparo_maquina()

tablero2.generador_disparo_maquina()

print(tablero1)
print(tablero2)