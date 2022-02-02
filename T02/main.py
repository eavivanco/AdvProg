from PyQt5.QtWidgets import QApplication
from front import MiVentana
from front_tienda import VentanaTienda, VentanaInput
from back import MiBack
import sys

if __name__ == '__main__':
    app = QApplication([])

    back = MiBack()
    ventana = MiVentana()
    ventana_input = VentanaInput()
    ventana_tienda = VentanaTienda()
    ventana_input.senal_eliminar_ventana_input = ventana.senal_eliminar_ventana_input
    back.senal_mapa_inicio = ventana_input.senal_mapa_inicio
    ventana.senal_limpiar_inicio = back.senal_limpiar_inicio
    ventana.senal_ticket_ganador = back.senal_ticket_ganador
    ventana_input.senal_procesar = back.senal_procesar
    ventana_input.senal_input_correcto = back.senal_input_correcto
    back.senal_iniciar_juego = ventana.senal_iniciar_juego
    ventana_tienda.senal_transaccion_fallida = ventana.senal_transaccion_fallida
    ventana_tienda.senal_mostrar_tienda = ventana.senal_mostrar_tienda
    ventana_tienda.senal_comprar_tienda = ventana.senal_comprar_tienda
    ventana_tienda.senal_vender_tienda = ventana.senal_vender_tienda

    sys.exit(app.exec_())
