from asyncio.windows_events import NULL
from cgitb import text
import math
from string import punctuation
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_NuevoPrestamo import Ui_Nuevoprestamo
from controllers.prestamo_registrado import mensaje
from PySide6.QtCore import Qt
from decimal import Decimal
from database import recipes
import datetime
from datetime import date
from fpdf import FPDF

class Prestamos(QWidget, Ui_Nuevoprestamo):
    def __init__(self, parent=None,Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.Id_cliente=Id_cliente
        self.setupUi(self) #1
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.llamar_nombre()
        self.setWindowFlag(Qt.Window)
        self.Guardar.clicked.connect(self.insertar_prestamos)
        self.Borrar.clicked.connect(self.limpirar_parametros)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    def llamar_nombre(self): 
        data=recipes.select_cliente(self.Id_cliente)
        Id_cl=data[0]
        nombre=str(data[1])
        punctuation=data[2]
        if punctuation <18:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 25000 con un plazo máximo de 18 meses para pagar")
        elif punctuation >= 18 and punctuation <42:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 100,000 con un plazo máximo de 24 meses para pagar")
        elif  punctuation >= 42:
            self.cantidad_prestamo.setText("  El cliente "+nombre+ " tiene acceso a un prestamo máximo de 300,000 con un plazo máximo de 36 meses para pagar")
        self.nom_cliente.setText(nombre)

#********************** INSERTAR DATOS PARA EL PRESTAMO **********************#
    def insertar_prestamos(self,):
        data=recipes.select_cliente(self.Id_cliente)
        Id_cl=data[0]
        punctuation=data[2]
        nombre=data[1]
        prestamo=Decimal(self.Cantidad.text())
        cantidad_prestamo=prestamo  #total prestamo
        frecuencia=Decimal(self.Frecuencia.text()) #si es mensual, trimestral, semestral
        a=Decimal(frecuencia)
        tiempo=Decimal(self.Tiempo.text()) #tiempo en años
        periodo=a*tiempo  #periodo=frecuencia*tiempo    condicion
        x=Decimal(self.Interes.text())
        Iva=x/100   #sacar porcentaje de tasa anual
        Iva_div=Iva/frecuencia  #porcentaje mensual
        #saldo_insolito=prestamo-renta
        x=prestamo*Iva_div
        y=1-(math.pow((1+Iva_div),-periodo))
        z=x/Decimal(y)
        renta=z         #pagos mensuales
        interes=prestamo*Iva_div    
        amortizacion=renta-interes
        amortizacion_acum=0
        saldo_insolito=prestamo
        fecha_inicio=datetime.datetime.now()
        fecha=datetime.datetime.now()
        dia_delta=datetime.timedelta(days=30)
        fecha_siguiente=fecha+dia_delta
        un_mes=fecha_siguiente.strftime('%Y-%m-%d %H:%M:%S')
        nombre_codeudor=self.Codeudor.text()
        Garantia=self.Garantia.text()
        #condiciones para el prestamo
        if punctuation <18 and cantidad_prestamo>25000:
            self.TextoError.setText("No se puede realizar esa cantidad de prestamo")
        elif punctuation >= 18 and punctuation <42 and cantidad_prestamo>100000:
            self.TextoError.setText("No se puede realizar esa cantidad de prestamo")
        elif  punctuation >= 42 and cantidad_prestamo>300000:
            self.TextoError.setText("No se puede realizar esa cantidad de prestamo")
        elif periodo>18 and cantidad_prestamo<=25000:
            self.Plazo_max.setText("El usuario excede el plazo máximo para pagar")
        elif periodo>24 and cantidad_prestamo<=100000:
            self.Plazo_max.setText("El usuario excede el plazo máximo para pagar")
        elif periodo>36 and cantidad_prestamo<=300000:
            self.Plazo_max.setText("El usuario excede el plazo máximo para pagar")
        else:
            b=date.today()
            ejemp=str(nombre)
            m=ejemp+"_"+str(b)
            l="imagenes\{m}"+".pdf"
            link=f"prestamos\{m}"+".pdf"
            dato=(Id_cl,cantidad_prestamo,frecuencia,tiempo,periodo,Iva,Iva_div,saldo_insolito,renta,interes,
              amortizacion,amortizacion_acum,fecha_inicio,fecha_siguiente,nombre_codeudor,Garantia,link) 
        
            if recipes.insert_Prestamos(dato):
                print("Recipe Added")
                self.limpirar_parametros()
            self.Open_emergente()
        return Id_cl
#********************** LIMPIAR LA INTERFAZ **********************    
    def limpirar_parametros(self):
        self.nom_cliente.clear()
        self.nom_cliente.clear()
        self.Cantidad.clear()
        self.Frecuencia.clear()
        self.Interes.clear()
        self.Tiempo.clear()
        self.Codeudor.clear()
        self.Garantia.clear()
        self.TextoError.clear()
        self.cantidad_prestamo.clear()
        self.Plazo_max.clear()
    
    """ABRIR VENTANA EMERGENTE"""
    def Open_emergente(self):
        self.window=mensaje(self)
        self.window.show()