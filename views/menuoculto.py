from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect   #sombra de interfaz
#ESTE SOLO FUNCIONA PARA EL ASPECTO DE VENTANA Y USO DE BOTONES DE MAXIMIZAR, MINIMIZAR Y CERRAR
#ui tiene el objeto de todas las caracteristicas de la clase
#from vistas.Ui_add_edit_windows import AddEditWindows

#para el metodo fill_category_cb
class Menu():
    def __init__(self, ui):
        self.ui=ui #contiene el objeto de las ventanas
        self.ui.content_frame.mouseMoveEvent = self.move_window #top_bar_frame= la barra principal azul
        self.set_window_shadow()
        self.buttons_actions() #boton de maximizar y minimizar
        
    #ubicación global del mouse
    def mouse_press_event(self, event):
        self.drag_pos=event.globalPos()
    #drag_post = posicion de la ventana que esta siendo arrastrada
    
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.ui.move(self.ui.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()
        
    #Programar botones de la barra azul
    def ocultar_botones_prestamo(self):
        self.ui.prestamo_2.setVisible(False)
        self.ui.pago.setVisible(False)
        self.ui.cancelar.setVisible(False)
    def ocultar_botones_consulta(self):
        self.ui.consulta.setVisible(False)
        self.ui.PLD.setVisible(False)
    
        #configuración de botones de barra principal
    def visibles_opciones_prestamo(self):
        self.ui.prestamo_2.setVisible(True)
        self.ui.pago.setVisible(True)
        self.ui.cancelar.setVisible(True)
    def vicible_opciones_consulta(self):
        self.ui.consulta.setVisible(True)
        self.ui.PLD.setVisible(True)
    def buttons_actions(self):
        self.ocultar_botones_prestamo()
        self.ocultar_botones_consulta()
        self.ui.prestamo.clicked.connect(self.ui.visibles_opciones_prestamo)
        self.ui.consultas.clicked.connect(self.ui.vicible_opciones_consulta)
    
    #objeto de la ventana de agregar, category_data fue creada arriba
    """ def fill_category_cb(self):
        self.ui.category_combo_box.addItems(category_data)"""