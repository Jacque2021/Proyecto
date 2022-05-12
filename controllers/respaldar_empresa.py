from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.empresaRespaldada import respaldo
from controllers.respaldoRealizado import RespaldoRealizado
from views.repaldar_empresa import RespaldarEmpresa
from views.Ui_resp import resp
from PySide6.QtCore import Qt
from controllers.error_prestamo import Error_p
from datetime import date, time
import datetime, time
from database import recipes


class RespaldarEmpresaForm(QWidget, resp):

    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_guardar.clicked.connect(self.resp_empresa)
        self.vista()
        
        
    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.fechar.setText(str(convertida1)) #lo pasa a la interfaz
        hora = time.strftime('%H:%M:%S')
        self.horar.setText(str(hora)) #lo pasa a la interfaz

    
    def resp_empresa(self):
        rfc = self.caja_RFC.text()
        nombre = self.caja_empresa.text()
        fecha = self.fechar.text()
        hora_r = self.horar.text()
        ruta = self.caja_ruta.text()
        nombre_res = self.caja_respaldo.text()

        data = (rfc, nombre, fecha, hora_r, ruta, nombre_res)

        if len(rfc)==0 or len(nombre)==0 or len(fecha)==0 or len(hora_r)==0 or len(ruta)==0 or len(nombre_res)==0:
            self.Open3()

        elif recipes.respladar_empresa(data):
           print("Empresa respaldada")
           self.Open()
           self.clear_inputs()
    
    def Open(self):
        window=RespaldoRealizado(self)
        window.show()
    
    def Open3(self):
        window=Error_p(self)
        window.show()

    def clear_inputs(self):
        self.caja_RFC.clear()
        self.caja_empresa.clear()
        self.fechar.clear()
        self.horar.clear()
        self.caja_ruta.clear()
        self.caja_respaldo.clear()
   