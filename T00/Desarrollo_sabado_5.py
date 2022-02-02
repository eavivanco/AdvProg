###################### Import ###################
import random
import parametros
import tablero
import math
import os

###################### Import ###################

def datos_tab():
    largo_valido = False
    ancho_valido = False
    while largo_valido == False:
        N = int(input("Ingresa el largo de tu tablero. Debe ser un número entero entre 3 y 15"))
        if N >= 3 and N <= 15 and type(N) == int:
            largo = N
            largo_valido = True
            print("El largo ingresado es valido!\n")
        else:
            print("El largo ingresado no es valido, por favor intenta otra vez\n")
            largo_valido = False

    while ancho_valido == False:
        M = int(input("Ingresa el ancho de tu tablero. Debe ser un número entero entre 3 y 15"))
        if M >= 3 and M <= 15 and type(M) == int:
            ancho = M
            ancho_valido = True
            print("El ancho ingresado es valido!\n")
        else:
            print("El ancho ingresado no es valido, por favor intenta otra vez\n")
            ancho_valido = False

    return largo, ancho


## Muestra el ranking actual
ranking = ["Esteban", "Pelao", "Daniel", "Cla"]


def ver_ranking():
    puntajes = open("puntajes.txt", "r")
    contador = 0
    for linea in puntajes:
        print(linea)
        contador += 1
        if contador == 10:
            break


## Crea tablero
def crear_tablero(largo, ancho):
    lista_fila = []
    columna = 1
    fila = 1
    while fila <= ancho:
        while columna <= largo:
            lista_fila.append(columna)
            columna += 1
        mi_tab.append(lista_fila)
        lista_fila = []
        columna = 1
        fila += 1

def crear_tablero_usuario(largo, ancho):
    lista_fila = []
    columna = 1
    fila = 1
    while fila <= ancho:
        while columna <= largo:
            lista_fila.append(' ')
            columna += 1
        usuario_tab.append(lista_fila)
        lista_fila = []
        columna = 1
        fila += 1


## Imprime tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)


## Carga partida
def cargar_partida(nombre):
    mi_tab = []
    print("Bienvenido otra vez {}".format(nombre))
    partida = open("partidas/{}.txt".format(nombre))
    for fila in partida:
        print(fila+"\n")
        mi_tab.append(fila)
        print(mi_tab)
    tablero.print_tablero(mi_tab, utf8=True)





## Guardar partida

def guardar_partida(nombre,tablero):
    partida = open("partidas/{}.txt".format(nombre),"w")
    for linea in tablero:
        partida.write("{}".format(linea))
    partida.close()

## Menu Inicio##

mi_tab = []
usuario_tab = []
def iniciar_partida():
    opciones = "[1] Crear partida\n[2] Cargar partida\n[3] Ver ranking\n[0] Salir\nMi respuesta ->"
    inicio_correcto = False
    while inicio_correcto == False:
        tipo_partida = str(input(
            "Seleccione una opcion:\n" + opciones))
        ####################### INICIAR PARTIDA ######################
        if tipo_partida == "1":
            con_vida = "si"
            inicio_correcto = True
            print("\nDecidiste iniciar una nueva partida, buena suerte!")
            nombre_usuario = str(input("Escribe un nombre de usuario aquí"))
            largo, ancho = datos_tab()
            L = largo * ancho * parametros.PROB_LEGO
            max_leg = math.ceil(L)
            crear_tablero(largo, ancho)
            crear_tablero_usuario(largo, ancho)
            agregar_leg(mi_tab, ancho, L)
            agregar_num(mi_tab, ancho, largo)
            print("Bienvenido a una nueva partida!")
            tablero.print_tablero(usuario_tab, utf8=True)
            movimientos = 0
            while con_vida == "si":
                con_vida = jugar(usuario_tab, mi_tab, ancho, largo)
                movimientos += 1
                if con_vida == "guardar":
                    guardar_partida(nombre_usuario, "{} \n {}".format(mi_tab, usuario_tab))
                    print("La partida ha sido guardada como {}".format(nombre_usuario))
            puntaje_final = max_leg * movimientos * parametros.POND_PUNT
            print("\nGracias por jugar! Tu puntaje es {}".format(puntaje_final))

            ################################# GUARDAR PARTIDA #######################

        ####################### INICIAR PARTIDA ######################

        ####################### CARGAR PARTIDA ######################
        elif tipo_partida == "2":
            inicio_correcto = True
            print("\nDecidiste cargar una partida existente, buena suerte!")
            mensaje_cargar = "Escribe el nombre de usuario con el que guardaste la partida"
            nombre_usuario = str(input(mensaje_cargar))
            if os.path.isfile("partidas/{}.txt".format(nombre_usuario)):
                cargar_partida(nombre_usuario)
            else:
                print("Esta partida no existe, intenta otra vez")
        ####################### CARGAR PARTIDA ######################
        elif tipo_partida == "3":
            inicio_correcto = True
            print("\nEl ranking de los 10 mejores puntajes es el siguiente:\n")
            ver_ranking()
        elif tipo_partida == "0":
            inicio_correcto = True
            print("\nDecidiste abandonar el menu, esperamos verte pronto!")
        else:
            print("\nPor favor elige una de las alternativas disponibles\n")

## Agrega legos al tablero
def agregar_leg(mi_tab, ancho,L):
    cant_leg = 0
    sub = 0
    max_leg = int(math.ceil(L))
    agregar_valido = False
    while agregar_valido == False:
        mi_tab[0].append('L')
        random.shuffle(mi_tab[0])
        mi_tab[0].pop()
        random.shuffle(mi_tab[0])
        random.shuffle(mi_tab)
        while sub <=ancho - 1:
            cant_leg += mi_tab[sub].count('L')
            sub += 1
        sub = 0
        if cant_leg == max_leg:
            agregar_valido = True
            cant_leg = 0
        else:
            cant_leg = 0

def agregar_num(tablero, ancho, largo):
    elem_lista = 0
    elem_sublista = 0
    while elem_lista < ancho:
        while elem_sublista < largo:
            if tablero[elem_lista][elem_sublista] != 'L':
                insertar_num_correcto(tablero, elem_lista, elem_sublista, ancho, largo)
            elem_sublista += 1
        elem_sublista = 0
        elem_lista += 1


def insertar_num_correcto(tablero, elem_lista, elem_sublista, ancho, largo):
    legos_cerca = 0
    if elem_lista == 0:
        if elem_sublista == 0:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
        elif elem_sublista == largo - 1:
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
        else:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
        tablero[elem_lista].pop(elem_sublista)
        tablero[elem_lista].insert(elem_sublista, legos_cerca)
    elif elem_lista == ancho - 1:
        if elem_sublista == 0:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
        elif elem_sublista == largo - 1:
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
        else:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
        tablero[elem_lista].pop(elem_sublista)
        tablero[elem_lista].insert(elem_sublista, legos_cerca)

    else:
        if elem_sublista == 0:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
        elif elem_sublista == largo - 1:
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
        else:
            if tablero[elem_lista][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista + 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista - 1] == 'L':
                legos_cerca += 1
            if tablero[elem_lista - 1][elem_sublista + 1] == 'L':
                legos_cerca += 1
        tablero[elem_lista].pop(elem_sublista)
        tablero[elem_lista].insert(elem_sublista, legos_cerca)

def pos_valida(ancho, largo):
    eleccion_correcta = False
    while eleccion_correcta == False:
        principio = "Ingresa el numero de la fila de la posicion que quieres descubrir"
        guardar = "\nSi quieres guardar la partida ingresa el numero 100"
        fila_elegida = int(input(principio + guardar))

        if fila_elegida == 100:
            eleccion_correcta = True
            return fila_elegida, fila_elegida
        columna_ingresada = str(input("Ingresa la columna de la posicion que quieres descubrir"))
        col_ele = reg_col(columna_ingresada)
        if col_ele <= largo and col_ele >= 0 and fila_elegida <= ancho and fila_elegida >= 0:
            eleccion_correcta = True
            return fila_elegida, col_ele
        else:
            eleccion_correcta = False
            print("Las coordenadas ingresadas no son validas! Intenta otra vez")


def reg_col(columna_ingresada):
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
    letras2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
    if columna_ingresada in letras:
        col_ele = letras.index(str(columna_ingresada))
    elif columna_ingresada in letras2:
        col_ele = letras2.index(str(columna_ingresada))
    else:
        col_ele = 55

    return col_ele

def jugar(usuario_tab, mi_tab, ancho, largo):
    fila_elegida, col_ele = pos_valida(ancho, largo)
    if fila_elegida == 100:
        con_vida = "guardar"
        return con_vida
    if mi_tab[fila_elegida][col_ele] == 'L':
        print("Perdiste! Te has encontrado con un Lego, suerte la proxima vez")
        tablero.print_tablero(mi_tab, utf8=True)
        con_vida = "no"
        return con_vida
    else:
        usuario_tab[fila_elegida].pop(col_ele)
        usuario_tab[fila_elegida].insert(col_ele, mi_tab[fila_elegida][col_ele])
        tablero.print_tablero(usuario_tab, utf8=True)
        con_vida = "si"
        return con_vida





## ancho -> numero de sublistas
## largo -> tamano sublista
############################### PROGRAMA ###############################

iniciar_partida()
