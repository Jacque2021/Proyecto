class Interfaz_Menu():
    def __init__(self, im):
        self.im=im #contiene el objeto de las ventanas
    def Open_pagosPrestamos(self):
        from controllers.busqueda_pago import buscueda_prestamo
        self.im.window=buscueda_prestamo(self)
        self.im.close()
        self.im.window.show()
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