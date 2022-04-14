from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.Ui_advertencia import Ui_VentanaEmergente

class Error(QWidget, Ui_VentanaEmergente):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.ui=GeneralCustomUi(self)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
    
