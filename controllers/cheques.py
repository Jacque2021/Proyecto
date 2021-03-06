import codecs
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from controllers.chequeRealizado import Cheque
from views.botonesMenu import Menu_Botones
from controllers.error_prestamo import Error_p
from views.cheque_exitoso import cheq
from datetime import datetime
from views.cheques import Cheques
import datetime 
from datetime import date
from PySide6.QtWidgets import (QWidget, QMenu)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QActionGroup
import datetime
from fpdf import FPDF
import webbrowser as wb
from database import recipes


class ChequesForm(QWidget, Cheques, FPDF):

    def __init__(self, parent=None, Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent) 
        #self.id=id
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.Id_cliente=Id_cliente
        self.llamar_nombre()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.vista()
        self.cc()
        self.menu()
        self.boton_cancelar_2.clicked.connect(self.clear_inputs)
        
       # self.boton_buscar_2.clicked.connect(self.open_busqueda)
        self.boton_emitir_2.clicked.connect(self.nuevo_cheque)
        
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
  
    
    def llamar_nombre(self): 
        data=recipes.select_cliente_cheque(self.Id_cliente)
        id=data[0]
        id = str(id)
        nombre=data[1]
        apellidos=data[2]
        apellidos = str(apellidos)
        self.id_c.setText(id)
        self.nombre_c.setText(nombre)
        self.apellidos_c.setText(apellidos)
    
    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.fechaf.setText(str(convertida1)) #lo pasa a la interfaz

    def nuevo_cheque(self):
        id = self.id_c.text()
        nombre = self.nombre_c.text()
        apellidos = self.apellidos_c.text()
        fecha = self.fechaf.text()
        monto = self.caja_monto_2.text()
        beneficiario = self.caja_beneficiario_2.text()
        descripcion = self.caja_descripcion_2.text()
        
 
        data = (id, nombre, apellidos, fecha, monto, beneficiario, descripcion)
        
        
  ### CREAR DOC PDF CHEQUE
         ##########
        pdf=FPDF(orientation='P',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
        #empresa=recipes.empresa      JACQUE
        empresa=recipes.empresa()
        nombre_empresa=str(empresa[0])
        direccion2=str(empresa[1])
        ##################################
        nombre_emp=nombre_empresa
        ubicacion_emp=direccion2
        #Arial bold 15
        pdf.set_font('Arial', '',18)
        #Titulo
        pdf.cell(w=0,h=10,txt=nombre_emp,border=0,ln=1,align='R',fill=0)
        pdf.set_font('Arial', '',8)
        pdf.cell(w=0,h=5,txt=ubicacion_emp,border=0,ln=1,align='R',fill=0)
        pdf.cell(w=0,h=5,txt=' '+"",border=0,ln=1,align='R',fill=0)
        #line breack
        pdf.ln(5)
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="CHEQUE",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="Páguese este cheque a la orden de:",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
        pdf.set_font('Arial', '', 12)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.cell(w=0,h=5, txt="Información del cliente",border=1,ln=1,align='C', fill=1)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.cell(w=25,h=4, txt="No° cliente",border=1,align='C', fill=1)
        pdf.cell(w=125,h=4, txt="Nombre del cliente",border=1,align='C', fill=1,ln=0)
        pdf.cell(w=0,h=4, txt="Apellidos del cliente",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=25,h=4, txt=str(id),border=1,align='C', fill=0)
        pdf.cell(w=125,h=4, txt=nombre,border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=apellidos,border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="",border=0,align='C', fill=0,ln=1)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.cell(w=0,h=5, txt="Información general del cheque",border=1,ln=1,align='C', fill=1)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.cell(w=45,h=4, txt="Cliente",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Fecha de emisión",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Monto",border=1,align='C', fill=1)
        pdf.cell(w=45,h=4, txt="Beneficiario",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Descripción",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=45,h=4, txt=str(id),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(fecha),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt='$'+str(monto),border=1,align='C', fill=0)
        pdf.cell(w=45,h=4, txt=str(beneficiario),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt=str(descripcion),border=1,align='C', fill=0,ln=1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(w=0,h=5, txt="FIRMA",border=0,ln=1,align='C', fill=0)
                
        if len(id)==0 or len(nombre)==0 or len(apellidos)==0 or len(fecha)==0 or len(monto)==0 or len(beneficiario)==0 or len(descripcion)==0:
            self.Open3()
       
        elif recipes.crear_cheque(data):
           print("Nuevo cheque realizado")
           self.clear_inputs()
           self.Open()
        
           b=date.today()
           ejemp=str(nombre)
           m=ejemp+"_"+str(b)
           pdf.output('cheques/'+str(m)+'.pdf','f')
           wb.open_new(f"cheques\{m}"+".pdf")#jacque
           #wb.open_new('C:/Users/Almar/Documents/Proyecto/cheques'+str(m)+'.pdf')
           #(f"pagos\{m}"+".pdf")
          

    def Open(self):
        window=Cheque(self)
        window.show()

    def Open3(self):
        window=Error_p(self)
        window.show()
    
    def clear_inputs(self):
        self.id_c.clear()
        self.nombre_c.clear()
        self.apellidos_c.clear()
        self.fechaf.clear()
        self.caja_monto_2.clear()
        self.caja_beneficiario_2.clear()
        self.caja_descripcion_2.clear()

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