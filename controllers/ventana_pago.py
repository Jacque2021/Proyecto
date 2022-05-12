import datetime
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from views.Ui_registro_pago import Ui_Form
from decimal import Decimal
import webbrowser as wb
from datetime import date, timedelta
from fpdf import FPDF
from database import recipes

class mensaje(QWidget, Ui_Form):
    def __init__(self, parent=None,Id_prestamo=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.Id_prestamo=Id_prestamo
        self.setupUi(self)
        self.frame.mouseMoveEvent = self.move_window
        self.setWindowFlag(Qt.Window)
        self.remove_defult_title_bar()
        self.set_window_shadow()
        #self.Ok.clicked.connect(self.crear_pdf())
        self.Ok.clicked.connect(self.hide)  
        self.crear_pdf()
    """*****************   ATRIBUTOS DE LA VENTANA VISTA    ********************"""
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.mouse_press_event(event)   
    #ubicación global del mouse
    def mouse_press_event(self, event):
        self.drag_pos=event.globalPos()
    #drag_post = posicion de la ventana que esta siendo arrastrada
    
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.move(self.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()
            
    #efecto de ventana
    def set_window_shadow(self):
        shadow=QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.frame.setGraphicsEffect(shadow)
    """***************** PDF  ****************************"""
    def crear_pdf(self):
        data=recipes.select_info_pdf_pagos(self.Id_prestamo)
        Id_cliente=data[0]
        nombre=data[1]
        telefono=data[2]
        telefono_add=data[3]
        direccion=data[4]
        correo=data[5]
        fecha_nacimiento=data[6]
        prestamo=data[7]
        periodo=data[8]
        Iva2=data[9]*100
        Iva=round(Iva2,0)
        r=data[10]
        renta=round(r,2)
        fecha_in=data[11]
        debe=data[13]
        k=data[14]
        wo=debe-k
        partes2 = str(fecha_in).split(" ")[0].split("-")
        fecha_inicio = "/".join(reversed(partes2))
        fecha_si=data[12]    #fecha siguiente
        #partes3 = str(fecha_in).split(" ")[0].split("-")
        #fecha_siguiente = "/".join(reversed(partes3))
        msj=""
        if wo>1:
            partes3 = str(fecha_si).split(" ")[0].split("-")
            fecha_siguiente = "/".join(reversed(partes3))
            fecha_sig=fecha_siguiente
        else:
            fecha_sig=msj
        fecha=datetime.datetime.now()
        partes = str(fecha).split(" ")[0].split("-")
        fecha_pago = "/".join(reversed(partes))
        pdf=FPDF(orientation='P',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        empresa=recipes.empresa()
        nombre_empresa=str(empresa[0])
        direccion2=str(empresa[1])
        #Arial bold 15
        pdf.set_font('Arial', '',18)
        #Titulo
        pdf.cell(w=0,h=10,txt=nombre_empresa,border=0,ln=1,align='R',fill=0)
        pdf.set_font('Arial', '',8)
        pdf.cell(w=0,h=5,txt=direccion2,border=0,ln=1,align='R',fill=0)
        pdf.cell(w=0,h=5,txt=' '+"",border=0,ln=1,align='R',fill=0)
        #line breack
        pdf.ln(5)
        #titulo
        pdf.set_font('Arial', '', 15)
        pdf.cell(w=0,h=5, txt="Reporte de registro pago de préstamo",border=0,ln=1,align='C', fill=0)
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
        pdf.cell(w=25,h=4, txt="No° socio",border=1,align='C', fill=1)
        pdf.cell(w=125,h=4, txt="Nombre del socio",border=1,align='C', fill=1,ln=0)
        pdf.cell(w=0,h=4, txt="Fecha de nacimiento",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=25,h=4, txt=str(Id_cliente),border=1,align='C', fill=0)
        pdf.cell(w=125,h=4, txt=str(nombre),border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=str(fecha_nacimiento),border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="Domicilio",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=0,h=4, txt=str(direccion),border=1,align='C', fill=0,ln=1)
        pdf.cell(w=40,h=4, txt="Telefono",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Telefono add",border=1,align='C', fill=1)
        pdf.cell(w=0,h=4, txt="Correo electronico",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=40,h=4, txt=str(telefono),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt=str(telefono_add),border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=str(correo),border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="",border=0,align='C', fill=0,ln=1)
        pdf.set_fill_color(r=0,g=0 , b=0) 
        pdf.set_text_color(r=255,g=255,b=255)
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.cell(w=0,h=5, txt="Información general del préstamo",border=1,ln=1,align='C', fill=1)
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.cell(w=45,h=4, txt="Monto del préstamo",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Tasa de interés",border=1,align='C', fill=1)
        pdf.cell(w=30,h=4, txt="Periodos",border=1,align='C', fill=1)
        pdf.cell(w=45,h=4, txt="Pago por periodo",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Interés moratorio",border=1,align='C', fill=1,ln=1)

        pdf.cell(w=45,h=4, txt='$'+str(prestamo),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(Iva)+'%',border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(periodo)+' pagos',border=1,align='C', fill=0)
        pdf.cell(w=45,h=4, txt='$'+str(renta),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt="6%",border=1,align='C', fill=0,ln=1)
        
        pdf.cell(w=64,h=4, txt="Fecha registro",border=1,align='C', fill=1)
        pdf.cell(w=63,h=4, txt="Fecha del pago",border=1,align='C', fill=1)
        pdf.cell(w=63,h=4, txt="Fecha del sig. pago",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=64,h=4, txt=str(fecha_inicio),border=1,align='C', fill=0)
        pdf.cell(w=63,h=4, txt=str(fecha_pago),border=1,align='C', fill=0)
        pdf.cell(w=63,h=4, txt=str(fecha_sig),border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=8, txt="",border=0,align='C', fill=0,ln=1)
        
        #TABLa
        #formato de tabla
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=30,h=10, txt="Monto pago",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="Interés",border=1,align='C', fill=1)
        pdf.cell(w=35,h=10, txt="Pago capital",border=1,align='C', fill=1)
        pdf.cell(w=35,h=10, txt="Cap. acumulado",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="Interés moratorio",border=1,align='C', fill=1)
        pdf.cell(w=0,h=10, txt="Sdo. capital",border=1,align='C', fill=1, ln=1)
        
        datos=recipes.select_info_pdf_pagos_Matriz(self.Id_prestamo)
        for valor in datos:
            pdf.cell(w=30,h=8, txt='$'+str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt='$'+str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=35,h=8, txt='$'+str(valor[3]),border=1,align='C', fill=0)
            pdf.cell(w=35,h=8, txt='$'+str(valor[4]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt='$'+str(valor[5]),border=1,align='C', fill=0)
            pdf.cell(w=0,h=8, txt='$'+str(valor[6]),border=1,align='C', fill=0, ln=1)
        
        """MANDA LLAMAR PAGOS DEL PRESTAMO"""
        b=date.today()
        ejemp=str(nombre)
        m=ejemp+"_"+str(b)
        pdf.output('pagos/'+str(m)+'.pdf','f')
        wb.open_new(f"pagos\{m}"+".pdf")