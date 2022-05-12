from decimal import Decimal
from distutils.log import error
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.retirar_ahorro import RetirarAhorro
from views.retiro_exitoso import retiro_ex
from controllers.retiroRealizado import RetiroE
from controllers.error_prestamo import Error_p
from controllers.erroretiro1 import Error1
from controllers.erroretiro2 import Error2
from fpdf import FPDF
import datetime 
from datetime import date
import datetime
from datetime import date, time
import datetime, time
from fpdf import FPDF
import webbrowser as wb
from database import recipes


class RetirarAhorroForm(QWidget, RetirarAhorro):

    def __init__(self, parent=None, Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.Id_cliente=Id_cliente
        self.llamar_nombre()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_retirar_2.clicked.connect(self.retiro)
        self.vista()
        #self.cc()
         
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.fechar.setText(str(convertida1)) #lo pasa a la interfaz
        hora = time.strftime('%H:%M:%S')
        self.horar.setText(str(hora)) #lo pasa a la interfaz
        if recipes.llamar_capital(self.Id_cliente):
            ahorro=recipes.llamar_capital(self.Id_cliente)
            cap=Decimal(ahorro[0])
            self.caja_capital.setText('$'+str(cap))
        else: 
            self.caja_capital.setText("Su cuenta es de 0.0 pesos")
    def llamar_nombre(self): 
        data=recipes.select_cliente2(self.Id_cliente)
        id=data[0]
        id = str(id)
        nombre=data[1]
        apellidos=data[2]
        apellidos = str(apellidos)
        self.id_c.setText(id)
        self.nombre_c.setText(nombre)
        self.apellidos_c.setText(apellidos)
       

    def retiro(self):
        ahorro=recipes.llamar_capital(self.Id_cliente)
        capi=Decimal(ahorro[0])
        impo=Decimal(ahorro[2])
        id = self.id_c.text()
        nombre = self.nombre_c.text()
        apellidos = self.apellidos_c.text()
        capital2 =capi
        total = self.caja_total_retiro.text()
        descripcion = self.caja_descrpcion.text()
        fecha = self.fechar.text()
        hora = self.horar.text()
        a = Decimal(total)
        b = capital2
        cap = b -a
        pago_con_capital=(cap,impo)
        if recipes.pagar_con_ahorro(self.Id_cliente, pago_con_capital):
                print("Descuento de ahorro hecho")
        data = (id, nombre, apellidos,capi, total, cap, descripcion, fecha, hora)
        
        ### CREAR DOC PDF CHEQUE
        #self.cell('logobueno.png', 10, 8 , 25) 

        ### CREAR DOC PDF CHEQUE
         ##########
        pdf=FPDF(orientation='P',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
        #empresa=recipes.empresa      JACQUE
        empresa=recipes.empresa()
        nombre_empresa=str(empresa[0])
        direccion2=str(empresa[1])
        ##################################
        nombre_emp=nombre_empresa
        ubicacion_emp=direccion2
        #Arial bold 15
        pdf.set_font('Arial', '',18)
        #Titulo
        pdf.cell(w=0,h=10,txt=nombre_emp,border=0,ln=1,align='R',fill=0)
        pdf.set_font('Arial', '',8)
        pdf.cell(w=0,h=5,txt=ubicacion_emp,border=0,ln=1,align='R',fill=0)
        pdf.cell(w=0,h=5,txt=' '+"",border=0,ln=1,align='R',fill=0)
        #line breack
        pdf.ln(5)
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="RETIRO",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="",border=0,ln=1,align='C', fill=0)
        pdf.set_font('Arial', '', 12)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.cell(w=0,h=5, txt="Información del cliente",border=1,ln=1,align='C', fill=1)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.cell(w=25,h=4, txt="No° cliente",border=1,align='C', fill=1)
        pdf.cell(w=70,h=4, txt="Nombre del cliente",border=1,align='C', fill=1,ln=0)
        pdf.cell(w=0,h=4, txt="Apellidos del cliente",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=25,h=4, txt=str(id),border=1,align='C', fill=0)
        pdf.cell(w=70,h=4, txt=nombre,border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=apellidos,border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="",border=0,align='C', fill=0,ln=1)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.cell(w=0,h=5, txt="Información general del retiro",border=1,ln=1,align='C', fill=1)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.cell(w=45,h=4, txt="Cliente",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Capital",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Monto",border=1,align='C', fill=1)
        pdf.cell(w=45,h=4, txt="Descripción",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Fecha de retiro",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=45,h=4, txt=str(id),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(cap),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt='$'+str(total),border=1,align='C', fill=0)
        pdf.cell(w=45,h=4, txt=str(descripcion),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt=str(fecha),border=1,align='C', fill=0,ln=1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(w=0,h=5, txt="FIRMA",border=0,ln=1,align='C', fill=0)
                
        if  a > b:
            cap = b
            print ("error el retiro no puede ser mayor que el capital")
            self.Open1()
            

        elif a >5000:
            cap = b
            print ("error el retiro no puede ser mayor a 5,000")
            self.Open2()
        
        elif len(id)==0 or len(nombre)==0 or len(apellidos)==0  or len(descripcion)==0:
            self.Open3()

        elif recipes.retirar_ahorro(data):
            print("Ahorro retirado")
            self.clear_inputs()
            self.texto_error.clear()
            self.texto_error_2.clear()
            self.Open()
            bb=date.today()
            
            ejemp=str(nombre)
            m=ejemp+"_"+str(bb)
            pdf.output('retiros/'+str(m)+'.pdf','f')
            wb.open_new(f"retiros\{m}"+".pdf")#jacque
           # wb.open_new('C:/Users/Almar/Documents/Proyecto/retiros'+str(m)+'.pdf')
            
    def Open(self):
        window=RetiroE(self)
        window.show()
    
    def Open1(self):
        window=Error1(self)
        window.show()
    
    def Open2(self):
        window=Error2(self)
        window.show()
    
    def Open3(self):
        window=Error_p(self)
        window.show()
        

    def clear_inputs(self):
        self.id_c.clear()
        self.nombre_c.clear()
        self.apellidos_c.clear()
        self.caja_capital.clear()
        self.caja_total_retiro.clear()
        self.caja_descrpcion.clear()
        self.fechar.clear()
        self.horar.clear()
   