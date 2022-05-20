from PySide6.QtWidgets import (QWidget, QMenu)
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtCore import Qt
import math
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_NuevoPrestamo import Ui_Nuevoprestamo
from controllers.prestamo_registrado import mensaje
from controllers.mensaje_error import mensaje_error
from controllers.mensaje_error2 import mensaje_error2
from controllers.mensaje_error3 import mensaje_error3
from decimal import Decimal
from database import recipes
from controllers.cancelacion import Error
import datetime
from datetime import date

class Prestamos(QWidget, Ui_Nuevoprestamo):
    def __init__(self, parent=None,Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.Id_cliente=Id_cliente
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.bm=Menu_Botones(self)
        self.ui=GeneralCustomUi(self)
        self.llamar_nombre()
        self.Guardar.clicked.connect(self.insertar_prestamos)
        self.Borrar.clicked.connect(self.limpirar_parametros)
        self.menu()
        self.cc()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    def llamar_nombre(self): 
        data=recipes.select_cliente(self.Id_cliente)
        Id_cl=data[0]
        nombre=str(data[1])
        punctuation=data[2]
        if punctuation <18:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 25000 con un plazo máximo de 18 meses para pagar")
        elif punctuation >= 18 and punctuation <42:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 100,000 con un plazo máximo de 24 meses para pagar")
        elif  punctuation >= 42:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 300,000 con un plazo máximo de 36 meses para pagar")
        self.nom_cliente.setText(nombre)

#********************** INSERTAR DATOS PARA EL PRESTAMO **********************#
    def insertar_prestamos(self,):
        data=recipes.select_cliente(self.Id_cliente)
        Id_cl=data[0]
        punctuation=data[2]
        nombre=data[1]
        prestamo=Decimal(self.Cantidad.text())
        cantidad_prestamo=prestamo  #total prestamo
        frecuencia=Decimal(self.Frecuencia.text()) #si es mensual, trimestral, semestral
        a=Decimal(frecuencia)
        tiempo="Mensual"
        #tiempo=Decimal(self.Tiempo.text()) #tiempo en años
        periodo=a #periodo=frecuencia*tiempo    condicion
        x=Decimal(self.Interes.text())
        Iva=x/100   #sacar porcentaje de tasa anual
        Iva_div=Iva/frecuencia  #porcentaje mensual
        #saldo_insolito=prestamo-renta
        x=prestamo*Iva_div
        y=1-(math.pow((1+Iva_div),-periodo))
        z=x/Decimal(y)
        renta=z         #pagos mensuales
        interes=prestamo*Iva_div    
        amortizacion=renta-interes
        amortizacion_acum=0
        saldo_insolito=prestamo
        fecha_inicio=datetime.date.today()
        fecha=datetime.date.today()
        dia_delta=datetime.timedelta(days=30)
        fecha_siguiente=fecha+dia_delta
        nombre_codeudor=self.Codeudor.text()
        Garantia=self.Garantia.text()
        #condiciones para el prestamo
        if punctuation <18 and cantidad_prestamo>25000 and a>18:
            self.window=mensaje_error3(self)
            self.window.show()
        elif punctuation >= 18 and punctuation <42 and cantidad_prestamo>100000 and a>24:
            self.window=mensaje_error3(self)
            self.window.show()
        elif punctuation >= 42 and cantidad_prestamo>300000 and a>36:
            self.window=mensaje_error3(self)
            self.window.show()
        elif punctuation <18 and cantidad_prestamo>25000:
            self.window=mensaje_error(self)
            self.window.show()
        elif punctuation >= 18 and punctuation <42 and cantidad_prestamo>100000:
            self.window=mensaje_error(self)
            self.window.show()
        elif  punctuation >= 42 and cantidad_prestamo>300000:
            self.window=mensaje_error(self)
            self.window.show()
        elif a>18 and cantidad_prestamo<=25000:
            self.window=mensaje_error2(self)
            self.window.show()
        elif a>24 and cantidad_prestamo<=100000:
            self.window=mensaje_error2(self)
            self.window.show()
        elif a>36 and cantidad_prestamo<=300000:
            self.window=mensaje_error2(self)
            self.window.show()
        else:
            b=date.today()
            ejemp=str(nombre)
            m=ejemp+"_"+str(b)
            l="imagenes\{m}"+".pdf"
            link=f"prestamos\{m}"+".pdf"
            dato=(Id_cl,cantidad_prestamo,frecuencia,tiempo,periodo,Iva,Iva_div,saldo_insolito,renta,interes,
              amortizacion,amortizacion_acum,fecha_inicio,fecha_siguiente,nombre_codeudor,Garantia,link) 
        
            if recipes.insert_Prestamos(dato):
                print("Recipe Added")
                self.limpirar_parametros()
                self.Guardar.setVisible(False)
            self.Open_emergente()
        return Id_cl
#********************** LIMPIAR LA INTERFAZ **********************    
    def limpirar_parametros(self):
        self.nom_cliente.clear()
        self.nom_cliente.clear()
        self.Cantidad.clear()
        self.Frecuencia.clear()
        self.Interes.clear()
        self.Tiempo.clear()
        self.Codeudor.clear()
        self.Garantia.clear()
        self.TextoError.clear()
        self.cantidad_prestamo.clear()
        self.Plazo_max.clear()
    
    """ABRIR VENTANA EMERGENTE"""
    def Open_emergente(self):
        self.window=mensaje(self)
        self.window.show()
        
################################################################################################
#########################                MENU                ###################################
################################################################################################ 
    def Open_pagosPrestamos(self):
        from controllers.busqueda_pago import buscueda_prestamo
        window=buscueda_prestamo(self)
        self.hide()
        window.show()
    def Open_cancelacion(self):
        from controllers.cancelacion import Error
        window=Error(self)
        self.hide()
        window.show()
    def open_busqueda(self):
        from controllers.busqueda import buscar
        window=buscar(self)
        self.hide()
        window.show()
    def cerrar(self):
        self.hide()
    def ayuda(self):
        from controllers.ayuda import Documento
        window=Documento(self)
        self.hide()
        window.show()
    def Notificacio(self):
        from controllers.notificaciones import Notificacion
        window=Notificacion(self)
        self.hide()
        window.show()
    """***AQUI ESTUVO MAY***"""
    def open_empresa(self):
        from controllers.mi_empresa import MiEmpresaForm
        self.window=MiEmpresaForm(self)
        self.hide()
        self.window.show()
    def open_repaldaempresa(self):
        from controllers.respaldar_empresa import RespaldarEmpresaForm
        self.window=RespaldarEmpresaForm(self)
        self.hide()
        self.window.show()
    def open_cheques(self):
        from controllers.busqueda_c import buscarc
        self.window=buscarc(self)
        self.hide()
        self.window.show()
    def open_consulta_cheques(self):
        from controllers.consulta_cheques import Consulta_chequesForm
        self.window=Consulta_chequesForm(self)
        self.hide()
        self.window.show()
    def open_nuevo_ahorro(self):
        from controllers.busqueda_re_ahorro import buscar_re_ahorro
        self.window=buscar_re_ahorro(self)
        self.hide()
        self.window.show()
    def open_retiro_ahorro(self):
        from controllers.busqueda_retirar_ahorro import buscar_retirar_ahorro
        self.window=buscar_retirar_ahorro(self)
        self.hide()
        self.window.show()
    """***AQUI ESTUVO PABLO***"""
    def Open_historial_cliente(self):
        from controllers.historial_cliente import HistorialClienteForm
        self.window=HistorialClienteForm(self)
        self.hide()
        self.window.show()
    def Open_listado_polizas(self):
        from controllers.listado_polizas import ListadoPolizasForm
        self.window=ListadoPolizasForm(self)
        self.hide()
        self.window.show()
    def Open_agregar_cliente(self):
        from controllers.agregar_cliente import AgregarClienteForm
        self.window=AgregarClienteForm(self)
        self.hide()
        self.window.show()
    def open_catalogo(self):
        from controllers.busqueda_e import buscar_empresa
        self.window=buscar_empresa(self)
        self.hide()
        self.window.show()
    """***AQUI ESTUVO JESUS***"""
    def open_estadoCUENTAS(self):
        from controllers.ConsultaEstadoCuentas import buscarCuenta
        self.window=buscarCuenta(self)
        self.hide()
        self.window.show()
    def open_emitirReport(self):
        from controllers.EmitirReporte import emite_R
        self.window=emite_R(self)
        self.hide()
        self.window.show()
    def open_emitirReport_2(self):
        from controllers.EmitirReporte_2 import emite_R_2
        self.window=emite_R_2(self)
        self.hide()
        self.window.show()
    def open_nPoliza(self):
        from controllers.NuevaPoliza import nuevaPoliza
        self.window=nuevaPoliza(self)
        self.hide()
        self.window.show()
################################################################################################
#########################                MENU V.2            ###################################
################################################################################################ 
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
        cancela.triggered.connect(self.open_catalogo)
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
    
        np.triggered.connect(self.Open_agregar_cliente)
        ap.triggered.connect(self.Open_historial_cliente)
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
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
         ########################3
        cancela2 = QActionGroup(self)
        cancela2.setExclusive(True)
        # create context menu
        self.popMenu4 = QMenu(self)
        self.popMenu4.addAction(QAction('Estado de cuentas', ap))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Emitir reporte de ahorro', cancela))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Emitir reporte de prestamos', cancela2))
        
        ap.triggered.connect(self.open_estadoCUENTAS)
        cancela.triggered.connect(self.open_emitirReport)
        cancela2.triggered.connect(self.open_emitirReport_2)
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
        
        np.triggered.connect(self.open_nPoliza)
        ap.triggered.connect(self.Open_listado_polizas)
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
        self.Cliente.clicked.connect(self.Open_agregar_cliente)
        self.Listado.clicked.connect(self.Open_listado_polizas)
        self.Historial.clicked.connect(self.Open_historial_cliente)
        self.Catalogo.clicked.connect(self.open_catalogo)
        self.Estado.clicked.connect(self.open_estadoCUENTAS)
        self.Reportes.clicked.connect(self.open_emitirReport)
        self.Reportes_2.clicked.connect(self.open_emitirReport_2)
        self.Polizas.clicked.connect(self.open_nPoliza)
    def menu(self):
        self.prestamos1()
        self.miempresa()
        self.clientes()
        self.ahorro()
        self.consultas()
        self.polizas()
        self.cheques()