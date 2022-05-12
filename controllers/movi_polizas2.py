from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from views.Ui_movi_polizas2 import Mov_polizas_2
from views.general_custom_ui import GeneralCustomUi
#from controllers.catalogo_cuentas import CatalogoForm
from database import recipes


class mov_poli2(QWidget, Mov_polizas_2):
    def __init__(self, parent =None, RFC=None):
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self)
        self.RFC=RFC
        self.llamar_b()
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.remove_defult_title_bar() 


    def llamar_b(self):
        data = recipes.select_empresa2(self.RFC)
        RFC=data[0] 
        RFC = str(RFC)
        nombre_b=data[1]
        nombre_b=str(nombre_b)
        codigo_SAT=data[2]
        codigo_SAT=str(codigo_SAT)
        self.caja_rfc_8.setText(RFC)
        self.caja_rfc_9.setText(codigo_SAT)

    """"*************************  MOVIMIENTO Y ACCION DE LOS BOTONES  *****************************"""   
    def set_title_bar_buttons_actions(self):
        self.maximizar.clicked.connect(self.close)
        self.minimizar.clicked.connect(self.showMinimized)
    
    def mousePressEvent(self, event): #ubicación mouse
        self.mouse_press_event2(event)
        
    def mouse_press_event2(self, event):
        self.drag_pos=event.globalPos()
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)
        
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.move(self.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()