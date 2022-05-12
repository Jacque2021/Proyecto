from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.Ui_historial_cliente_prestamo import Ui_historial_cliente_p
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from database import recipes
import webbrowser as wb
from fpdf import FPDF
from datetime import date
from controllers.error_pdf import ErrorpdfForm

class HistorialClientePForm(QWidget, Ui_historial_cliente_p):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.config_table() #medidas de la tabla 
        self.codigo_cliente.returnPressed.connect(self.busqueda_id)
        self.apellidos.returnPressed.connect(self.busqueda_apellidos)
        self.nombre.returnPressed.connect(self.busqueda_nombre)
        self.boton_b_ID.clicked.connect(self.busqueda_id)
        self.boton_b_nombre.clicked.connect(self.busqueda_nombre)
        self.boton_b_apellidos.clicked.connect(self.busqueda_apellidos)
        self.boton_imprimir.clicked.connect(self.pdf_historial)
        self.boton_imprimir.clicked.connect(self.abrir)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    def busqueda_id(self):
        Id_cliente = self.codigo_cliente.text()
        data=recipes.busqueda_id_p(Id_cliente)
        if data:
            self.populate_table(data)
            self.pdf_historial(data)
        else:
            self.window=ErrorpdfForm(self)
            self.window.show()

    def busqueda_nombre(self):
        nombre = self.nombre.text()
        data = recipes.busqueda_nombre_p(nombre)
        if data:
            self.populate_table(data)
            self.pdf_historial(data)
        else:
            self.window=ErrorpdfForm(self)
            self.window.show()

    def busqueda_apellidos(self):
        apellidos = self.apellidos.text()
        data=recipes.busqueda_apellidos_p(apellidos)
        if data:
            self.populate_table(data)
            self.pdf_historial(data)
        else:
            self.window=ErrorpdfForm(self)
            self.window.show()
    
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("ID", "NOMBRE", "APELLIDOS", "DEBITOS")
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 30) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 140) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(2, 140) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(5, 70) #creditos
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        #self.tabla_clientes.setColumnHidden(0, True)#selecciona una celda, lo pone en color azul
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion JACQUE

    def populate_table(self, data): #crea tabla
           
       # data=recipes.select_tabal_clientes()  #retorna datos de la tabla  #Lo elimino en video 4 y pego en otro metodo llamado set_table_tabla
        self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
        
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                #la celda que va contener la imagen, esta en la posicion 1
                self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def pdf_historial(self, data):
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
         #formato de tabla
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="Reporte del historial del cliente por préstamo",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
         #formato de tabla
        pdf.ln(5)
        pdf.set_font('Arial', '', 8)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=20,h=10, txt="ID",border=1,align='C', fill=1)
        pdf.cell(w=50,h=10, txt="NOMBRE",border=1,align='C', fill=1)
        pdf.cell(w=80,h=10, txt="APELLIDOS",border=1,align='C', fill=1)
        pdf.cell(w=40,h=10, txt="DEBITOS",border=1,align='C', fill=1, ln=1)
        data1=[]
        data1=data
        for valor in data:
            pdf.cell(w=20,h=8, txt=str(valor[0]),border=1,align='C', fill=0)
            pdf.cell(w=50,h=8, txt=str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=80,h=8, txt=str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=40,h=8, txt=str(valor[3]),border=1,align='C', fill=0, ln=1)
        b=date.today()
        pdf.output('reporte_historial/historial_prestamo'+str(b)+'.pdf', 'F')
    def abrir(self):
        b=date.today()
        wb.open_new(f"reporte_historial\historial_prestamo"+str(b)+".pdf") #jacque
