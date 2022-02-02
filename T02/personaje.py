from PyQt5.QtCore import QObject, pyqtSignal
import parametros_generales


class Personaje(QObject):

    senal_actualizar_personaje = pyqtSignal(str)

    def __init__(self, x, y, dinero, energia):
        super().__init__()
        self.direction = 'derecha'
        self._x = x
        self._y = y
        self.initial_y = y
        self._dinero = dinero
        self._energia = energia
        self.inventario = []
        self._azada = None
        self._hacha = None

        # Senal para actualizar el interfaz cuando el personaje se mueve (funcion externa)
        self.senal_actualizar_interfaz = None

        # Senal para actualizar los datos del personaje (funcion propia)
        self.senal_actualizar_personaje.connect(self.move)

    # Funcion para los movimientos del personaje
    def move(self, evento):
        if evento == 'derecha':
            self.direction = 'derecha'
            self.x += parametros_generales.VEL_MOVIMIENTO
        elif evento == 'izquierda':
            self.direction = 'izquierda'
            self.x -= parametros_generales.VEL_MOVIMIENTO
        elif evento == 'arriba':
            self.direction = 'arriba'
            self.y -= parametros_generales.VEL_MOVIMIENTO
        elif evento == "abajo":
            self.direction = 'abajo'
            self.y += parametros_generales.VEL_MOVIMIENTO

    # Permite equipar las herramientas
    @property
    def hacha(self):
        return self._hacha

    @hacha.setter
    def hacha(self, valor):
        self._hacha = valor

    @property
    def azada(self):
        return self._azada

    @azada.setter
    def azada(self, valor):
        self._azada = valor

    # Energia
    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor <= 0:
            self._energia = 0
        if valor > parametros_generales.ENERGIA_JUGADOR:
            self._energia = parametros_generales.ENERGIA_JUGADOR
        else:
            self._energia = valor

    # Dinero
    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, valor):
        self._dinero = valor

    # Movimiento
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if 132 < valor < 468:
            self._x = valor
            self.actualizar_datos_personaje('walk')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        if 64 < valor < 286:
            self._y = valor
            self.actualizar_datos_personaje('walk')

    # Envio de los datos del personaje
    def actualizar_datos_personaje(self, position='stand'):
        if self.senal_actualizar_interfaz:
            self.senal_actualizar_interfaz.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction,
                'position': position
            })

    def comprar(self, nombre, valor):
        self.inventario.append(nombre)
        self.dinero -= valor

    def vender(self, nombre, valor):
        self.inventario.remove(nombre)
        self.dinero += valor


class Cultivos(QObject):
    def __init__(self, *posicion):
        super().__init__(*posicion)
        self.posicion = posicion
        self.etapa_crecimiento = 0
        self.listo_cortar = False


class Choclo(Cultivos):
    def __init__(self, *posicion):
        super().__init__(*posicion)
        self.posicion = posicion
        self.etapa_crecimiento = 0
        self.listo_cortar = False


class Alcachofa(Cultivos):
    def __init__(self, *posicion):
        super().__init__(*posicion)
        self.posicion = posicion
        self.etapa_crecimiento = 0
        self.listo_cortar = False

class Arbol(QObject):
    def __init__(self, tiempo):
        super().__init__(tiempo)
        self.tiempo = tiempo
        self.listo_cortar = True
