from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from views.Ui_consulta_c import Ui_consulta_c
from controllers.actualizar import ActualizarForm
from controllers.cliente_e import EliminarForm
from views import components2
from database import recipes


class edi_eli_cliente(QWidget, Ui_consulta_c):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.set_title_bar_buttons_actions()
        self.config_table_2() #medidas de la tabla
        self.set_table_data_2()
        self.ingre_nombre.returnPressed.connect(self.search_2)  #returnPressed= al dar enter hace la accion
        self.ingre_nombre.textChanged.connect(self.restore_table_data_2)
        

        """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table_2(self, data): #crea tabla
        self.tabla_cliente.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_cliente.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
            self.tabla_cliente.setCellWidget(
                index_row, 10, self.build_action_buttons()
            )
                
    def  config_table_2(self): #MEDIDAS DE LA TABLA
        column_labels=("ID", "NOMBRE", "APELLIDOS", "TELEFONO", "TELEFONO_ADD", "DIRECCION", "CORREO", "FECHA DE NACIMIENTO", "PUNTUACION", "MUNICIPIO", "")
        self.tabla_cliente.setColumnCount(len(column_labels)) 
        self.tabla_cliente.setHorizontalHeaderLabels(column_labels)
        self.tabla_cliente.setColumnWidth(0, 30) #ancho de la tabla en la celda ID
        self.tabla_cliente.setColumnWidth(1, 100) #ancho de la celda Nombre
        self.tabla_cliente.setColumnWidth(2, 140) #ancho de la celda Apellidos
        self.tabla_cliente.setColumnWidth(3, 70) #ancho telefono
        self.tabla_cliente.setColumnWidth(4, 110) #ancho telefono add
        self.tabla_cliente.setColumnWidth(5, 180) #ancho direccion
        self.tabla_cliente.setColumnWidth(6, 100) #ancho correo
        self.tabla_cliente.setColumnWidth(7, 140) #ancho fecha
        self.tabla_cliente.setColumnWidth(8, 100) #ancho puntuacion
        self.tabla_cliente.setColumnWidth(9, 100) #ancho municipio
        self.tabla_cliente.setColumnWidth(10, 120)
        self.tabla_cliente.verticalHeader().setDefaultSectionSize(50) #tamaño de las filas 
        self.tabla_cliente.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_cliente.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
        """self.tabla_cliente.setCellWidget(
                index_row, 4, self.build_action_buttons()
            )"""
    def set_table_data_2(self):
        data=recipes.buscar2c()  
        self.populate_table_2(data) 

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
    """*********************  METODO DE BUSQUEDA   ***************************"""  
    #Metodo de buscar  
    def search_2(self):
        param = self.ingre_nombre.text()
        if param != "":
            data = recipes.buscarc(param)
            self.populate_table_2(data)
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    def restore_table_data_2(self):
        param = self.ingre_nombre.text()
        if param == "":
            self.set_table_data_2()

    """*********************  AGREGAR BOTON DE BORRAR   ***************************"""  
    def build_action_buttons(self):

        edit_button= components2.Button_1("edit", "#74AA50")
        delete_button= components2.Button_1("delete", "#F9423A")
        
        buttons_layout=QHBoxLayout()
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)
       
        #Los layout deben estar dentro de un frame
        buttons_frame=QFrame()
        buttons_frame.setLayout(buttons_layout)
        
        edit_button.clicked.connect(self.editar_cliente)
        delete_button.clicked.connect(self.delete_cliente)
        
        return buttons_frame

    def editar_cliente(self):
        button = self.sender()
        table = self.tabla_cliente

        if button:
            Id_cliente = self.get_cliente_id_from_table(table, button)
            self.editar_c(Id_cliente)

    def editar_c(self, Id_cliente):
        self.window=ActualizarForm(self, Id_cliente)
        self.window.show()


    def delete_cliente(self):
        button = self.sender()
        table = self.tabla_cliente
        
        if button:
            cliente_id = self.get_cliente_id_from_table(table, button)
            if recipes.eli_cliente(cliente_id):
                self.set_table_data_2()
                self.eliminarc()

    def get_cliente_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        cliente_id = table.model().data(cell_id_index)
        return cliente_id

    def eliminarc(self):
        window=EliminarForm(self)
        window.show()