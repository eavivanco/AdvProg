import funciones
import formulas
import parametros
import random


def una_vuelta(piloto, pr_veh, contrincantes, pista, vuelta, tiempo_total_piloto):
    tiempo_piloto, tiempo_total_piloto, accidente, tiempos_contr = \
        funciones.posiciones_carrera(piloto, pr_veh, contrincantes, pista, vuelta,
                                     tiempo_total_piloto)
    dano_recibido = formulas.dano_recibido_cada_vuelta(pista.rocas, pr_veh.carroceria)
    pr_veh.carroceria -= dano_recibido
    accidente_final = funciones.murio(accidente)
    ventaja_con_ultimo_lugar, gana_piloto = ventaja(tiempo_piloto, tiempos_contr)
    dinero = formulas.dinero_vuelta_x(vuelta, pista.dif)
    dinero_ganador = formulas.dinero_ganador(pista.vueltas, pista.dif, pista.hielo, pista.rocas)
    experiencia = formulas.experiencia_recibida(piloto.personalidad, ventaja_con_ultimo_lugar,
                                                pista.dif)

    piloto.dinero += int(dinero)
    ventaja_final, gana_piloto = ventaja(tiempo_piloto, tiempos_contr)

    if gana_piloto:
        print('Esta vuelta el primer puesto es tuyo!')
        piloto.dinero += dinero_ganador
        piloto.experiencia += experiencia

    lugares = ordenar_lugares(piloto, tiempo_piloto, tiempos_contr, contrincantes)

    return tiempo_piloto, tiempo_total_piloto, accidente_final, lugares


def ventaja(tiempo_piloto, tiempos_contr):
    for tiempo in tiempos_contr:
        if tiempo <= tiempo_piloto:
            ventaja_final = 0
            gana_piloto = False
            return ventaja_final, gana_piloto

    gana_piloto = True
    tiempos_contr.sort(reverse=True)
    ventaja_final = tiempos_contr[0] - tiempo_piloto
    return ventaja_final, gana_piloto


def ordenar_lugares(piloto, tiempo_piloto, tiempos_contr, contrincantes):
    lugares = []
    corredores = []
    for elemento in contrincantes:
        corredores.append(elemento)
    corredores.append([piloto.nombre, '', '', '', '', '', '', '', piloto.tiempo,
                       piloto.tiempo_total])
    tiempos_gen = tiempos_contr
    tiempos_gen.append(tiempo_piloto)
    tiempos_gen.sort()
    lugar = 0
    while lugar < len(tiempos_gen):
        for elemento in corredores:
            if int(elemento[8]) == int(tiempos_gen[lugar]):
                lugares.append([lugar + 1, elemento[0], elemento[8], elemento[9]])
                lugar += 1
            else:
                lugar += 1
                pass
    lug = 1
    for ele in lugares:
        ele[0] = lug
        lug += 1

    return lugares

def printear_lugares(lugares, vuelta, vuelta_max):
    print(f'Vuelta {vuelta} de {vuelta_max}\nLas posiciones son las siguientes!\n')
    print(f'Lugar - Corredor - Tiempo vuelta - Tiempo total')
    for lugar in lugares:
        print(f'{lugar[0]} - {lugar[1]} - {lugar[2]} seg - {lugar[3]} seg')

def guardar_partida(piloto):
    with open(parametros.PATHS['PILOTOS'], "r", encoding="UTF-8") as base:
        indice = 0
        lista_base = []
        for line in base:
            if indice == 0:
                uno, dos, tres, cuatro, cinco, seis, siete = line.strip().split(",")
                elementos = [uno, dos, tres, cuatro, cinco, seis, siete]
                nombre = elementos.index('Nombre')
                dinero = elementos.index('Dinero')
                personalidad = elementos.index('Personalidad')
                contextura = elementos.index('Contextura')
                equilibrio = elementos.index('Equilibrio')
                experiencia = elementos.index('Experiencia')
                equipo = elementos.index('Equipo')
                indice += 1
            else:
                uno, dos, tres, cuatro, cinco, seis, siete = line.strip().split(",")
                asignar = [uno, dos, tres, cuatro, cinco, seis, siete]
                nom = asignar[nombre]
                din = asignar[dinero]
                per = asignar[personalidad]
                cont = asignar[contextura]
                equili = asignar[equilibrio]
                exp = asignar[experiencia]
                equip = asignar[equipo]
                lista_base.append([nom, din, per, cont, equili, exp, equip])
    with open(parametros.PATHS['PILOTOS'], "w", encoding="UTF-8") as file:
        file.write('Nombre,Dinero,Personalidad,Contextura,Equilibrio,Experiencia,Equipo\n')
        for elemento in lista_base:
            junto = ','.join(elemento)
            file.write(f'{junto}\n')
        file.write(f'{piloto.nombre},{piloto.dinero},{piloto.personalidad},'
                   f'{piloto.contextura},{piloto.equilibrio},{piloto.experiencia},{piloto.equipo}')

def unicidad_pil(nombre):
    unico = True
    with open(parametros.PATHS['PILOTOS'], "r", encoding="UTF-8") as file:
        for line in file:
            if nombre == line[0]:
                unico = False

    return unico


def unicidad_veh(nombre):
    unico = True
    with open(parametros.PATHS['VEHICULOS'], "r", encoding="UTF-8") as file:
        for line in file:
            if nombre == line[0]:
                unico = False

    return unico


def reiniciar_tiempos(contrincantes):
    for elemento in contrincantes:
        elemento[8] = 0
        elemento[9] = 0

def guardar_auto(piloto):
    with open(parametros.PATHS['VEHICULOS'], "r", encoding="UTF-8") as base:
        indice = 0
        lista_base = []
        for line in base:
            if indice == 0:
                uno, dos, tres, cuatro, cinco, seis, siete, ocho = line.strip().split(",")
                elementos = [uno, dos, tres, cuatro, cinco, seis, siete, ocho]
                nombre = elementos.index('Nombre')
                due = elementos.index('Dueño')
                cat = elementos.index('Categoría')
                cha = elementos.index('Chasis')
                car = elementos.index('Carrocería')
                rue = elementos.index('Ruedas')
                mot = elementos.index('Motor o Zapatillas')
                pes = elementos.index('Peso')
                indice += 1
            else:
                uno, dos, tres, cuatro, cinco, seis, siete, ocho = line.strip().split(",")
                asignar = [uno, dos, tres, cuatro, cinco, seis, siete, ocho]
                nom = asignar[nombre]
                din = asignar[due]
                per = asignar[cat]
                cont = asignar[cha]
                equili = asignar[car]
                exp = asignar[rue]
                equip = asignar[mot]
                peso = asignar[pes]
                lista_base.append([nom, din, per, cont, equili, exp, equip, peso])
    with open(parametros.PATHS['VEHICULOS'], "w", encoding="UTF-8") as file:
        file.write('Nombre,Dueño,Categoría,Chasis,Carrocería,Ruedas,Motor o Zapatillas,Peso\n')
        for elemento in lista_base:
            junto = ','.join(elemento)
            file.write(f'{junto}\n')
        file.write(f'{piloto.vehiculos.nombre},{piloto.vehiculos.dueno},'
                   f'{piloto.vehiculos.categoria},{piloto.vehiculos.chasis},'
                   f'{piloto.vehiculos.carroceria},{piloto.vehiculos.ruedas},'
                   f'{piloto.vehiculos.motor},{piloto.vehiculos.peso}')

