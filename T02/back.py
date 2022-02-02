from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from os.path import isfile
from parametros_generales import DURACION_DIA, PROB_ARBOL, PROB_ORO
from os.path import join
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QImage
from PyQt5.QtCore import QMimeData, Qt
import front


class MiBack(QObject):
    senal_ticket_ganador = pyqtSignal()
    senal_procesar = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.senal_limpiar_inicio = None
        self.senal_mapa_inicio = None
        self.senal_iniciar_juego = None
        self.senal_input_correcto = None
        #
        self.senal_procesar.connect(self.procesar_input)
        self.senal_ticket_ganador.connect(self.ticket_ganador)

        self.ganador = False

    # Procesa la info desde el front -> Funciona
    def procesar_input(self, texto_input):
        if not self.mapa_valido(texto_input):
            self.actualizar_mensaje_back('El mapa elegido no existe, intenta nuevamente')
        else:
            self.actualizar_interfaz(texto_input)
            self.cargar_background(texto_input)

    # Manda la senal de que el input fue incorrecto -> Listo
    def actualizar_mensaje_back(self, texto):
        if self.senal_mapa_inicio:
            self.senal_mapa_inicio.emit(texto)

    # Manda la senal de sacar los componentes iniciales -> Listo
    def actualizar_interfaz(self, texto):
        if self.senal_limpiar_inicio:
            self.senal_limpiar_inicio.emit(texto)

    # Carga el mapa
    def cargar_background(self, texto):
        if self.senal_iniciar_juego:
            self.senal_iniciar_juego.emit(texto)

    # Verifica la existencia del mapa -> Listo
    def mapa_valido(self, texto_input):
        if not isfile(f'mapas/{texto_input}.txt'):
            return False
        return True

    def ticket_ganador(self):
        self.ganador = True


######### TIMER ###########
class TiempoJuego(QObject):
    senal_actualizar_tiempo = pyqtSignal(str)
    senal_actualizar_dia = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.tiempo = ''
        self._dia = 1
        self.hora = 14
        self._minuto = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tiempo_juego)
        self.contador = 0

    def tiempo_juego(self):
        self.tiempo = f'{str(self.hora).zfill(2)}:{str(self._minuto).zfill(2)}'
        self._minuto += 1
        self.contador += 1
        if self._minuto >= 60:
            self._minuto -= 60
            self.hora += 1
            if self.hora == 24:
                self.hora = 0
        if self.contador == DURACION_DIA:
            self._dia += 1
            self.contador = 0
            self.actualizar_dia(f'{self._dia}')
        self.actualizar_tiempo(self.tiempo)

    def comenzar(self):
        self.timer.start()

    def pausar(self):
        self.timer.stop()

    def timer_activo(self):
        return self.timer.isActive()

    def actualizar_tiempo(self, texto):
        if self.senal_actualizar_tiempo:
            self.senal_actualizar_tiempo.emit(texto)

    def actualizar_dia(self, texto):
        if self.senal_actualizar_dia:
            self.senal_actualizar_dia.emit(texto)

    @property
    def minuto(self):
        return self._minuto

    @minuto.setter
    def minuto(self, valor):
        self._minuto = valor

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, valor):
        self._dia = valor


class DraggableLabel(QLabel):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() \
                < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)


class DropLabel(QLabel):

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.ventana = front.MiVentana()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            print("event accepted - Drop event")
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
