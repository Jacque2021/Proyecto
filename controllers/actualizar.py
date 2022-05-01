from re import T
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from PySide6.QtCore import Qt
from views.Ui_actualizarye_cliente import Ui_act_eli_cliente
from controllers.actualizar_cliente import Actualizar_cForm
from database import recipes


class ActualizarForm(QWidget, Ui_act_eli_cliente):
    def __init__(self, parent=None, Id_cliente=None): #Capturar instancia en mainwindows    
        super().__init__(parent)
        self.parent=parent
        self.Id_cliente=Id_cliente
        self.setupUi(self) #1
        self.llamar_d()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.setWindowFlag(Qt.Window)
        self.boton_actualizar.clicked.connect(self.editar_cliente)
    
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    
    def llamar_d(self):
        data=recipes.select_cliente3(self.Id_cliente)
        Id=data[0]
        Id =str(Id)
        nom=data[1]
        nom =str(nom) 
        ape=data[2]
        ape =str(ape)
        tel=data[3]
        tel =str(tel)
        tel_add=data[4]
        tel_add =str(tel_add)
        dir=data[5]
        dir =str(dir)
        cor=data[6]
        cor =str(cor)
        nac=data[7]
        nac =str(nac)
        pun=data[8]
        pun =str(pun) 
        mun=data[9]
        mun =str(mun)
        self.codigo_cliente.setText(Id)
        self.nombre.setText(nom)
        self.apellidos.setText(ape)
        self.telefono.setText(tel)
        self.telefono_adicional.setText(tel_add)
        self.direccion.setText(dir)
        self.correo_elec.setText(cor) 
        self.fecha_de_nacimiento.setText(nac)
        self.puntuacion.setText(pun)
        self.municipio.setText(mun)

    def editar_cliente(self):
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
        
        if recipes.actualizar_cliente(self.Id_cliente, data):
            print("Cliente editado exitosamente")
            self.clear_inputs()
            self.cliente_actualizado()
    
    def clear_inputs(self):
        self.codigo_cliente.clear()
        self.nombre.clear() 
        self.apellidos.clear()
        self.telefono.clear()
        self.telefono_adicional.clear() 
        self.direccion.clear()
        self.correo_elec.clear() 
        self.fecha_de_nacimiento.clear() 
        self.puntuacion.clear() 
        self.municipio.clear()

    def cliente_actualizado(self):
        window=Actualizar_cForm(self)
        window.show()