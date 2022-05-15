import datetime
from views.Ui_borrar_prestamo import Ui_consulta_cliente
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from database import recipes
from controllers.info_cliente import ActualizarForm
class Notificacion(QWidget, Ui_consulta_cliente):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.config_table() #medidas de la tabla
        self.set_table_data()
        self.ingre_nombre.returnPressed.connect(self.search)  #returnPressed= al dar enter hace la accion
        self.ingre_nombre.textChanged.connect(self.restore_table_data)
        self.tabla_clientes.cellDoubleClicked.connect(self.funcional_dobleclicked)
             
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table(self, data): #crea tabla
        self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

                
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("ID", "NOMBRE", "APELLIDOS", "PRESTAMO", "PAGO", "FECHA LIMITE DE PAGO")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 1) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 100) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(2, 200) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(3, 120) #ancho prestamo
        self.tabla_clientes.setColumnWidth(4, 120) #ancho pago 
        self.tabla_clientes.setColumnWidth(5, 70) #ancho fecha
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
    def set_table_data(self):
        hoy=datetime.date.today()
        dia_delta=datetime.timedelta(days=2)
        q=hoy+dia_delta
        data=recipes.tabla_notificacio(q)
        self.populate_table(data)  
    """*********************  BUSQUEDA DE PAGO PRESTAMO   ***************************"""
    #Metodo de buscar
    def search(self):
        param = self.ingre_nombre.text()
        if param != "":
            data = recipes.busqueda_notificacion(param)
            self.populate_table(data)
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    def restore_table_data(self):
        param = self.ingre_nombre.text()
        if param == "":
            self.set_table_data()
    """*************************  MOVIMIENTO Y ACCION DE LOS BOTONES  *****************************"""   
    def set_title_bar_buttons_actions(self):
        self.maximizar.clicked.connect(self.hide)
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

    def funcional_dobleclicked(self,Id_cliente):
        self.var = int(self.tabla_clientes.selectedIndexes()[0].data())
        numero=int(self.tabla_clientes.selectedIndexes()[0].data())
        Id_cliente=numero
        #p=recipes.condicion(Id_cliente)
        #mm=recipes.condicion2(Id_cliente)
        #if p:
        error=ActualizarForm(self,Id_cliente)
        error.show()
        
            
        #self.close() 