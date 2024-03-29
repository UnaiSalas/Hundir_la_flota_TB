from variables import *
import numpy as np
import os
import random
import time


contador_usuario = 20
contador_maquina = 20
'''
Disparo de coordenadas
Como parametros entran el tablero disparado (tablero/jugador al que se dispara) y el tablero disparador (el tablero/jugador que dispara)
Si es el turno del usuario se le piden las coordenadas y si es el turno de la maquina se generan las coordenadas
Si se da el caso de acertar se sustituye en el tablero principal del disparado la O del barco por X y en el tablero de anotaciones del
que disparador se añade la X en esa posicion. Despues se comprueba si el barco esta simplemente tocao o hundido. Despues de impreso se
sustituye la posicion en su diccionario por X y si fuera el final de la partida.
Si se falla, se sustituye y cambio de turno y los campos igual que si se acertase pero con un guion. Se hace cambio de turno.
En caso de repetir tirada se indica con un print y volverá a tocarle a quien haya tirado
'''
def disparo_coordenada(tablero_disparado, tablero_disparador): #realiza el disparo tanto de la máquina como del usuario.
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
        fila = random.randint(0, ALTO_TABLERO-1)
        columna = random.randint(0, ANCHO_TABLERO-1)
        coordenadas = [fila,columna]

    print(f"Intentando disparar a las coordenadas {fila} {columna}...")
    time.sleep(3)  # Aplicar un retraso de 5 segundos

    if tablero_disparado.tablero_usuario[fila, columna] == "O":
        tablero_disparado.tablero_usuario[fila, columna] = "X"
        tablero_disparador.tablero_maquina[fila,columna] = "X"
        tocado_hundido(tablero_disparado, coordenadas)
        coordenadas_tocadas(tablero_disparado,coordenadas)
        fin_partida = comprobacion_fin(tablero_disparado)
        if(fin_partida):
            imprimir_tablero(tablero_disparador.tablero_maquina)
            exit()
    elif tablero_disparado.tablero_usuario[fila, columna] == " ":
        tablero_disparado.tablero_usuario[fila, columna] = "-"
        tablero_disparador.tablero_maquina[fila,columna] = "-"
        print("¡Agua!, Disparo en agua")     
        if TURNO == 0:
            TURNO = 1 #definimos de quién es el turno, si del usuario o de la máquina
        else:
            TURNO = 0
    else:
        print("Ya habias disparado en esas coordenadas")
    

'''
Comprobacion de final
Si todos los elementos del diccionario del que ha sido disparado son X se termina el juego
'''      
def comprobacion_fin(tablero):
    todos_hundidos = all(all(posicion == 'X' for posicion in posiciones) for posiciones in tablero.dicc_barcos_usuario.values())
    if todos_hundidos == True:
        print("Se acabo el juego")
    return todos_hundidos

'''
Comprobacion de final
Si todos los elementos del barco en el diccionario del que ha sido disparado son X (a excepcion del que se acaba de disparar)
barco hundido, sino tocado
''' 
def tocado_hundido(tablero, coordenadas):
    coordenadas = tuple(map(int, coordenadas))
    for barcos, posiciones in tablero.dicc_barcos_usuario.items():
        if coordenadas in posiciones:
            todas_X = all((posicion == 'X') or (tablero.tablero_usuario[posicion] == 'X') for posicion in posiciones)
            if todas_X:
                print(f"Tocado y hundido el barco {barcos}")
            else:
                print(f"Tocado")

'''
Cambio de coordenadas a X en dicc
'''
def coordenadas_tocadas(tablero,coordenadas):
    fila = int(coordenadas[0])
    columna = int(coordenadas[1])
    for posiciones in tablero.dicc_barcos_usuario.values():
        if(fila,columna) in posiciones:
            posiciones[posiciones.index((fila, columna))] = 'X'

#entramos en diccionario y cambiamos la coordenada a X i.e. {'barco1': [[2,4],[2,5],[2,6]]} --> {'barco1': [X,X,X]}

'''
Comprobacion coordenadas
'''
def coordenadas_correctas(fila,columna):
    if 0 <= fila < ALTO_TABLERO and 0 <= columna < ANCHO_TABLERO:
        return True
    else:
        print("Coordenadas fuera de los límites del tablero. Introduce coordenadas válidas.")
        return False


'''
Bucle principal del juego
Disparo del que corresponda y prints de tablero
'''
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
    #TURNO = random.randint(0, 1) #la primera vez, tiene que ser random
    while True: 
        os.system('cls')  # Limpiar pantalla
        if TURNO == 0:  # Turno del jugador
            print('¡Tu turno!')
            disparo_coordenada(tablero_maquina, tablero_jugador)
            print("Aquí tienes el tablero de la máquina:")
            imprimir_tablero(tablero_jugador.tablero_maquina)
            print(tablero_maquina.dicc_barcos_usuario) #Ver barcos enemigos
            #print(tablero_maquina.tablero_maquina) #Ver tablero disparos del enemigo
            #print(tablero_jugador.tablero_maquina)
            time.sleep(3)  # Aplicar un retraso de 5 segundos
            input("Presiona Enter para continuar...")
        else:  # Turno de la máquina
            print('¡Es el turno de la máquina!')
            disparo_coordenada(tablero_jugador, tablero_maquina)
            print("Aquí tienes tu tablero:")
            #print(tablero_jugador.tablero_usuario)
            imprimir_tablero(tablero_jugador.tablero_usuario)
            time.sleep(3)  # Aplicar un retraso de 5 segundos
            input("Presiona Enter para continuar...")

'''
v2 impresion tablero
'''
def imprimir_tablero(tablero):
    letras = '0123456789'
    print("   " + " ".join(letras))
    for i, fila in enumerate(tablero):
        print(str(i).rjust(2) + '|' + '|'.join(fila) + '|')
        #for celda in fila:
    