"""video 3"""
#componente que va mostrar la foto de la receta
from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QCursor
from PySide6.QtCore import Qt

class RecipeImg(QLabel):
    #cuando crea un objeto de la clase  va recibir la direccion de la imagen que queremos mostrar
    def __init__(self, img_path):
        super().__init__()  #super para llamar el constructor del padre
        #toma la dirección de la imagen que queremos mostrar
        self.img=QPixmap(img_path).scaledToWidth(200)  #scaledToWidth(200) es el tamaño de la imagen 
        self.setPixmap(self.img)  #muestra la imagen en el label
        
#Crea la nueva clase para el boton de palomita  
class Button(QPushButton):
    def __init__(self, icon):
        super().__init__()
        self.setMinimumSize(25, 25)
        self.set_cursor()
        self.setIcon(QIcon(f"iconos/icons/{icon}.png"))
        self.setStyleSheet(f"border-style: solid;")
        
    #cambie el efecto del boton cuando el cursor del rato pase por encima 
    def set_cursor(self):
        pointer=QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)
    