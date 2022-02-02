from PyQt5.QtCore import pyqtSignal, QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, \
    QHBoxLayout, QProgressBar
from PyQt5.QtGui import QPixmap
from os.path import join
from personaje import Personaje
from back import TiempoJuego
from random import randint, choice
import parametros_generales
from back import DraggableLabel, DropLabel
import time


class MiVentana(QWidget):
    senal_iniciar_juego = pyqtSignal(str)
    # Actualiza la posicion del personaje
    senal_actualizar_interfaz = pyqtSignal(dict)
    senal_limpiar_inicio = pyqtSignal()
    # Tienda
    senal_comprar_tienda = pyqtSignal(str, int)
    senal_vender_tienda = pyqtSignal(str, int)
    imagenes_tienda = {
        'alcachofa_semillas': join("sprites/cultivos", 'alcachofa/seeds.png'),
        'alcachofa': join("sprites/cultivos", 'alcachofa/icon.png'),
        'choclo_semillas': join("sprites/cultivos", 'choclo/seeds.png'),
        'choclo': join("sprites/cultivos", 'choclo/icon.png'),
        'azador': join("sprites/otros", "hoe.png"), 'hacha': join("sprites/otros", 'axe.png'),
        'madera': join("sprites/recursos", "wood.png"),
        'oro': join("sprites/recursos", 'gold.png'), 'ticket': join("sprites/otros", "ticket.png")
    }
    imagenes_mapa = {
        'H': join("sprites/mapa", 'house.png'), 'T': join("sprites/mapa", 'store.png'),
        'O': join("sprites/mapa", "tile006.png"), 'C': join("sprites/mapa", "tile004.png"),
        'R': join("sprites/mapa", "tile030.png")
    }
    imagenes_mapa_generacion = {
        'oro': join("sprites/recursos", 'gold.png'), 'arbol': join("sprites/otros", 'tree.png')
    }
    imagenes_personaje = {('abajo', 'stand'): join("sprites/personaje", "down_1.png"),
                          ('abajo', 'walk', 1): join("sprites/personaje", "down_2.png"),
                          ('abajo', 'walk', 2): join("sprites/personaje", "down_4.png"),
                          ('izquierda', 'stand'): join("sprites/personaje", "left_1.png"),
                          ('izquierda', 'walk', 1): join("sprites/personaje", "left_2.png"),
                          ('izquierda', 'walk', 2): join("sprites/personaje", "left_4.png"),
                          ('derecha', 'stand'): join("sprites/personaje", "right_1.png"),
                          ('derecha', 'walk', 1): join("sprites/personaje", "right_2.png"),
                          ('derecha', 'walk', 2): join("sprites/personaje", "right_4.png"),
                          ('arriba', 'stand'): join("sprites/personaje", "up_1.png"),
                          ('arriba', 'walk', 1): join("sprites/personaje", "up_2.png"),
                          ('arriba', 'walk', 2): join("sprites/personaje", "up_4.png")
                          }

    def __init__(self):
        super().__init__()
        self.timer = None
        self.set_teclas = set()
        self.mapa_elegido = ''
        self.columnas_mapa = 0
        self.filas_mapa = 0
        self.posiciones_mapa = []
        self._frame = 1
        self.mapa = []
        self.personaje_back = Personaje(375, 167, parametros_generales.MONEDAS_INICIALES,
                                        parametros_generales.ENERGIA_JUGADOR)
        self.vbox = None
        self.vbox_generacion = None
        self.personaje_front = None
        self.current_sprite = None
        self.senal_actualizar_personaje = None
        self.senal_eliminar_ventana_input = None
        self.senal_mostrar_tienda = None
        self.senal_transaccion_fallida = None
        self.senal_ticket_ganador = None
        self.init_gui()
        self.init_signals()

    def init_signals(self):
        self.senal_iniciar_juego.connect(self.pantalla_juego)
        self.senal_actualizar_interfaz.connect(self.update_window)
        self.senal_actualizar_personaje = self.personaje_back.senal_actualizar_personaje
        self.personaje_back.senal_actualizar_interfaz = self.senal_actualizar_interfaz
        self.senal_limpiar_inicio.connect(self.limpiar_pantalla)
        self.senal_comprar_tienda.connect(self.comprar_tienda)
        self.senal_vender_tienda.connect(self.vender_tienda)

    def init_gui(self):
        self.setWindowTitle('DCCAMPO - ventana juego')
        self.setGeometry(230, 160, 600, 400)
        self.label_inventario = QLabel('Inventario', self)
        self.label_inventario.move(10, 5)
        self.labels_d = {i: DraggableLabel(self) for i in range(0, 200)}
        self.labels_n = {i: QLabel(self) for i in range(0, 200)}
        self.boton_dormir = QPushButton('Dormir', self)
        self.boton_dormir.move(480, 320)
        self.boton_dormir.clicked.connect(self.boton_dormir_f)
        self.boton_pausar = QPushButton('Pausar', self)
        self.boton_pausar.move(480, 345)
        self.boton_pausar.clicked.connect(self.boton_pausa)
        self.boton_salir = QPushButton('Salir', self)
        self.boton_salir.move(480, 370)
        self.boton_salir.clicked.connect(QCoreApplication.instance().quit)
        self.label_stats = QLabel('Stats:', self)
        self.label_stats.move(480, 170)
        self.label_dia = QLabel('Dia: 1 ', self)
        self.label_dia.move(480, 200)
        self.label_hora = QLabel('Hora:', self)
        self.label_hora.move(480, 230)
        self.label_dinero = QLabel(f'Dinero: ${self.personaje_back._dinero}', self)
        self.label_dinero.move(480, 260)
        self.label_energia = QLabel(f'Energia: {self.personaje_back._energia}', self)
        self.label_energia.move(480, 285)
        self.pbar_energia = QProgressBar(self)
        self.pbar_energia.setGeometry(530, 280, 50, 65)
        self.pbar_energia.setValue(100)
        self.grilla_mapa = QGridLayout()
        self.grilla_mapa_generacion = QGridLayout()
        self.grilla_inventario = QGridLayout()

    def boton_clickeado(self):
        if self.senal_procesar:
            texto_input = self.input.text()
            self.senal_procesar.emit(texto_input)

    def boton_pausa(self):
        if self.timer.timer_activo():
            self.timer.pausar()
        else:
            self.timer.comenzar()

    def boton_dormir_f(self):
        self.label_inventario.setText(f'{parametros_generales.ENERGIA_DORMIR}')
        self.actualizar_energia(parametros_generales.ENERGIA_DORMIR, 'sumar')
        self.timer.minuto += parametros_generales.DURACION_DIA
        self.timer.dia += 1
        self.actualizar_dia(self.timer._dia)

    def actualizar_mensaje(self, texto):
        self.label.setText(texto)

    def limpiar_pantalla(self):
        if self.senal_eliminar_ventana_input:
            self.senal_eliminar_ventana_input.emit()

    def pantalla_juego(self, texto):
        self.setWindowTitle(f'DCCAMPO - {texto}')
        self.ejecutar_timer()
        self.mapa_elegido = texto
        self.crear_mapa_fondo(texto)
        self.personaje_front = QLabel(self)
        self.current_sprite = QPixmap(self.imagenes_personaje[('derecha', 'stand')])
        self.personaje_front.setPixmap(self.current_sprite)
        self.personaje_front.move(375, 167)
        self.limpiar_pantalla()
        self.actualizar_inventario()
        self.acceder_tienda()
        self.show()

    diccionario_eventos = {
        Qt.Key_D: 'derecha', Qt.Key_A: 'izquierda', Qt.Key_W: 'arriba', Qt.Key_S: 'abajo',
        Qt.Key_K: 'K', Qt.Key_I: 'I', Qt.Key_P: 'P', Qt.Key_M: 'M', Qt.Key_N: 'N', Qt.Key_Y: 'Y',
        Qt.Key_R: 'R', Qt.Key_1: 'M', Qt.Key_2: 'N', Qt.Key_3: 'Y', Qt.Key_G: 'G', Qt.Key_B: 'B'
    }

    def keyPressEvent(self, event):
        if event.key() in self.diccionario_eventos:
            self.set_teclas.add(self.diccionario_eventos[event.key()])
            if self.diccionario_eventos[event.key()] == 'abajo' or 'derecha' or 'izquierda' or \
                    'arriba':
                accion = self.diccionario_eventos[event.key()]
                self.senal_actualizar_personaje.emit(accion)
            else:
                self.set_teclas.add(self.diccionario_eventos[event.key()])
            self.atajos_teclas(self.set_teclas)

    def keyReleaseEvent(self, event):
        if event.key() in self.diccionario_eventos:
            self.set_teclas = set()

    def atajos_teclas(self, grupo):
        if 'K' in grupo and 'I' in grupo and 'P' in grupo:
            self.actualizar_energia(parametros_generales.ENERGIA_JUGADOR, 'sumar')
        if 'M' in grupo and 'N' in grupo and 'Y' in grupo:
            self.personaje_back.dinero += parametros_generales.DINERO_TRAMPA
            self.label_dinero.setText(f'Dinero: ${self.personaje_back._dinero}')
        if 'R' in grupo and 'G' in grupo and 'B' in grupo:
            self.actualizar_energia(5, 'restar')

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        self._frame = value if value < 3 else 1

    def update_window(self, event):
        direccion = event['direction']
        position = event['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(self.imagenes_personaje[(direccion,
                                                                   position, self._frame)])
        else:
            self.current_sprite = QPixmap(self.imagenes_personaje[(direccion, position)])
        self.personaje_front.setPixmap(self.current_sprite)
        self.personaje_front.move(event['x'], event['y'])

    def crear_mapa_fondo(self, texto_input):
        with open(f'mapas/{texto_input}.txt', "r", encoding="UTF-8") as file:
            for line in file:
                self.filas_mapa += 1
                self.columnas_mapa = 0
                for elemento in line:
                    if elemento != ' ' and elemento != '\n':
                        self.columnas_mapa += 1
                        self.mapa.append(elemento)
                    else:
                        pass
        self.posiciones_mapa = [(i, j) for i in range(self.filas_mapa) for j in
                                range(self.columnas_mapa)]
        for posicion, valor in zip(self.posiciones_mapa, self.mapa):
            if valor == 'R' or 'T' or 'H':
                imagen = QPixmap(self.imagenes_mapa['O'])
                label = QLabel(self)
                label.setPixmap(imagen)
                label.setMinimumSize(parametros_generales.PIXELES_TILES,
                                     parametros_generales.PIXELES_TILES)
                label.setMaximumSize(parametros_generales.PIXELES_TILES,
                                     parametros_generales.PIXELES_TILES)
                label.setScaledContents(True)
                self.grilla_mapa.addWidget(label, *posicion)
            imagen = QPixmap(self.imagenes_mapa[valor])
            label = QLabel(self)
            label.setPixmap(imagen)
            label.setMinimumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setMaximumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setScaledContents(True)
            self.grilla_mapa.addWidget(label, *posicion)
            if valor == 'C':
                imagen = QPixmap(self.imagenes_mapa['C'])
                label = DropLabel(self)
                label.setPixmap(imagen)
                label.setMinimumSize(parametros_generales.PIXELES_TILES,
                                     parametros_generales.PIXELES_TILES)
                label.setMaximumSize(parametros_generales.PIXELES_TILES,
                                     parametros_generales.PIXELES_TILES)
                label.setScaledContents(True)
                self.grilla_mapa.addWidget(label, *posicion)
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.addLayout(hbox)
        hbox.addLayout(self.grilla_mapa)
        self.setLayout(self.vbox)

    def generacion_espontanea(self):
        elegibles = []
        for posicion_posible, valor in zip(self.posiciones_mapa, self.mapa):
            if valor == 'O':
                elegibles.append(posicion_posible)
        posicion = choice(elegibles)
        if self.realizar_evento_generacion(parametros_generales.PROB_ORO):
            imagen = QPixmap(self.imagenes_mapa_generacion['oro'])
            label = QLabel(self)
            label.setPixmap(imagen)
            label.setMinimumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setMaximumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setScaledContents(True)
            self.grilla_mapa.addWidget(label, *posicion)
            elegibles.remove(posicion)
            posicion = choice(elegibles)
        if self.realizar_evento_generacion(parametros_generales.PROB_ARBOL):
            imagen = QPixmap(self.imagenes_mapa_generacion['arbol'])
            label = QLabel(self)
            label.setPixmap(imagen)
            label.setMinimumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setMaximumSize(parametros_generales.PIXELES_TILES,
                                 parametros_generales.PIXELES_TILES)
            label.setScaledContents(True)
            self.grilla_mapa.addWidget(label, *posicion)

    def realizar_evento_generacion(self, valor):
        oraculo = randint(0, 100)
        if oraculo <= valor * 100:
            return True
        return False

    def ejecutar_timer(self):
        timer = TiempoJuego()
        timer.senal_actualizar_tiempo.connect(self.actualizar_tiempo)
        timer.senal_actualizar_dia.connect(self.actualizar_dia)
        self.timer = timer
        timer.comenzar()

    def actualizar_energia(self, delta, accion):
        if accion == 'sumar':
            self.personaje_back.energia += delta
        if accion == 'restar':
            if self.personaje_back._energia - delta >= 0:
                self.personaje_back.energia -= delta
            else:
                self.personaje_back.energia -= self.personaje_back._energia
                self.personaje_sin_energia()
        self.label_energia.setText(f'Energia: {self.personaje_back._energia}')
        self.pbar_energia.setValue(100 * self.personaje_back._energia /
                                   parametros_generales.ENERGIA_JUGADOR)


    def actualizar_tiempo(self, texto):
        self.label_hora.setText(f'Hora: {texto}')

    def actualizar_dia(self, texto):
        self.label_dia.setText(f'Dia: {texto}')
        self.generacion_espontanea()

    def acceder_tienda(self):
        if self.senal_mostrar_tienda:
            self.senal_mostrar_tienda.emit()

    def comprar_tienda(self, nombre, valor):
        if self.personaje_back._dinero - valor >= 0:
            self.personaje_back.comprar(nombre, valor)
            self.label_dinero.setText(f'Dinero: ${self.personaje_back._dinero}')
            self.actualizar_inventario()
            if nombre == 'ticket':
                self.senal_ticket_ganador.emit()
                self.label_inventario.setText('Ganaste!')
        else:
            self.transaccion_fallida()

    def vender_tienda(self, nombre, valor):
        if nombre in self.personaje_back.inventario:
            self.actualizar_inventario()
            self.personaje_back.vender(nombre, valor)
        else:
            self.transaccion_fallida()

    def transaccion_fallida(self):
        if self.senal_transaccion_fallida:
            self.senal_transaccion_fallida.emit('No es posible realizar esta transaccion! :(')

    def actualizar_inventario(self):
        indice = 0
        x = 10
        y = 30
        for elemento in self.personaje_back.inventario:
            imagen = QPixmap(self.imagenes_tienda[elemento])
            if elemento == 'alcachofa_semillas' or elemento == 'choclo_semillas':
                self.labels_d[indice].setPixmap(imagen)
                self.labels_d[indice].setMinimumSize(parametros_generales.PIXELES_TILES,
                                                   parametros_generales.PIXELES_TILES)
                self.labels_d[indice].setMaximumSize(parametros_generales.PIXELES_TILES,
                                                   parametros_generales.PIXELES_TILES)
                self.labels_d[indice].setScaledContents(True)
                self.labels_d[indice].move(x, y)
                self.labels_d[indice].show()
                x += 1 + parametros_generales.PIXELES_TILES
                indice += 1
                if x > 580:
                    x = 10
                    y += 20
            else:
                self.labels_n[indice].setPixmap(imagen)
                self.labels_n[indice].setMinimumSize(parametros_generales.PIXELES_TILES,
                                                     parametros_generales.PIXELES_TILES)
                self.labels_n[indice].setMaximumSize(parametros_generales.PIXELES_TILES,
                                                     parametros_generales.PIXELES_TILES)
                self.labels_n[indice].setScaledContents(True)
                self.labels_n[indice].move(x, y)
                self.labels_n[indice].show()
                x += 1 + parametros_generales.PIXELES_TILES
                indice += 1
                if x > 580:
                    x = 10
                    y += 20

    def personaje_sin_energia(self):
        self.label_inventario.setText('Perdiste :(')
        self.label_stats.setText('Super F')
        self.label_dinero.setText('(La pantalla se \ndeberia cerrar)')
        self.boton_pausa()
        self.personaje_back.dinero -= self.personaje_back._dinero
        time.sleep(3)
        self.personaje_front.deleteLater()
        self.personaje_back.deleteLater()
