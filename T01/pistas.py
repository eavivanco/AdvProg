class Pista():
    def __init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo):
        self.nombre = nombre
        self.tipo = tipo
        self.hielo = hielo
        self.rocas = rocas
        self.dif = dif
        self.vueltas = vueltas
        self.contr = contr.split(';')
        self.largo = largo


class PistaHielo(Pista):
    def __init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo):
        Pista.__init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo)
        self.tipo = 'pista hielo'
        self.rocas = 0


class PistaRocas(Pista):
    def __init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo):
        Pista.__init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo)
        self.tipo = 'pista rocosa'
        self.hielo = 0


class PistaSuprema(Pista):
    def __init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo):
        Pista.__init__(self, nombre, tipo, hielo, rocas, dif, vueltas, contr, largo)
        self.tipo = 'pista suprema'
