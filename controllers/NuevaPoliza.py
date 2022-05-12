from multiprocessing import parent_process
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_NuevaPoliza import Polizas
#from controllers.movi_polizas import mov_poli
from controllers.busqueda_poliza import buscar_empresa_poli
from controllers.cuenta_a import CuentaForm
from database import recipes

class nuevaPoliza(QWidget, Polizas):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.setWindowFlag(Qt.Window)
        self.config_table()
        self.boton_nuevo.clicked.connect(self.open_moviPoliz)
        self.boton_guardar.clicked.connect(self.llenar_poliza)
        self.set_table_data()
        self.ui.opciones_c()
        self.ui.tipo_De_poliza()

    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)

    def llenar_poliza(self):
        cuenta=self.codigo_SAT.currentText()
        fecha=self.fecha.text()
        tipo=self.tipo_poliza.currentText()
        numero=self.numero.text()
        concepto=self.concepto.text()
        data=(cuenta,fecha,tipo,numero,concepto)
        if recipes.llena_poliza(data):
            print("Cuenta Agregada")
            self.clear_inputs()
            self.cuenta_agregada()
        else:
            print("Error al agregar cuenta")

    def clear_inputs(self):
        self.fecha.clear()
        self.numero.clear()
        self.concepto.clear()

    def cuenta_agregada(self):
        window=CuentaForm(self)
        window.show()

    def config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("MOVIMIENTO", "CUENTA", "RFC", "CARGO", "ABONO", "REFERENCIA")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tableWidget.setColumnCount(len(column_labels)) 
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(0, 120) #ancho de la tabla en la celda ID
        self.tableWidget.setColumnWidth(1, 230) #ancho de la celda Nombre
        self.tableWidget.setColumnWidth(2, 120) #ancho de la celda Apellidos
        self.tableWidget.setColumnWidth(3, 120) #ancho de la celda Apellidos
        self.tableWidget.setColumnWidth(4, 120) #ancho de la celda Apellidos
        self.tableWidget.setColumnWidth(5, 120) #ancho de la celda Apellidos
        self.tableWidget.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
    def populate_table(self, data): #crea tabla
        #print(data)
        self.tableWidget.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            # print(index_row)
            # print(row)
            # print(data)
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 
    
    def set_table_data(self):
        data=recipes.select_busca_poliza()  
        self.populate_table(data)

    def open_moviPoliz(self):
        self.window = buscar_empresa_poli(self)
        self.window.show()

