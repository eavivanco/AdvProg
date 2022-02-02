import parametros
import random
import usuarios
import pistas
import formulas
import math
import funciones2

dicci_contr = {1: ''}
dicci_pist = {1: ''}


def nueva_partida_gen():
    print('Esta comenzando una nueva partida...')
    inicio_correcto = False
    nombre_correcto = False
    equipo_correcto = False
    tareos = 'Tareos'
    hibridos = 'Híbridos'
    docencios = 'Docencios'
    while not nombre_correcto:
        nombre = input('Ingresa un nombre de usuario! (Este debe ser alfanumerico)')
        valido = funciones2.unicidad_pil(nombre)
        n2 = nombre.strip().split()
        n3 = ''.join(n2)
        if n3.isalnum() and valido:
            nombre_correcto = True
            while not equipo_correcto:
                equipo = str(input('Elige tu equipo! \n'
                                   f'[1] {tareos}\n'
                                   f'[2] {hibridos}\n'
                                   f'[3] {docencios}'))
                if equipo == '1':
                    equipo_piloto = f'{tareos}'
                    equipo_correcto = True
                    inicio_correcto = True
                    personalidad = parametros.EQUIPOS['TAREOS']['PERSONALIDAD']
                    min_con = parametros.EQUIPOS['TAREOS']['CONTEXTURA']['MIN']
                    max_con = parametros.EQUIPOS['TAREOS']['CONTEXTURA']['MAX']
                    contextura = random.randint(min_con, max_con)
                    min_eq = parametros.EQUIPOS['TAREOS']['EQUILIBRIO']['MIN']
                    max_eq = parametros.EQUIPOS['TAREOS']['EQUILIBRIO']['MAX']
                    equilibrio = random.randint(min_eq, max_eq)
                    return inicio_correcto, nombre, contextura, equilibrio, \
                           personalidad, equipo_piloto
                elif equipo == '2':
                    equipo_piloto = f'{hibridos}'
                    equipo_correcto = True
                    inicio_correcto = True
                    personalidad = parametros.EQUIPOS['HIBRIDOS']['PERSONALIDAD']
                    min_con = parametros.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MIN']
                    max_con = parametros.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MAX']
                    contextura = random.randint(min_con, max_con)
                    min_eq = parametros.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MIN']
                    max_eq = parametros.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MAX']
                    equilibrio = random.randint(min_eq, max_eq)
                    return inicio_correcto, nombre, contextura, equilibrio, \
                           personalidad, equipo_piloto
                elif equipo == '3':
                    equipo_piloto = f'{docencios}'
                    equipo_correcto = True
                    inicio_correcto = True
                    personalidad = parametros.EQUIPOS['DOCENCIOS']['PERSONALIDAD']
                    min_con = parametros.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MIN']
                    max_con = parametros.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MAX']
                    contextura = random.randint(min_con, max_con)
                    min_eq = parametros.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN']
                    max_eq = parametros.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MAX']
                    equilibrio = random.randint(min_eq, max_eq)
                    return inicio_correcto, nombre, contextura, equilibrio, \
                           personalidad, equipo_piloto
                else:
                    print('Ingresaste un valor no valido, intentalo otra vez!')
        else:
            print('Ingresaste un nombre no valido, intentalo otra vez!')


def cargar_partida_gen(nombre_cargar):
    with open(parametros.PATHS['PILOTOS'], "r", encoding="UTF-8") as file:
        indice = 0
        for line in file:
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
                correcto = False
                if nombre_cargar == asignar[nombre]:
                    nom = asignar[nombre]
                    din = asignar[dinero]
                    per = asignar[personalidad]
                    cont = asignar[contextura]
                    equili = asignar[equilibrio]
                    exp = asignar[experiencia]
                    equip = asignar[equipo]
                    correcto = True
                    return correcto, nom, din, per, cont, equili, exp, equip
                else:
                    pass
        return correcto, correcto, correcto, correcto, correcto, correcto, correcto, correcto


def param_bicicletas():
    min_cha = parametros.BICICLETA['CHASIS']['MIN']
    max_cha = parametros.BICICLETA['CHASIS']['MAX']
    min_car = parametros.BICICLETA['CARROCERIA']['MIN']
    max_car = parametros.BICICLETA['CARROCERIA']['MAX']
    min_rue = parametros.BICICLETA['RUEDAS']['MIN']
    max_rue = parametros.BICICLETA['RUEDAS']['MAX']
    min_mot = parametros.BICICLETA['MOTOR']['MIN']
    max_mot = parametros.BICICLETA['MOTOR']['MAX']
    min_pes = parametros.BICICLETA['PESO']['MIN']
    max_pes = parametros.BICICLETA['PESO']['MAX']
    cha = random.randint(min_cha, max_cha)
    car = random.randint(min_car, max_car)
    rue = random.randint(min_rue, max_rue)
    mot = random.randint(min_mot, max_mot)
    pes = random.randint(min_pes, max_pes)

    return cha, car, rue, mot, pes


def param_motocicletas():
    min_cha = parametros.MOTOCICLETA['CHASIS']['MIN']
    max_cha = parametros.MOTOCICLETA['CHASIS']['MAX']
    min_car = parametros.MOTOCICLETA['CARROCERIA']['MIN']
    max_car = parametros.MOTOCICLETA['CARROCERIA']['MAX']
    min_rue = parametros.MOTOCICLETA['RUEDAS']['MIN']
    max_rue = parametros.MOTOCICLETA['RUEDAS']['MAX']
    min_mot = parametros.MOTOCICLETA['MOTOR']['MIN']
    max_mot = parametros.MOTOCICLETA['MOTOR']['MAX']
    min_pes = parametros.MOTOCICLETA['PESO']['MIN']
    max_pes = parametros.MOTOCICLETA['PESO']['MAX']
    cha = random.randint(min_cha, max_cha)
    car = random.randint(min_car, max_car)
    rue = random.randint(min_rue, max_rue)
    mot = random.randint(min_mot, max_mot)
    pes = random.randint(min_pes, max_pes)

    return cha, car, rue, mot, pes


def param_troncomovil():
    min_cha = parametros.TRONCOMOVIL['CHASIS']['MIN']
    max_cha = parametros.TRONCOMOVIL['CHASIS']['MAX']
    min_car = parametros.TRONCOMOVIL['CARROCERIA']['MIN']
    max_car = parametros.TRONCOMOVIL['CARROCERIA']['MAX']
    min_rue = parametros.TRONCOMOVIL['RUEDAS']['MIN']
    max_rue = parametros.TRONCOMOVIL['RUEDAS']['MAX']
    min_mot = parametros.TRONCOMOVIL['MOTOR']['MIN']
    max_mot = parametros.TRONCOMOVIL['MOTOR']['MAX']
    min_pes = parametros.TRONCOMOVIL['PESO']['MIN']
    max_pes = parametros.TRONCOMOVIL['PESO']['MAX']
    cha = random.randint(min_cha, max_cha)
    car = random.randint(min_car, max_car)
    rue = random.randint(min_rue, max_rue)
    mot = random.randint(min_mot, max_mot)
    pes = random.randint(min_pes, max_pes)

    return cha, car, rue, mot, pes


def param_automovil():
    min_cha = parametros.AUTOMOVIL['CHASIS']['MIN']
    max_cha = parametros.AUTOMOVIL['CHASIS']['MAX']
    min_car = parametros.AUTOMOVIL['CARROCERIA']['MIN']
    max_car = parametros.AUTOMOVIL['CARROCERIA']['MAX']
    min_rue = parametros.AUTOMOVIL['RUEDAS']['MIN']
    max_rue = parametros.AUTOMOVIL['RUEDAS']['MAX']
    min_mot = parametros.AUTOMOVIL['MOTOR']['MIN']
    max_mot = parametros.AUTOMOVIL['MOTOR']['MAX']
    min_pes = parametros.AUTOMOVIL['PESO']['MIN']
    max_pes = parametros.AUTOMOVIL['PESO']['MAX']
    cha = random.randint(min_cha, max_cha)
    car = random.randint(min_car, max_car)
    rue = random.randint(min_rue, max_rue)
    mot = random.randint(min_mot, max_mot)
    pes = random.randint(min_pes, max_pes)

    return cha, car, rue, mot, pes


def cargar_contrincantes_gen():
    with open(parametros.PATHS['CONTRINCANTES'], "r", encoding="UTF-8") as file:
        indice = 0
        for line in file:
            if indice == 0:
                uno, dos, tres, cuatro, cinco, seis, siete = line.strip().split(",")
                elementos = [uno, dos, tres, cuatro, cinco, seis, siete]
                nombre = elementos.index('Nombre')
                nivel = elementos.index('Nivel')
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
                niv = asignar[nivel]
                per = asignar[personalidad]
                cont = asignar[contextura]
                equili = asignar[equilibrio]
                exp = asignar[experiencia]
                equip = asignar[equipo]
                autos_contr = []
                with open(parametros.PATHS['VEHICULOS'], "r", encoding="UTF-8") as file2:
                    indice2 = 0
                    for line2 in file2:
                        if indice2 == 0:
                            un, do, tre, cuatr, cinc, sei, siet, och = line2.strip().split(",")
                            element = [un, do, tre, cuatr, cinc, sei, siet, och]
                            nombr = element.index('Nombre')
                            duen = element.index('Dueño')
                            cat = element.index('Categoría')
                            cha = element.index('Chasis')
                            car = element.index('Carrocería')
                            rue = element.index('Ruedas')
                            mot = element.index('Motor o Zapatillas')
                            pes = element.index('Peso')
                            indice2 += 1
                        else:
                            un, do, tre, cuatr, cinc, sei, siet, och = line2.strip().split(",")
                            asignar2 = [un, do, tre, cuatr, cinc, sei, siet, och]
                            nom2 = asignar2[nombr]
                            duen2 = asignar2[duen]
                            cat2 = asignar2[cat]
                            cha2 = asignar2[cha]
                            car2 = asignar2[car]
                            rue2 = asignar2[rue]
                            mot2 = asignar2[mot]
                            pes2 = asignar2[pes]
                            if duen2 == nom:
                                autos_contr.append([nom2, duen2, cat2, cha2, car2, rue2, mot2,
                                                    pes2])
                                auto_final = random.choice(autos_contr)
                                dicci_contr[indice] = [nom, niv, per, cont, equili, exp, equip,
                                                       auto_final, 0, 0]
                            else:
                                pass
                    indice += 1


def cargar_pista():
    with open(parametros.PATHS['PISTAS'], "r", encoding="UTF-8") as file:
        indice = 0
        for line in file:
            if indice == 0:
                uno, dos, tres, cuatro, cinco, seis, siete, ocho = line.strip().split(",")
                elementos = [uno, dos, tres, cuatro, cinco, seis, siete, ocho]
                nombre = elementos.index('Nombre')
                tipo = elementos.index('Tipo')
                hielo = elementos.index('Hielo')
                rocas = elementos.index('Rocas')
                dificultad = elementos.index('Dificultad')
                num_vuel = elementos.index('NúmeroVueltas')
                contri = elementos.index('Contrincantes')
                larg = elementos.index('LargoPista')
                indice += 1
            else:
                uno, dos, tres, cuatro, cinco, seis, siete, ocho = line.strip().split(",")
                asignar = [uno, dos, tres, cuatro, cinco, seis, siete, ocho]
                nom = asignar[nombre]
                tip = asignar[tipo]
                hie = asignar[hielo]
                roc = asignar[rocas]
                difi = asignar[dificultad]
                num = asignar[num_vuel]
                con = asignar[contri]
                lar = asignar[larg]
                dicci_pist[indice] = [nom, tip, hie, roc, difi, num, con, lar]
                indice += 1

    elegido = random.randint(1, len(dicci_pist))
    return dicci_pist[elegido][0], dicci_pist[elegido][1], dicci_pist[elegido][2], \
           dicci_pist[elegido][3], dicci_pist[elegido][4], dicci_pist[elegido][5], \
           dicci_pist[elegido][6], dicci_pist[elegido][7]


def iniciar_pista(nom_pis, tip_pis, hie_pis, roc_pis, dif_pis, num_pis, con_pis, lar_pis):
    if tip_pis == 'pista hielo':
        pista = pistas.PistaHielo(nom_pis, tip_pis, hie_pis, 0, dif_pis, num_pis, con_pis, lar_pis)
        return pista
    if tip_pis == 'pista rocosa':
        pista = pistas.PistaHielo(nom_pis, tip_pis, 0, roc_pis, dif_pis, num_pis, con_pis, lar_pis)
        return pista
    if tip_pis == 'pista suprema':
        pista = pistas.PistaHielo(nom_pis, tip_pis, hie_pis, roc_pis, dif_pis, num_pis,
                                  con_pis, lar_pis)
        return pista


def cargar_contrincantes_pis(contr_pista):
    random.shuffle(contr_pista)
    contrincantes_final = []
    num_contr = 0
    max_contr = min(len(contr_pista), parametros.NUMERO_CONTRINCANTES)
    for elemento in contr_pista:
        indice = 1
        while indice < len(dicci_contr) and num_contr <= max_contr:
            if elemento == dicci_contr[indice][0]:
                contrincantes_final.append(dicci_contr[indice])
                num_contr += 1
            else:
                pass
            indice += 1

    return contrincantes_final


def posiciones_carrera(piloto, pr_veh, contrincantes, pista, vuelta, tiempo_total_piloto):
    dur_max_car = pr_veh.dur_max
    tiempos_contr = []
    hipotermia = formulas.hipotermia(vuelta, piloto.contextura, pista)
    dificultad_control = formulas.dificultad_control(pr_veh.categoria, piloto.personalidad,
                                                     piloto.equilibrio, pr_veh.peso)
    velocidad_recomendada = formulas.velocidad_recomendada(pr_veh.motor, pr_veh.ruedas,
                                                           pista.hielo, pr_veh.carroceria,
                                                           pista.rocas, piloto.experiencia,
                                                           pista.dif)
    velocidad_intencional = formulas.velocidad_intencional(velocidad_recomendada,
                                                           piloto.personalidad)
    velocidad_real = formulas.velocidad_real(velocidad_intencional, dificultad_control, hipotermia)
    tiempo_piloto = formulas.tiempo_vuelta(pista.largo, velocidad_real)
    tiempo_total_piloto += tiempo_piloto
    piloto.tiempo = tiempo_piloto
    piloto.tiempo_total += tiempo_piloto
    accidente = formulas.probabilidad_accidente(velocidad_real, velocidad_recomendada,
                                                dur_max_car, pr_veh.carroceria)
    for elemento in contrincantes:
        hipotermia_con = formulas.hipotermia(vuelta, elemento[3], pista)
        dificultad_control_con = formulas.dificultad_control(elemento[7][2], elemento[2],
                                                             elemento[4], elemento[7][7])
        velocidad_recomendada_con = formulas.velocidad_recomendada(elemento[7][6], elemento[7][5],
                                                                   pista.hielo, elemento[7][4],
                                                                   pista.rocas, elemento[5],
                                                                   pista.dif)
        velocidad_intencional_con = formulas.velocidad_intencional(velocidad_recomendada_con,
                                                                   elemento[2])
        velocidad_real_con = formulas.velocidad_real(velocidad_intencional_con,
                                                     dificultad_control_con, hipotermia_con)
        tiempo_con = formulas.tiempo_vuelta(pista.largo, velocidad_real_con)
        tiempos_contr.append(tiempo_con)
        elemento[8] = tiempo_con
        elemento[9] += tiempo_con



    return tiempo_piloto, tiempo_total_piloto, accidente, tiempos_contr

def murio(accidente):
    max_indice = math.floor(accidente * 100)
    salvavidas = 100 - math.ceil(accidente * 100)
    indice = 0
    oraculo = []
    while indice <= max_indice:
        oraculo.append(1)
        indice += 1
    indice_salva = 0
    while indice_salva <= salvavidas:
        oraculo.append(0)
        indice_salva += 1
    random.shuffle(oraculo)
    mano_invisible_adam_smith = random.choice(oraculo)
    final = mano_invisible_adam_smith

    return False




