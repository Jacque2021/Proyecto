from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect   #sombra de interfaz
#ESTE SOLO FUNCIONA PARA EL ASPECTO DE VENTANA Y USO DE BOTONES DE MAXIMIZAR, MINIMIZAR Y CERRAR
#ui tiene el objeto de todas las caracteristicas de la clase
#from vistas.Ui_add_edit_windows import AddEditWindows

#para el metodo fill_category_cb
category_data=(
    "Recetas Italianas",
    "Postres",
    "Bebidas"
)

opciones=(
    "Contables",
    "Fiscales"
)

codigos=(
    "CA=100, Activo",
    "CA=100.01, Activo a corto plazo",
    "Nivel=1, CA=101, Caja",
    "Nivel=2, CA=101.01, Caja y efectivo",
    "Nivel=1, CA=102, Bancos",
    "Nivel=2, CA=102.01, Bancos nacionales",
    "Nivel=2, CA=102.02, Bancos extranjeros",
    "Nivel=1, CA=102, Iversiones",
    "Nivel=2, CA=102, Inversiones temporales",
    "Nivel=2, CA=102, Inversiones en fideicomisos",
    "Nivel=2, CA=102, Otras inversiones",
    "Nivel=1, CA=105, Clientes",
    "Nivel=2, CA=105.01, Clientes nacionales",
    "Nivel=2, CA=105.02, Clientes extranjeros",
    "Nivel=2, CA=105.03, Clientes nacionales parte relacionada",
    "Nivel=2, CA=105.04, Clientes extranjeros parte relacionada",
    "Nivel=1, CA=107, Deudores diversos",
    "Nivel=2, CA=107.01, Funcionarios y empleados",
    "Nivel=2, CA=107.02, Socios y accionistas",
    "Nivel=2, CA=107.03, Partes relacionadas nacionales",
    "Nivel=2, CA=107.04, Partes relacionadas extranjeros",
    "Nivel=2, CA=107.05, Otros deudores diversos",
    "Nivel=2, CA=216.06, Impuestos retenidos de ISR por intereses",
    "Nivel=2, CA=216.07, Impuestos retenidos de ISR por pagos al extranjero",
    "Nivel=2, CA=216.08, Impuestos retenidos de ISR por venta de acciones",
    "Nivel=2, CA=216.09, Impuestos retenidos de ISR por venta de partes sociales",
    "Nivel=2, CA=216.10, Impuestos retenidos de IVA",
    "Nivel=2, CA=251.01, Socios, accionistas o representante legal",
    "Nivel=2, CA=251.02, Acreedores diversos a largo plazo nacional",
    "Nivel=2, CA=251.03, Acreedores diversos a largo plazo extranjero",
    "Nivel=2, CA=251.04, Acreedores diversos a largo plazo nacional parte relacionada",
    "Nivel=2, CA=251.05, Acreedores diversos a largo plazo extranjero parte relacionada",
    "Nivel=2, CA=251.06, Otros acreedores diversos a largo plazo",
    "Nivel=1, CA=403, Otros ingresos",
    "Nivel=1, CA=606, Facilidades administrativas fiscales",
    "Nivel=2, CA=611.01, Impuesto Sobre la renta",
    "Nivel=2, CA=611.02, Impuesto Sobre la renta por remanente distribuible",
    "CA=800, Cuentas en orden",
)


class GeneralCustomUi():
    def __init__(self, ui):
        self.ui=ui #contiene el objeto de las ventanas
        self.remove_defult_title_bar()
        self.miximize_window()
        self.ui.top_bar_frame.mouseMoveEvent = self.move_window #top_bar_frame= la barra principal azul
        self.set_window_shadow()
        self.set_title_bar_buttons_actions() #boton de maximizar y minimizar
        
    def remove_defult_title_bar(self):   #hacer el fondo transparente
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        #Quitar la barra de titulo
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        
    #ubicación global del mouse
    def mouse_press_event(self, event):
        self.drag_pos=event.globalPos()
    #drag_post = posicion de la ventana que esta siendo arrastrada
    
    def move_window(self, event):
        #cuando el boton se mueva dentro de la barra azul pero ejecutando el boton izquierdo, ejecuta lo que este en el lefstame
        if event.buttons()== Qt.LeftButton: #LeftButton=boton izquierdo
            #obtener posicion actual de la ventana
            #event.globalPos = posicion actaul del mouse cuando presione boton izquierdo
            self.ui.move(self.ui.pos() + event.globalPos()- self.drag_pos)
            self.drag_pos=event.globalPos()
            
    #efecto de ventana
    def set_window_shadow(self):
        shadow=QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)
        
 #Programar botones de la barra azul
        #maximizar ventana
    def miximize_window(self):
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False) #oculta boton maximizar
        self.ui.shadow_layout.setContentsMargins(0, 0, 0, 0) #elimina margenes 
        #minimiza ventana
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True) 
        self.ui.shadow_layout.setContentsMargins(10, 10, 10, 10)
        #une ambos metodos
        #configuración de botones de barra principal
    def set_title_bar_buttons_actions(self):
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)
        self.ui.maximize_button.clicked.connect(self.miximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)
        
    #objeto de la ventana de agregar, category_data fue creada arriba
    """ def fill_category_cb(self):
        self.ui.category_combo_box.addItems(category_data)"""
        
    def fiscal_contable(self):
        self.ui.elegir_c_f.addItems(opciones)

    def opciones_c(self):
        self.ui.codigo_SAT.addItems(codigos)
    
    