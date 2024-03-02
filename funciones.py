from variables import *
import numpy as np
import random


contador_usuario = 20 #suma las esloras de todos los barcos
contador_maquina = 20 #20 es un ejemplo.

def disparo_coordenada(tablero): #realiza el disparo tanto de la máquina como del usuario.
    if tablero.jugador == 1:
#        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split()
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
    else:
        fila = random.randint(0 , ALTO_TABLERO)
        columna = random.randint(0 , ANCHO_TABLERO)
    print(f"Intentando disparar a las coordenadas {fila} {columna}...")
    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        if turno == 0:
            contador_usuario -= 1 #atributo de tablero??
        else: 
            contador_maquina -= 1
        print("¡Tocado!, Barco alcanzado. Te quedan {contador_} oportunidades para matarlo") #rematar
        #nueva funcion que detecta si está todo alcanzado comprobacion ()
    elif tablero[fila, columna] == " ":
        tablero[fila, columna] = "-"
        print("¡Agua!, Disparo en agua")
        if turno == 0:
            turno = 1 #definimos de quién es el turno, si del usuario o de la máquina
        else:
            turno = 0
    else:
        print("Ya habias disparado en esas coordenadas")
    

def comprobacion_fin_partida(tablero): #funcion para acabar la partida
    #diccionario barcos con listas de las posiciones. Estas posiciones se actualizan al inicio.
    if turno == 0:   
        if all(barco == X for barco in dicc_barcos_usuario.values()):
            print('Estas acabado')

    else:
        
def comprobacion_tocado_hundido()
#entramso en diccionario y cambiamos la coordenada a X i.e. {'barco1': [[2,4],[2,5],[2,6]]} --> {'barco1': [X,[2,5],[2,6]]}






dicc_barcos_usuario o dicc_barcos_maquina




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