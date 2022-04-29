from views.Ui_ayuda import Ayuda
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
#from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QMovie
#import sys

class Documento(QWidget, Ayuda):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.imagen()
        self.cc()
        #self.bm.cc()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    def imagen(self):
        self.movie = QMovie("imagenes/dul.gif")
        self.imagen1.setMovie(self.movie)
        self.movie.start()
        
        self.movie2 = QMovie("imagenes/presta.gif")
        self.imagen2.setMovie(self.movie2)
        self.movie2.start()
        
        """self.movie3 = QMovie("imagenes/prestamo.gif")
        self.imagen3.setMovie(self.movie3)
        self.movie3.start()
        
        self.movie4 = QMovie("imagenes/prestamo.gif")
        self.imagen4.setMovie(self.movie4)
        self.movie4.start()"""
        
        self.movie5 = QMovie("imagenes/pdf.gif")
        self.imagen5.setMovie(self.movie5)
        self.movie5.start()
        
        """self.movie6 = QMovie("imagenes/cancelacion.gif")
        self.imagen6.setMovie(self.movie6)
        self.movie6.start()"""
    """  Menu  """
    def Open_pagosPrestamos(self):
        from controllers.busqueda_pago import buscueda_prestamo
        self.window=buscueda_prestamo(self)
        self.hide()
        self.window.show()
    def Open_cancelacion(self):
        from controllers.cancelacion import Error
        self.window=Error(self)
        self.hide()
        self.window.show()
    def open_busqueda(self):
        from controllers.busqueda import buscar
        self.window=buscar(self)
        self.hide()
        self.window.show()
    def ayuda(self):
        from controllers.ayuda import Documento
        self.window=Documento(self)
        self.hide()
        self.window.show()
    def Notificacio(self):
        from controllers.notificaciones import Notificacion
        self.window=Notificacion(self)
        self.hide()
        self.window.show()
    def cc(self):
        self.cancelar.clicked.connect(self.Open_cancelacion)
        #self.prestamo.triggered.connect(self.Open_cancelacion)###
        self.abonar.clicked.connect(self.Open_pagosPrestamos)
        self.prestamo.clicked.connect(self.open_busqueda)
        self.Ayuda.clicked.connect(self.ayuda)
        self.Notificaciones.clicked.connect(self.Notificacio)
        self.Salir.clicked.connect(self.close)