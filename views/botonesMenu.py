from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class Menu_Botones():
    def __init__(self, bm):
        self.bm=bm #contiene el objeto de las ventanas
        self.ocultar_boton() ##oculta todos los botones
        self.abracadabra() 
        
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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)

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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)
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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)
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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)
        ##  Metodo para abrir nueva interfaz
    def ver_ahorros(self):
        self.bm.Retirar.setVisible(True) #Visualisa los sub-botones
        self.bm.abonar_ahorro.setVisible(True)
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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
    
    def ver_consultas(self):
        self.bm.Estado.setVisible(True) #Visualisa los sub-botones
        self.bm.PLD.setVisible(True)
        self.bm.Reportes.setVisible(True)
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
        self.bm.abonar_ahorro.setVisible(False)
    
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
        self.bm.PLD.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)
        
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
        self.bm.PLD.setVisible(False)
        self.bm.Polizas.setVisible(False)
        self.bm.Reportes.setVisible(False)
        self.bm.Respaldo.setVisible(False)
        self.bm.Retirar.setVisible(False)
        self.bm.Ahorro.setVisible(False)
        self.bm.abonar_ahorro.setVisible(False)
    
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

#*******************************ABRIR INTERFACES************************
