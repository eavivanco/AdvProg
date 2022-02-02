class Piloto:
    def __init__(self, nombre, dinero, experiencia, contextura, equilibrio, personalidad, equipo,
                 tiempo, tiempo_total):
        self.nombre = nombre
        self.dinero = dinero
        self.experiencia = experiencia
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.personalidad = personalidad
        self.equipo = equipo
        self.vehiculos = None
        self.tiempo = tiempo
        self.tiempo_total = tiempo_total

    @property
    def vehiculo(self):
        print('Se ha agregado un nuevo auto a tu coleccion!')
        return self.vehiculo

    @vehiculo.setter
    def vehiculo(self, veh):
        if not self.vehiculos:
            print(f'Nuevo vehiculo equipado! {veh.nombre}')
            self.vehiculos = veh
        else:
            print('No es posible!')


class Vehiculo:
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max):
        self.nombre = nombre
        self.dueno = dueno
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.motor = motor
        self.peso = peso
        self.dur_max = dur_max

class Automovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max):
        Vehiculo.__init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max)
        self.categoria = 'automovil'


class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max):
        Vehiculo.__init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max)
        self.categoria = 'troncomovil'


class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max):
        Vehiculo.__init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max)
        self.categoria = 'bicicleta'


class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max):
        Vehiculo.__init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso, dur_max)
        self.categoria = 'motocicleta'


class Contrincantes():
    def __init__(self, nombre, nivel, per, cont, equilibrio, exp, equipo):
        self.nombre = nombre
        self.nivel = nivel
        self.per = per
        self.cont = cont
        self.equilibrio = equilibrio
        self.exp = exp
        self.equipo = equipo
        self.contrincantes = []


class Contrincante(Contrincantes):
    def __init__(self, nombre, nivel, per, cont, equilibrio, exp, equipo):
        Contrincantes.__init__(self, nombre, nivel, per, cont, equilibrio, exp, equipo)
