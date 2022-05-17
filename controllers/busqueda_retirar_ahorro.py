from ast import Param
from typing import TextIO
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from controllers.retirar_ahorro import RetirarAhorroForm
from views.consulta_re_ahorro_tabla import consulta_re_ahorro
#from controllers.cheques import ChequesForm
from views.cheques import Cheques
from views.retirar_ahorro import RetirarAhorro
from views.general_custom_ui import GeneralCustomUi
from database import recipes

class buscar_retirar_ahorro(QWidget, consulta_re_ahorro):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.contenido_frame.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.config_table() #medidas de la tabla
        self.set_table_data()
        #self.ui = GeneralCustomUi(self)
        self.ingre_nombre.returnPressed.connect(self.search)  #returnPressed= al dar enter hace la accion
        self.ingre_nombre.textChanged.connect(self.restore_table_data)
        self.tabla_cheques.cellDoubleClicked.connect(self.funcional_dobleclicked)
        self.tabla_cheques.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion jacque
    
    """*********************  DISEÑAR LA TABLA CONSULTA CLIENTES DE RETIRO  ***************************"""  
    def populate_table(self, data): #crea tabla
            
       # data=recipes.select_tabal_clientes()  #retorna datos de la tabla  #Lo elimino en video 4 y pego en otro metodo llamado set_table_tabla
        self.tabla_cheques.setRowCount(len(data)) #cantidad de filas que va tener
        
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                #la celda que va contener la imagen, esta en la posicion 1
                self.tabla_cheques.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("ID", "NOMBRE", "APELLIDOS")
        self.tabla_cheques.setColumnCount(len(column_labels)) 
        self.tabla_cheques.setHorizontalHeaderLabels(column_labels)
        self.tabla_cheques.setColumnWidth(0, 30) #ancho de la tabla
        self.tabla_cheques.setColumnWidth(1, 80) #
        self.tabla_cheques.setColumnWidth(4, 150) #
        self.tabla_cheques.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        #self.tabla_clientes.setColumnHidden(0, True)#selecciona una celda, lo pone en color azul
        self.tabla_cheques.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        
        """self.tabla_clientes.setCellWidget(
                index_row, 4, self.build_action_buttons()
            )"""
    def set_table_data(self):
        data=recipes.select_tabal_re_ahorro()  
        self.populate_table(data) 



    """*********************  METODO DE BUSQUEDA   ***************************"""  
    #Metodo de buscar  
    def search(self):
        param = self.ingre_nombre.text()
        if param != "":
            data = recipes.select_by_parameter(param)
            self.populate_table(data)
  
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    def restore_table_data(self):
        param = self.ingre_nombre.text()
        if param == "":
            self.set_table_data()
            #param = self.id
    

    def funcional_dobleclicked(self,Id_cliente):
        self.var = int(self.tabla_cheques.selectedIndexes()[0].data())
        numero=int(self.tabla_cheques.selectedIndexes()[0].data())
        Id_cliente=numero
        window=RetirarAhorroForm(self,Id_cliente)
        self.hide()
        #self.close()
        window.show()

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
    """*************************   FIN DE MOVIMIENTO Y ACCION DE LOS BOTONES   *****************************"""
    