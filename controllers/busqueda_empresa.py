from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.Ui_consulta_empresa import Ui_consulta_empresa
from controllers.catalogo_cuentas import CatalogoForm
from database import recipes


class buscar_empresa(QWidget, Ui_consulta_empresa):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.config_table_1() #medidas de la tabla
        self.set_table_data_1()
        self.ingre_nombre.returnPressed.connect(self.search_1)  #returnPressed= al dar enter hace la accion
        self.ingre_nombre.textChanged.connect(self.restore_table_data_1)
        #self.on_selec_change()
        #self.tabla_clientes.setSelectionMode(QAbstractItemView.SingleSelection)   #no es necesario
        #self.tabla_empresa.cellClicked.connect(self.funcionalclickearceldas)
        #cellClicked=1    self.tableSusAmigos.doubleClicked.connect(self.doubleClicked_table) =doble clicked
        self.tabla_empresa.cellDoubleClicked.connect(self.funcional_dobleclicked)
        
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table_1(self, data): #crea tabla
        self.tabla_empresa.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_empresa.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
    def  config_table_1(self): #MEDIDAS DE LA TABLA
        column_labels=("RFC", "NOMBRE DE LA EMPRESA")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_empresa.setColumnCount(len(column_labels)) 
        self.tabla_empresa.setHorizontalHeaderLabels(column_labels)
        self.tabla_empresa.setColumnWidth(0, 30) #ancho de la tabla en la celda ID
        self.tabla_empresa.setColumnWidth(1, 145) #ancho de la celda Nombre
        self.tabla_empresa.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_empresa.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_empresa.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
    def set_table_data_1(self):
        data=recipes.select_tabal_clientes_1()  
        self.populate_table_1(data)  
    """*********************  METODO DE BUSQUEDA   ***************************"""  
    #Metodo de buscar
    def search_1(self):
        param = self.ingre_nombre.text()
        if param != "":
            data = recipes.select_by_parameter_1(param)
            self.populate_table_1(data)
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    def restore_table_data_1(self):
        param = self.ingre_nombre.text()
        if param == "":
            self.set_table_data_1()

    def funcional_dobleclicked(self, RFC_e):
        self.var = str(self.tabla_empresa.selectedIndexes()[0].data())
        cadena=str(self.tabla_empresa.selectedIndexes()[0].data())
        RFC_e=cadena
        window=CatalogoForm(self, RFC_e)
        self.hide()
        #self.close()
        window.show()

       
            
        #self.close()   
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

