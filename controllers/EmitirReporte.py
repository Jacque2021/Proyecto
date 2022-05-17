from multiprocessing import parent_process
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from controllers.error_prestamo import Error_p
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_EmitirReporte import Emi_report
from datetime import datetime
from database import recipes
from datetime import date
from fpdf import FPDF
import webbrowser as wb
from PySide6.QtWidgets import (QWidget, QMenu)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QActionGroup



class emite_R(QWidget, Emi_report):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.setWindowFlag(Qt.Window)
        self.config_table()
        self.boton_buscar_fechas.clicked.connect(self.filtro_fechas)
        self.codigo_cliente2.returnPressed.connect(self.filtro_fechas)
        self.boton_imprimir.clicked.connect(self.crear_pdf)
        self.boton_imprimir.clicked.connect(self.abrir)
        #self.boton_buscar_ID.clicked.connect(self.flitro_ID)
        self.cc()
        self.menu()

    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)

    def filtro_fechas(self):
        fecha1 = self.fecha_1.text()
        fecha2 = self.fecha_2.text()
        fecha_1 = datetime.strptime(fecha1,'%d/%m/%Y')
        fecha_2 = datetime.strptime(fecha2,'%d/%m/%Y')
        #fecha_1 = str('2022-06-01 00:00:00')
        #fecha_2 = str('2022-08-01 00:00:00')
        codigo_cliente1 = self.codigo_cliente1.text()
        codigo_cliente2 = self.codigo_cliente2.text()
        if fecha_1 != "" and fecha_2 != "" and codigo_cliente1 != "" and codigo_cliente2 != "":
            # print("PRIMER METODO")
            # print(fecha_1)
            # print(fecha_2)
            # print(codigo_cliente1)
            # print(codigo_cliente2)
            data=recipes.filtro_Ahorro_fecha_ID(fecha_1,fecha_2,codigo_cliente1,codigo_cliente2)
            self.populate_table(data)
            self.crear_pdf(data)
            print(data)
        
        elif fecha_1 != "" and fecha_2 != "" and codigo_cliente1 == "" and codigo_cliente2 == "":
            print("SEGUNDO METODO")
            data=recipes.filtro_Nuevo_ahorro(fecha_1,fecha_2)
            print(data)
            # print(fecha_1)
            # print(fecha_2)
            self.populate_table(data)
            self.crear_pdf(data)
        else:
            print("DEBES LLENAR TODOS LOS CAMPOS") 
            self.window=Error_p(self)
            self.window.show()

    def config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("ID \nCLIENTE","NOMBRE", "APELLIDOS", "ID\nAHORRO",
        "IMPORTE","T.E.A.","PLAZO","CAPITAL","FECHA \nDE APERTURA"
        ,"FECHA \nINICIO","FECHA \nVENCIMIENTO")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 70) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 120) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(2, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(3, 90) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(4, 90) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(5, 90) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(6, 90) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(7, 90) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(8, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(9, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(10, 70) #ancho de la celda Apellidos
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
    def populate_table(self, data): #crea tabla
        #print(data)
        self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            # print(index_row)
            # print(row)
            # print(data)
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 

    def crear_pdf(self, data):
        ##########
        pdf=FPDF(orientation='L',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
        empresa=recipes.empresa
        nombre_emp=str(data[0])#data[0]
        ubicacion_emp=str(data[1])#data[1]
        #Arial bold 15
        pdf.set_font('Arial', '',18)
        #Titulo
        pdf.cell(w=0,h=10,txt=nombre_emp,border=0,ln=1,align='R',fill=0)
        pdf.set_font('Arial', '',8)
        pdf.cell(w=0,h=5,txt=ubicacion_emp,border=0,ln=1,align='R',fill=0)
        pdf.cell(w=0,h=5,txt=' '+"",border=0,ln=1,align='R',fill=0)
        #line breack
        pdf.ln(5)
         #formato de tabla
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="Reporte de pago de prestamos",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
         #formato de tabla
        pdf.ln(5)
        pdf.set_font('Arial', '', 8)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=17,h=10, txt="ID CLIENTE",border=1,align='C', fill=1)
        pdf.cell(w=25,h=10, txt="NOMBRE",border=1,align='C', fill=1)
        pdf.cell(w=25,h=10, txt="APELLIDOS",border=1,align='C', fill=1)
        pdf.cell(w=17,h=10, txt="ID AHORRO",border=1,align='C', fill=1)
        pdf.cell(w=15,h=10, txt="IMPORTE",border=1,align='C', fill=1)
        pdf.cell(w=15,h=10, txt="T.E.A.",border=1,align='C', fill=1)
        pdf.cell(w=15,h=10, txt="PLAZO",border=1,align='C', fill=1)
        pdf.cell(w=20,h=10, txt="CAPITAL",border=1,align='C', fill=1)
        pdf.cell(w=27,h=10, txt="FECHA APERTURA",border=1,align='C', fill=1)
        pdf.cell(w=27,h=10, txt="FECHA INICIO",border=1,align='C', fill=1)
        pdf.cell(w=38,h=10, txt="FECHA VENCIMIENTO",border=1,ln=1,align='C', fill=1)
        data1=[]
        data1=data
        for valor in data1:
            pdf.cell(w=17,h=8, txt=str(valor[0]),border=1,align='C', fill=0)
            pdf.cell(w=25,h=8, txt=str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=25,h=8, txt=str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=17,h=8, txt=str(valor[3]),border=1,align='C', fill=0)
            pdf.cell(w=15,h=8, txt=str(valor[4]),border=1,align='C', fill=0)
            pdf.cell(w=15,h=8, txt=str(valor[5]),border=1,align='C', fill=0)
            pdf.cell(w=15,h=8, txt=str(valor[6]),border=1,align='C', fill=0)
            pdf.cell(w=20,h=8, txt=str(valor[7]),border=1,align='C', fill=0)
            pdf.cell(w=27,h=8, txt=str(valor[8]),border=1,align='C', fill=0)
            pdf.cell(w=27,h=8, txt=str(valor[9]),border=1,align='C', fill=0)
            pdf.cell(w=38,h=8, txt=str(valor[10]),border=1,align='C', fill=0,ln=1)
        #pdf.output('C:/Users/jesus/OneDrive/Escritorio/proyectoPy/Reporte_Ahorros/Reporte_Ahorros.pdf', 'F')
        b=date.today()
        ejemp=str(valor[1])
        self.m=ejemp+"_"+str(b)
        pdf.output('Reporte_Ahorros/'+str(self.m)+'.pdf','f')
        #pdf.output('C:/Users/Almar/Documents/Proyecto/Reporte_Ahorros/'+str(m)+'.pdf')
    def abrir(self):
        wb.open_new(f"Reporte_Ahorros\{self.m}"+".pdf")#jacque

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
        self.Salir.clicked.connect(self.hide())
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