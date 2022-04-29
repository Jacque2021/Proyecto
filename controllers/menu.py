from PySide6.QtWidgets import (QWidget)
#from PySide6.QtGui import QAction, QActionGroup
from views.general_custom_ui import GeneralCustomUi
from views.Ui_menuBotones import Ui_MenuPrincipal
from views.botonesMenu import Menu_Botones
from PySide6.QtWidgets import (QWidget, QMenu)
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtCore import Qt
from controllers.busqueda_pago import buscueda_prestamo
from controllers.cancelacion import Error
from controllers.busqueda_retirar_ahorro import buscar_retirar_ahorro
from controllers.busqueda_re_ahorro import buscar_re_ahorro
from controllers.busqueda import buscar
from controllers.busqueda_c import buscarc
from controllers.consulta_cheques import Consulta_chequesForm
from controllers.notificaciones import Notificacion
from controllers.ayuda import Documento
from controllers.mi_empresa import MiEmpresaForm
from controllers.respaldar_empresa import RespaldarEmpresaForm
from controllers.cheques import ChequesForm
from database import recipes
import os
class Menu(QWidget, Ui_MenuPrincipal):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.bm=Menu_Botones(self)
        self.ui=GeneralCustomUi(self)
        self.cc()
        self.menu()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    def cc(self):
        self.cancelar.clicked.connect(self.Open_cancelacion)
        #self.prestamo.triggered.connect(self.Open_cancelacion)###
        self.abonar.clicked.connect(self.Open_pagosPrestamos)
        self.prestamo.clicked.connect(self.open_busqueda)
        self.Mi_Empresa.clicked.connect(self.open_empresa)
        self.Respaldo.clicked.connect(self.open_repaldaempresa)
        self.Cheques.clicked.connect(self.open_cheques)
        self.Consulta_cheque.clicked.connect(self.open_consulta_cheques)
        self.Ahorro.clicked.connect(self.open_nuevo_ahorro)
        self.Retirar.clicked.connect(self.open_retiro_ahorro)
        self.Ayuda.clicked.connect(self.ayuda)
        self.Notificaciones.clicked.connect(self.Notificacio)
        self.Salir.clicked.connect(self.close)
    def Open_pagosPrestamos(self):
        window=buscueda_prestamo(self)
        window.show()
    def Open_cancelacion(self):
        window=Error(self)
        window.show()
    def open_busqueda(self):
        window=buscar(self)
        window.show()
    def cerrar(self):
        window=Menu(self)
        window.close()
    def ayuda(self):
        window=Documento(self)
        window.show()
    def Notificacio(self):
        window=Notificacion(self)
        window.show()
    """***AQUI ESTUVO MAY***"""
    def open_empresa(self):
        self.window=MiEmpresaForm(self)
        self.window.show()
    def open_repaldaempresa(self):
        self.window=RespaldarEmpresaForm(self)
        self.window.show()
    def open_cheques(self):
        self.window=buscarc(self)
        self.window.show()
    def open_consulta_cheques(self):
        self.window=Consulta_chequesForm(self)
        self.window.show()
    def open_nuevo_ahorro(self):
        self.window=buscar_re_ahorro(self)
        self.window.show()
    def open_retiro_ahorro(self):
        self.window=buscar_retirar_ahorro(self)
        self.window.show()
    """***AQUI ESTUVO ??***"""  
        
        
    """*************************  SUB MENU 2 ****************************"""
    ###################################################################  
    def prestamos1(self):
        self.Prestamos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Prestamos.customContextMenuRequested.connect(self.on_context_menu)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('Nuevo prestamo', np))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Abonar pago', ap))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Cancelar pago', cancela))
        
        np.triggered.connect(self.open_busqueda)
        ap.triggered.connect(self.Open_pagosPrestamos)
        cancela.triggered.connect(self.Open_cancelacion)
    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.Prestamos.mapToGlobal(point))
        
    ##############################################################
    def miempresa(self):
        self.Empresa.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Empresa.customContextMenuRequested.connect(self.on_context_menu1)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu1 = QMenu(self)
        self.popMenu1.addAction(QAction('Mi empresa', np))
        self.popMenu1.addSeparator()
        self.popMenu1.addAction(QAction('Respaldar empresa', ap))
        self.popMenu1.addSeparator()
        self.popMenu1.addAction(QAction('Catálogo de cuentas', cancela))
        
        np.triggered.connect(self.open_empresa)
        ap.triggered.connect(self.open_repaldaempresa)
        cancela.triggered.connect(self.Open_cancelacion)
    def on_context_menu1(self, point):
        # show context menu
        self.popMenu1.exec_(self.Empresa.mapToGlobal(point))
    ##############################################################
    def clientes(self):
        self.Clientes.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Clientes.customContextMenuRequested.connect(self.on_context_menu2)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu2 = QMenu(self)
        self.popMenu2.addAction(QAction('Agregar nuevo cliente', np))
        self.popMenu2.addSeparator()
        self.popMenu2.addAction(QAction('Historial del cliente', ap))
    
        np.triggered.connect(self.open_busqueda)
        ap.triggered.connect(self.Open_pagosPrestamos)
    def on_context_menu2(self, point):
        # show context menu
        self.popMenu2.exec_(self.Clientes.mapToGlobal(point))
    ##############################################################
    def ahorro(self):
        self.Ahorros.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Ahorros.customContextMenuRequested.connect(self.on_context_menu3)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu3 = QMenu(self)
        self.popMenu3.addAction(QAction('Nuevo ahorro', np))
        self.popMenu3.addSeparator()
        self.popMenu3.addAction(QAction('Retirar ahorro', ap))
    
        np.triggered.connect(self.open_nuevo_ahorro)
        ap.triggered.connect(self.open_retiro_ahorro)
    def on_context_menu3(self, point):
        # show context menu
        self.popMenu3.exec_(self.Ahorros.mapToGlobal(point))
    ##############################################################
    def consultas(self):
        self.Consultas.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Consultas.customContextMenuRequested.connect(self.on_context_menu4)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu4 = QMenu(self)
        self.popMenu4.addAction(QAction('PLD', np))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Estado de cuentas', ap))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Emitir reporte', cancela))
        
        np.triggered.connect(self.open_busqueda)
        ap.triggered.connect(self.Open_pagosPrestamos)
        cancela.triggered.connect(self.Open_cancelacion)
    def on_context_menu4(self, point):
        # show context menu
        self.popMenu4.exec_(self.Consultas.mapToGlobal(point))
    ##############################################################
    def polizas(self):
        self.PolizaS.setContextMenuPolicy(Qt.CustomContextMenu)
        self.PolizaS.customContextMenuRequested.connect(self.on_context_menu5)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu5 = QMenu(self)
        self.popMenu5.addAction(QAction('Nueva poliza', np))
        self.popMenu5.addSeparator()
        self.popMenu5.addAction(QAction('Listado de polizas', ap))
        
        np.triggered.connect(self.open_busqueda)
        ap.triggered.connect(self.Open_pagosPrestamos)
    def on_context_menu5(self, point):
        # show context menu
        self.popMenu5.exec_(self.PolizaS.mapToGlobal(point))
    ##############################################################
    def cheques(self):
        self.ChequeS.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ChequeS.customContextMenuRequested.connect(self.on_context_menu6)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu6 = QMenu(self)
        self.popMenu6.addAction(QAction('Cheques', np))
        self.popMenu6.addSeparator()
        self.popMenu6.addAction(QAction('Consultar cheques', ap))
        
        np.triggered.connect(self.open_cheques)
        ap.triggered.connect(self.open_consulta_cheques)

    def on_context_menu6(self, point):
        # show context menu
        self.popMenu6.exec_(self.ChequeS.mapToGlobal(point))
    
    def menu(self):
        self.prestamos1()
        self.miempresa()
        self.clientes()
        self.ahorro()
        self.consultas()
        self.polizas()
        self.cheques()