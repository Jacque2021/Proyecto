from views.Ui_ayuda import Ayuda
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QMovie
import sys

class Documento(QWidget, Ayuda):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.imagen()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    def imagen(self):
        self.movie = QMovie("imagenes/dul.gif")
        self.imagen1.setMovie(self.movie)
        self.movie.start()
        
        self.movie2 = QMovie("imagenes/presta.gif")
        self.imagen2.setMovie(self.movie2)
        self.movie2.start()
        
        self.movie3 = QMovie("imagenes/im3.gif")
        self.label_13.setMovie(self.movie3)
        self.movie3.start()
        
        """self.movie4 = QMovie("imagenes/prestamo.gif")
        self.imagen4.setMovie(self.movie4)
        self.movie4.start()"""
        
        self.movie5 = QMovie("imagenes/pdf.gif")
        self.imagen5.setMovie(self.movie5)
        self.movie5.start()
        
        self.movie6 = QMovie("imagenes/cancelacion.gif")
        self.label_15.setMovie(self.movie6)
        self.movie6.start()

## EMPRESA
        self.movie7 = QMovie("imagenes/empresa.gif")
        self.imagen6.setMovie(self.movie7)
        self.movie7.start()

## RESPALDA EMPRESA
        self.movie8 = QMovie("imagenes/respaldo.gif")
        self.imagen7.setMovie(self.movie8)
        self.movie8.start()

## NUEVO AHORRO
        self.movie9 = QMovie("imagenes/ahorro.gif")
        self.imagen8.setMovie(self.movie9)
        self.movie9.start()

## RETIRAR AHORRO
        self.movie10 = QMovie("imagenes/retiro.gif")
        self.imagen9.setMovie(self.movie10)
        self.movie10.start()

## CHEQUE
        self.movie11 = QMovie("imagenes/cheques.gif")
        self.imagen10.setMovie(self.movie11)
        self.movie11.start()

## CONSULTA CHEQUE
        self.movie12 = QMovie("imagenes/consultach.PNG")
        self.imagen10_2.setMovie(self.movie12)
        self.movie12.start()

## CATALOGO DE CUENTAS
        self.movie13 = QMovie("imagenes/catalogo.gif")
        self.imagen_ca1.setMovie(self.movie13)
        self.movie13.start()

## AGREGAR CLIENTE
        self.movie14 = QMovie("imagenes/agregar_cliente.gif")
        self.imagen_c1.setMovie(self.movie14)
        self.movie14.start()

## HISTORIAL DEL CLIENTE
        self.movie15 = QMovie("imagenes/historial.gif")
        self.imagen_c2.setMovie(self.movie15)
        self.movie15.start()

## NUEVA POLIZA
        self.movie16 = QMovie("imagenes/Nueva-poliza-1.gif")
        self.imagen_np.setMovie(self.movie16)
        self.movie16.start()

## LISTADO DE POLIZAS
        self.movie17 = QMovie("imagenes/listado_polizas.gif")
        self.imagen_lp.setMovie(self.movie17)
        self.movie17.start()

## ESTADO DE CUENTAS
        self.movie18 = QMovie("imagenes/Estado-de-cuenta-1.gif")
        self.imagen_ec.setMovie(self.movie18)
        self.movie18.start()

## EMITIR REPORTE DE AHORROS 1
        self.movie19 = QMovie("imagenes/Reporte-1.gif")
        self.imagen_ra.setMovie(self.movie19)
        self.movie19.start()

## EMITIR REPORTE DE AHORROS 2
        self.movie20 = QMovie("imagenes/Reporte-2.gif")
        self.imagen_ra_avi.setMovie(self.movie20)
        self.movie20.start()    

## EMITIR REPORTE DE AHORROS 3
        self.movie21 = QMovie("imagenes/Reporte-3.gif")
        self.imagen_ra_PDF.setMovie(self.movie21)
        self.movie21.start()    

## EMITIR REPORTE DE PRESTAMOS 1
        self.movie22 = QMovie("imagenes/Reporte-4.gif")
        self.imagen_rp.setMovie(self.movie22)
        self.movie22.start()

## EMITIR REPORTE DE PRESTAMOS 2
        self.movie23 = QMovie("imagenes/Reporte-5.gif")
        self.imagen_rp_avi.setMovie(self.movie23)
        self.movie23.start()    

## EMITIR REPORTE DE PRESTAMOS 3
        self.movie24 = QMovie("imagenes/Reporte-6.gif")
        self.imagen_rp_PDF.setMovie(self.movie24)
        self.movie24.start()    

