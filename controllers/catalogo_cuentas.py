from tkinter.messagebox import NO
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustomUi
from views.botonesMenu import Menu_Botones
from views.Ui_catalogo_cuentas import Ui_Catalogo_cuentas
from controllers.cuenta_a import CuentaForm
from controllers.error_prestamo import Error_p
from database import recipes


class CatalogoForm(QWidget, Ui_Catalogo_cuentas):
    def __init__(self, parent=None, RFC_e=None): #Capturar instancia en mainwindows    
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.RFC_e=RFC_e
        self.llamar_b()
        self.ui=GeneralCustomUi(self)
        self.bm=Menu_Botones(self)
        self.boton_guardar_1.clicked.connect(self.nuevo_catalogo_cuentas)
        self.boton_borrar.clicked.connect(self.clear_inputs)
        self.ui.fiscal_contable()
        self.ui.opciones_c()
    
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)

    def llamar_b(self):
        data = recipes.select_empresa(self.RFC_e)
        RFC_e=data[0] 
        RFC_e = str(RFC_e)
        nombre_b=data[1]
        nombre_b=str(nombre_b)
        self.clave_e.setText(RFC_e)
        self.nombre_b.setText(nombre_b)
        
    def nuevo_catalogo_cuentas(self):
        RFC_e = self.clave_e.text() 
        nombre_b = self.nombre_b.text()
        registro = self.registro.text()
        elegircf = self.elegir_c_f.currentText()
        codig_SAT = self.codigo_SAT.currentText()
        rubro = self.rubro.text()
        digito_fiscal_1 = self.digito_fiscal.text() 
        digito_fiscal_2 = self.digito_fis.text() 

        data = (RFC_e, nombre_b, registro, elegircf, codig_SAT, rubro, digito_fiscal_1, digito_fiscal_2)

        if recipes.insertar_catalogo_cuentas(data):
            print("Cuenta Agregada")
            self.clear_inputs()
            self.cuenta_agregada()
        else: 
            self.window=Error_p(self)
            self.window.show()
            print("Error al agregar cuenta")

    def clear_inputs(self):
        self.clave_e.clear()
        self.nombre_b.clear()
        self.registro.clear()
        self.rubro.clear()
        self.digito_fiscal.clear() 
        self.digito_fis.clear()

    def cuenta_agregada(self):
        window=CuentaForm(self)
        window.show()