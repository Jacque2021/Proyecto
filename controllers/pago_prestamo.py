from decimal import Decimal
from turtle import clear
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_AbonarPago import Ui_Nuevoprestamo
from controllers.ventana_pago import mensaje
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget,  QMenu)
from PySide6.QtGui import QAction, QActionGroup
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
        self.setWindowFlag(Qt.Window)
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.llenar_datos_prestamo()
        #self.minimenu()
        self.boton_pagar.clicked.connect(self.registrar_pago)
        self.pagar_ahorro.clicked.connect(self.pagarConAhorro)
        self.cc()
        self.menu()
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    ##################################################################################
    """****************    LLENAR INFORMACIÓN DEL PRESTAMO (VISTA)   **************"""
    def llenar_datos_prestamo(self):
        self.pagar_ahorro.setVisible(False)
        self.boton_pagar.setVisible(False)
        data=recipes.select_info_cliente_prestamo(self.Id_cliente)
        if data:   #si el cliente tiene una deuda con la cooperativa
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
            saldo=data[8]
            #limite=datetime.strptime( fecha_limite , '%dd/%mm/%Y' )
            dia_delta=datetime.timedelta(days=30)
            restame=saldo-pago 
            if restame<1:     #si el saldo es menor a 1, ya no hay fecha siguiente
                self.fecha_sig_2.setText(" ")
            else:  #muestra una fecha siguiente
                fecha_siguiente=limite+dia_delta
                h1=str(fecha_siguiente)
                partes = h1.split(" ")[0].split("-")
                convertida1 = "/".join(reversed(partes))
                self.fecha_sig_2.setText(str(convertida1))
            if fecha_registro>=limite:   #para pagar con ahorro
                if recipes.capital_ahorro(self.Id_cliente): #si el cliente tiene cuenta de ahorro
                    a=recipes.capital_ahorro(self.Id_cliente)
                    ca=a[0]
                    if ca>Decimal(renta):   #si capital ahorro es mayor o igual a lo que debe
                        self.pagar_ahorro.setVisible(True)
                else: None  #no muestra el boton de pagar con ahorro 
                d1=limite  #muestra informacion del pago prestamo
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
            else:  #si la fecha aun no vence, oculta el boton y registra todo normal 
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
        else:   #no hace nada 
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
################################################################################################
#########################                MENU                ###################################
################################################################################################ 
    def Open_pagosPrestamos(self):
        from controllers.busqueda_pago import buscueda_prestamo
        window=buscueda_prestamo(self)
        self.close()
        window.show()
    def Open_cancelacion(self):
        from controllers.cancelacion import Error
        window=Error(self)
        self.close()
        window.show()
    def open_busqueda(self):
        from controllers.busqueda import buscar
        window=buscar(self)
        self.close()
        window.show()
    def cerrar(self):
        self.close()
    def ayuda(self):
        from controllers.ayuda import Documento
        window=Documento(self)
        self.close()
        window.show()
    def Notificacio(self):
        from controllers.notificaciones import Notificacion
        window=Notificacion(self)
        self.close()
        window.show()
    """***AQUI ESTUVO MAY***"""
    def open_empresa(self):
        from controllers.mi_empresa import MiEmpresaForm
        self.window=MiEmpresaForm(self)
        self.close()
        self.window.show()
    def open_repaldaempresa(self):
        from controllers.respaldar_empresa import RespaldarEmpresaForm
        self.window=RespaldarEmpresaForm(self)
        self.close()
        self.window.show()
    def open_cheques(self):
        from controllers.busqueda_c import buscarc
        self.window=buscarc(self)
        self.close()
        self.window.show()
    def open_consulta_cheques(self):
        from controllers.consulta_cheques import Consulta_chequesForm
        self.window=Consulta_chequesForm(self)
        self.close()
        self.window.show()
    def open_nuevo_ahorro(self):
        from controllers.busqueda_re_ahorro import buscar_re_ahorro
        self.window=buscar_re_ahorro(self)
        self.close()
        self.window.show()
    def open_retiro_ahorro(self):
        from controllers.busqueda_retirar_ahorro import buscar_retirar_ahorro
        self.window=buscar_retirar_ahorro(self)
        self.close()
        self.window.show()
    """***AQUI ESTUVO PABLO***"""
    def Open_historial_cliente(self):
        from controllers.historial_cliente import HistorialClienteForm
        self.window=HistorialClienteForm(self)
        self.close()
        self.window.show()
    def Open_listado_polizas(self):
        from controllers.listado_polizas import ListadoPolizasForm
        self.window=ListadoPolizasForm(self)
        self.close()
        self.window.show()
    def Open_agregar_cliente(self):
        from controllers.agregar_cliente import AgregarClienteForm
        self.window=AgregarClienteForm(self)
        self.close()
        self.window.show()
    def open_catalogo(self):
        from controllers.busqueda_e import buscar_empresa
        self.window=buscar_empresa(self)
        self.close()
        self.window.show()
    """***AQUI ESTUVO JESUS***"""
    def open_estadoCUENTAS(self):
        from controllers.ConsultaEstadoCuentas import buscarCuenta
        self.window=buscarCuenta(self)
        self.close()
        self.window.show()
    def open_emitirReport(self):
        from controllers.EmitirReporte import emite_R
        self.window=emite_R(self)
        self.close()
        self.window.show()
    def open_emitirReport_2(self):
        from controllers.EmitirReporte_2 import emite_R_2
        self.window=emite_R_2(self)
        self.close()
        self.window.show()
    def open_nPoliza(self):
        from controllers.NuevaPoliza import nuevaPoliza
        self.window=nuevaPoliza(self)
        self.close()
        self.window.show()
################################################################################################
#########################                MENU V.2            ###################################
################################################################################################ 
    def prestamos1(self):
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
        
    ##############################################################
    def miempresa(self):
        self.Empresa.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Empresa.customContextMenuRequested.connect(self.on_context_menu1)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
        # create context menu
        self.popMenu1 = QMenu(self)
        self.popMenu1.addAction(QAction('Mi empresa', np))
        self.popMenu1.addSeparator()
        self.popMenu1.addAction(QAction('Respaldar empresa', ap))
        self.popMenu1.addSeparator()
        self.popMenu1.addAction(QAction('Catálogo de cuentas', cancela))
        
        np.triggered.connect(self.open_empresa)
        ap.triggered.connect(self.open_repaldaempresa)
        cancela.triggered.connect(self.open_catalogo)
    def on_context_menu1(self, point):
        # show context menu
        self.popMenu1.exec_(self.Empresa.mapToGlobal(point))
    ##############################################################
    def clientes(self):
        self.Clientes.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Clientes.customContextMenuRequested.connect(self.on_context_menu2)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu2 = QMenu(self)
        self.popMenu2.addAction(QAction('Agregar nuevo cliente', np))
        self.popMenu2.addSeparator()
        self.popMenu2.addAction(QAction('Historial del cliente', ap))
    
        np.triggered.connect(self.Open_agregar_cliente)
        ap.triggered.connect(self.Open_historial_cliente)
    def on_context_menu2(self, point):
        # show context menu
        self.popMenu2.exec_(self.Clientes.mapToGlobal(point))
    ##############################################################
    def ahorro(self):
        self.Ahorros.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Ahorros.customContextMenuRequested.connect(self.on_context_menu3)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu3 = QMenu(self)
        self.popMenu3.addAction(QAction('Nuevo ahorro', np))
        self.popMenu3.addSeparator()
        self.popMenu3.addAction(QAction('Retirar ahorro', ap))
    
        np.triggered.connect(self.open_nuevo_ahorro)
        ap.triggered.connect(self.open_retiro_ahorro)
    def on_context_menu3(self, point):
        # show context menu
        self.popMenu3.exec_(self.Ahorros.mapToGlobal(point))
    ##############################################################
    def consultas(self):
        self.Consultas.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Consultas.customContextMenuRequested.connect(self.on_context_menu4)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        cancela = QActionGroup(self)
        cancela.setExclusive(True)
         ########################3
        cancela2 = QActionGroup(self)
        cancela2.setExclusive(True)
        # create context menu
        self.popMenu4 = QMenu(self)
        self.popMenu4.addAction(QAction('Estado de cuentas', ap))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Emitir reporte de ahorro', cancela))
        self.popMenu4.addSeparator()
        self.popMenu4.addAction(QAction('Emitir reporte de prestamos', cancela2))
        
        ap.triggered.connect(self.open_estadoCUENTAS)
        cancela.triggered.connect(self.open_emitirReport)
        cancela2.triggered.connect(self.open_emitirReport_2)
    def on_context_menu4(self, point):
        # show context menu
        self.popMenu4.exec_(self.Consultas.mapToGlobal(point))
    ##############################################################
    def polizas(self):
        self.PolizaS.setContextMenuPolicy(Qt.CustomContextMenu)
        self.PolizaS.customContextMenuRequested.connect(self.on_context_menu5)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu5 = QMenu(self)
        self.popMenu5.addAction(QAction('Nueva poliza', np))
        self.popMenu5.addSeparator()
        self.popMenu5.addAction(QAction('Listado de polizas', ap))
        
        np.triggered.connect(self.open_nPoliza)
        ap.triggered.connect(self.Open_listado_polizas)
    def on_context_menu5(self, point):
        # show context menu
        self.popMenu5.exec_(self.PolizaS.mapToGlobal(point))
    ##############################################################
    def cheques(self):
        self.ChequeS.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ChequeS.customContextMenuRequested.connect(self.on_context_menu6)
        np = QActionGroup(self)
        np.setExclusive(True)
        ######################3
        ap = QActionGroup(self)
        ap.setExclusive(True)
        ########################3
        # create context menu
        self.popMenu6 = QMenu(self)
        self.popMenu6.addAction(QAction('Cheques', np))
        self.popMenu6.addSeparator()
        self.popMenu6.addAction(QAction('Consultar cheques', ap))
        
        np.triggered.connect(self.open_cheques)
        ap.triggered.connect(self.open_consulta_cheques)
    def on_context_menu6(self, point):
        # show context menu
        self.popMenu6.exec_(self.ChequeS.mapToGlobal(point))
        
    def cc(self):
        self.cancelar.clicked.connect(self.Open_cancelacion)
        #self.prestamo.triggered.connect(self.Open_cancelacion)###
        self.abonar.clicked.connect(self.Open_pagosPrestamos)
        self.prestamo.clicked.connect(self.open_busqueda)
        self.Mi_Empresa.clicked.connect(self.open_empresa)
        self.Respaldo.clicked.connect(self.open_repaldaempresa)
        self.Cheques.clicked.connect(self.open_cheques)
        self.Consulta_cheque.clicked.connect(self.open_consulta_cheques)
        self.Ahorro.clicked.connect(self.open_nuevo_ahorro)
        self.Retirar.clicked.connect(self.open_retiro_ahorro)
        self.Ayuda.clicked.connect(self.ayuda)
        self.Notificaciones.clicked.connect(self.Notificacio)
        self.Salir.clicked.connect(self.close)
        self.Cliente.clicked.connect(self.Open_agregar_cliente)
        self.Listado.clicked.connect(self.Open_listado_polizas)
        self.Historial.clicked.connect(self.Open_historial_cliente)
        self.Catalogo.clicked.connect(self.open_catalogo)
        self.Estado.clicked.connect(self.open_estadoCUENTAS)
        self.Reportes.clicked.connect(self.open_emitirReport)
        self.Reportes_2.clicked.connect(self.open_emitirReport_2)
        self.Polizas.clicked.connect(self.open_nPoliza)
    def menu(self):
        self.prestamos1()
        self.miempresa()
        self.clientes()
        self.ahorro()
        self.consultas()
        self.polizas()
        self.cheques()