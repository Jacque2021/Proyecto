import datetime
from database import recipes
class Menu_Botones():
    def __init__(self, bm):
        self.bm=bm #contiene el objeto de las ventanas
        self.ocultar_boton() ##oculta todos los botones
        self.abracadabra() 
        self.contador()
        #self.minimenu()
        
    #def mouse_press_event(self, event):
        #self.drag_pos=event.globalPos()
        
#####################    OCULTAR SUBMENUS ****************************    
    def ocultar_boton(self):
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)

#####################    VER SUBMENUS ****************************
    def ver_empresa(self):
        self.bm.Catalogo.setVisible(True) #Visualisa los sub-botones
        self.bm.Mi_Empresa.setVisible(True)
        self.bm.Respaldo.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
    def ver_clientes(self):
        self.bm.Cliente.setVisible(True) #Visualisa los sub-botones
        self.bm.Historial.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
    def ver_prestamos(self):
        self.bm.cancelar.setVisible(True) #Visualisa los sub-botones
        self.bm.prestamo.setVisible(True)
        self.bm.abonar.setVisible(True)
        self.bm.Ahorro.setVisible(False) #oculta sub-botones inescesarios
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        ##  Metodo para abrir nueva interfaz
    def ver_ahorros(self):
        self.bm.Retirar.setVisible(True) #Visualisa los sub-botones
        self.bm.Ahorro.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
    
    def ver_consultas(self):
        self.bm.Estado.setVisible(True) #Visualisa los sub-botones
        self.bm.Reportes.setVisible(True)
        self.bm.Reportes_2.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
    
    def ver_Polizas(self):
        self.bm.Listado.setVisible(True) #Visualisa los sub-botones
        self.bm.Polizas.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cheques.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Consulta_cheque.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        
    def ver_cheques(self):
        self.bm.Cheques.setVisible(True) #Visualisa los sub-botones
        self.bm.Consulta_cheque.setVisible(True)
        self.bm.cancelar.setVisible(False) #oculta sub-botones
        self.bm.prestamo.setVisible(False)
        self.bm.abonar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.Catalogo.setVisible(False)
        self.bm.Cliente.setVisible(False)
        self.bm.Estado.setVisible(False)
        self.bm.Historial.setVisible(False)
        self.bm.Listado.setVisible(False)
        self.bm.Mi_Empresa.setVisible(False)
        self.bm.Reportes_2.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
    def oculta_cheque(self):
        if self.bm.Cheques.setVisible(True) and self.bm.Consulta_cheque.setVisible(True):
           self.bm.Cheques.setVisible(False) and self.bm.Consulta_cheque.setVisible(False) 
    
    def salir(self):
        self.bm.cancelar.setVisible(True) #Visualisa los sub-botones
    
        
#####################    MAGIA NEGRA ****************************
    def abracadabra(self):
         self.bm.Empresa.clicked.connect(self.ver_empresa)#al dar click a uno de los botones principales, aparece los sub-botones
         self.bm.Clientes.clicked.connect(self.ver_clientes)
         self.bm.Prestamos.clicked.connect(self.ver_prestamos)
         self.bm.Ahorros.clicked.connect(self.ver_ahorros)
         self.bm.Consultas.clicked.connect(self.ver_consultas)
         self.bm.PolizaS.clicked.connect(self.ver_Polizas)
         self.bm.ChequeS.clicked.connect(self.ver_cheques)
         self.bm.ChequeS.clicked.connect(self.oculta_cheque)

#*******************************NOTIFICACIONES************************
    def contador(self):
       # self.bm.notify.setVisible(False)
        self.hoy=datetime.date.today()
        self.dia_delta=datetime.timedelta(days=2)
        self.q=self.hoy+self.dia_delta
        self.fecha=recipes.conteo(self.q)
        self.x=self.fecha[0]
        self.m=str(self.x)
        self.characters = "(',!?)"
        self.m = ''.join( x for x in self.m if x not in self.characters)
        self.entero=int(self.m)
        #print(self.m)
        if self.entero>0 and self.entero<=9:
            self.bm.notify.setVisible(True)
            self.bm.notify.setText("  "+self.m)
            #print(entero)
        elif self.entero>9:
            self.bm.notify.setVisible(True)
            self.bm.notify.setText("+9")
        elif self.hoy==None:
            print("error")
        else: 
            self.bm.notify.setVisible(False)