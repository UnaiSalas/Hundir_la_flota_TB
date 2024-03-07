from variables import *
import numpy as np
import os
import random
import time


contador_usuario = 20
contador_maquina = 20

def disparo_coordenada(tablero): #realiza el disparo tanto de la máquina como del usuario.
    global TURNO
    if TURNO == 0:
        coordenadas = input("Introduce las dos coordenadas para el disparo: " ).split() 
        fila = int(coordenadas[0])
        columna = int(coordenadas[1])
        while not coordenadas_correctas(fila, columna): #validacion para comprobar que las coordenadas que nos han dado son correctas
            coordenadas = input("Introduce las dos coordenadas para el disparo: ").split()
            fila = int(coordenadas[0])
            columna = int(coordenadas[1])
    else:
        fila = random.randint(0, ALTO_TABLERO)
        columna = random.randint(0, ANCHO_TABLERO)
        coordenadas = [fila,columna]

    print(f"Intentando disparar a las coordenadas {fila} {columna}...")
    time.sleep(5)  # Aplicar un retraso de 5 segundos

    if tablero.tablero_usuario[fila, columna] == "O":
        tablero.tablero_usuario[fila, columna] = "X"
        tocado_hundido(tablero, coordenadas)
        coordenadas_tocadas(tablero,coordenadas)
        fin_partida = comprobacion_fin(tablero)
        print(fin_partida)
    elif tablero.tablero_usuario[fila, columna] == " ":
        tablero.tablero_usuario[fila, columna] = "-"
        print("¡Agua!, Disparo en agua") 
        TURNO = 1     
        if TURNO == 0:
              TURNO = 1 #definimos de quién es el turno, si del usuario o de la máquina --> No entiendo porque esta esto comentado. No sería esta validacion?
        else:
              TURNO = 0
    else:
        print("Ya habias disparado en esas coordenadas")
    
      
def comprobacion_fin(tablero):
    if TURNO == 0:
        todos_hundidos = all(all(posicion == 'X' for posicion in posiciones) for posiciones in tablero.dicc_barcos_usuario.values())
        if todos_hundidos == True:
            print("Se acabo el juego")
    else:
        todos_hundidos = all(all(posicion == 'X' for posicion in posiciones) for posiciones in tablero.dicc_barcos_maquina.values())
        if todos_hundidos == True:
            print("Se acabo el juego")
    return todos_hundidos

def tocado_hundido(tablero, coordenadas):
    print(coordenadas)
    coordenadas = tuple(map(int, coordenadas))
    print(coordenadas)
    if TURNO == 0:
        for barcos, posiciones in tablero.dicc_barcos_usuario.items():
            if coordenadas in posiciones:
                todas_X = all((posicion == 'X') or (tablero.tablero_usuario[posicion] == 'X') for posicion in posiciones)
                if todas_X:
                    print(f"Tocado y hundido el barco {barcos}")
                else:
                    print(f"Tocado")
    else:
        for barcos, posiciones in tablero.dicc_barcos_maquina.items():
            if coordenadas in posiciones:
                todas_X = all((posicion == 'X') or (tablero.tablero_usuario[posicion] == 'X') for posicion in posiciones)
                if todas_X:
                    print(f"Tocado y hundido el barco {barcos}")
                else:
                    print(f"Tocado")


def coordenadas_tocadas(tablero,coordenadas):
    fila = int(coordenadas[0])
    columna = int(coordenadas[1])
    if TURNO == 0:
        for posiciones in tablero.dicc_barcos_usuario.values():
            if(fila,columna) in posiciones:
                posiciones[posiciones.index((fila, columna))] = 'X'
    else:
        for posiciones in tablero.dicc_barcos_maquina.values():
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

def coordenadas_correctas(fila,columna):
    if 0 <= fila < ALTO_TABLERO and 0 <= columna < ANCHO_TABLERO:
        return True
    else:
        print("Coordenadas fuera de los límites del tablero. Introduce coordenadas válidas.")
        return False

def partida(tablero_jugador, tablero_maquina):
    print('''¡Hola! ¡Bienvenido al juego de HUNDIR LA FLOTA!

Veamos las normas antes de comenzar:

Objetivo del juego:
El objetivo principal del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos.

Jugadas:
Los jugadores se turnan para realizar una jugada.
Una jugada consiste en seleccionar una coordenada en el tablero del oponente para intentar hundir uno de sus barcos.
El oponente informa si la jugada fue un "impacto" (tocó un barco) o un "agua" (no tocó ningún barco).

Ganador:
El jugador que hunde todos los barcos del oponente primero es el ganador.
          ''')
    input("Presiona Enter para continuar...")
    TURNO = 0
    #TURNO = random.randint(0, 1) #la primera vez, tiene que ser random
    while True: 
        os.system('cls')  # Limpiar pantalla
        if TURNO == 0:  # Turno del jugador
            print('¡Tu turno!')
            disparo_coordenada(tablero_maquina)
            print("Aquí tienes el tablero de la máquina:")
            print(tablero_maquina.tablero_usuario)
            time.sleep(5)  # Aplicar un retraso de 5 segundos
            input("Presiona Enter para continuar...")
        else:  # Turno de la máquina
            print('¡Es el turno de la máquina!')
            disparo_coordenada(tablero_jugador)
            print("Aquí tienes tu tablero:")
            print(tablero_jugador.tablero_usuario)
            time.sleep(5)  # Aplicar un retraso de 5 segundos
            input("Presiona Enter para continuar...")

    