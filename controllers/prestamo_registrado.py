from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from views.Ui_registro_prestamo import Ui_Form
from datetime import datetime
from datetime import date, timedelta
import datetime
from decimal import Decimal
import webbrowser as wb
from fpdf import FPDF
from database import recipes

class mensaje(QWidget, Ui_Form):
    def __init__(self, parent=None,Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.Id_cliente=Id_cliente
        self.setupUi(self)
        self.frame.mouseMoveEvent = self.move_window
        self.setWindowFlag(Qt.Window)
        self.remove_defult_title_bar()
        self.set_window_shadow()
        self.Ok.clicked.connect(self.crear_pdf())
        self.Ok.clicked.connect(self.close)  
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
################################################################
    def crear_pdf(self):
        prestamo=recipes.ultimo_prestamo()
        id_cliente=int(prestamo[0])
        cantidad_prestamo=Decimal(prestamo[1])
        cantidad_prestamo2=round(cantidad_prestamo, 2)
        frecuencia=Decimal(prestamo[2])
        tiempo=str(prestamo[3])
        periodo=Decimal(prestamo[4])
        periodo2=round(periodo, 0)
        Iva=Decimal(prestamo[5])
        Iva2=round(Iva*100, 0)
        Iva_div=Decimal(prestamo[6])
        saldo_insolito=Decimal(prestamo[7])
        renta=Decimal(prestamo[8])
        renta2=round(renta, 2)
        interes=Decimal(prestamo[9])
        amortizacion=Decimal(prestamo[10])
        fecha_inicio=datetime.datetime.now()
        dia_delta=datetime.timedelta(days=30)
        fecha_siguiente=fecha_inicio+dia_delta
        amortizacion_acum=0
        cliente=recipes.select_clientes(id_cliente)
        nombre=str(cliente[1])
        telefono=str(cliente[2])
        telefono_add=str(cliente[3])
        direccion=str(cliente[4])
        correo=str(cliente[5])
        fecha_nacimiento= str(cliente[6])
        h1=str(fecha_inicio)
        partes = h1.split(" ")[0].split("-")
        fecha_inicio2 = "/".join(reversed(partes))
        h2=str(fecha_siguiente)
        partess = h2.split(" ")[0].split("-")
        fecha_siguiente2= "/".join(reversed(partess))

        x=6
        y=periodo
        matriz=[]
        for i in range(int(y)):
            lista=[]
            for j in range(int(x)):
                if i==0 and j==0:
                    h1=str(fecha_siguiente)
                    partes = h1.split(" ")[0].split("-")
                    dato = "/".join(reversed(partes))
                    lista.append(dato)
                elif i==0 and j==1:
                    #dato=renta
                    dato=round(renta, 2)
                    lista.append(dato)
                elif i==0 and j==2:
                    #dato=interes
                    dato=round(interes, 2)
                    lista.append(dato)
                elif i==0 and j==3:
                    dato=round(amortizacion, 2)
                    lista.append(dato)
                elif i==0 and j==4:
                    #dato=amortizacion
                    dato=round(amortizacion, 2)
                    lista.append(dato)
                    amortizacion2=amortizacion
                    amortizacion_acum+=amortizacion+amortizacion_acum
                elif i==0 and j==5:
                    saldo_insolito2=saldo_insolito-amortizacion
                    dato=round(saldo_insolito2, 2)
                    lista.append(dato)
                    saldo_insolito=saldo_insolito2
                elif i and j==0:
                    dia_delta=datetime.timedelta(days=30)
                    fecha=fecha_siguiente+dia_delta
                    h1=str(fecha)
                    partes = h1.split(" ")[0].split("-")
                    dato = "/".join(reversed(partes))
                    lista.append(dato)
                    fecha_siguiente=fecha
                elif i and j==1:
                    dato=round(renta, 2)
                    lista.append(dato)
                elif i and j==2:
                    interes2=saldo_insolito2*Decimal(Iva_div)
                    dato=round(interes2, 2)
                    lista.append(dato)
                    interes=interes2
                elif i and j==3:
                    amortizacion2=renta-Decimal(interes2)
                    dato=round(amortizacion2, 2)
                    lista.append(dato)
                    amortizacion=amortizacion2
                elif i and j==4:
                    amortizacion2=round(amortizacion, 2)
                    h=amortizacion_acum+amortizacion2
                    dato=round(h,2)
                    lista.append(dato)
                    amortizacion2=amortizacion
                    amortizacion_acum+=amortizacion2
                elif i and j==5:
                    saldo_insolito2=saldo_insolito-amortizacion
                    dato=round(saldo_insolito2, 2)
                    lista.append(dato)
                    saldo_insolito=saldo_insolito2
                else:
                    print("error")
            matriz.append(lista)
        ultima_fecha=matriz[i-int(periodo2)][0]
                #print(matriz)
        #print(matriz[i-periodo][0])
        #print(nuevo)
        ##########
        pdf=FPDF(orientation='P',unit='mm',format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        #texto
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(r=0,g=0,b=0)
        #Encabezado
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
        pdf.cell(w=0,h=5, txt="Reporte pago de préstamo",border=0,ln=1,align='C', fill=0)
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
        pdf.cell(w=25,h=4, txt=str(id_cliente),border=1,align='C', fill=0)
        pdf.cell(w=125,h=4, txt=nombre,border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=fecha_nacimiento,border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=4, txt="Domicilio",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=0,h=4, txt=direccion,border=1,align='C', fill=0,ln=1)
        pdf.cell(w=40,h=4, txt="Telefono",border=1,align='C', fill=1)
        pdf.cell(w=40,h=4, txt="Telefono add",border=1,align='C', fill=1)
        pdf.cell(w=0,h=4, txt="Correo electronico",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=40,h=4, txt=telefono,border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt=telefono_add,border=1,align='C', fill=0)
        pdf.cell(w=0,h=4, txt=correo,border=1,align='C', fill=0,ln=1)
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

        pdf.cell(w=45,h=4, txt='$'+str(cantidad_prestamo2),border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(Iva2)+'%',border=1,align='C', fill=0)
        pdf.cell(w=30,h=4, txt=str(periodo2)+' pagos',border=1,align='C', fill=0)
        pdf.cell(w=45,h=4, txt='$'+str(renta2),border=1,align='C', fill=0)
        pdf.cell(w=40,h=4, txt="6%",border=1,align='C', fill=0,ln=1)

        pdf.cell(w=64,h=4, txt="Fecha registro",border=1,align='C', fill=1)
        pdf.cell(w=63,h=4, txt="Fecha primer pago",border=1,align='C', fill=1)
        pdf.cell(w=63,h=4, txt="Fecha ultimo pago",border=1,align='C', fill=1,ln=1)
        pdf.cell(w=64,h=4, txt=str(fecha_inicio2),border=1,align='C', fill=0)
        pdf.cell(w=63,h=4, txt=str(fecha_siguiente2),border=1,align='C', fill=0)
        pdf.cell(w=63,h=4, txt=str(ultima_fecha),border=1,align='C', fill=0,ln=1)
        pdf.cell(w=0,h=8, txt="",border=0,align='C', fill=0,ln=1)
        #formato de tabla
        pdf.set_draw_color(r=0,g=0 , b=0)#color del borde
        pdf.set_fill_color(r=151,g=153 , b=155) #color de fondo
        pdf.cell(w=30,h=10, txt="Fecha limite",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="Monto pago",border=1,align='C', fill=1)
        pdf.cell(w=25,h=10, txt="Interés",border=1,align='C', fill=1)
        pdf.cell(w=35,h=10, txt="Pago capital",border=1,align='C', fill=1)
        pdf.cell(w=40,h=10, txt="Cap. acumulado",border=1,align='C', fill=1)
        pdf.cell(w=30,h=10, txt="Sdo. capital",border=1,ln=1,align='C', fill=1)
        #valores
        for valor in matriz:
            pdf.cell(w=30,h=8, txt=str(valor[0]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[1]),border=1,align='C', fill=0)
            pdf.cell(w=25,h=8, txt=str(valor[2]),border=1,align='C', fill=0)
            pdf.cell(w=35,h=8, txt=str(valor[3]),border=1,align='C', fill=0)
            pdf.cell(w=40,h=8, txt=str(valor[4]),border=1,align='C', fill=0)
            pdf.cell(w=30,h=8, txt=str(valor[5]),border=1,align='C', fill=0,ln=1)
        ###
        b=date.today()
        dia_delta=timedelta(days=30)
        suma=b+dia_delta
        ejemp=str(nombre)
        m=ejemp+"_"+str(b)
        pdf.output('prestamos/'+str(m)+'.pdf','f')
        wb.open_new(f"prestamos\{m}"+".pdf")
        #wb.open_new('C:/Users/Almar/Documents/Proyecto/prestamos/'+str(m)+'.pdf')
    