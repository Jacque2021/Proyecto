import codecs
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustomUi
from controllers.chequeRealizado import Cheque
from views.botonesMenu import Menu_Botones
from controllers.error_prestamo import Error_p
from views.cheque_exitoso import cheq
from datetime import datetime
from views.cheques import Cheques
import datetime 
from datetime import date
import datetime
from fpdf import FPDF
import webbrowser as wb
from database import recipes


class ChequesForm(QWidget, Cheques, FPDF):

    def __init__(self, parent=None, Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent) 
        #self.id=id
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.Id_cliente=Id_cliente
        self.llamar_nombre()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.vista()

        
       # self.boton_buscar_2.clicked.connect(self.open_busqueda)
        self.boton_emitir_2.clicked.connect(self.nuevo_cheque)
        
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
  
    
    def llamar_nombre(self): 
        data=recipes.select_cliente_cheque(self.Id_cliente)
        id=data[0]
        id = str(id)
        nombre=data[1]
        apellidos=data[2]
        apellidos = str(apellidos)
        self.id_c.setText(id)
        self.nombre_c.setText(nombre)
        self.apellidos_c.setText(apellidos)
    
    def vista(self):
        fecha_registro=datetime.datetime.now() #Fecha de hoy
        h1=str(fecha_registro) #convierte a string
        partes = h1.split(" ")[0].split("-") #quita la hora, dejando la fecha
        convertida1 = "/".join(reversed(partes)) #cambia formato de fecha
        self.fechaf.setText(str(convertida1)) #lo pasa a la interfaz

    def nuevo_cheque(self):
        id = self.id_c.text()
        nombre = self.nombre_c.text()
        apellidos = self.apellidos_c.text()
        id_cheque = self.caja_id_cheque_2.text()
        fecha = self.fechaf.text()
        monto = self.caja_monto_2.text()
        beneficiario = self.caja_beneficiario_2.text()
        descripcion = self.caja_descripcion_2.text()
        
 
        data = (id, nombre, apellidos, id_cheque, fecha, monto, beneficiario, descripcion)
        
        
  ### CREAR DOC PDF CHEQUE
         ##########
        pdf=FPDF(orientation='P',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
        empresa=recipes.empresa
        nombre_emp=str('Caja popular mexicana')
        ubicacion_emp=str('México')
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
        pdf.cell(w=0,h=5, txt="CHEQUE",border=0,ln=1,align='C', fill=0)
        pdf.cell(w=0,h=5, txt="Páguese este cheque a la orden de:",border=0,ln=1,align='C', fill=0)
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
        pdf.cell(w=125,h=4, txt="Nombre del cliente",border=1,align='C', fill=1,ln=0)
        pdf.cell(w=0,h=4, txt="Apellidos del cliente",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=25,h=4, txt=str(id),border=1,align='C', fill=0)
        pdf.cell(w=125,h=4, txt=nombre,border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=apellidos,border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="",border=0,align='C', fill=0,ln=1)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.cell(w=0,h=5, txt="Información general del cheque",border=1,ln=1,align='C', fill=1)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.cell(w=45,h=4, txt="No. de cheque",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Fecha de emisión",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Monto",border=1,align='C', fill=1)
        pdf.cell(w=45,h=4, txt="Beneficiario",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Descripción",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=45,h=4, txt=str(id_cheque),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(fecha),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt='$'+str(monto),border=1,align='C', fill=0)
        pdf.cell(w=45,h=4, txt=str(beneficiario),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt=str(descripcion),border=1,align='C', fill=0,ln=1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(40,10, '', 0,1)
        pdf.cell(w=0,h=5, txt="FIRMA",border=0,ln=1,align='C', fill=0)
                
        if len(id)==0 or len(nombre)==0 or len(apellidos)==0 or len(id_cheque)==0 or len(fecha)==0 or len(monto)==0 or len(beneficiario)==0 or len(descripcion)==0:
            self.Open3()
       
        elif recipes.crear_cheque(data):
           print("Nuevo cheque realizado")
           self.clear_inputs()
           self.Open()
        
           b=date.today()
           ejemp=str(nombre)
           m=ejemp+"_"+str(b)
           pdf.output('cheques/'+str(m)+'.pdf','f')
           wb.open_new('C:/Users/Laptop/Desktop/Proyecto/cheques/'+str(m)+'.pdf')

    def Open(self):
        window=Cheque(self)
        window.show()

    def Open3(self):
        window=Error_p(self)
        window.show()
    
    def clear_inputs(self):
        self.id_c.clear()
        self.nombre_c.clear()
        self.apellidos_c.clear()
        self.caja_id_cheque_2.clear()
        self.fechaf.clear()
        self.caja_monto_2.clear()
        self.caja_beneficiario_2.clear()
        self.caja_descripcion_2.clear()

        