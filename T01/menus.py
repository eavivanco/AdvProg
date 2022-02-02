import usuarios
import parametros
import funciones
import funciones2


class Menu:
    def __init__(self):
        pass

    def recibir_input(self):
        pass


class MenuSesion(Menu):
    def __init__(self):
        super().__init__()

    def recibir_input(self):
        inicio_correcto = False
        while not inicio_correcto:
            respuesta_usuario_ms = str(input("Bienvenido a Initial P! Selecciona una de las "
                                             "siguientes opciones para continuar\n"
                                             "[1] Nueva partida\n[2] Cargar partida\n[0] Salir"))
            if respuesta_usuario_ms == '1':
                inicio_correcto = True
                self.nueva_partida()
            elif respuesta_usuario_ms == '2':
                inicio_correcto = True
                self.cargar_partida()
            elif respuesta_usuario_ms == '0':
                inicio_correcto = True
                print('Nos vemos pronto!')
            else:
                print('El numero elegido no esta entre nuestras opciones, intenta nuevamente')

    def nueva_partida(self):
        inicio_correcto, nombre, contextura, equilibrio, personalidad, \
        equipo_piloto = funciones.nueva_partida_gen()
        if inicio_correcto:
            piloto = usuarios.Piloto(f'{nombre}', 1500000, 0, f'{contextura}', f'{equilibrio}'
                                     , f'{personalidad}', f'{equipo_piloto}', 0, 0)
            salir = self.veh_inicial(piloto)
            if salir:
                print('')
            else:
                partida = MenuPrincipal(piloto)
                partida.recibir_input(piloto)

    def cargar_partida(self):
        inicio_correcto = False
        while not inicio_correcto:
            nombre_cargar = input('Ingresa el nombre del usuario que quieres cargar!'
                                  '(Para salir presiona 0)\n->')
            if nombre_cargar == '0' or 0:
                inicio_correcto = True
                pass
            if nombre_cargar != 0 and nombre_cargar != '0':
                correcto, nom, din, per, cont, equili, exp \
                    , equip = funciones.cargar_partida_gen(nombre_cargar)
                if correcto:
                    print('Esta cargando una partida...')
                    piloto = usuarios.Piloto(f'{nom}', f'{din}', f'{exp}', f'{cont}', f'{equili}'
                                             , f'{per}', f'{equip}', 0)
                    partida = MenuPrincipal(piloto)
                    partida.recibir_input(piloto)
                    inicio_correcto = True
                else:
                    print('El usuario no fue encontrado, intenta nuevamente!')

    def veh_inicial(self, piloto):
        op_uno, op_dos, op_tres, op_cua = 'Automovil', 'Troncomovil', 'Motocicleta', 'Bicicleta'
        inicio_correcto = False
        while not inicio_correcto:
            respuesta_usuario_mv = str(input("Elige un vehiculo para comenzar!\n"
                                             " Selecciona una de las siguientes "
                                             f"opciones para continuar\n[1] {op_uno}\n"
                                             f"[2] {op_dos}\n[3] {op_tres}\n[4] {op_cua}\n"
                                             "[0] Salir"))
            if respuesta_usuario_mv == '1':
                veh_correcto = False
                inicio_correcto = True
                while not veh_correcto:
                    veh = input(f'Elige un nombre para tu {op_uno}! (Debe ser alfanumerico)')
                    v2 = veh.strip().split()
                    v3 = ''.join(v2)
                    valido = funciones2.unicidad_veh(veh)
                    if v3.isalnum() and valido:
                        veh_correcto = True
                        cha, car, rue, mot, pes = funciones.param_automovil()
                        pr_veh = usuarios.Automovil(veh, piloto.nombre, cha, car, rue, mot, pes,
                                                    car)
                        piloto.vehiculo = pr_veh
                        return False
                    else:
                        print(f'El nombre \"{veh}\" no es valido, intenta nuevamente')
            elif respuesta_usuario_mv == '2':
                veh_correcto = False
                inicio_correcto = True
                while not veh_correcto:
                    veh = input(f'Elige un nombre para tu {op_dos}! (Debe ser alfanumerico)')
                    v2 = veh.strip().split()
                    v3 = ''.join(v2)
                    if v3.isalnum():
                        veh_correcto = True
                        cha, car, rue, mot, pes = funciones.param_troncomovil()
                        pr_veh = usuarios.Troncomovil(veh, piloto.nombre, cha, car, rue, mot, pes,
                                                      car)
                        piloto.vehiculo = pr_veh
                        return False
                    else:
                        print(f'El nombre \"{veh}\" no es valido, intenta nuevamente')
            elif respuesta_usuario_mv == '3':
                veh_correcto = False
                inicio_correcto = True
                while not veh_correcto:
                    veh = input(f'Elige un nombre para tu {op_tres}! (Debe ser alfanumerico)')
                    v2 = veh.strip().split()
                    v3 = ''.join(v2)
                    if v3.isalnum():
                        veh_correcto = True
                        cha, car, rue, mot, pes = funciones.param_motocicletas()
                        pr_veh = usuarios.Motocicleta(veh, piloto.nombre, cha, car, rue, mot, pes,
                                                      car)
                        piloto.vehiculo = pr_veh
                        return False
                    else:
                        print(f'El nombre \"{veh}\" no es valido, intenta nuevamente')
            elif respuesta_usuario_mv == '4':
                veh_correcto = False
                inicio_correcto = True
                while not veh_correcto:
                    veh = input(f'Elige un nombre para tu {op_cua}!(Debe ser alfanumerico)')
                    v2 = veh.strip().split()
                    v3 = ''.join(v2)
                    if v3.isalnum():
                        veh_correcto = True
                        cha, car, rue, mot, pes = funciones.param_bicicletas()
                        pr_veh = usuarios.Bicicleta(veh, piloto.nombre, cha, car, rue, mot, pes,
                                                    car)
                        piloto.vehiculo = pr_veh
                        return False
                    else:
                        print(f'El nombre \"{veh}\" no es valido, intenta nuevamente')
            elif respuesta_usuario_mv == '0':
                inicio_correcto = True
                print('Decidiste salir! Nos vemos pronto')
                return True
            else:
                print('El numero elegido no esta entre nuestras opciones, intenta nuevamente')


class MenuPrincipal(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto

    def recibir_input(self, piloto):
        inicio_correcto = False
        print("Bienvenido a una nueva partida!")
        while not inicio_correcto:
            respuesta_usuario_mp = str(input(" Selecciona una de las siguientes opciones para "
                                             "continuar\n[1] Comprar nuevos vehiculos\n"
                                             "[2] Iniciar una carrera\n[3] Guardar la partida\n"
                                             "[0] Salir"))
            if respuesta_usuario_mp == '1':
                self.comprar_vehiculos(piloto)
            elif respuesta_usuario_mp == '2':
                piloto.tiempo_total = 0
                salir = self.iniciar_carrera(piloto)
                if salir:
                    inicio_correcto = True
                    print('Nos vemos pronto!')
            elif respuesta_usuario_mp == '3':
                self.guardar_partida(piloto)
                inicio_correcto = True
            elif respuesta_usuario_mp == '0':
                inicio_correcto = True
                print('Nos vemos pronto!')
            else:
                print('El numero elegido no esta entre nuestras opciones, intenta nuevamente')

    def comprar_vehiculos(self, piloto):
        compra = MenuVehiculos(piloto)
        compra.recibir_input(piloto)

    def iniciar_carrera(self, piloto):
        print('Esta iniciando la partida...')
        vuelta = - 1
        funciones.cargar_contrincantes_gen()
        nom_pis, tip_pis, hie_pis, roc_pis, dif_pis, num_pis, con_pis, \
        lar_pis = funciones.cargar_pista()
        pista = funciones.iniciar_pista(nom_pis, tip_pis, hie_pis, roc_pis, dif_pis, num_pis,
                                        con_pis, lar_pis)
        print(f'\nTe ha tocado correr en la pista {nom_pis}! Mucha suerte\n')
        vuel_max = pista.vueltas
        contrincantes_final = funciones.cargar_contrincantes_pis(pista.contr)
        tiempo_piloto = 0
        tiempo_total_piloto = 0
        lugares = []
        funciones2.reiniciar_tiempos(contrincantes_final)
        carrera = MenuCarrera(piloto)
        salir = carrera.recibir_input(piloto, vuelta, vuel_max, piloto.vehiculos,
                                      contrincantes_final, pista, tiempo_piloto,
                                      tiempo_total_piloto, lugares)
        if salir:
            print('')
            return True
        else:
            return False

    def guardar_partida(self, piloto):
        print('Se esta guardando la partida...')
        funciones2.guardar_partida(piloto)
        funciones2.guardar_auto(piloto)


class MenuVehiculos(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto

    def recibir_input(self, piloto):
        op_uno, op_dos, op_tres, op_cua = 'Automovil', 'Troncomovil', 'Motocicleta', 'Bicicleta'

        inicio_correcto = False
        while not inicio_correcto:
            respuesta_usuario_mv = str(input("Bienvenido a la tienda de vehiculos!\n"
                                             f"Tu dinero es: {piloto.dinero}\n"
                                             " Selecciona una de las siguientes "
                                             f"opciones para continuar\n[1] {op_uno}  $P 600\n"
                                             f"[2] {op_dos}  $P 1200\n[3] {op_tres} SS  $P 1400\n"
                                             f"[4] {op_cua} $P 1700\n[0] Salir"))
            if respuesta_usuario_mv == '1':
                inicio_correcto = True
                print(f'Felicidades, conseguiste {op_uno}!')
            elif respuesta_usuario_mv == '2':
                inicio_correcto = True
                print(f'Felicidades, conseguiste {op_dos}!')
            elif respuesta_usuario_mv == '3':
                inicio_correcto = True
                print(f'Felicidades, conseguiste {op_tres}!')
            elif respuesta_usuario_mv == '4':
                inicio_correcto = True
                print(f'Felicidades, conseguiste {op_cua}!')
            else:
                print('El numero elegido no esta entre nuestras opciones, intenta nuevamente')


class MenuPits(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto

    def recibir_input(self, piloto):
        dinero_actual = piloto.dinero
        op_uno, op_dos, op_tres = 'Chasis', 'Carroceria', 'Ruedas'
        costo_uno = parametros.MEJORAS['CHASIS']['COSTO']
        costo_dos = parametros.MEJORAS['CARROCERIA']['COSTO']
        costo_tres = parametros.MEJORAS['RUEDAS']['COSTO']
        if piloto.vehiculos.categoria == 'automovil' or 'motocicleta':
            costo_cuatro = parametros.MEJORAS['MOTOR']['COSTO']
            op_cuatro = 'Motor'
        else:
            costo_cuatro = parametros.MEJORAS['ZAPATILLAS']['COSTO']
            op_cuatro = 'Zapatillas'
        inicio_correcto = False
        while not inicio_correcto:
            respuesta_usuario_mp = str(input(f"Bienvenido a los pits {piloto.nombre}\n"
                                             f"Tu saldo es {dinero_actual}:\n"
                                             "Deseas hacer alguna mejora?\n"
                                             f"[1] {op_uno}: {costo_uno}\n"
                                             f"[2] {op_dos}: {costo_dos}\n"
                                             f"[3] {op_tres}: {costo_tres}\n"
                                             f"[4] {op_cuatro}: {costo_cuatro}\n[0] Salir"))
            if respuesta_usuario_mp == '1' \
                    and parametros.MEJORAS['CHASIS']['COSTO'] <= dinero_actual:
                inicio_correcto = True
                piloto.vehiculos.chasis += parametros.MEJORAS['CHASIS']['EFECTO']
                piloto.dinero -= parametros.MEJORAS['CHASIS']['COSTO']
            elif respuesta_usuario_mp == '2' \
                    and parametros.MEJORAS['CARROCERIA']['COSTO'] <= dinero_actual:
                inicio_correcto = True
                piloto.vehiculos.carroceria += parametros.MEJORAS['CARROCERIA']['EFECTO']
                piloto.dinero -= parametros.MEJORAS['CARROCERIA']['COSTO']
            elif respuesta_usuario_mp == '3' \
                    and parametros.MEJORAS['RUEDAS']['COSTO'] <= dinero_actual:
                inicio_correcto = True
                piloto.vehiculos.ruedas += parametros.MEJORAS['RUEDAS']['EFECTO']
                piloto.dinero -= parametros.MEJORAS['RUEDAS']['COSTO']
            elif respuesta_usuario_mp == '4':
                if piloto.vehiculos.categoria == 'automovil' or 'motocicleta' and \
                        parametros.MEJORAS['MOTOR']['COSTO'] <= dinero_actual:
                    inicio_correcto = True
                    piloto.vehiculos.motor += parametros.MEJORAS['MOTOR']['EFECTO']
                    piloto.dinero -= parametros.MEJORAS['MOTOR']['COSTO']
                    print(f'{piloto.vehiculos.motor}')
                if piloto.vehiculos.categoria == 'bicicleta' or 'troncomovil' and \
                        parametros.MEJORAS['ZAPATILLAS']['COSTO'] <= dinero_actual:
                    inicio_correcto = True
                    piloto.vehiculos.motor += parametros.MEJORAS['ZAPATILLAS']['EFECTO']
                    piloto.dinero -= parametros.MEJORAS['ZAPATILLAS']['COSTO']
                else:
                    print('La opcion elegida no esta disponible, intenta nuevamente')
            elif respuesta_usuario_mp == '5' \
                    and parametros.MEJORAS['ZAPATILLAS']['COSTO'] <= dinero_actual:
                inicio_correcto = True
                piloto.vehiculos.zapatillas += parametros.MEJORAS['ZAPATILLAS']['EFECTO']
                piloto.dinero -= parametros.MEJORAS['ZAPATILLAS']['COSTO']
            elif respuesta_usuario_mp == '0':
                inicio_correcto = True
                print('Nos vemos pronto!')
            else:
                print('La opcion elegida no esta disponible, intenta nuevamente')


class MenuCarrera(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto

    def recibir_input(self, piloto, vuelta, vuel_max, pr_veh, contrincantes, pista, tiempo_piloto,
                      tiempo_total_piloto, lugares):
        inicio_correcto = False
        vuelta += 1
        if vuelta == int(vuel_max):
            print('La carrera ha finalizado!')
            return False
        while not inicio_correcto:
            funciones2.printear_lugares(lugares, vuelta, vuel_max)
            respuesta_usuario_mc = str(input("Selecciona una de las siguientes "
                                             "opciones para continuar\n[1] Otra vuelta\n"
                                             "[2] Ir a los pits y luego comenzar otra vuelta\n"
                                             "[0] Salir"))
            if respuesta_usuario_mc == '1':
                tiempo_piloto, tiempo_total_piloto, accidente_final, lugares \
                    = funciones2.una_vuelta(piloto, pr_veh, contrincantes, pista, vuelta,
                                            tiempo_total_piloto)
                if accidente_final == True:
                    print('Tu auto ha explotado :(, la carrera ha terminado (para ti)')
                    return False
                self.recibir_input(piloto, vuelta, vuel_max, pr_veh, contrincantes, pista,
                                   tiempo_piloto, tiempo_total_piloto, lugares)
                inicio_correcto = True
            elif respuesta_usuario_mc == '2':
                inicio_correcto = True
                pits = MenuPits(piloto)
                pits.recibir_input(piloto)
                tiempo_piloto, tiempo_total_piloto, accidente_final, lugares \
                    = funciones2.una_vuelta(piloto, pr_veh, contrincantes, pista, vuelta,
                                            tiempo_total_piloto)
                if accidente_final == True:
                    print(f'Tu auto ha explotado por {accidente_final}:(, la carrera ha terminado (para ti)')
                    return False
                self.recibir_input(piloto, vuelta, vuel_max, pr_veh, contrincantes, pista,
                                   tiempo_piloto, tiempo_total_piloto, lugares)
            elif respuesta_usuario_mc == '0':
                print('Nos vemos pronto!')
                return True
            else:
                print('El numero elegido no esta entre nuestras opciones, intenta nuevamente')
