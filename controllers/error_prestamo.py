
from PySide6.QtWidgets import QWidget
from views.general_custom_ui import GeneralCustomUi
from views.Ui_error_prestamo import error_prestamo

class Error_p(QWidget, error_prestamo):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.parent=parent
        self.setupUi(self) #1
        self.ui=GeneralCustomUi(self)
        self.regresar_button.clicked.connect(self.close)
        
    def mousePressEvent(self, event): #ubicación mouse
        self.ui.mouse_press_event(event)
        
    