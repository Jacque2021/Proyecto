from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.Ui_mensaje_error import Ui_Form
class mensaje_error(QWidget, Ui_Form):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.rojo.mouseMoveEvent = self.move_window
        self.remove_defult_title_bar()
        self.mensaje.setAlignment(Qt.AlignCenter)
        self.mensaje.setText("No se puede realizar esa \ncantidad de prestamo")
        self.Ok.clicked.connect(self.close)
        
    """*****************   ATRIBUTOS DE LA VENTANA VISTA    ********************"""
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.mouse_press_event(event)   
    #ubicación global del mouse
    def mouse_press_event(self, event):
        self.drag_pos=event.globalPos()
    #drag_post = posicion de la ventana que esta siendo arrastrada
    
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.move(self.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()