from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from controllers.diarios_polizas import DiarioForm
from views.Ui_listado_polizas import Ui_listado_polizas
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from controllers.error_poliza import ErrorPolizaForm
from database import recipes
import webbrowser as wb
from fpdf import FPDF
from datetime import date

class ListadoPolizasForm(QWidget, Ui_listado_polizas):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.config_table() #medidas de la tabla 
        self.boton_b_nombre.clicked.connect(self.busqueda_rfc)
        self.RFC_e.returnPressed.connect(self.busqueda_rfc)
        self.boton_diarios_y_polizas.clicked.connect(self.Open_diarios_p)

    def busqueda_rfc(self):
        numero = self.RFC_e.text()
        data=recipes.busqueda_rfc(numero)
        if data:
            self.populate_table(data)
        else:
            self.window=ErrorPolizaForm(self)
            self.window.show

    def Open_diarios_p(self):
        self.window=DiarioForm(self)
        self.window.show()
    
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("NUMERO", "FECHA", "CONCEPTO", "CARGO", "ABONO")
        self.tabla_listado_polizas.setColumnCount(len(column_labels)) 
        self.tabla_listado_polizas.setHorizontalHeaderLabels(column_labels)
        self.tabla_listado_polizas.setColumnWidth(0, 90) #ancho de la tabla en la celda ID
        self.tabla_listado_polizas.setColumnWidth(1, 140) #ancho de la celda Nombre
        self.tabla_listado_polizas.setColumnWidth(2, 140) #ancho de la celda Apellidos
        self.tabla_listado_polizas.setColumnWidth(3, 100) #ancho fecha a
        self.tabla_listado_polizas.setColumnWidth(4, 100) #ancho fecha c
        self.tabla_listado_polizas.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        #self.tabla_listado_polizas.setColumnHidden(0, True)#selecciona una celda, lo pone en color azul
        self.tabla_listado_polizas.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_listado_polizas.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion jacque

    def populate_table(self, data): #crea tabla
           
       # data=recipes.select_tabal_clientes()  #retorna datos de la tabla  #Lo elimino en video 4 y pego en otro metodo llamado set_table_tabla
        self.tabla_listado_polizas.setRowCount(len(data)) #cantidad de filas que va tener
        
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                #la celda que va contener la imagen, esta en la posicion 1
                self.tabla_listado_polizas.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
    
    #jacque
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)