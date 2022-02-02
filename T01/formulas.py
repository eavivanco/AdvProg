import parametros
import math


def velocidad_real(velocidad_intencional, dificultad_control, hipotermia):
    velocidad_real = math.floor(max(parametros.VELOCIDAD_MINIMA,
                                    velocidad_intencional + dificultad_control + hipotermia))
    return velocidad_real


def velocidad_intencional(velocidad_recomendada, personalidad):
    if personalidad == 'osado':
        velocidad_intencional = math.floor(parametros.EFECTO_OSADO + velocidad_recomendada)
        return velocidad_intencional
    elif personalidad == 'precavido':
        velocidad_intencional = math.floor(parametros.EFECTO_PRECAVIDO + velocidad_recomendada)
        return velocidad_intencional


def velocidad_recomendada(velocidad_base, traccion_ruedas, hielo_pista, defensa_carroceria,
                          rocas_pista, experiencia_piloto, dificultad_pista):
    velocidad_recomendada = math.floor(int(velocidad_base) + (int(traccion_ruedas) -
                                                              int(hielo_pista)) * \
                                       int(parametros.POND_EFECT_HIELO) +
                                       (int(defensa_carroceria) - int(rocas_pista)) * \
                                       int(parametros.POND_EFECT_ROCAS) + \
                                       (int(experiencia_piloto) - int(dificultad_pista)) * \
                                       int(parametros.POND_EFECT_DIFICULTAD))
    return velocidad_recomendada


def hipotermia(numero_vuelta, contextura, pista):
    if pista.tipo == 'pista rocosa':
        hipotermia = math.floor(min(0, numero_vuelta * (int(contextura))))
    else:
        hipotermia = math.floor(min(0, numero_vuelta * (int(contextura) - int(pista.hielo))))

    return hipotermia


def dificultad_control(tipo, personalidad, equilibrio, peso_vehiculo):
    if tipo == 'automovil' or 'troncomovil':
        dificultad_control = 0
        return dificultad_control
    if tipo == 'bicicleta' or 'motocicleta':
        if personalidad == 'osado':
            dificultad_control = math.floor(min(0, equilibrio - (parametros.PESO_MEDIO /
                                                                 peso_vehiculo)))
            return dificultad_control
        if personalidad == 'precavido':
            dificultad_control = math.floor(min(0, equilibrio * parametros.EQUILIBRIO_PRECAVIDO -
                                                (parametros.PESO_MEDIO / peso_vehiculo)))
            return dificultad_control


def dano_recibido_cada_vuelta(rocas_pista, defensa_carroceria):
    dano_recibido = math.floor(max(0, int(rocas_pista) - int(defensa_carroceria)))
    return dano_recibido


def tiempo_pits(durabilidad_inicial_chasis, durabilidad_actual_chasis):
    tiempo_pits = math.floor(parametros.TIEMPO_MINIMO_PITS + \
                             (durabilidad_inicial_chasis - durabilidad_actual_chasis) * \
                             parametros.VELOCIDAD_PITS)
    return tiempo_pits


def dinero_vuelta_x(numero_vuelta, dificultad_pista):
    dinero_vuelta_x = math.floor(int(numero_vuelta) * int(dificultad_pista))
    return dinero_vuelta_x


def probabilidad_accidente(velocidad_real, velocidad_recomendada, durabilidad_maxima_chasis,
                           durabilidad_actual_chasis):
    probabilidad_accidente = min(1, max(0, ((velocidad_real - velocidad_recomendada) /
                                            velocidad_recomendada) + ((durabilidad_maxima_chasis -
                                                                       durabilidad_actual_chasis) /
                                                                      durabilidad_maxima_chasis)))
    return probabilidad_accidente


def tiempo_vuelta(largo_pista, velocidad_real):
    tiempo_vuelta = math.floor(int(largo_pista) / int(velocidad_real))
    return tiempo_vuelta


def dinero_ganador(numero_vueltas_total, dificultad_pista, hielo_pista, rocas_pista):
    dinero_ganador = math.floor(int(numero_vueltas_total) * int(int(dificultad_pista) +
                                                                int(hielo_pista) +
                                                                int(rocas_pista)))
    return dinero_ganador


def experiencia_recibida(personalidad, ventaja_con_ultimo_lugar, dificultad_pista):
    if personalidad == 'osado':
        experiencia_recibida = math.floor((int(ventaja_con_ultimo_lugar) +
                                           int(dificultad_pista)) *
                                          int(parametros.DESBONIFICACION_OSADO))
        return experiencia_recibida
    if personalidad == 'precavido':
        experiencia_recibida = math.floor((int(ventaja_con_ultimo_lugar) +
                                           int(dificultad_pista)) *
                                          int(parametros.BONIFICACION_PRECAVIDO))
        return experiencia_recibida
