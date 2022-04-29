from distutils.command.config import config
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.mi_empresa import Miempresa
from controllers.errorempresa import ErrorForm
from controllers.EmpresaAgregada import EmpresaAgregada
from controllers.error_prestamo import Error_p
from mysql import connector
from datetime import date
from mysql import connector
import datetime
from database import recipes

from mysql import connector

class MiEmpresaForm(QWidget, Miempresa):

    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_guardar.clicked.connect(self.nueva_empresa)
        self.vista()
        
        
    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.fechar.setText(str(convertida1)) #lo pasa a la interfaz

    def nueva_empresa(self): 
        RFC = self.caja_rfc.text()
        nombre = self.caja_empresa.text()
        ubicacion = self.caja_ubicacion_bd.text()
        inicio = self.fechar.text()
        fin = self.fecha_fin.text()
        tipo_periodo = self.caja_periodo.text()
        usu = self.caja_usuario.text()
        u = 'root'
        #print(usu)
        c ='12345678'
        contra = self.caja_contrasena.text()
        #print(contra)
        hos = self.caja_host.text()
        h = 'localhost'
        #print(hos)
        bd = self.caja_base.text()
        b = 'aqui'
        #print(bd)


        data = (RFC, nombre, ubicacion, inicio, fin, tipo_periodo, usu,contra, hos, bd )
##########################        CONEXION    ############################
        config = {
            'user': usu,
            'password': contra,
            'host': hos,
            'database': bd
            }
       # conn = None
        try:
            conn = connector.connect(**config)
            print("Conexión con base de datos ¡CORRECTAMENTE!")
        
        
        except connector.Error as err:
            print(f"Error at create_connection function: {err.msg}" )
             
 #########################################################################    
        if len(RFC)==0 or len(nombre)==0 or len(ubicacion)==0 or len(inicio)==0 or len(fin)==0 or len(tipo_periodo)==0 or len(usu)==0 or len(contra)==0 or len(hos)==0 or len(bd)==0:
            self.Open3()

        elif u!= usu or  c != contra or h != hos or b!=bd :
            self.Open2() 

        elif recipes.insertar_empresa(data):
           print("Empresa agregada")
           self.Open()
           self.clear_inputs()
    
#############################
   # def con(config):
    #    print("Conexión establecida correctamnete")
     #   conn = None
     #   try:
      #      conn = connector.connect(**config)
       #     print("Conexión establecida correctamnete")
       # except connector.Error as err:
        #    print(f"Error at create_connection function: {err.msg}" )
        #return conn 
#################################
    def Open(self):
        window=EmpresaAgregada(self)
        window.show()
    
    def Open2(self):
        window=ErrorForm(self)
        window.show()
    
    def Open3(self):
        window=Error_p(self)
        window.show()

    def clear_inputs(self):
        self.caja_rfc.clear()
        self.caja_empresa.clear()
        self.caja_ubicacion_bd.clear()
        self.fechar.clear()
        self.fecha_fin.clear()
        self.caja_periodo.clear()
        self.caja_usuario.clear()
        self.caja_contrasena.clear()
        self.caja_host.clear()
        self.caja_base.clear()
       

   