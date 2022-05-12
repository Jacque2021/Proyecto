from calendar import month
from ctypes.wintypes import FLOAT
from decimal import Decimal
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
import datetime
from cgitb import text
from PySide6.QtWidgets import QWidget
#from controllers.busqueda_re_ahorro import buscar_re_ahorro
from views.general_custom_ui import GeneralCustomUi
from views.ahorro_exitoso import ahorro_ex
from controllers.ahorroRealizado import AhorroRealizado
from controllers.error_prestamo import Error_p
from views.botonesMenu import Menu_Botones
from controllers.busqueda import buscar
from views.nuevo_ahorro import NuevoAhorro
import datetime
from datetime import date, time
import datetime, time
from database import recipes 


class NuevoAhorroForm(QWidget, NuevoAhorro):

    def __init__(self, parent=None, Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.Id_cliente=Id_cliente
        self.llamar_nombre()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_procesar.clicked.connect(self.nuevo_ahorro)
        self.vista()
        

        #self.cc()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    
    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.horan.setText(str(convertida1)) #lo pasa a la interfaz
        self.horan_2.setText(str(convertida1)) #lo pasa a la interfaz

    
    def llamar_nombre(self): 
        data=recipes.select_cliente2(self.Id_cliente)
        id=data[0]
        id = str(id)
        nombre=data[1]
        nombre = str(nombre)
        apellidos=data[2]
        apellidos = str(apellidos)
        self.id_c.setText(id)
        self.nombre_c.setText(nombre)
        self.apellidos_c.setText(apellidos)
       

    def nuevo_ahorro(self):
        id = self.id_c.text()
        nombre = self.nombre_c.text()
        apellidos = self.apellidos_c.text()
        tea = self.caja_tea.text()
        importe = self.caja_importe.text()
        fecha_ven = self.fecha_venc.text()
        fecha_ven = datetime.datetime.strptime(fecha_ven,'%d/%m/%Y')
        print(fecha_ven) 
        fecha_ap = self.horan.text()
        fecha_ini = self.horan_2.text() 
    
        importe = float(importe)
        tea = float(tea)
        teea = tea/100 
        plazo = 360
        interes = 0
        cancelacion = 0

        interes = importe * teea
        print("El interes es:",interes)
        cancelacion = importe + interes
        print("Si cancela el total es:",cancelacion)
    
        intt = str(interes)
        self.interes_c.setText(intt)
       
        cancc =str(cancelacion)
        self.cancelacion.setText(cancc)
        
        plazo = str(plazo)
        inttt = self.interes_c.text()
        canccc = self.cancelacion.text()
        ###
        importe = float(importe)
        impor = importe /360
        imp = impor * teea
        im = str(imp)
        self.interes1.setText(im)
        self.interes1_2.setText(im)
        self.interes1_3.setText(im)
        self.interes1_4.setText(im)
        self.interes1_5.setText(im)
        self.interes1_359.setText(im)
        self.interes1_360.setText(im)

        plazo = float(plazo)
        tot = imp * plazo
        tot = str(tot)
        self.interes1_total.setText(tot)
        plazo = str(plazo)
        teea = str(tea)
        
        importe = self.caja_importe.text()
        if recipes.llama_capital(self.Id_cliente):
            dato=recipes.llama_capital(self.Id_cliente)
            cap=dato[0]
            capital=Decimal(cap)+Decimal(cancelacion)
        else: capital=cancelacion
        data = (id, nombre, apellidos, importe, teea, plazo,  fecha_ven, fecha_ap, fecha_ini, inttt,
                cancelacion,capital)

        

        if len(id)==0 or len(nombre)==0 or len(apellidos)==0:
            self.Open3()

        elif recipes.crear_ahorro(data):
           print("Nuevo ahorro realizado")
           self.Open()
           self.clear_inputs()
    
    def Open(self):
        window=AhorroRealizado(self)
        window.show()
    
    def Open3(self):
        window=Error_p(self)
        window.show()
        
    def clear_inputs(self):
            self.id_c.clear()
            self.nombre_c.clear()
            self.apellidos_c.clear()
            self.caja_importe.clear()
            self.caja_tea.clear()
            self.fecha_venc.clear()
            self.horan.clear()
            self.horan_2.clear()
          