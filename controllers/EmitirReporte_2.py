from multiprocessing import parent_process
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from controllers.error_prestamo import Error_p
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_EmitirReporte_2 import Emi_report_2
from datetime import datetime
from datetime import date
from database import recipes
from fpdf import FPDF
import webbrowser as wb



class emite_R_2 (QWidget, Emi_report_2):
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
            data=recipes.filtro_pago_fecha_ID(fecha_1,fecha_2,codigo_cliente1,codigo_cliente2)
            self.populate_table(data)
            self.crear_pdf(data)
            print(data)
        
        elif fecha_1 != "" and fecha_2 != "" and codigo_cliente1 == "" and codigo_cliente2 == "":
            print("SEGUNDO METODO")
            data=recipes.filtro_pago(fecha_1,fecha_2)
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
        column_labels=("ID \nPAGO","ID \nPRESTAMO", "ID \nCLIENTES", "SALDO \nINSOLITO",
        "INTERES","AMORTIZACION","AMORTIZACION \n ACOMULADA","FECHA \nLIMITE","FECHA \n DE PAGO","FECHA \n SIGUIENTE"
        ,"MORATORIO")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 70) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 70) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(2, 70) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(3, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(4, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(5, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(6, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(7, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(8, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(9, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(10, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(11, 100) #ancho de la celda Apellidos
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
        #empresa=recipes.empresa
        #nombre_emp=str(data[0])
        #ubicacion_emp=str(data[1])
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
         #formato de tabla
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="Reporte de pago de prestamos",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
        #pdf.ln(5)
        pdf.set_font('Arial', '', 8)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=15,h=10, txt="ID PAGO",border=1,align='C', fill=1)
        pdf.cell(w=22,h=10, txt="ID PRESTAMO",border=1,align='C', fill=1)
        pdf.cell(w=20,h=10, txt="ID CLIENTES",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="SALDO INSOLITO",border=1,align='C', fill=1)
        pdf.cell(w=20,h=10, txt="INTERES",border=1,align='C', fill=1)
        pdf.cell(w=28,h=10, txt="AMORTIZACIÓN",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="AMORT. ACOM.",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="FECHA LIMITE",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="FECHA DE PAGO",border=1,align='C', fill=1)
        pdf.cell(w=32,h=10, txt="FECHA SIGUIENTE",border=1,align='C', fill=1)
        pdf.cell(w=0,h=10, txt="MORATORIO",border=1,align='C', fill=1,ln=1)
        #pdf.cell(w=20,h=10, txt="AHORRO",border=1,ln=1,align='C', fill=1)
        data1=[]
        data1=data
        for valor in data1:
            pdf.cell(w=15,h=8, txt=str(valor[0]),border=1,align='C', fill=0)
            pdf.cell(w=22,h=8, txt=str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=20,h=8, txt=str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[3]),border=1,align='C', fill=0)
            pdf.cell(w=20,h=8, txt=str(valor[4]),border=1,align='C', fill=0)
            pdf.cell(w=28,h=8, txt=str(valor[5]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[6]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[7]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[8]),border=1,align='C', fill=0)
            pdf.cell(w=32,h=8, txt=str(valor[9]),border=1,align='C', fill=0)
            pdf.cell(w=0,h=8, txt=str(valor[10]),border=1,align='C', fill=0,ln=1)
        b=date.today()
        ejemp=str(valor[1])
        self.m=ejemp+"_"+str(b)
        pdf.output('Reporte_Prestamos/'+str(self.m)+'.pdf','f')
    def abrir(self):
        wb.open_new(f"Reporte_Prestamos\{self.m}"+".pdf")#jacque

