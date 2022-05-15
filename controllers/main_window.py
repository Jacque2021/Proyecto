
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.Ui_InicioSesion import InicioSesion
from controllers.menu import Menu
from controllers.error import Error
from database import recipes
class MainWindowsForm(QWidget,InicioSesion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui=GeneralCustomUi(self) #manda llamar la clase GeneralCustomUi para el funcionamiento de botones de maximiza, minimizar y cerrar 
        self.iniciar_button.clicked.connect(self.logeo) #manda llamar la función "logeo" al momento de dar click al boton "iniciar_button"
        self.contrasena.returnPressed.connect(self.logeo) #manda llamar la función "logeo" al momento de dar enter al cuadro de contrasena
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)  
    def logeo(self): #función de inicio de sesión
        usuario=self.usuario.text() #almacena el texto que fue ingresado en front-end, recuadro usuario
        contrasena=self.contrasena.text() #almacena el texto que fue ingresado en front-end, recuadro contrasena
 
        if len(usuario)==0 or len(contrasena)==0:
            self.texto_error.setText("               Ingrese todos los datos") #Mensaje al no ingresar un dato
        elif usuario=="Admin" and contrasena=="123": #validación de usuario y contraseña
            self.open_menu()    #si los datos son correctos, abre la ventana de menu
            self.hide()   #OCULTA MENU
        else:                   #si los datos son incorrectos, abre la venta Error
            self.error()
            self.texto_error.setText("")
    def open_menu(self):
        window=Menu(self) #abrir la interfaz de Menu
        window.show()
                    
    def error(self):
        window=Error(self) #abrir interfaz de error
        window.show()