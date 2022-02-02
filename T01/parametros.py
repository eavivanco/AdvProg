# Valores máximos y mínimos de las partes y el peso de los vehículos

import math
import random
import menus


# Paths de los archivos

PATHS = {
    'PISTAS': 'pistas.csv',
    'CONTRINCANTES': 'contrincantes.csv',
    'PILOTOS': 'pilotos.csv',
    'VEHICULOS': 'vehículos.csv',
    'CONTRINCANTES2': 'contrincantes2.csv'
}

def contri():
    with open(PATHS['CONTRINCANTES'], "r", encoding="UTF-8") as file:
        indice = 0
        contr = []
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
                contr.append([nom, niv, per, cont, equili, exp, equip])
    return contr


contr = contri()

def cont_contr(contr):
    osados = 0
    precavidos = 0
    for elemento in contr:
        if elemento[2] == 'precavido':
            precavidos += 1
        elif elemento[2] == 'osado':
            osados += 1

    return osados, precavidos


osados, precavidos = cont_contr(contr)

with open(PATHS['VEHICULOS'], "r", encoding="UTF-8") as file:
    cant_au = 0
    cant_tro = 0
    cant_mot = 0
    cant_bi = 0
    tot_cha_au = 0
    tot_car_au = 0
    tot_rue_au = 0
    tot_mot_au = 0
    tot_pes_au = 0
    tot_cha_tro = 0
    tot_car_tro = 0
    tot_rue_tro = 0
    tot_mot_tro = 0
    tot_pes_tro = 0
    tot_cha_mot = 0
    tot_car_mot = 0
    tot_rue_mot = 0
    tot_mot_mot = 0
    tot_pes_mot = 0
    tot_cha_bi = 0
    tot_car_bi = 0
    tot_rue_bi = 0
    tot_mot_bi = 0
    tot_pes_bi = 0
    indice = 1
    for line in file:
        if indice == 1:
            uno, dos, tres, cuatro, cinco, seis, siete, ocho = line.strip().split(",")
            elementos = [uno, dos, tres, cuatro, cinco, seis, siete, ocho]
            nom = elementos.index('Nombre')
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
            if 'auto' in asignar[cat]:
                tot_cha_au += int(asignar[cha])
                tot_car_au += int(asignar[car])
                tot_rue_au += int(asignar[rue])
                tot_mot_au += int(asignar[mot])
                tot_pes_au += int(asignar[pes])
                cant_au += 1
            elif 'tronco' in asignar[cat]:
                tot_cha_tro += int(asignar[cha])
                tot_car_tro += int(asignar[car])
                tot_rue_tro += int(asignar[rue])
                tot_mot_tro += int(asignar[mot])
                tot_pes_tro += int(asignar[pes])
                cant_tro += 1
            elif 'mot' in asignar[cat]:
                tot_cha_mot += int(asignar[cha])
                tot_car_mot += int(asignar[car])
                tot_rue_mot += int(asignar[rue])
                tot_mot_mot += int(asignar[mot])
                tot_pes_mot += int(asignar[pes])
                cant_mot += 1
            elif 'bici' in asignar[cat]:
                tot_cha_bi += int(asignar[cha])
                tot_car_bi += int(asignar[car])
                tot_rue_bi += int(asignar[rue])
                tot_mot_bi += int(asignar[mot])
                tot_pes_bi += int(asignar[pes])
                cant_bi += 1
            indice += 1

tot_car_gen = tot_car_au + tot_car_bi + tot_car_mot + tot_car_tro
tot_cha_gen = tot_cha_au + tot_cha_bi + tot_cha_mot + tot_cha_tro
tot_rue_gen = tot_rue_au + tot_rue_bi + tot_rue_mot + tot_rue_tro
tot_mot_gen = tot_mot_au + tot_mot_bi + tot_mot_mot + tot_mot_tro
tot_pes_gen = tot_pes_au + tot_pes_bi + tot_pes_mot + tot_pes_tro
tot_cant = cant_au + cant_bi + cant_mot + cant_tro


AUTOMOVIL = {
    'CHASIS': {
        'MIN': math.ceil((tot_cha_au / cant_au) / 1.4),
        'MAX': math.ceil((tot_cha_au / cant_au) * 1.4)
    },
    'CARROCERIA': {
        'MIN': math.ceil((tot_car_au / cant_au) / 1.4),
        'MAX': math.ceil((tot_car_au / cant_au) * 1.4)
    },
    'RUEDAS': {
        'MIN': math.ceil((tot_rue_au / cant_au) / 1.4),
        'MAX': math.ceil((tot_rue_au / cant_au) * 1.4)
    },
    'MOTOR': {
        'MIN': math.ceil((tot_mot_au / cant_au / 1.4)),
        'MAX': math.ceil((tot_mot_au / cant_au) * 1.4)
    },
    'ZAPATILLAS': {
        'MIN': math.ceil((tot_mot_au / cant_au) / 1.4),
        'MAX': math.ceil((tot_mot_au / cant_au) * 1.4)
    },
    'PESO': {
        'MIN': math.ceil((tot_pes_au / cant_au)),
        'MAX': math.ceil((tot_pes_au / cant_au) * 1.4)
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': math.ceil((tot_cha_tro / cant_tro) / 1.4),
        'MAX': math.ceil((tot_cha_tro / cant_tro) * 1.4)
    },
    'CARROCERIA': {
        'MIN': math.ceil((tot_car_tro / cant_tro) / 1.4),
        'MAX': math.ceil((tot_car_tro / cant_tro) * 1.4)
    },
    'RUEDAS': {
        'MIN': math.ceil((tot_rue_tro / cant_tro) / 1.4),
        'MAX': math.ceil((tot_rue_tro / cant_tro) * 1.4)
    },
    'MOTOR': {
        'MIN': math.ceil((tot_mot_tro / cant_tro) / 1.4),
        'MAX': math.ceil((tot_mot_tro / cant_tro) * 1.4)
    },
    'ZAPATILLAS': {
        'MIN': math.ceil((tot_mot_tro / cant_tro) / 1.4),
        'MAX': math.ceil((tot_mot_tro / cant_tro) * 1.4)
    },
    'PESO': {
        'MIN': math.ceil((tot_pes_tro / cant_tro)) ,
        'MAX': math.ceil((tot_pes_tro / cant_tro) * 1.4)
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': math.ceil((tot_cha_mot / cant_mot) / 1.4),
        'MAX': math.ceil((tot_cha_mot / cant_mot) * 1.4)
    },
    'CARROCERIA': {
        'MIN': math.ceil((tot_car_mot / cant_mot) / 1.4),
        'MAX': math.ceil((tot_car_mot / cant_mot) * 1.4)
    },
    'RUEDAS': {
        'MIN': math.ceil((tot_rue_mot / cant_mot) / 1.4),
        'MAX': math.ceil((tot_rue_mot / cant_mot) * 1.4)
    },
    'MOTOR': {
        'MIN': math.ceil((tot_mot_mot / cant_mot) / 1.4),
        'MAX': math.ceil((tot_mot_mot / cant_mot) * 1.4)
    },
    'ZAPATILLAS': {
        'MIN': math.ceil((tot_mot_mot / cant_mot) / 1.4),
        'MAX': math.ceil((tot_mot_mot / cant_mot) * 1.4)
    },
    'PESO': {
        'MIN': math.ceil((tot_pes_mot / cant_mot)),
        'MAX': math.ceil((tot_pes_mot / cant_mot) * 1.4)
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': math.ceil((tot_cha_bi / cant_bi) / 1.4),
        'MAX': math.ceil((tot_cha_bi / cant_bi) * 1.4)
    },
    'CARROCERIA': {
        'MIN': math.ceil((tot_car_bi / cant_bi) / 1.4),
        'MAX': math.ceil((tot_car_bi / cant_bi) * 1.4)
    },
    'RUEDAS': {
        'MIN': math.ceil((tot_rue_bi / cant_bi) / 1.4),
        'MAX': math.ceil((tot_rue_bi / cant_bi) * 1.4)
    },
    'MOTOR': {
        'MIN': math.ceil((tot_mot_bi / cant_bi) / 1.4),
        'MAX': math.ceil((tot_mot_bi / cant_bi) * 1.4)
    },
    'ZAPATILLAS': {
        'MIN': math.ceil((tot_mot_bi / cant_bi) / 1.4),
        'MAX': math.ceil((tot_mot_bi / cant_bi) * 1.4)
    },
    'PESO': {
        'MIN': math.ceil((tot_pes_bi / cant_bi)) ,
        'MAX': math.ceil((tot_pes_bi / cant_bi) * 1.4)
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 150,
        'EFECTO': math.ceil(tot_cha_gen / (tot_cant * 2))
    },
    'CARROCERIA': {
        'COSTO': 250,
        'EFECTO': math.ceil(tot_car_gen / (tot_cant * 2))
    },
    'RUEDAS': {
        'COSTO': 150,
        'EFECTO': math.ceil(tot_rue_gen / (tot_cant * 2))
    },
    'MOTOR': {
        'COSTO': 400,
        'EFECTO': math.ceil(tot_mot_gen / (tot_cant * 2))
    },
    'ZAPATILLAS': {
        'COSTO': 400,
        'EFECTO': math.ceil(tot_mot_gen / (tot_cant * 2))
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': 'precavido'
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': random.choice(['osado', 'precavido'])
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': 'osado'
    }
}


NUMERO_CONTRINCANTES = random.randint(1, 10)
# Velocidad real
VELOCIDAD_MINIMA = math.floor(tot_mot_gen / (2 * tot_cant))

# Velocidad intencional
EFECTO_OSADO = (2 - osados / len(contr)) * 10
EFECTO_PRECAVIDO = (1 - precavidos / len(contr)) * 5

# Dificultad de control del vehículo
PESO_MEDIO = tot_pes_gen / tot_cant
EQUILIBRIO_PRECAVIDO = (2 - osados / len(contr))

# Tiempo pits
TIEMPO_MINIMO_PITS = math.ceil(4 * tot_cant / 10)
VELOCIDAD_PITS = math.ceil(len(contr) / 4)

# Experiencia por ganar
BONIFICACION_PRECAVIDO = (1 - precavidos / len(contr)) * 2
DESBONIFICACION_OSADO = 1 - osados / len(contr)

POND_EFECT_HIELO = (1 + random.randint(1, 3) / 2) * 4
POND_EFECT_ROCAS = (1 + random.randint(1, 3) / 2) * 4
POND_EFECT_DIFICULTAD = (1 + random.randint(1, 3) / 2) * 4
# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
