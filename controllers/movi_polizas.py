from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.Ui_movi import Ui_Form
from views.general_custom_ui import GeneralCustomUi
from controllers.cuenta_a import CuentaForm
from PySide6.QtCore import Qt
#from controllers.catalogo_cuentas import CatalogoForm

from database import recipes


class mov_poli(QWidget, Ui_Form):
    def __init__(self, parent =None, RFC=None):
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self)
        self.RFC=RFC
        self.llamar_b()
        self.frame.mouseMoveEvent = self.move_window
        self.setWindowFlag(Qt.Window)
        self.set_title_bar_buttons_actions()
        self.remove_defult_title_bar()    
        #self.ui=GeneralCustomUi(self)
        self.boton_guardar.clicked.connect(self.guardar_info)
        #self.set_title_bar_buttons_actions()


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
    
    def guardar_info(self):
        movimiento=self.caja_rfc_7.text()
        RFC=self.caja_rfc_8.text()
        cuenta=self.caja_rfc_9.text()
        cargo=self.caja_rfc_10.text() 
        abono=self.caja_rfc_11.text() 
        referencia=self.caja_rfc_12.text() 
        concepto=self.caja_rfc_13.text()
        data=(movimiento,RFC,cuenta,cargo,abono,referencia,concepto)
        if recipes.crear_movimiento(data):
            print("Cuenta Agregada")
            self.clear_inputs()
            self.cuenta_agregada()
        else:
            print("Error al agregar cuenta")

    def clear_inputs(self):
        self.caja_rfc_7.clear()
        self.caja_rfc_8.clear()
        self.caja_rfc_9.clear()
        self.caja_rfc_10.clear()
        self.caja_rfc_11.clear()
        self.caja_rfc_12.clear()
        self.caja_rfc_13.clear()

    def cuenta_agregada(self):
        window=CuentaForm(self)
        window.show()

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