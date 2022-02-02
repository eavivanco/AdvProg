from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from os.path import join
import front

import parametros_precios

class VentanaTienda(QWidget):
    senal_mostrar_tienda = pyqtSignal()
    senal_transaccion_fallida = pyqtSignal(str)

    imagenes_tienda = {
        'alcachofa_semillas': join("sprites/cultivos", 'alcachofa/seeds.png'),
        'alcachofa': join("sprites/cultivos", 'alcachofa/icon.png'),
        'choclo_semillas': join("sprites/cultivos", 'choclo/seeds.png'),
        'choclo': join("sprites/cultivos", 'choclo/icon.png'),
        'azador': join("sprites/otros", "hoe.png"),
        'hacha': join("sprites/otros", 'axe.png'),
        'madera': join("sprites/recursos", "wood.png"),
        'oro': join("sprites/recursos", 'gold.png'),
        'ticket': join("sprites/otros", "ticket.png")
    }

    def __init__(self):
        super().__init__()

        # Compra y venta
        self.senal_comprar_tienda = None
        self.senal_vender_tienda = None

        self.init_gui()
        self.init_signals()

    def init_signals(self):
        self.senal_mostrar_tienda.connect(self.show)
        self.senal_transaccion_fallida.connect(self.transaccion_fallida)


    def init_gui(self):
        self.setWindowTitle('DCCAMPO - Tienda')
        self.setGeometry(900, 160, 600, 400)

        self.label_bienvenida = QLabel('Bienvenido a la Tienda! Aquí podrás vender y comprar '
                                       'recursos para avanzar en el juego!',self)
        self.label_bienvenida.move(32, 18)

        self.azador = QLabel(self)
        self.azador.setGeometry(50, 60, 30, 30)
        imagen_azador = QPixmap(self.imagenes_tienda['azador'])
        self.azador.setPixmap(imagen_azador)
        self.azador.setScaledContents(True)
        self.azador_precio = QLabel(f'$ {parametros_precios.PRECIO_AZADA}', self)
        self.azador_precio.move(100, 70)
        self.azador_comprar = QPushButton("Comprar", self)
        self.azador_comprar.move(140, 50)
        self.azador_comprar.clicked.connect(self.boton_comprar)
        self.azador_vender = QPushButton("Vender", self)
        self.azador_vender.move(140, 70)
        self.azador_vender.clicked.connect(self.boton_vender)

        self.hacha = QLabel(self)
        self.hacha.setGeometry(50, 120, 30, 30)
        imagen_hacha = QPixmap(self.imagenes_tienda['hacha'])
        self.hacha.setPixmap(imagen_hacha)
        self.hacha.setScaledContents(True)
        self.hacha_precio = QLabel(f'$ {parametros_precios.PRECIO_HACHA}', self)
        self.hacha_precio.move(100, 130)
        self.hacha_comprar = QPushButton("Comprar", self)
        self.hacha_comprar.move(140, 110)
        self.hacha_comprar.clicked.connect(self.boton_comprar)
        self.hacha_vender = QPushButton("Vender", self)
        self.hacha_vender.move(140, 130)
        self.hacha_vender.clicked.connect(self.boton_vender)

        self.semilla_choclo = QLabel(self)
        self.semilla_choclo.setGeometry(50, 180, 30, 30)
        imagen_semilla_choclo = QPixmap(self.imagenes_tienda['choclo_semillas'])
        self.semilla_choclo.setPixmap(imagen_semilla_choclo)
        self.semilla_choclo.setScaledContents(True)
        self.semilla_choclo_precio = QLabel(f'$ {parametros_precios.PRECIO_SEMILLA_CHOCLOS}', self)
        self.semilla_choclo_precio.move(100, 190)
        self.semilla_choclo_comprar = QPushButton("Comprar", self)
        self.semilla_choclo_comprar.move(140, 170)
        self.semilla_choclo_comprar.clicked.connect(self.boton_comprar)
        self.semilla_choclo_vender = QPushButton("Vender", self)
        self.semilla_choclo_vender.move(140, 190)
        self.semilla_choclo_vender.clicked.connect(self.boton_vender)

        self.semilla_alcachofa = QLabel(self)
        self.semilla_alcachofa.setGeometry(50, 240, 30, 30)
        imagen_semilla_alcachofa = QPixmap(self.imagenes_tienda['alcachofa_semillas'])
        self.semilla_alcachofa.setPixmap(imagen_semilla_alcachofa)
        self.semilla_alcachofa.setScaledContents(True)
        self.semilla_alcachofa_precio = QLabel(f'$ {parametros_precios.PRECIO_SEMILLA_ALCACHOFAS}'
                                               , self)
        self.semilla_alcachofa_precio.move(100, 250)
        self.semilla_alcachofa_comprar = QPushButton("Comprar", self)
        self.semilla_alcachofa_comprar.move(140, 230)
        self.semilla_alcachofa_comprar.clicked.connect(self.boton_comprar)
        self.semilla_alcachofa_vender = QPushButton("Vender", self)
        self.semilla_alcachofa_vender.move(140, 250)
        self.semilla_alcachofa_vender.clicked.connect(self.boton_vender)

        self.choclo = QLabel(self)
        self.choclo.setGeometry(400, 60, 30, 30)
        imagen_choclo = QPixmap(self.imagenes_tienda['choclo'])
        self.choclo.setPixmap(imagen_choclo)
        self.choclo.setScaledContents(True)
        self.choclo_precio = QLabel(f'$ {parametros_precios.PRECIO_CHOCLOS}', self)
        self.choclo_precio.move(450, 65)
        self.choclo_vender = QPushButton("Vender", self)
        self.choclo_vender.move(490, 60)
        self.choclo_vender.clicked.connect(self.boton_vender)

        self.alcachofa = QLabel(self)
        self.alcachofa.setGeometry(400, 120, 30, 30)
        imagen_alcachofa = QPixmap(self.imagenes_tienda['alcachofa'])
        self.alcachofa.setPixmap(imagen_alcachofa)
        self.alcachofa.setScaledContents(True)
        self.alcachofa_precio = QLabel(f'$ {parametros_precios.PRECIO_ALACACHOFAS}', self)
        self.alcachofa_precio.move(450, 125)
        self.alcachofa_vender = QPushButton("Vender", self)
        self.alcachofa_vender.move(490, 120)
        self.alcachofa_vender.clicked.connect(self.boton_vender)

        self.madera = QLabel(self)
        self.madera.setGeometry(400, 180, 30, 30)
        imagen_madera = QPixmap(self.imagenes_tienda['madera'])
        self.madera.setPixmap(imagen_madera)
        self.madera.setScaledContents(True)
        self.madera_precio = QLabel(f'$ {parametros_precios.PRECIO_LEÑA}', self)
        self.madera_precio.move(450, 185)
        self.madera_vender = QPushButton("Vender", self)
        self.madera_vender.move(490, 180)
        self.madera_vender.clicked.connect(self.boton_vender)

        self.oro = QLabel(self)
        self.oro.setGeometry(400, 240, 30, 30)
        imagen_oro = QPixmap(self.imagenes_tienda['oro'])
        self.oro.setPixmap(imagen_oro)
        self.oro.setScaledContents(True)
        self.oro_precio = QLabel(f'$ {parametros_precios.PRECIO_ORO}', self)
        self.oro_precio.move(450, 245)
        self.oro_vender = QPushButton("Vender", self)
        self.oro_vender.move(490, 240)
        self.oro_vender.clicked.connect(self.boton_vender)

        self.ticket = QLabel(self)
        self.ticket.setGeometry(220, 320, 40, 40)
        imagen_ticket = QPixmap(self.imagenes_tienda['ticket'])
        self.ticket.setPixmap(imagen_ticket)
        self.ticket.setScaledContents(True)
        self.ticket_precio = QLabel(f'$ {parametros_precios.PRECIO_TICKET}', self)
        self.ticket_precio.move(260, 330)
        self.ticket_comprar = QPushButton("Comprar", self)
        self.ticket_comprar.move(310, 325)
        self.ticket_comprar.clicked.connect(self.boton_comprar)

        self.show()

    def boton_comprar(self):
        sender = f'{self.sender()}'
        if sender == f'{self.azador_comprar}':
            self.senal_comprar_tienda.emit('azador', parametros_precios.PRECIO_AZADA)
        if sender == f'{self.hacha_comprar}':
            self.senal_comprar_tienda.emit('hacha', parametros_precios.PRECIO_HACHA)
        if sender == f'{self.semilla_choclo_comprar}':
            self.senal_comprar_tienda.emit('choclo_semillas',
                                           parametros_precios.PRECIO_SEMILLA_CHOCLOS)
        if sender == f'{self.semilla_alcachofa_comprar}':
            self.senal_comprar_tienda.emit('alcachofa_semillas',
                                           parametros_precios.PRECIO_SEMILLA_ALCACHOFAS)
        if sender == f'{self.ticket_comprar}':
            self.senal_comprar_tienda.emit('ticket', parametros_precios.PRECIO_TICKET)

    def boton_vender(self):
        sender = f'{self.sender()}'
        if sender == f'{self.azador_vender}':
            self.senal_vender_tienda.emit('azador', parametros_precios.PRECIO_AZADA)
        if sender == f'{self.hacha_vender}':
            self.senal_vender_tienda.emit('hacha', parametros_precios.PRECIO_HACHA)
        if sender == f'{self.semilla_choclo_vender}':
            self.senal_vender_tienda.emit('choclo_semillas',
                                          parametros_precios.PRECIO_SEMILLA_CHOCLOS)
        if sender == f'{self.semilla_alcachofa_vender}':
            self.senal_vender_tienda.emit('alcachofa_semillas',
                                          parametros_precios.PRECIO_SEMILLA_ALCACHOFAS)
        if sender == f'{self.choclo_vender}':
            self.senal_vender_tienda.emit('choclo', parametros_precios.PRECIO_CHOCLOS)
        if sender == f'{self.alcachofa_vender}':
            self.senal_vender_tienda.emit('alcachofa', parametros_precios.PRECIO_ALACACHOFAS)
        if sender == f'{self.madera_vender}':
            self.senal_vender_tienda.emit('madera', parametros_precios.PRECIO_LEÑA)
        if sender == f'{self.oro_vender}':
            self.senal_vender_tienda.emit('oro', parametros_precios.PRECIO_ORO)

    def transaccion_fallida(self, texto):
        self.label_bienvenida.setText(texto)


class VentanaInput(QWidget):
    senal_mapa_inicio = pyqtSignal(str)
    senal_eliminar_ventana_input = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.senal_iniciar_ventana_juego = None
        self.senal_procesar = None
        self.ventana_juego = front.MiVentana()
        self.init_gui()
        self.init_signals()

    def init_gui(self):
        self.setWindowTitle('DCCAMPO')
        self.setGeometry(230, 160, 600, 400)
        self.logo = QLabel(self)
        self.logo.setGeometry(95, 30, 400, 200)
        imagen = QPixmap(join("new_sprites", 'DCCAMPO.png'))
        self.logo.setPixmap(imagen)
        self.logo.setScaledContents(True)
        self.label = QLabel("Ingresa el nombre del mapa que quieres cargar", self)
        self.label.move(150, 250)
        self.input = QLineEdit('', self)
        self.input.setGeometry(150, 280, 285, 20)
        self.boton = QPushButton("Jugar", self)
        self.boton.move(245, 305)
        self.boton.clicked.connect(self.boton_clickeado)
        self.show()

    def init_signals(self):
        self.senal_mapa_inicio.connect(self.actualizar_mensaje)
        self.senal_eliminar_ventana_input.connect(self.input_correcto)
        self.senal_eliminar_ventana_input = self.ventana_juego.senal_eliminar_ventana_input

    def boton_clickeado(self):
        if self.senal_procesar:
            texto_input = self.input.text()
            self.senal_procesar.emit(texto_input)

    def actualizar_mensaje(self, texto):
        self.label.setText(texto)

    def input_correcto(self):
        self.hide()
