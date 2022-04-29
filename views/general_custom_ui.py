from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect   #sombra de interfaz
#ESTE SOLO FUNCIONA PARA EL ASPECTO DE VENTANA Y USO DE BOTONES DE MAXIMIZAR, MINIMIZAR Y CERRAR
#ui tiene el objeto de todas las caracteristicas de la clase
#from vistas.Ui_add_edit_windows import AddEditWindows

#para el metodo fill_category_cb
category_data=(
    "Recetas Italianas",
    "Postres",
    "Bebidas"
)

class GeneralCustomUi():
    def __init__(self, ui):
        self.ui=ui #contiene el objeto de las ventanas
        self.remove_defult_title_bar()
        self.miximize_window()
        self.ui.top_bar_frame.mouseMoveEvent = self.move_window #top_bar_frame= la barra principal azul
        self.set_window_shadow()
        self.set_title_bar_buttons_actions() #boton de maximizar y minimizar
        
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        
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
            
    #efecto de ventana
    def set_window_shadow(self):
        shadow=QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)
        
 #Programar botones de la barra azul
        #maximizar ventana
    def miximize_window(self):
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False) #oculta boton maximizar
        self.ui.shadow_layout.setContentsMargins(0, 0, 0, 0) #elimina margenes 
        #minimiza ventana
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True) 
        self.ui.shadow_layout.setContentsMargins(10, 10, 10, 10)
        #une ambos metodos
        #configuración de botones de barra principal
    def set_title_bar_buttons_actions(self):
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)
        self.ui.maximize_button.clicked.connect(self.miximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)
        
    #objeto de la ventana de agregar, category_data fue creada arriba
    """ def fill_category_cb(self):
        self.ui.category_combo_box.addItems(category_data)"""
        
    
    