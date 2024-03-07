from variables import *
from clases import *
import numpy as np
import random

def disparo_coordenada(tablero):
    global TURNO

    if tablero.jugador == 0:
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
        print(coordenadas)
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
    else:
        fila = random.randint(0, ALTO_TABLERO-1)
        columna = random.randint(0, ANCHO_TABLERO-1)
        coordenadas = [fila, columna]
    print(f"Intentando disparar a las coordenadas {fila} {columna}...")
    if tablero.tablero_usuario[fila, columna] == "O":
        tablero.tablero_usuario[fila, columna] = "X"
        tocado_hundido(tablero, coordenadas)
        coordenadas_tocadas(tablero,coordenadas)
        #if TURNO == 0:
        #    contador_usuario -= 1 #atributo de tablero??
        #else: 
        #    contador_maquina -= 1
        fin_partida = comprobacion_fin(tablero)
        print(fin_partida)
        #print("¡Tocado!, Barco alcanzado. Te quedan {contador_} oportunidades para matarlo") #rematar
        #nueva funcion que detecta si está todo alcanzado comprobacion ()
    elif tablero.tablero_usuario[fila, columna] == " ":
        tablero.tablero_usuario[fila, columna] = "-"
        print("¡Agua!, Disparo en agua") 
        #TURNO = 1     
        # if TURNO == 0:
        #      TURNO = 1 #definimos de quién es el turno, si del usuario o de la máquina
        # else:
        #      TURNO = 0
    else:
        print("Ya habias disparado en esas coordenadas")
    
    if TURNO == 0:  # Cambiar turno si ha disparado en agua
        TURNO = 1
    else:
        TURNO = 0
    

# def comprobacion_fin_partida(tablero): #funcion para acabar la partida
#     #diccionario barcos con listas de las posiciones. Estas posiciones se actualizan al inicio.
#     if TURNO == 0:   
#         if all(barco == 'X' for barco in dicc_barcos_usuario.values()):
#             print('Estas acabado')
#     else:
#         pass
        
def comprobacion_fin(tablero):
    todos_hundidos = all(all(posicion == 'X' for posicion in posiciones) for posiciones in tablero.dicc_barcos_usuario.values())
    if todos_hundidos == True:
        print("Se acabo el juego")
    return todos_hundidos

def tocado_hundido(tablero, coordenadas):
    print(coordenadas)
    coordenadas = tuple(map(int, coordenadas))
    print(coordenadas)
    for barcos, posiciones in tablero.dicc_barcos_usuario.items():
        if coordenadas in posiciones:
            todas_X = all((posicion == 'X') or (tablero.tablero_usuario[posicion] == 'X') for posicion in posiciones)
            if todas_X:
                print(f"Tocado y hundido el barco {barcos}")
            else:
                print(f"Tocado")

def coordenadas_tocadas(tablero,coordenadas):
    fila = int(coordenadas[0])
    columna = int(coordenadas[1])
    for posiciones in tablero.dicc_barcos_usuario.values():
        if(fila,columna) in posiciones:
            posiciones[posiciones.index((fila, columna))] = 'X'

#entramso en diccionario y cambiamos la coordenada a X i.e. {'barco1': [[2,4],[2,5],[2,6]]} --> {'barco1': [X,X,X]}


# Funcion cambio de turno

# def cambio_turno(tablero):
#     if tablero.jugador == 0:
#         fila = random.randint(0, ALTO_TABLERO)
#         columna = random.randint(0, ANCHO_TABLERO)
#     else:
#         print("La maquina ha hecho agua, te vuelve a toca a ti¡¡")


'''
--> dentro del all hacemos la comprobacion. Que value != X. Iteramos. Gerenamos bool. Comprboamos todos bool. 
All devolverá True si todos son Trues. 
disparo 5,4

key : barco_
valor: X

dicc.values()
value != X:
continuamos
'''
def partida(tablero_jugador, tablero_maquina):
    while True:
        if TURNO == 0: # Si se da el turno del jugador
            disparo_coordenada(tablero_maquina)
            print("Aqui tenemos el tablero de la maquina")
            print(tablero_maquina.tablero_usuario)
        else:
            disparo_coordenada(tablero_jugador)
            print("Aqui tenemos el tablero del jugador")
            print(tablero_jugador.tablero_usuario)
