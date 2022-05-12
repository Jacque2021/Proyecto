from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.Ui_Diarios_polizas import Ui_diarios_polizas
from datetime import date
from controllers.error_prestamo import Error_p
import webbrowser as wb
from fpdf import FPDF
from database import recipes
from controllers.error_pdf import ErrorpdfForm

class DiarioForm(QWidget, Ui_diarios_polizas):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.config_table() #medidas de la tabla
        self.boton_buscar.clicked.connect(self.filtro_numero)
        self.numero_fin.returnPressed.connect(self.filtro_numero)
        self.boton_imprimir.clicked.connect(self.abrir)
        
    def filtro_numero(self):
        numero_1 = self.numero_ini.text()
        numero_2 = self.numero_fin.text()
        if numero_1 != "" and numero_2 != "":
            data=recipes.filtro_numero(numero_1,numero_2)
            if data:
                self.populate_table(data)
                self.pdf_diarios(data)
            else:
                self.window=ErrorpdfForm(self)
                self.window.show()
        else:
            print("DEBES LLENAR TODOS LOS CAMPOS") 
            self.window=Error_p(self)
            self.window.show()

    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("FECHA", "REFERENCIA", "TIPO", "CUENTA", "NÚMERO", "CONCEPTO", "CARGOS", "ABONOS")
        self.tabla_datos.setColumnCount(len(column_labels)) 
        self.tabla_datos.setHorizontalHeaderLabels(column_labels)
        self.tabla_datos.setColumnWidth(0, 70)
        self.tabla_datos.setColumnWidth(1, 100) 
        self.tabla_datos.setColumnWidth(3, 70)
        self.tabla_datos.setColumnWidth(4, 110) 
        self.tabla_datos.setColumnWidth(5, 180) 
        self.tabla_datos.setColumnWidth(6, 100)
        self.tabla_datos.setColumnWidth(7, 140) 
        self.tabla_datos.verticalHeader().setDefaultSectionSize(50) #tamaño de las filas 
        self.tabla_datos.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_datos.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
    
    def populate_table(self, data): #crea tabla
        self.tabla_datos.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_datos.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
    """*************************  MOVIMIENTO Y ACCION DE LOS BOTONES  *****************************"""   
    def set_title_bar_buttons_actions(self):
        self.maximizar.clicked.connect(self.close)
        self.minimizar.clicked.connect(self.showMinimized)
    
    def mousePressEvent(self, event): #ubicación mouse
        self.mouse_press_event2(event)
        
    def mouse_press_event2(self, event):
        self.drag_pos=event.globalPos()
        
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.move(self.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)

    def pdf_diarios(self, data):
        ##########
        pdf=FPDF(orientation='L',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
        #empresa=recipes.empresa
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
        pdf.cell(w=0,h=5, txt="Reporte de diarios y polizas",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
         #formato de tabla
        pdf.ln(5)
        pdf.set_font('Arial', '', 8)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=30,h=10, txt="FECHA",border=1,align='C', fill=1)
        pdf.cell(w=50,h=10, txt="REFERENCIA",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="TIPO",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="CUENTA",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="NÚMERO",border=1,align='C', fill=1)
        pdf.cell(w=50,h=10, txt="CONCEPTO",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="CARGOS",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="ABONOS",border=1,align='C', fill=1, ln=1)
        data1=[]
        data1=data
        for valor in data1:
            pdf.cell(w=30,h=8, txt=str(valor[0]),border=1,align='C', fill=0)
            pdf.cell(w=50,h=8, txt=str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[3]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[4]),border=1,align='C', fill=0)
            pdf.cell(w=50,h=8, txt=str(valor[5]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[6]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[7]),border=1,align='C', fill=0, ln=1)
        pdf.output('reporte_diarios/diarios.pdf', 'F')
    def abrir(self):
        b=date.today()
        wb.open_new(f"reporte_diarios\diarios.pdf")