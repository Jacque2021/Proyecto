from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.Ui_borrar_prestamo import Ui_consulta_cliente
from database import recipes
class buscar(QWidget, Ui_consulta_cliente):
    def __init__(self, parent=None,Id_cliente=None):
        super().__init__(parent)
        self.Id_cliente=Id_cliente
        self.setupUi(self) #1
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.config_table() #medidas de la tabla
        self.set_table_data()
        self.ingre_nombre.setVisible(False)
        self.titulo_cliente.setVisible(False)
        #self.ingre_nombre.returnPressed.connect(self.search)  #returnPressed= al dar enter hace la accion
        #self.ingre_nombre.textChanged.connect(self.restore_table_data)
        
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table(self, data): #crea tabla
        self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("SALDO INSOLITO", "RENTA", "INTERES", "AMORTIZACIÓN", "MORATORIO", "FECHA LIMITE", "FECHA DE PAGO")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 100) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(1, 100) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(3, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(4, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(5, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(6, 100) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(7, 100) #ancho de la celda Apellidos
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla_clientes.setTextElideMode(Qt.ElideRight)# Qt.ElideNone

        # Establecer el ajuste de palabras del texto 
        self.tabla_clientes.setWordWrap(False)
        
    def set_table_data(self):
        data=recipes.select_info_cliente_prestamo2(self.Id_cliente)  
        self.populate_table(data)  
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