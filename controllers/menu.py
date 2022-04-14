from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.Ui_menuBotones import Ui_MenuPrincipal
from views.botonesMenu import Menu_Botones

#from controllers.pago_prestamo import Pagos
from controllers.busqueda_pago import buscueda_prestamo
from controllers.cancelacion import Error
from PySide6.QtCore import Qt
from controllers.busqueda import buscar

from database import recipes
import os
class Menu(QWidget, Ui_MenuPrincipal):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.cc()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    def cc(self):
        self.cancelar.clicked.connect(self.Open_cancelacion)
        self.abonar.clicked.connect(self.Open_pagosPrestamos)
        self.prestamo.clicked.connect(self.open_busqueda)
    def Open_pagosPrestamos(self):
        self.window=buscueda_prestamo(self)
        self.window.show()
    def Open_cancelacion(self):
        self.window=Error(self)
        self.window.show()
    def open_busqueda(self):
        self.window=buscar(self)
        self.window.show()
    def cerrar(self):
        self.window=Menu(self)
        self.window.close()
        
       
    
    
        
    
        