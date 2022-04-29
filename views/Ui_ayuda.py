# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ayuda.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
from imagenes import res_rc

class Ayuda(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(1365, 686)
        DetailWindow.setMinimumSize(QSize(1365, 0))
        DetailWindow.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setMinimumSize(QSize(1365, 0))
        self.central_widget_frame.setStyleSheet(u"border-radius: 5px")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(5, 5, 5, 5)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setMinimumSize(QSize(1365, 0))
        self.background_frame.setStyleSheet(u"QWidgget#background_frame{background-color: rgb(245, 240, 225);}")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;\n"
"border-radius: 5px")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(1100, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(180, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(100, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./../pys6-recipes-organizer-master/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon)
        self.restore_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(140, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./../pys6-recipes-organizer-master/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(97, 0, 31, 22))
        icon2 = QIcon()
        icon2.addFile(u"./../pys6-recipes-organizer-master/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./../pys6-recipes-organizer-master/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(1365, 0))
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.barra_principal_frame = QFrame(self.content_frame)
        self.barra_principal_frame.setObjectName(u"barra_principal_frame")
        self.barra_principal_frame.setEnabled(True)
        self.barra_principal_frame.setMinimumSize(QSize(0, 40))
        self.barra_principal_frame.setMaximumSize(QSize(16777215, 40))
        self.barra_principal_frame.setStyleSheet(u"QWidget#barra_principal_frame{background-color: rgb(48, 127, 226);\n"
"border-radius: 5px}")
        self.barra_principal_frame.setFrameShape(QFrame.StyledPanel)
        self.barra_principal_frame.setFrameShadow(QFrame.Raised)
        self.Empresa = QPushButton(self.barra_principal_frame)
        self.Empresa.setObjectName(u"Empresa")
        self.Empresa.setGeometry(QRect(10, 10, 143, 31))
        self.Empresa.setFont(font)
        self.Empresa.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon4 = QIcon()
        icon4.addFile(u"./assets/Iconos/house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Empresa.setIcon(icon4)
        self.Empresa.setIconSize(QSize(40, 40))
        self.Clientes = QPushButton(self.barra_principal_frame)
        self.Clientes.setObjectName(u"Clientes")
        self.Clientes.setGeometry(QRect(150, 10, 143, 31))
        self.Clientes.setFont(font)
        self.Clientes.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon5 = QIcon()
        icon5.addFile(u"./assets/Iconos/60eb68bb3242ef4ac327a3fe28d25719.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Clientes.setIcon(icon5)
        self.Clientes.setIconSize(QSize(30, 30))
        self.Prestamos = QPushButton(self.barra_principal_frame)
        self.Prestamos.setObjectName(u"Prestamos")
        self.Prestamos.setGeometry(QRect(290, 10, 143, 31))
        self.Prestamos.setFont(font)
        self.Prestamos.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon6 = QIcon()
        icon6.addFile(u"./assets/Iconos/prestamos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Prestamos.setIcon(icon6)
        self.Prestamos.setIconSize(QSize(35, 35))
        self.Ahorros = QPushButton(self.barra_principal_frame)
        self.Ahorros.setObjectName(u"Ahorros")
        self.Ahorros.setGeometry(QRect(430, 10, 143, 31))
        self.Ahorros.setFont(font)
        self.Ahorros.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon7 = QIcon()
        icon7.addFile(u"./assets/Iconos/497f1ee33d47f13536a037095be32bde-icono-de-circulo-de-banco-de-cerdo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ahorros.setIcon(icon7)
        self.Ahorros.setIconSize(QSize(35, 30))
        self.Consultas = QPushButton(self.barra_principal_frame)
        self.Consultas.setObjectName(u"Consultas")
        self.Consultas.setGeometry(QRect(570, 10, 143, 31))
        self.Consultas.setFont(font)
        self.Consultas.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon8 = QIcon()
        icon8.addFile(u"./assets/Iconos/consultas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Consultas.setIcon(icon8)
        self.Consultas.setIconSize(QSize(40, 40))
        self.Ayuda = QPushButton(self.barra_principal_frame)
        self.Ayuda.setObjectName(u"Ayuda")
        self.Ayuda.setGeometry(QRect(1140, 10, 101, 31))
        self.Ayuda.setFont(font)
        self.Ayuda.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon9 = QIcon()
        icon9.addFile(u"./assets/Iconos/ayuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ayuda.setIcon(icon9)
        self.Ayuda.setIconSize(QSize(40, 40))
        self.Salir = QPushButton(self.barra_principal_frame)
        self.Salir.setObjectName(u"Salir")
        self.Salir.setGeometry(QRect(1240, 10, 101, 31))
        self.Salir.setFont(font)
        self.Salir.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon10 = QIcon()
        icon10.addFile(u"./assets/Iconos/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Salir.setIcon(icon10)
        self.Salir.setIconSize(QSize(30, 30))
        self.Notificaciones = QPushButton(self.barra_principal_frame)
        self.Notificaciones.setObjectName(u"Notificaciones")
        self.Notificaciones.setGeometry(QRect(1000, 10, 143, 31))
        self.Notificaciones.setFont(font)
        self.Notificaciones.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon11 = QIcon()
        icon11.addFile(u"./assets/Iconos/Imagen2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Notificaciones.setIcon(icon11)
        self.Notificaciones.setIconSize(QSize(25, 25))
        self.PolizaS = QPushButton(self.barra_principal_frame)
        self.PolizaS.setObjectName(u"PolizaS")
        self.PolizaS.setGeometry(QRect(712, 10, 151, 31))
        self.PolizaS.setFont(font)
        self.PolizaS.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon12 = QIcon()
        icon12.addFile(u"./assets/Iconos/polizas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PolizaS.setIcon(icon12)
        self.PolizaS.setIconSize(QSize(25, 25))
        self.ChequeS = QPushButton(self.barra_principal_frame)
        self.ChequeS.setObjectName(u"ChequeS")
        self.ChequeS.setGeometry(QRect(860, 10, 143, 31))
        self.ChequeS.setFont(font)
        self.ChequeS.setStyleSheet(u"border-style: solid;\n"
"background-color: rgb(48, 127, 226);\n"
"border-width: 1px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 1px;")
        icon13 = QIcon()
        icon13.addFile(u"./assets/Iconos/cheques.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ChequeS.setIcon(icon13)
        self.ChequeS.setIconSize(QSize(40, 40))
        self.notify = QLabel(self.barra_principal_frame)
        self.notify.setObjectName(u"notify")
        self.notify.setGeometry(QRect(1010, 20, 16, 16))
        self.notify.setStyleSheet(u"image: url(:/imagen/rojo.png);\n"
"")

        self.verticalLayout_3.addWidget(self.barra_principal_frame)

        self.contenido = QFrame(self.content_frame)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setMinimumSize(QSize(0, 500))
        self.contenido.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contenido.setFrameShape(QFrame.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contenido)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.contenido)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(241, 20, 750, 61))
        self.label_17.setMinimumSize(QSize(750, 0))
        self.label_17.setMaximumSize(QSize(1600, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1200, 10, 80, 80))
        self.label_10.setMinimumSize(QSize(80, 80))
        self.label_10.setPixmap(QPixmap(u":/imagen/logobueno_preview_rev_1.png"))
        self.Catalogo = QPushButton(self.frame)
        self.Catalogo.setObjectName(u"Catalogo")
        self.Catalogo.setGeometry(QRect(10, 60, 141, 31))
        self.Catalogo.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Respaldo = QPushButton(self.frame)
        self.Respaldo.setObjectName(u"Respaldo")
        self.Respaldo.setGeometry(QRect(10, 30, 141, 31))
        self.Respaldo.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Mi_Empresa = QPushButton(self.frame)
        self.Mi_Empresa.setObjectName(u"Mi_Empresa")
        self.Mi_Empresa.setGeometry(QRect(10, 0, 141, 31))
        self.Mi_Empresa.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.PLD = QPushButton(self.frame)
        self.PLD.setObjectName(u"PLD")
        self.PLD.setGeometry(QRect(570, 0, 141, 31))
        self.PLD.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Ahorro = QPushButton(self.frame)
        self.Ahorro.setObjectName(u"Ahorro")
        self.Ahorro.setGeometry(QRect(430, 0, 141, 31))
        self.Ahorro.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.abonar = QPushButton(self.frame)
        self.abonar.setObjectName(u"abonar")
        self.abonar.setGeometry(QRect(290, 30, 141, 31))
        self.abonar.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Reportes = QPushButton(self.frame)
        self.Reportes.setObjectName(u"Reportes")
        self.Reportes.setGeometry(QRect(570, 60, 141, 31))
        self.Reportes.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Polizas = QPushButton(self.frame)
        self.Polizas.setObjectName(u"Polizas")
        self.Polizas.setGeometry(QRect(710, 0, 151, 31))
        self.Polizas.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Historial = QPushButton(self.frame)
        self.Historial.setObjectName(u"Historial")
        self.Historial.setGeometry(QRect(150, 30, 141, 31))
        self.Historial.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Estado = QPushButton(self.frame)
        self.Estado.setObjectName(u"Estado")
        self.Estado.setGeometry(QRect(570, 30, 141, 31))
        self.Estado.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.cancelar = QPushButton(self.frame)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(290, 60, 141, 31))
        self.cancelar.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Cliente = QPushButton(self.frame)
        self.Cliente.setObjectName(u"Cliente")
        self.Cliente.setGeometry(QRect(150, 0, 141, 31))
        self.Cliente.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Retirar = QPushButton(self.frame)
        self.Retirar.setObjectName(u"Retirar")
        self.Retirar.setGeometry(QRect(430, 30, 141, 31))
        self.Retirar.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Cheques = QPushButton(self.frame)
        self.Cheques.setObjectName(u"Cheques")
        self.Cheques.setGeometry(QRect(860, 0, 141, 31))
        self.Cheques.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Consulta_cheque = QPushButton(self.frame)
        self.Consulta_cheque.setObjectName(u"Consulta_cheque")
        self.Consulta_cheque.setGeometry(QRect(860, 30, 141, 31))
        self.Consulta_cheque.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Listado = QPushButton(self.frame)
        self.Listado.setObjectName(u"Listado")
        self.Listado.setGeometry(QRect(710, 30, 151, 31))
        self.Listado.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.prestamo = QPushButton(self.frame)
        self.prestamo.setObjectName(u"prestamo")
        self.prestamo.setGeometry(QRect(290, 0, 141, 31))
        self.prestamo.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")

        self.verticalLayout_4.addWidget(self.frame)

        self.Desarrollo = QFrame(self.contenido)
        self.Desarrollo.setObjectName(u"Desarrollo")
        self.Desarrollo.setMinimumSize(QSize(0, 490))
        self.Desarrollo.setFrameShape(QFrame.StyledPanel)
        self.Desarrollo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Desarrollo)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.Desarrollo)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"selection-background-color: rgb(255, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1348, 5000))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 5000))
        self.frame_2.setStyleSheet(u"QWidget#frame_2{background-color: rgb(223, 223, 223);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, -10, 1411, 3000))
        self.frame_3.setMinimumSize(QSize(0, 3000))
        self.frame_3.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Titulo = QLabel(self.frame_3)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(20, 10, 111, 31))
        self.Titulo.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 1331, 31))
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 121, 31))
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 100, 1281, 81))
        self.Imagen1 = QLabel(self.frame_3)
        self.Imagen1.setObjectName(u"Imagen1")
        self.Imagen1.setGeometry(QRect(340, 180, 781, 171))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 430, 1291, 241))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 990, 1291, 91))
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 1300, 121, 41))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 1340, 1271, 161))
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 1500, 1251, 51))
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 1830, 1301, 131))
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 2250, 181, 31))
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 2290, 1301, 91))
        self.imagen1 = QLabel(self.frame_3)
        self.imagen1.setObjectName(u"imagen1")
        self.imagen1.setGeometry(QRect(360, 190, 701, 221))
        self.imagen1.setStyleSheet(u"")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 1080, 751, 261))
        self.label_13.setStyleSheet(u"image: url(:/imagen/prestamonuevo.png);")
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(430, 1570, 551, 241))
        self.label_14.setStyleSheet(u"image: url(:/imagen/abonar ahorro.png);")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(240, 2410, 871, 241))
        self.label_15.setStyleSheet(u"image: url(:/imagen/cancela.png);")
        self.imagen5 = QLabel(self.frame_3)
        self.imagen5.setObjectName(u"imagen5")
        self.imagen5.setGeometry(QRect(420, 1990, 641, 261))
        self.imagen2 = QLabel(self.frame_3)
        self.imagen2.setObjectName(u"imagen2")
        self.imagen2.setGeometry(QRect(470, 660, 691, 311))

        self.verticalLayout_6.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.Desarrollo)


        self.verticalLayout_3.addWidget(self.contenido)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText("")
        self.restore_button.setText("")
        self.close_button.setText("")
        self.maximize_button.setText("")
        self.minimize_button.setText("")
        self.Empresa.setText(QCoreApplication.translate("DetailWindow", u"Empresa", None))
        self.Clientes.setText(QCoreApplication.translate("DetailWindow", u"Clientes", None))
        self.Prestamos.setText(QCoreApplication.translate("DetailWindow", u"Pr\u00e9stamos", None))
        self.Ahorros.setText(QCoreApplication.translate("DetailWindow", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("DetailWindow", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("DetailWindow", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("DetailWindow", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("DetailWindow", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("DetailWindow", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("DetailWindow", u"Cheques", None))
        self.notify.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Ayuda</p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("DetailWindow", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("DetailWindow", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("DetailWindow", u"Mi empresa", None))
        self.PLD.setText(QCoreApplication.translate("DetailWindow", u"PLD", None))
        self.Ahorro.setText(QCoreApplication.translate("DetailWindow", u"Nuevo ahorro", None))
        self.abonar.setText(QCoreApplication.translate("DetailWindow", u"Abonar pago", None))
        self.Reportes.setText(QCoreApplication.translate("DetailWindow", u"Emitir reporte", None))
        self.Polizas.setText(QCoreApplication.translate("DetailWindow", u"Nueva poliza", None))
        self.Historial.setText(QCoreApplication.translate("DetailWindow", u"Historial del cliente", None))
        self.Estado.setText(QCoreApplication.translate("DetailWindow", u"Estado de cuentas", None))
        self.cancelar.setText(QCoreApplication.translate("DetailWindow", u"Cancelar pago", None))
        self.Cliente.setText(QCoreApplication.translate("DetailWindow", u"Agregar nuevo cliente", None))
        self.Retirar.setText(QCoreApplication.translate("DetailWindow", u"Retirar ahorro", None))
        self.Cheques.setText(QCoreApplication.translate("DetailWindow", u"Cheques", None))
        self.Consulta_cheque.setText(QCoreApplication.translate("DetailWindow", u"Consultar cheques", None))
        self.Listado.setText(QCoreApplication.translate("DetailWindow", u"Listado de polizas", None))
        self.prestamo.setText(QCoreApplication.translate("DetailWindow", u"Nuevo prestamo", None))
        self.Titulo.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Pr\u00e9stamos</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de pr\u00e9stamos cuenta con tres opciones las cuales son; nuevo pr\u00e9stamo, Abonar pago y Cancelar pago. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Nuevo pr\u00e9stamo:</span></p><p><span style=\" font-size:12pt; color:#307fe2;\"><br/></span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Como primera funci\u00f3n, el administrador deber\u00e1 buscar el nombre del cliente que solicita dicho pr\u00e9stamo en la tabla de clientes registrados. Para facilitar dicha b\u00fasqueda, se ingres\u00f3 un </span></p><p align=\"justify\"><span style=\" font-size:11pt;\">recuadro donde dice \u201cNombre del cliente\u201d, el cual el administrador puede escribir ya sea el nombre, apellidos o Id del cliente para dar con el cliente m\u00e1s r\u00e1pido. Una vez encontrado el nombre, </span></p><p align=\"justify\"><span style=\" font-size:11pt;\">el administrador deber\u00e1 dar doble click sobre la celda seleccionada del cliente. </span></p></body></html>", None))
        self.Imagen1.setText("")
        self.label_2.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Una vez seleccionado el nombre, se abrir\u00e1 una nueva ventana, en ella se muestra el nombre del cliente el cual hab\u00eda sido seleccionado en la tabla anterior. En la parte de arriba </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">de la tabla de datos del pr\u00e9stamo, se muestra un texto en azul el cual indica la cantidad m\u00e1xima permitida para ese cliente y de igual forma, el m\u00e1ximo de plazos a pagar dicho pr\u00e9stamo. </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Cabe mencionar que la cantidad de pr\u00e9stamo autorizada por cliente, se maneja a trav\u00e9s de la cantidad de puntos que tenga el cliente, el cual ira ganando conforme a su puntualidad </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">de pago de prestamos anteriores. Despu\u00e9s se muestra la tabla de datos del pr\u00e9stamo, en la que el administrador deber\u00e1 ingresar la cantidad del pr\u00e9stamo qu"
                        "e solicita el cliente el </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">cual no debe sobrepasar el limite permitido ya que por el contrari\u00f3 marcara un mensaje de error tal y como se muestra en la imagen; de igual forma el administrador deber\u00e1 ingresar </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">la tasa de inter\u00e9s anual con el que administran en la cooperativa correspondiente; se ingresa el tiempo en a\u00f1os, del cual tardara el cliente en liquidar el pr\u00e9stamo y de igualmente la </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">frecuencia con la que pagara. </span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Por \u00faltimo, se muestra la tabla de otros datos la cual tiene como par\u00e1metros que son el nombre el codeudor y la garant\u00eda del pr\u00e9stamo. Estos par\u00e1metros son opcionales para rellenar, ya </span></p><p><span style=\" font-size:12pt;\">que en algunos casos no se requiere de ingresar el nombre de un codeudor, eso lo tendr\u00e1 que valorar el administrador; la garant\u00eda del pr\u00e9stamo es solo hacer menci\u00f3n de que es lo que el </span></p><p><span style=\" font-size:12pt;\">cliente esta dejando como garant\u00eda en caso de no cumplir con sus obligaciones del pago del pr\u00e9stamo. </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Abonar pago:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de Abonar pr\u00e9stamo, se muestra una tabla en la que el administrador deber\u00e1 buscar al cliente que va realizar su pago de pr\u00e9stamo, una vez seleccionado, se abre </span></p><p><span style=\" font-size:12pt;\">una nueva ventana en la que se muestra el n\u00famero de cuenta, el nombre del cliente, la cantidad del pr\u00e9stamo que solicito el cliente, continuando con la informaci\u00f3n de pago del </span></p><p><span style=\" font-size:12pt;\">pr\u00e9stamo, que incluye el inter\u00e9s y el inter\u00e9s moratorio, este ultimo como se puede mostrar, esta en cero ya que el cliente est\u00e1 pagando en la fecha limite establecida, si este pagara con </span></p><p><span style=\" font-size:12pt;\">d\u00edas de retraso, el inter\u00e9s moratorio aumentar\u00eda, cabe se\u00f1alar que el inter\u00e9s moratorio esta establecido del 6% mensual, dicho esto, al ultimo se hace la suma del total que el cliente </span></p><p><spa"
                        "n style=\" font-size:12pt;\">deber\u00e1 pagar. </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Del lado derecho se muestra tres fechas, uno como bien lo dice es la fecha limite que tiene el cliente para dar su pago mensual, luego muestra la fecha del registro del pago y la fecha </span></p><p><span style=\" font-size:12pt;\">limite siguiente que se tiene para pagar el siguiente pago mensual, el cual cada uno tiene un rango de 30 d\u00edas. </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">Por \u00faltimo, se muestra dos botones, el primero que dice \u201cpagar con cuenta de ahorro\u201d, este bot\u00f3n solo ser\u00e1 visible si el cliente tiene una cuenta de ahorro registrada en el sistema y si su cuenta </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">de ahorro es mayor o igual al monto total a pagar por mes, de esta forma podr\u00e1 liberar su pago mensual y al mismo tiempo ser\u00e1 descontado la cantidad registrada en la cuenta de ahorro. El otro </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">bot\u00f3n que dice \u201cPagar\u201d es para pagar con efectivo el pr\u00e9stamo. Una vez abonado el pago con cualquiera de las dos opciones, se crear\u00e1 un documento en formato PDF el cual es considerado como </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">reporte de pago en caso de requerir de una aclar"
                        "aci\u00f3n de \u00e9l. </span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Cancelar pago:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Por \u00faltima opci\u00f3n dentro del men\u00fa de pr\u00e9stamos, tenemos \u201ccancelar pago\u201d, la cual consiste en borrar un pago de pr\u00e9stamo que por error fue realizado, solo bastara con dar click al </span></p><p><span style=\" font-size:12pt;\">icono de basura seg\u00fan la celda correspondiente del pago que desea cancelar. Se a\u00f1adi\u00f3 un apartado de b\u00fasqueda donde el administrador podr\u00e1 buscar al cliente del cual se realiz\u00f3 </span></p><p><span style=\" font-size:12pt;\">por error el pr\u00e9stamo ingresando el nombre o apellido. </span></p></body></html>", None))
        self.imagen1.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.imagen5.setText("")
        self.imagen2.setText("")
    # retranslateUi

