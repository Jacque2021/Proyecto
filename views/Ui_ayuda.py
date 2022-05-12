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

class Ayuda(object):
    def setupUi(self, Nuevoprestamo):
        if not Nuevoprestamo.objectName():
            Nuevoprestamo.setObjectName(u"Nuevoprestamo")
        Nuevoprestamo.resize(1400, 685)
        Nuevoprestamo.setMinimumSize(QSize(0, 0))
        Nuevoprestamo.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(Nuevoprestamo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(Nuevoprestamo)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setMinimumSize(QSize(1350, 0))
        self.central_widget_frame.setStyleSheet(u"border-radius: 5px")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(5, 5, 5, 5)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setMinimumSize(QSize(1350, 0))
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
        self.restore_button.setGeometry(QRect(80, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./../pys6-recipes-organizer-master/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon)
        self.restore_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(120, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./../pys6-recipes-organizer-master/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(77, 0, 31, 22))
        icon2 = QIcon()
        icon2.addFile(u"./../pys6-recipes-organizer-master/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(40, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./../pys6-recipes-organizer-master/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.barra_principal_frame = QFrame(self.content_frame)
        self.barra_principal_frame.setObjectName(u"barra_principal_frame")
        self.barra_principal_frame.setEnabled(True)
        self.barra_principal_frame.setMinimumSize(QSize(0, 20))
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
        self.notify.setStyleSheet(u"image: url(:/imagen/rojo.png);")

        self.verticalLayout_3.addWidget(self.barra_principal_frame)

        self.contenido = QFrame(self.content_frame)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contenido.setFrameShape(QFrame.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.contenido)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1000, 10, 251, 51))
        self.frame = QFrame(self.contenido)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1431, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.IngresaTitulo = QLabel(self.frame)
        self.IngresaTitulo.setObjectName(u"IngresaTitulo")
        self.IngresaTitulo.setGeometry(QRect(292, 20, 841, 61))
        self.IngresaTitulo.setMinimumSize(QSize(750, 0))
        self.IngresaTitulo.setMaximumSize(QSize(1600, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.IngresaTitulo.setFont(font1)
        self.IngresaTitulo.setStyleSheet(u"")
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
        self.Reportes.setGeometry(QRect(570, 30, 141, 31))
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
        self.Estado.setGeometry(QRect(570, 0, 141, 31))
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
        self.Reportes_2 = QPushButton(self.frame)
        self.Reportes_2.setObjectName(u"Reportes_2")
        self.Reportes_2.setGeometry(QRect(570, 60, 141, 41))
        self.Reportes_2.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);\n"
"border-radius: 1px;\n"
"")
        self.Desarrollo = QFrame(self.contenido)
        self.Desarrollo.setObjectName(u"Desarrollo")
        self.Desarrollo.setGeometry(QRect(0, 100, 1390, 3905))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1373, 15000))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 15000))
        self.frame_2.setStyleSheet(u"QWidget#frame_2{background-color: rgb(223, 223, 223);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 1360, 14151))
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
        self.label_5.setGeometry(QRect(30, 1320, 121, 41))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 1360, 1271, 161))
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 1520, 1251, 71))
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
        self.label_13.setGeometry(QRect(350, 1080, 741, 281))
        self.label_13.setStyleSheet(u"image: url(:/imagen/prestamonuevo.png);")
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(430, 1610, 551, 201))
        self.label_14.setStyleSheet(u"image: url(:/imagen/abonar ahorro.png);")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(240, 2410, 871, 311))
        self.label_15.setStyleSheet(u"image: url(:/imagen/cancela.png);")
        self.imagen5 = QLabel(self.frame_3)
        self.imagen5.setObjectName(u"imagen5")
        self.imagen5.setGeometry(QRect(420, 1990, 641, 261))
        self.imagen2 = QLabel(self.frame_3)
        self.imagen2.setObjectName(u"imagen2")
        self.imagen2.setGeometry(QRect(470, 660, 691, 311))
        self.Titulo_2 = QLabel(self.frame_3)
        self.Titulo_2.setObjectName(u"Titulo_2")
        self.Titulo_2.setGeometry(QRect(0, 2700, 111, 31))
        self.Titulo_2.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 2740, 1331, 31))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 2770, 121, 31))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 2800, 1271, 191))
        self.imagen6 = QLabel(self.frame_3)
        self.imagen6.setObjectName(u"imagen6")
        self.imagen6.setGeometry(QRect(390, 3040, 641, 261))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 3320, 151, 31))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 3350, 1271, 181))
        self.imagen7 = QLabel(self.frame_3)
        self.imagen7.setObjectName(u"imagen7")
        self.imagen7.setGeometry(QRect(300, 3530, 701, 311))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 3850, 151, 31))
        self.Titulo_3 = QLabel(self.frame_3)
        self.Titulo_3.setObjectName(u"Titulo_3")
        self.Titulo_3.setGeometry(QRect(0, 4510, 111, 31))
        self.Titulo_3.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 4540, 1331, 31))
        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 4570, 151, 31))
        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 4600, 1271, 311))
        self.imagen8 = QLabel(self.frame_3)
        self.imagen8.setObjectName(u"imagen8")
        self.imagen8.setGeometry(QRect(220, 4910, 1081, 331))
        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(20, 5240, 151, 31))
        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 5270, 1271, 301))
        self.imagen9 = QLabel(self.frame_3)
        self.imagen9.setObjectName(u"imagen9")
        self.imagen9.setGeometry(QRect(270, 5570, 841, 301))
        self.Titulo_7 = QLabel(self.frame_3)
        self.Titulo_7.setObjectName(u"Titulo_7")
        self.Titulo_7.setGeometry(QRect(0, 5880, 111, 31))
        self.Titulo_7.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_49 = QLabel(self.frame_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 5910, 1331, 31))
        self.label_50 = QLabel(self.frame_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 5940, 151, 31))
        self.label_51 = QLabel(self.frame_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, 5970, 1271, 241))
        self.imagen10 = QLabel(self.frame_3)
        self.imagen10.setObjectName(u"imagen10")
        self.imagen10.setGeometry(QRect(340, 6220, 751, 321))
        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(20, 6560, 151, 31))
        self.label_53 = QLabel(self.frame_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(20, 6580, 1271, 171))
        self.imagen10_2 = QLabel(self.frame_3)
        self.imagen10_2.setObjectName(u"imagen10_2")
        self.imagen10_2.setGeometry(QRect(110, 6770, 1181, 261))
        self.label_54 = QLabel(self.frame_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(20, 7080, 1331, 31))
        self.label_55 = QLabel(self.frame_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(20, 7110, 151, 31))
        self.Titulo_8 = QLabel(self.frame_3)
        self.Titulo_8.setObjectName(u"Titulo_8")
        self.Titulo_8.setGeometry(QRect(0, 7050, 111, 31))
        self.Titulo_8.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_56 = QLabel(self.frame_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(20, 7140, 1351, 481))
        self.imagen_c1 = QLabel(self.frame_3)
        self.imagen_c1.setObjectName(u"imagen_c1")
        self.imagen_c1.setGeometry(QRect(140, 7640, 1181, 261))
        self.label_57 = QLabel(self.frame_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 7950, 1351, 191))
        self.label_58 = QLabel(self.frame_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 7920, 151, 31))
        self.imagen_c2 = QLabel(self.frame_3)
        self.imagen_c2.setObjectName(u"imagen_c2")
        self.imagen_c2.setGeometry(QRect(90, 8150, 1181, 241))
        self.label_59 = QLabel(self.frame_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(30, 3880, 1301, 311))
        self.imagen_ca1 = QLabel(self.frame_3)
        self.imagen_ca1.setObjectName(u"imagen_ca1")
        self.imagen_ca1.setGeometry(QRect(260, 4200, 981, 221))
        self.label_61 = QLabel(self.frame_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(20, 8480, 151, 31))
        self.label_62 = QLabel(self.frame_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(20, 8450, 1331, 31))
        self.Titulo_9 = QLabel(self.frame_3)
        self.Titulo_9.setObjectName(u"Titulo_9")
        self.Titulo_9.setGeometry(QRect(0, 8420, 111, 31))
        self.Titulo_9.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_63 = QLabel(self.frame_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(30, 9380, 151, 31))
        self.label_64 = QLabel(self.frame_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(30, 9410, 1351, 251))
        self.imagen_lp = QLabel(self.frame_3)
        self.imagen_lp.setObjectName(u"imagen_lp")
        self.imagen_lp.setGeometry(QRect(220, 9680, 1181, 261))
        self.Titulo_10 = QLabel(self.frame_3)
        self.Titulo_10.setObjectName(u"Titulo_10")
        self.Titulo_10.setGeometry(QRect(20, 9970, 111, 31))
        self.Titulo_10.setStyleSheet(u"\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_65 = QLabel(self.frame_3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(20, 10000, 1331, 51))
        self.label_66 = QLabel(self.frame_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(20, 10080, 151, 31))
        self.label_67 = QLabel(self.frame_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(20, 10110, 1351, 191))
        self.imagen_ec = QLabel(self.frame_3)
        self.imagen_ec.setObjectName(u"imagen_ec")
        self.imagen_ec.setGeometry(QRect(120, 10320, 1181, 261))
        self.label_68 = QLabel(self.frame_3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(20, 10590, 191, 31))
        self.label_69 = QLabel(self.frame_3)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(20, 10620, 1351, 161))
        self.imagen_ra = QLabel(self.frame_3)
        self.imagen_ra.setObjectName(u"imagen_ra")
        self.imagen_ra.setGeometry(QRect(100, 10850, 1181, 261))
        self.label_70 = QLabel(self.frame_3)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(30, 11170, 1351, 71))
        self.imagen_ra_avi = QLabel(self.frame_3)
        self.imagen_ra_avi.setObjectName(u"imagen_ra_avi")
        self.imagen_ra_avi.setGeometry(QRect(80, 11260, 1181, 261))
        self.label_71 = QLabel(self.frame_3)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(30, 11610, 1351, 61))
        self.imagen_ra_PDF = QLabel(self.frame_3)
        self.imagen_ra_PDF.setObjectName(u"imagen_ra_PDF")
        self.imagen_ra_PDF.setGeometry(QRect(50, 11710, 1181, 261))
        self.label_72 = QLabel(self.frame_3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(30, 12030, 211, 31))
        self.label_73 = QLabel(self.frame_3)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(30, 12070, 1351, 161))
        self.imagen_rp = QLabel(self.frame_3)
        self.imagen_rp.setObjectName(u"imagen_rp")
        self.imagen_rp.setGeometry(QRect(100, 12270, 1181, 261))
        self.label_74 = QLabel(self.frame_3)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(30, 12600, 1351, 71))
        self.imagen_rp_avi = QLabel(self.frame_3)
        self.imagen_rp_avi.setObjectName(u"imagen_rp_avi")
        self.imagen_rp_avi.setGeometry(QRect(90, 12700, 1181, 261))
        self.label_75 = QLabel(self.frame_3)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(20, 13010, 1351, 61))
        self.imagen_rp_PDF = QLabel(self.frame_3)
        self.imagen_rp_PDF.setObjectName(u"imagen_rp_PDF")
        self.imagen_rp_PDF.setGeometry(QRect(100, 13130, 1181, 261))
        self.label_76 = QLabel(self.frame_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(30, 8520, 1351, 281))
        self.imagen_np = QLabel(self.frame_3)
        self.imagen_np.setObjectName(u"imagen_np")
        self.imagen_np.setGeometry(QRect(80, 8900, 1181, 261))

        self.verticalLayout_6.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.contenido)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(Nuevoprestamo)

        QMetaObject.connectSlotsByName(Nuevoprestamo)
    # setupUi

    def retranslateUi(self, Nuevoprestamo):
        Nuevoprestamo.setWindowTitle(QCoreApplication.translate("Nuevoprestamo", u"Form", None))
        self.title_label.setText("")
        self.restore_button.setText("")
        self.close_button.setText("")
        self.maximize_button.setText("")
        self.minimize_button.setText("")
        self.Empresa.setText(QCoreApplication.translate("Nuevoprestamo", u"Empresa", None))
        self.Clientes.setText(QCoreApplication.translate("Nuevoprestamo", u"Clientes", None))
        self.Prestamos.setText(QCoreApplication.translate("Nuevoprestamo", u"Prestamos", None))
        self.Ahorros.setText(QCoreApplication.translate("Nuevoprestamo", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("Nuevoprestamo", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("Nuevoprestamo", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("Nuevoprestamo", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("Nuevoprestamo", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("Nuevoprestamo", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("Nuevoprestamo", u"Cheques", None))
        self.notify.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_18.setText("")
        self.IngresaTitulo.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\">Ayuda</p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("Nuevoprestamo", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("Nuevoprestamo", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("Nuevoprestamo", u"Mi empresa", None))
        self.Ahorro.setText(QCoreApplication.translate("Nuevoprestamo", u"Nuevo ahorro", None))
        self.abonar.setText(QCoreApplication.translate("Nuevoprestamo", u"Abonar pago", None))
        self.Reportes.setText(QCoreApplication.translate("Nuevoprestamo", u"Emitir reporte", None))
        self.Polizas.setText(QCoreApplication.translate("Nuevoprestamo", u"Nueva poliza", None))
        self.Historial.setText(QCoreApplication.translate("Nuevoprestamo", u"Historial del cliente", None))
        self.Estado.setText(QCoreApplication.translate("Nuevoprestamo", u"Estado de cuentas", None))
        self.cancelar.setText(QCoreApplication.translate("Nuevoprestamo", u"Cancelar pago", None))
        self.Cliente.setText(QCoreApplication.translate("Nuevoprestamo", u"Agregar nuevo cliente", None))
        self.Retirar.setText(QCoreApplication.translate("Nuevoprestamo", u"Retirar ahorro", None))
        self.Cheques.setText(QCoreApplication.translate("Nuevoprestamo", u"Cheques", None))
        self.Consulta_cheque.setText(QCoreApplication.translate("Nuevoprestamo", u"Consultar cheques", None))
        self.Listado.setText(QCoreApplication.translate("Nuevoprestamo", u"Listado de polizas", None))
        self.prestamo.setText(QCoreApplication.translate("Nuevoprestamo", u"Nuevo prestamo", None))
        self.Reportes_2.setText(QCoreApplication.translate("Nuevoprestamo", u"Emitir reporte \n"
"de prestamos", None))
        self.Titulo.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Pr\u00e9stamos</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de pr\u00e9stamos cuenta con tres opciones las cuales son; nuevo pr\u00e9stamo, Abonar pago y Cancelar pago. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Nuevo pr\u00e9stamo:</span></p><p><span style=\" font-size:12pt; color:#307fe2;\"><br/></span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Como primera funci\u00f3n, el administrador deber\u00e1 buscar el nombre del cliente que solicita dicho pr\u00e9stamo en la tabla de clientes registrados. Para facilitar dicha b\u00fasqueda, se ingres\u00f3 un </span></p><p align=\"justify\"><span style=\" font-size:11pt;\">recuadro donde dice \u201cNombre del cliente\u201d, el cual el administrador puede escribir ya sea el nombre, apellidos o Id del cliente para dar con el cliente m\u00e1s r\u00e1pido. Una vez encontrado el nombre, </span></p><p align=\"justify\"><span style=\" font-size:11pt;\">el administrador deber\u00e1 dar doble click sobre la celda seleccionada del cliente. </span></p></body></html>", None))
        self.Imagen1.setText("")
        self.label_2.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Una vez seleccionado el nombre, se abrir\u00e1 una nueva ventana, en ella se muestra el nombre del cliente el cual hab\u00eda sido seleccionado en la tabla anterior. En la parte de arriba </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">de la tabla de datos del pr\u00e9stamo, se muestra un texto en azul el cual indica la cantidad m\u00e1xima permitida para ese cliente y de igual forma, el m\u00e1ximo de plazos a pagar dicho pr\u00e9stamo. </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Cabe mencionar que la cantidad de pr\u00e9stamo autorizada por cliente, se maneja a trav\u00e9s de la cantidad de puntos que tenga el cliente, el cual ira ganando conforme a su puntualidad </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">de pago de prestamos anteriores. Despu\u00e9s se muestra la tabla de datos del pr\u00e9stamo, en la que el administrador deber\u00e1 ingresar la cantidad del pr\u00e9stamo qu"
                        "e solicita el cliente el </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">cual no debe sobrepasar el limite permitido ya que por el contrari\u00f3 marcara un mensaje de error tal y como se muestra en la imagen; de igual forma el administrador deber\u00e1 ingresar </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">la tasa de inter\u00e9s anual con el que administran en la cooperativa correspondiente; se ingresa el tiempo en a\u00f1os, del cual tardara el cliente en liquidar el pr\u00e9stamo y de igualmente la </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">frecuencia con la que pagara. </span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Por \u00faltimo, se muestra la tabla de otros datos la cual tiene como par\u00e1metros que son el nombre el codeudor y la garant\u00eda del pr\u00e9stamo. Estos par\u00e1metros son opcionales para rellenar, ya </span></p><p><span style=\" font-size:12pt;\">que en algunos casos no se requiere de ingresar el nombre de un codeudor, eso lo tendr\u00e1 que valorar el administrador; la garant\u00eda del pr\u00e9stamo es solo hacer menci\u00f3n de que es lo que el </span></p><p><span style=\" font-size:12pt;\">cliente esta dejando como garant\u00eda en caso de no cumplir con sus obligaciones del pago del pr\u00e9stamo. </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Abonar pago:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de Abonar pr\u00e9stamo, se muestra una tabla en la que el administrador deber\u00e1 buscar al cliente que va realizar su pago de pr\u00e9stamo, una vez seleccionado, se abre </span></p><p><span style=\" font-size:12pt;\">una nueva ventana en la que se muestra el n\u00famero de cuenta, el nombre del cliente, la cantidad del pr\u00e9stamo que solicito el cliente, continuando con la informaci\u00f3n de pago del </span></p><p><span style=\" font-size:12pt;\">pr\u00e9stamo, que incluye el inter\u00e9s y el inter\u00e9s moratorio, este ultimo como se puede mostrar, esta en cero ya que el cliente est\u00e1 pagando en la fecha limite establecida, si este pagara con </span></p><p><span style=\" font-size:12pt;\">d\u00edas de retraso, el inter\u00e9s moratorio aumentar\u00eda, cabe se\u00f1alar que el inter\u00e9s moratorio esta establecido del 6% mensual, dicho esto, al ultimo se hace la suma del total que el cliente </span></p><p><spa"
                        "n style=\" font-size:12pt;\">deber\u00e1 pagar. </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Del lado derecho se muestra tres fechas, uno como bien lo dice es la fecha limite que tiene el cliente para dar su pago mensual, luego muestra la fecha del registro del pago y la fecha </span></p><p><span style=\" font-size:12pt;\">limite siguiente que se tiene para pagar el siguiente pago mensual, el cual cada uno tiene un rango de 30 d\u00edas. </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">Por \u00faltimo, se muestra dos botones, el primero que dice \u201cpagar con cuenta de ahorro\u201d, este bot\u00f3n solo ser\u00e1 visible si el cliente tiene una cuenta de ahorro registrada en el sistema y si su cuenta </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">de ahorro es mayor o igual al monto total a pagar por mes, de esta forma podr\u00e1 liberar su pago mensual y al mismo tiempo ser\u00e1 descontado la cantidad registrada en la cuenta de ahorro. El otro </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">bot\u00f3n que dice \u201cPagar\u201d es para pagar con efectivo el pr\u00e9stamo. Una vez abonado el pago con cualquiera de las dos opciones, se crear\u00e1 un documento en formato PDF el cual es considerado como </span></p><p><span style=\" font-family:'Calibri','sans-serif'; font-size:12pt;\">reporte de pago en caso de requerir de una aclar"
                        "aci\u00f3n de \u00e9l. </span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Cancelar pago:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Por \u00faltima opci\u00f3n dentro del men\u00fa de pr\u00e9stamos, tenemos \u201ccancelar pago\u201d, la cual consiste en borrar un pago de pr\u00e9stamo que por error fue realizado, solo bastara con dar click al </span></p><p><span style=\" font-size:12pt;\">icono de basura seg\u00fan la celda correspondiente del pago que desea cancelar. Se a\u00f1adi\u00f3 un apartado de b\u00fasqueda donde el administrador podr\u00e1 buscar al cliente del cual se realiz\u00f3 </span></p><p><span style=\" font-size:12pt;\">por error el pr\u00e9stamo ingresando el nombre o apellido. </span></p></body></html>", None))
        self.imagen1.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.imagen5.setText("")
        self.imagen2.setText("")
        self.Titulo_2.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Empresa</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de empresa cuenta con tres opciones las cuales son; mi empresa, respaldar empresa y catalogo de cuentas. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Mi empresa:</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de mi empresa, se muestra la interfaz, en donde se llenan los datos de la que se quiera registrar, como lo es: Nombre.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">En la secci\u00f3n de datos generales se encuentra: RFC y la ubicaci\u00f3n de la empresa.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">En inicio de historia: se encuentra la fecha del inicio del ejercicio, el cual se llena por default con la fecha del dia y el fin del ejercicio.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">En datos generales del servidor: se agrega el usuario, la contrase\u00f1a, el host y el nombre de la base de datos, lo cual es para hacer la conexi\u00f3n de la misma.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Por ultimo se tiene la secci\u00f3n de periodos contables: en donde se agrega el tipo de periodo.</span></p><p align=\"justify\"><span style=\" "
                        "font-size:12pt;\">Una vez que se han llenado los datos se hace el registro de la empresa una vez que se da clic en el bot\u00f3n de guardar.</span></p></body></html>", None))
        self.imagen6.setText("")
        self.label_21.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Respaldar empresa:</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de respaldar empresa, se muestra la interfaz, en donde se llenan los datos para hacer el respaldo de la misma.</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">En la secci\u00f3n de nuevo respaldo se encuentran los datos del respaldo como lo son:</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">RFC, nombre de la empresa, ruta y respaldo. </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">La fecha y hora de respaldo se muestran por default, siendo las del dia. </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Una vez que se han llenado los datos se hace el respaldo, una vez que se da clic en el bot\u00f3n de guardar.</span></p></body></html>", None))
        self.imagen7.setText("")
        self.label_23.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Cat\u00e1logo de cuentas:</span></p></body></html>", None))
        self.Titulo_3.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Ahorros</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de ahorros cuenta con dos opciones las cuales son; nuevo ahorro y retirar ahorro. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Nuevo ahorro: </span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de nuevo ahorro, se muestra una tabla en la que el administrador deber\u00e1 buscar al cliente que va realizar su ahorro, una vez seleccionado,</span></p><p><span style=\" font-size:12pt;\">se abre una nueva ventana en donde ya se ven reflejados los datos del cliente se se selecciono anteriormente, seguido de los datos del ahorro, en donde se tiene:</span></p><p><span style=\" font-size:12pt;\">Id de ahorro: este debe ser \u00fanico e irrepetible.</span></p><p><span style=\" font-size:12pt;\">Importe: se ingresa la cantidad para ahorrar.</span></p><p><span style=\" font-size:12pt;\">TEA: es la tasa efectiva anual, y se ingresa por medio de porcentaje.</span></p><p><span style=\" font-size:12pt;\">Capital: Cantidad que se tiene como capital.</span></p><p><span style=\" font-size:12pt;\">La fecha de inicio y fecha de apertura estan definidas por default al dia actual en que se hace el ahorro.</span></p><p><span style=\" font-size"
                        ":12pt;\">La fecha de venciemiento debe ser ingresada por el usuario, esta a plazo de 360 dias como ya esta establecido. </span></p><p><span style=\" font-size:12pt;\">Una vez que se han llenado los campos se da clic en el bot\u00f3n de guardar, y se calcula automaticamente el inter\u00e9s y la cancelaci\u00f3n.</span></p><p><span style=\" font-size:12pt;\">En la parte derecha hay una tabla la cu\u00e1l refleja cual seria el inter\u00e9s por dia, por los 360 y asi se muestra el total del interes que salen el letras rojas.</span></p></body></html>", None))
        self.imagen8.setText("")
        self.label_47.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Retirar ahorro: </span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de retirar ahorro, se muestra una tabla en la que el administrador deber\u00e1 buscar al cliente que va realizar su retiro, una vez seleccionado,</span></p><p><span style=\" font-size:12pt;\">se abre una nueva ventana en donde ya se ven reflejados los datos del cliente se se selecciono anteriormente, seguido de los datos del ahorro, en donde se tiene:</span></p><p><span style=\" font-size:12pt;\">Transacci\u00f3n no.: este debe ser \u00fanico e irrepetible.</span></p><p><span style=\" font-size:12pt;\">Capital ahorrado</span></p><p><span style=\" font-size:12pt;\">Total de retiro: cantidad a retirar, la cual se establece que logicamnete no tiene que ser mayor al capital ahorrado, asi como tampoco debe ser mayor a 5,000 pesos </span></p><p><span style=\" font-size:12pt;\">porque si llega a suceder el caso se deber\u00e1 realizar un cheque.</span></p><p><span style=\" font-size:12pt;\">La fecha y hora de retiro estan definidas po"
                        "r default al dia actual en que se hace el ahorro.</span></p><p><span style=\" font-size:12pt;\">Descripci\u00f3n: referente al retiro.</span></p><p><span style=\" font-size:12pt;\">Una vez que se han llenado los campos se da clic en el bot\u00f3n de retirar, en ese momento se genera un pdf con los datos correspondientes para poder realizar el retiro de dinero.</span></p></body></html>", None))
        self.imagen9.setText("")
        self.Titulo_7.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cheques</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de cheques cuenta con dos opciones las cuales son; cheques y consultar cheques. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Cheques:</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de cheque, se muestra una tabla en la que el administrador deber\u00e1 buscar al cliente que va realizar su cheque, una vez seleccionado,</span></p><p><span style=\" font-size:12pt;\">se abre una nueva ventana en donde ya se ven reflejados los datos del cliente se se selecciono anteriormente, seguido de los datos del cliente, en donde se tiene:</span></p><p><span style=\" font-size:12pt;\">Id del cheque: este debe ser \u00fanico e irrepetible.</span></p><p><span style=\" font-size:12pt;\">Beneficiario del cliente: Persona que es acreedor del cheque.</span></p><p><span style=\" font-size:12pt;\">Monto total: Cantidad generada para el cheque.</span></p><p><span style=\" font-size:12pt;\">Descripci\u00f3n.</span></p><p><span style=\" font-size:12pt;\">La fecha de emisi\u00f3n esta definida por default al dia actual en que se hace el cheque.</span></p><p><span style=\" font-size:12pt;\">Una vez que se han llenado los campos se da c"
                        "lic en el bot\u00f3n de emitir, y se genera un pdf para que pueda ser cobrado el cheque.</span></p></body></html>", None))
        self.imagen10.setText("")
        self.label_52.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Consulta cheques:</span></p><p><br/></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de consulta cheques, se muestra la interfaz, en donde se muestra la tabla con los cheques generados, los cuales se buscan por el nombre del cliente, </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">esto para que sean identificados f\u00e1cilmente.  </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Que tiene datos importantes como lo son: </span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Id, nombre, apellidos, id del cheque, fecha de emisi\u00f3n, monto total, beneficiario, descripci\u00f3n.</span><br/></p><p align=\"justify\"><br/></p></body></html>", None))
        self.imagen10_2.setText("")
        self.label_54.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de clientes cuenta con dos opciones las cuales son; agregar cliente e historial de clientes. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Agregar cliente:</span></p></body></html>", None))
        self.Titulo_8.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\">Clientes</p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de agregar cliente, se muestran los campos en los cu\u00e1les se puede visualizar los campos en donde se pondr\u00e1n los datos del cliente que se va a registrar. Los datos a registrar son los siguientes:</span></p><p><span style=\" font-size:12pt;\">ID del cliente: Este debe ser \u00fanico e irrepetible en cada cliente.</span></p><p><span style=\" font-size:12pt;\">Nombre: Nombre del cliente.</span></p><p><span style=\" font-size:12pt;\">T\u00e9lefono: T\u00e9lefono del cliente.</span></p><p><span style=\" font-size:12pt;\">Apellidos: Apellidos del cliente.</span></p><p><span style=\" font-size:12pt;\">Direcci\u00f3n: Direcci\u00f3n del cliente.</span></p><p><span style=\" font-size:12pt;\">T\u00e9lefono adicional: T\u00e9lefono adicional del cliente puede ser de alg\u00fan familiar.</span></p><p><span style=\" font-size:12pt;\">Correo electr\u00f3nico: Correo electr\u00f3nico del cliente.</span></p><p><span style=\" font-size"
                        ":12pt;\">Fecha de nacimiento: Fecha en que el cliente naci\u00f3.</span></p><p><span style=\" font-size:12pt;\">Puntuaci\u00f3n: La puntuaci\u00f3n del cliente al inicio puede ser de 0 ya que no ha realizado pr\u00e9stamos o ahorros.</span></p><p><span style=\" font-size:12pt;\">Municipio: El municipio donde vive el cliente este debe ser el mismo que el de la sociedad cooperativa.</span></p><p><span style=\" font-size:12pt;\">En la parte de abajo hay otras dos opciones con el bot\u00f3n Guardar guardara dicha informaci\u00f3n colocada.</span></p><p><span style=\" font-size:12pt;\">Con el bot\u00f3n Buscar abrira una tabla en la cu\u00e1l se muestra los clientes registrados hasta la fecha, esta tabla contiene dos iconos uno para eliminar y el otro para eliminar en el cu\u00e1l abre, </span></p><p><span style=\" font-size:12pt;\">otra ventana llamada Actualizar cliente esta ventana muestra los campos llenados con la informaci\u00f3n seleccionada anteriormente,</span></p><p><span style=\" font-size:12pt;\">contie"
                        "ne los mismos campos descritos anteriormente, en la parte de abajo contiene el bot\u00f3n actualizar con el cu\u00e1l se actualizara la informaci\u00f3n de dicho cliente seleccionado.</span></p></body></html>", None))
        self.imagen_c1.setText("")
        self.label_57.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n del historial del cliente se muestra 3 campos y 3 botones de buscar, los campos que se muestran son:</span></p><p><span style=\" font-size:12pt;\">Buscar por nombre del cliente: Aqu\u00ed se inserta el nombre del cliente, despu\u00e9s se da clic en el boton de Buscar que se encuentra a su izquierda, para buscar por el nombre.</span></p><p><span style=\" font-size:12pt;\">Buscar por apellidos del cliente: Aqu\u00ed se insertas los apellidos del cliente, despu\u00e9s se da clic en el boton de Buscar que se encuentra a su izquierda, para buscar por el apellidos.</span></p><p><span style=\" font-size:12pt;\">Buscar ID del cliente: Aqu\u00ed se inserta el ID del cliente, despu\u00e9s se da clic en el boton de Buscar que se encuentra a su izquierda, para buscar por el ID.</span></p><p><span style=\" font-size:12pt;\">En la parte de abajo se encuentra un bot\u00f3n de Imprimir, en el cu\u00e1l imprime dicha tabla que arrojo al buscar "
                        "por cualquier campo y hay otros botones de historial del cliente por ahorros o </span></p><p><span style=\" font-size:12pt;\">por pr\u00e9stamos en caso de que el cliente no cuente con un pr\u00e9stamo o un ahorro.</span></p><p><br/></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Historial del cliente:</span></p></body></html>", None))
        self.imagen_c2.setText("")
        self.label_59.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al seleccionar el bot\u00f3n de Cat\u00e1logo de cuentas, se muestra una tabla en la que el administrador deber\u00e1 buscar a la empresa que va realizar su registro del c\u00e1talogo, una vez seleccionado,</span></p><p><span style=\" font-size:12pt;\">se abre una nueva ventana en donde ya se ven reflejados los datos del cliente se se selecciono anteriormente, seguido de los datos de la empresa, en donde se tiene:</span></p><p><span style=\" font-size:12pt;\">Registro: La fecha en que se va a registrar la cuenta.</span></p><p><span style=\" font-size:12pt;\">Cuenta: La cuenta debe ser unica e irrepetible.</span></p><p><span style=\" font-size:12pt;\">Contables y fiscales: Aqu\u00ed elige si es una cuenta fiscal o contable.</span></p><p><span style=\" font-size:12pt;\">C\u00f3digo agrupador de cuentas del SAT: Aqu\u00ed el usuario elige el c\u00f3digo del SAT que necesite para la cuenta.</span></p><p><span style=\" font-size:12pt;\">Rubro: Aqu\u00ed coloca "
                        "el rubro asociado a esa cuenta.</span></p><p><span style=\" font-size:12pt;\">D\u00edgito fiscal 1: Coloca el n\u00famero fiscal 1.</span></p><p><span style=\" font-size:12pt;\">D\u00edgito fiscal 2: Coloca el n\u00famero fiscal 2.</span></p></body></html>", None))
        self.imagen_ca1.setText("")
        self.label_61.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Nueva Poliza:</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de polizas cuenta con dos opciones las cuales son; Nueva poliza y Listado polizas. A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.Titulo_9.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\">Polizas</p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Listado polizas:</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al presionar el bot\u00f3n Listado de polizas se abre una interfaz en la cu\u00e1l se muestra lo siguiente:</span></p><p><span style=\" font-size:12pt;\">Buscar por n\u00famero: Se ingresa el n\u00famero de la poliza, y se presiona el bot\u00f3n de buscar para que muestre los datos relacionados con el n\u00famero de la poliza.</span></p><p><span style=\" font-size:12pt;\">En la parte izaquierda se muestra un bot\u00f3n de diarios y polizas, en el cu\u00e1l abre una peque\u00f1a interfaz donde muestra:</span></p><p><span style=\" font-size:12pt;\">Buscar por n\u00famero inicial: Se coloca el n\u00famero inicial de la poliza.</span></p><p><span style=\" font-size:12pt;\">Buscar por n\u00famero final: Se coloca el n\u00famero final de la poliza.</span></p><p><span style=\" font-size:12pt;\">Se presiona el bot\u00f3n de Buscar esta busqueda se hace por un rango con el n\u00famero inicial y final que se colocaron anteriormente, en la parte de abajo se muestra e"
                        "l bot\u00f3n de Imprimir en el cu\u00e1l </span></p><p><span style=\" font-size:12pt;\">genera un reporte con los datos encontrados anteriormente.</span></p></body></html>", None))
        self.imagen_lp.setText("")
        self.Titulo_10.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p align=\"center\">Consultas</p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">El men\u00fa de consultas cuenta con tres opciones las cuales son: Estado de cuentas, Reporte de ahorros y Reporte de prestamos. <br/>A continuaci\u00f3n, se muestra a detalle como funciona cada uno de ellos.</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Estado de cuentas:</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al presionar el bot\u00f3n Estado de cuentas se abre una interfaz emergente en la cu\u00e1l se muestra lo siguiente:</span></p><p><span style=\" font-size:12pt;\">Una tabla con los datos del cliente, tanto su ID como su nombre y apellidos, si se desea ser mas especifico, hay un recuadro para escribir el nombre que se desea saber la informaci\u00f3n.</span></p><p><span style=\" font-size:12pt;\">Al momento de seleccionar el cliente se reedirige a una ventana con una tabla con los datos correspondientes.</span></p><p><span style=\" font-size:12pt;\">Estos son, ID_PRESTAMOS, ID_CLIENTE, NOMBRE, FECHA_INICIO, FECHA_SIGUIENTE E INTERES.</span></p><p><br/></p></body></html>", None))
        self.imagen_ec.setText("")
        self.label_68.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Emitir reporte de ahorros:</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al presionar el bot\u00f3n de Emitir reporte de ahorros se abre una interfaz en la cu\u00e1l se muestra lo siguiente:</span></p><p><span style=\" font-size:12pt;\">Una tabla con los datos correspondientes a dicho reporte, estos son, ID_CLIENTE, NOMBRE, APELLIDOS, ID_AHORRO, IMPORTE, T.E.A, PLAZO, CAPITAL, CAPITAL_ACTUALIZADO, </span></p><p><span style=\" font-size:12pt;\">FECHA_APERTURA, FECHA_INICIO, Y FECHA_VENCIMIENTO.</span></p><p><span style=\" font-size:12pt;\">Ademas, este contiene un filtro tanto de fecha como de ID del cliente para realizar la busqueda los cuales el usario puede usar el que mas le convenga para obtener </span></p><p><span style=\" font-size:12pt;\">la informaci\u00f3n correspondiente.</span></p><p><br/></p></body></html>", None))
        self.imagen_ra.setText("")
        self.label_70.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">En dado caso que los campos solicitados no sean llenados se mostrara una ventana emergente advirtiendo que debe de llenar la informaci\u00f3n necesaria para extraer los datos para el llenado </span></p><p><span style=\" font-size:12pt;\">de la tabla.</span></p></body></html>", None))
        self.imagen_ra_avi.setText("")
        self.label_71.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Finalmente, si los datos son ingresados correctamente y se muestra la informaci\u00f3n en la tabla, se da click en el bot\u00f3n de continuar para generar el PDF con el reporte creado</span></p><p><span style=\" font-size:12pt;\">de manera automatica.</span></p></body></html>", None))
        self.imagen_ra_PDF.setText("")
        self.label_72.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt; color:#307fe2;\">Emitir reporte de prestamos:</span></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al presionar el bot\u00f3n de Emitir reporte de ahorros se abre una interfaz en la cu\u00e1l se muestra lo siguiente:</span></p><p><span style=\" font-size:12pt;\">Una tabla con los datos correspondientes a dicho reporte, estos son, ID_PAGO, ID_PRESTAMO, ID_CLIENTES, SALDO INSOLITO, INTERES, AMORTIZACION, AMORTIZACION ACOMULADA, </span></p><p><span style=\" font-size:12pt;\">FECHA_LIMITE, FECHA DE PAGO, FECHA_SIGUIENTE, MORATORIO Y AHORRO</span></p><p><span style=\" font-size:12pt;\">Ademas, este contiene un filtro tanto de fecha como de ID del cliente para realizar la busqueda los cuales el usario puede usar el que mas le convenga para obtener </span></p><p><span style=\" font-size:12pt;\">la informaci\u00f3n correspondiente.</span></p><p><br/></p></body></html>", None))
        self.imagen_rp.setText("")
        self.label_74.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">En dado caso que los campos solicitados no sean llenados se mostrara una ventana emergente advirtiendo que debe de llenar la informaci\u00f3n necesaria para extraer los datos para el llenado </span></p><p><span style=\" font-size:12pt;\">de la tabla.</span></p></body></html>", None))
        self.imagen_rp_avi.setText("")
        self.label_75.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Finalmente, si los datos son ingresados correctamente y se muestra la informaci\u00f3n en la tabla, se da click en el bot\u00f3n de continuar para generar el PDF con el reporte creado</span></p><p><span style=\" font-size:12pt;\">de manera automatica.</span></p></body></html>", None))
        self.imagen_rp_PDF.setText("")
        self.label_76.setText(QCoreApplication.translate("Nuevoprestamo", u"<html><head/><body><p><span style=\" font-size:12pt;\">Al presionar el bot\u00f3n Nueva poliza se abre una interfaz en la cu\u00e1l se muestra lo siguiente:</span></p><p><span style=\" font-size:12pt;\">En el bot\u00f3n Nuevo, se abre una ventana emergente con el catalogo de cuentas, el cual se selecciona la cuenta y se abre otra ventana </span></p><p><span style=\" font-size:12pt;\">En esta otra se llenan los datos o en este caso el CARGO, ABONO, REFERENCIA Y CONCEPTO, ya que extrae del catalogo de cuentas el numero de cuenta y la clave del SAT.</span></p><p><span style=\" font-size:12pt;\">Despues, ahora si en la ventana principal, se llenan los datos registrados anteriormente para que se visualicen en una tabla, solo que ahora, incorpora la FECHA, TIPO DE POLIZA y NUMERO, </span></p><p><span style=\" font-size:12pt;\">ademas de un peque\u00f1o concepto que tambien se ocupa para identificar la poliza </span></p><p><span style=\" font-size:12pt;\">Y finalmente revisando que sea la misma cuenta que se agrego a"
                        " traves del catalogo, se da un peque\u00f1o click en la opcion de guardar y esta se visualiza en una tabla que contiene</span></p><p><span style=\" font-size:12pt;\">los siguientes datos almacenados:</span></p><p><span style=\" font-size:12pt;\">MOVIMIENTO, CUENTA, RFC, CARGO, ABONO y REFERENCIA </span></p><p><br/></p></body></html>", None))
        self.imagen_np.setText("")
    # retranslateUi

