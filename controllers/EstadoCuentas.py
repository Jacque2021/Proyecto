from cgitb import text
from string import punctuation
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.EstCuentas import EstCuentas
from controllers.info_prestamo import buscar
#from controllers.ConsultaEstadoCuentas import buscarCuenta
from PySide6.QtCore import Qt
from database import recipes

class estadoCuentas (QWidget, EstCuentas):
    def __init__(self, parent=None,Id_cliente=None):
        super().__init__(parent)
        self.Id_cliente=Id_cliente
        self.setupUi(self) #1
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.setWindowFlag(Qt.Window)
        self.config_table()
        self.set_nombre_cliente()
        #cellClicked=1    self.tableSusAmigos.doubleClicked.connect(self.doubleClicked_table) =doble clicked
        self.tabla_clientes.cellDoubleClicked.connect(self.funcional_dobleclicked)

    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)

        

    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table(self, data): #crea tabla
         self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
         for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
             #enumerate(data) retorna el indice y los datos
             for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                 self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
    def config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("ID","NOMBRE","APELLIDOS","FECHA_INICIO","FECHA_SIGUIENTE","PRÉSTAMO","TIEMPO")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 10) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 130) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(2, 120) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(2, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(3, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(4, 130) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(5, 100) #ancho de la celda Apellidos
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        

    """*********************  METODO DE OBTENER LAS CUENTAS DEL CLIENTE   ***************************"""  
    #Metodo de buscar
    def set_nombre_cliente(self):
        data=recipes.select_cliente_ESTADO_CUENTA(self.Id_cliente)
        Id_cl=data[0]
        param = Id_cl
        if param != "":
            data = recipes.select_by_cuenta(param)
            print(data)
            self.populate_table(data)
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    # def restore_table_data(self):
    #     param = self.ingre_nombre.text()
    #     if param == "":
    #         self.set_table_data()
    def funcional_dobleclicked(self,Id_cliente):
        self.var = int(self.tabla_clientes.selectedIndexes()[0].data())
        numero=int(self.tabla_clientes.selectedIndexes()[0].data())
        Id_cliente=numero
        error=buscar(self, Id_cliente)
        error.show()