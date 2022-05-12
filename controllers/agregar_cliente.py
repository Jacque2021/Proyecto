from turtle import clear
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from PySide6.QtCore import Qt
from views.Ui_agregar_cliente import Ui_Agregar_cliente
from controllers.editar_eliminar_cliente import edi_eli_cliente
from controllers.mensaje_error4 import mensaje_error4
from controllers.cliente_a import ClienteForm
from controllers.errorcliente import ErrorForm
from database import recipes


class AgregarClienteForm(QWidget, Ui_Agregar_cliente):
    def __init__(self, parent=None): #Capturar instancia en mainwindows    
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_guardar.clicked.connect(self.nuevo_cliente)
        self.municipio.returnPressed.connect(self.nuevo_cliente)
        self.cc()

    def cc(self):
        self.boton_buscar.clicked.connect(self.buscar_cli)

    def buscar_cli(self):
        self.window=edi_eli_cliente(self)
        self.mensaje.clear()
        self.window.show()
    
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)

    def nuevo_cliente(self):
        nombre = self.nombre.text() 
        apellidos = self.apellidos.text()
        telefono = self.telefono.text()
        telefono_add = self.telefono_adicional.text() 
        direccion = self.direccion.text()
        correo = self.correo_elec.text() 
        fecha_nacimiento = self.fecha_de_nacimiento.text() 
        puntuacion = self.puntuacion.text() 
        municipio = self.municipio.text()

        data = (nombre, apellidos, telefono, telefono_add, direccion, correo, fecha_nacimiento, puntuacion, municipio)
        
        if recipes.insertar_clientes(data):
            print("Cliente agregado")
            self.clear_inputs()
            self.cliente_agregado()
        else:
            if self.nombre.text()=="" or self.apellidos.text()=="" or self.telefono.text()=="" or self.telefono_adicional.text()=="" or self.direccion.text()=="" or self.correo_elec.text()=="" or self.fecha_de_nacimiento.text()=="" or self.puntuacion.text() =="" or self.municipio.text()=="":
                self.window=mensaje_error4(self)
                self.window.show()
            else:
                self.cliente_error()
                print("Error en el cliente")

    def clear_inputs(self):
        self.nombre.clear()
        self.apellidos.clear()
        self.telefono.clear()
        self.telefono_adicional.clear() 
        self.direccion.clear()
        self.correo_elec.clear() 
        self.fecha_de_nacimiento.clear() 
        self.puntuacion.clear() 
        self.municipio.clear()
        self.mensaje.clear()

    def cliente_agregado(self):
        window=ClienteForm(self)
        window.show()

    def cliente_error(self):
        window=ErrorForm(self)
        self.mensaje.clear()
        window.show()