from decimal import Decimal
from turtle import clear
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_AbonarPago import Ui_Nuevoprestamo
from controllers.ventana_pago import mensaje
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,  QMenu)
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtCore import Qt
from controllers.cancelacion import Error
from controllers.busqueda import buscar
from database import recipes
import datetime 
#from datetime import datetime

class Pagos(QWidget, Ui_Nuevoprestamo):
    def __init__(self, parent=None,Id_cliente=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.Id_cliente=Id_cliente #1
        self.setupUi(self)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_datos_prestamo()
        #self.minimenu()
        self.boton_pagar.clicked.connect(self.registrar_pago)
        self.pagar_ahorro.clicked.connect(self.pagarConAhorro)
        self.cc()
        self.minimenu()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    ##################################################################################
    """****************    LLENAR INFORMACIÓN DEL PRESTAMO (VISTA)   **************"""
    def llenar_datos_prestamo(self):
        self.pagar_ahorro.setVisible(False)
        self.boton_pagar.setVisible(False)
        data=recipes.select_info_cliente_prestamo(self.Id_cliente)
        if data:
            self.boton_pagar.setVisible(True)
            renta=round(data[5],2)
            tasa_moratorio=0.06
            moratorio_mensual=(tasa_moratorio*renta)
            x=(moratorio_mensual/30)
            moratorio_dia=round(x, 2)
            cuenta=data[0]
            nombre=data[1] 
            prestamo=(data[2])
            pago=round(data[4],2)
            interes=round(data[3],2)
            fecha_registro=datetime.date.today()
            limite=data[6]
            #limite=datetime.strptime( fecha_limite , '%dd/%mm/%Y' )
            dia_delta=datetime.timedelta(days=30)
            fecha_siguiente=limite+dia_delta
            h1=str(fecha_siguiente)
            partes = h1.split(" ")[0].split("-")
            convertida1 = "/".join(reversed(partes))
            self.fecha_sig_2.setText(str(convertida1))
            if fecha_registro>=limite:
                if recipes.capital_ahorro(self.Id_cliente):
                    a=recipes.capital_ahorro(self.Id_cliente)
                    ca=a[0]
                    if ca>renta:
                        self.pagar_ahorro.setVisible(True)
                else: None
                d1=limite
                d2=fecha_registro
                intervalo=d2-d1
                dias=intervalo.days
                #print(dias)###################3
                aumento=dias*moratorio_dia
                mortizacin=round(aumento,2)
                tp=renta+aumento
                total_pago=round(tp,2)
                self.amortizacin.setText(str(mortizacin))
                self.total_pago.setText(str(total_pago))
            else:
                self.pagar_ahorro.setVisible(False)
                self.total_pago.setText(str(renta))
                self.amortizacin.setText("No aplica")
            self.cuenta.setText(str(cuenta))
            self.nombre.setText(nombre)
            self.prestamo_2.setText(str(prestamo))
            self.pago.setText(str(pago))
            self.interes.setText(str(interes))
            #REDUCE FECHA
            h1=str(fecha_registro)
            partes = h1.split(" ")[0].split("-")
            convertida1 = "/".join(reversed(partes))
            h2=str(limite)
            partes1 = h2.split(" ")[0].split("-")
            convertida2 = "/".join(reversed(partes1))
            self.fecha_registro.setText(str(convertida1 ))
            self.fecha_limite.setText(str(convertida2))
        else: 
            self.hide()
        ##################################################################################
        """****************    ALMACENAR REGISTRO PAGO   **************"""   
    def registrar_pago(self):    
        data=recipes.select_info_cliente_prestamo(self.Id_cliente) 
        nombre1=data[1]
        Id_p=data[7]
        renta=Decimal(data[5]) #ES LA MISMA SIEMPRE
        deuda=Decimal(data[8]) #Cuanto debe aun
        interes=Decimal(data[3]) #interes 
        amortizacion=Decimal(data[4]) #pago sin intereses
        fecha_limite=data[6] #fecha limite
        #datetime.date.today()
        amor_acum=Decimal(data[10])
        iva=data[9]#IVA dividido
        puntitos=recipes.clientes_puntos(self.Id_cliente)
        nombre=puntitos[1]
        punt=puntitos[0]
        """PAGO"""
        menos_deuna=deuda-amortizacion #se le resta la deusa =saldo insolito
        #interes_2=Decimal(deuda*iva)
        #pago_sin_interes=renta-interes_2 #amortización
        s=amor_acum+amortizacion #amortizacion acumulada
        fecha=datetime.date.today() #hoy
        dia_delta=datetime.timedelta(days=30)
        fecha_siguiente=fecha_limite+dia_delta
        if fecha>fecha_limite:     ###################################
            puntos=punt
            intervalo=fecha-fecha_limite
            dias=intervalo.days
            tasa_moratorio=Decimal(0.06)
            moratorio_mensual=(tasa_moratorio*renta)
            x=(moratorio_mensual/30)
            moratorio_dia=x
            aumento=dias*moratorio_dia
            #amortizacion=aumento
            datas=(int(puntos), str(nombre))
            g=0
            link=f"pagos\{nombre1}"+".pdf"
            bandera=int(g)
            if recipes.clientes_puntos_mas(self.Id_cliente,datas):
                print("puntos eliminados")
            Inserta=(Id_p,menos_deuna,interes,amortizacion,s,fecha_limite,fecha,fecha_siguiente,aumento,bandera,link)
            if recipes.insert_Pagos(Inserta):
             print("Recipe Added")
             self.limpirar_parametros()
        else:
            puntos=punt+1
            g=0
            bandera=int(g)
            datas=(int(puntos), str(nombre))
            if recipes.clientes_puntos_mas(self.Id_cliente,datas):
                print("puntos aumentados")
            aumento=0
            link=f"pagos\{nombre1}"+".pdf"
            Inserta=(Id_p,menos_deuna,interes,amortizacion,s,fecha_limite,fecha,fecha_siguiente,aumento,bandera,link)
            if recipes.insert_Pagos(Inserta):
             print("Recipe Added")
             self.limpirar_parametros()
             self.boton_pagar.setVisible(False)
             
        """****************    ACTUALIZA DATOS DE PRESTAMO   **************"""  
        saldo_insolito2=menos_deuna
        interes2=saldo_insolito2*Decimal(iva)
        amortizacion2=renta-interes2
        amortizacion_acum2=s
        fecha_siguiente2=fecha_siguiente
        data=(saldo_insolito2,interes2,amortizacion2,amortizacion_acum2,fecha_siguiente2)
        if recipes.update_prestamo(Id_p, data):
            print("Recipe Edited")
        Id_prestamo=Id_p
        self.window=mensaje(self,Id_prestamo)
        self.close()
        self.window.show() 
            
    ##################################################################################
    """****************    PAGAR CON AHORRO   **************"""    
    def pagarConAhorro(self):
        data=recipes.select_info_cliente_prestamo(self.Id_cliente) 
        nombre1=data[1]
        Id_p=data[7]
        renta=Decimal(data[5]) #ES LA MISMA SIEMPRE
        deuda=Decimal(data[8]) #Cuanto debe aun
        interes=Decimal(data[3]) #interes 
        amortizacion=Decimal(data[4]) #pago sin intereses
        fecha_limite=data[6] #fecha limite
        amor_acum=Decimal(data[10])
        iva=data[9]#IVA dividido
        ahorro=recipes.llamar_capital(self.Id_cliente)
        cap=Decimal(ahorro[0])
        impo=Decimal(ahorro[2])
        puntitos=recipes.clientes_puntos(self.Id_cliente)
        nombre=puntitos[1]
        punt=puntitos[0]
        """PAGO"""
        menos_deuna=deuda-amortizacion #se le resta la deusa =saldo insolito
        #interes_2=Decimal(deuda*iva)
        #pago_sin_interes=renta-interes_2 #amortización
        s=amor_acum+amortizacion #amortizacion acumulada
        fecha=datetime.date.today()
        dia_delta=datetime.timedelta(days=30)
        fecha_siguiente=fecha_limite+dia_delta
        if fecha>fecha_limite:
            puntos=punt
            intervalo=fecha-fecha_limite
            dias=intervalo.days
            tasa_moratorio=Decimal(0.06)
            moratorio_mensual=(tasa_moratorio*renta)
            x=(moratorio_mensual/30)
            moratorio_dia=x
            aumento=dias*moratorio_dia
            #amortizacion=aumento
            total=aumento+renta #total a pagar
            restar=cap-total    #resta al capital
            pago_con_capital=(restar,impo)
            g=1
            bandera=int(g)
            link=f"pagos\{nombre1}"+".pdf"
            Inserta=(Id_p,menos_deuna,interes,amortizacion,s,fecha_limite,fecha,fecha_siguiente,aumento,bandera,link)
            if recipes.insert_Pagos(Inserta):
             print("Recipe Added")
             self.limpirar_parametros()
            if recipes.pagar_con_ahorro(self.Id_cliente, pago_con_capital):
                print("Pago hecho con ahorro")
            datas=(int(puntos), str(nombre))
            if recipes.clientes_puntos_mas(self.Id_cliente,datas):
                print("puntos eliminados")
        else:
            total=renta #total a pagar
            restar=cap-total    #resta al capital
            pago_con_capital=(restar,impo)
            if recipes.pagar_con_ahorro(self.Id_cliente, pago_con_capital):
                print("Pago hecho con ahorro")
            aumento=0
            puntos=punt+1
            g=1
            bandera=int(g)
            link=f"pagos\{nombre1}"+".pdf"
            datas=(int(puntos), str(nombre))
            if recipes.clientes_puntos_mas(self.Id_cliente,datas):
                print("puntos aumentados")
            Inserta=(Id_p,menos_deuna,interes,amortizacion,s,fecha_limite,fecha,fecha_siguiente,aumento,bandera,link)
            if recipes.insert_Pagos(Inserta):
             print("Se realizó el pago")
             self.limpirar_parametros()
             
        """****************    ACTUALIZA DATOS DE PRESTAMO   **************"""  
        saldo_insolito2=menos_deuna
        interes2=saldo_insolito2*Decimal(iva)
        amortizacion2=renta-interes2
        amortizacion_acum2=s
        fecha_siguiente2=fecha_siguiente
        data=(saldo_insolito2,interes2,amortizacion2,amortizacion_acum2,fecha_siguiente2)
        if recipes.update_prestamo(Id_p, data):
            print("Se actualizó datos de prestamo")
        Id_prestamo=Id_p
        self.window=mensaje(self,Id_prestamo)
        self.window.show()  
    ##################################################################################     
    """****************    LIMPIAR PARAMETROS DE INTERFAZ   **************"""     
    def limpirar_parametros(self):
        self.cuenta.clear()
        self.nombre.clear()
        self.prestamo_2.clear()
        self.pago.clear()
        self.interes.clear()
        self.amortizacin.clear()
        self.total_pago.clear() 
        self.fecha_limite.clear()
        self.fecha_registro.clear()
        self.advertencia.clear()  
        self.realizo_pago.clear() 
        self.fecha_sig.clear()
        self.fecha.clear()   
        self.fecha_sig_2.clear()
    #################################  ABRIR VENTANA EMERGENTE  ##################################### 
    def Open_ventana(self):
        Id_prestamo=self.pagarConAhorro()
        self.window=mensaje(self,Id_prestamo)
        self.window.show()
    ##################################################################################################
    def minimenu(self):
        #self.barra_principal_frame.setMenuBar(self.menubar)
        #self.menubar = QMenuBar(self.barra_principal_frame)
        self.Prestamos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Prestamos.customContextMenuRequested.connect(self.on_context_menu)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('Nuevo prestamo', np))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Abonar pago', ap))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Cancelar pago', cancela))
        
        np.triggered.connect(self.open_busqueda)
        cancela.triggered.connect(self.Open_cancelacion)
    ###################################################
    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.Prestamos.mapToGlobal(point))
    def Open_cancelacion(self):
        self.window=Error(self)
        self.window.show()
    def open_busqueda(self):
        self.window=buscar(self)
        self.window.show()
        
    """  Menu  """
    def Open_pagosPrestamos(self):
        from controllers.busqueda_pago import buscueda_prestamo
        self.window=buscueda_prestamo(self)
        self.close()
        self.window.show()
    def Open_cancelacion(self):
        from controllers.cancelacion import Error
        self.window=Error(self)
        self.hide()
        self.window.show()
    def open_busqueda(self):
        from controllers.busqueda import buscar
        self.window=buscar(self)
        self.hide()
        self.window.show()
    def ayuda(self):
        from controllers.ayuda import Documento
        self.window=Documento(self)
        self.hide()
        self.window.show()
    def Notificacio(self):
        from controllers.notificaciones import Notificacion
        self.window=Notificacion(self)
        self.hide()
        self.window.show()
    def cc(self):
        self.cancelar.clicked.connect(self.Open_cancelacion)
        #self.prestamo.triggered.connect(self.Open_cancelacion)###
        self.abonar.clicked.connect(self.Open_pagosPrestamos)
        self.prestamo.clicked.connect(self.open_busqueda)
        self.Ayuda.clicked.connect(self.ayuda)
        self.Notificaciones.clicked.connect(self.Notificacio)
        self.Salir.clicked.connect(self.close)
        
    ###################################################################  
    def minimenu(self):
        self.Prestamos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Prestamos.customContextMenuRequested.connect(self.on_context_menu)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('Nuevo prestamo', np))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Abonar pago', ap))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Cancelar pago', cancela))
        
        np.triggered.connect(self.open_busqueda)
        ap.triggered.connect(self.Open_pagosPrestamos)
        cancela.triggered.connect(self.Open_cancelacion)
    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.Prestamos.mapToGlobal(point))