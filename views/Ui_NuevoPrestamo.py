# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuevoPrestamo.ui'
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
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
from imagenes import res_rc

class Ui_Nuevoprestamo(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(1314, 685)
        DetailWindow.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setStyleSheet(u"border-radius: 5px")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(5, 5, 5, 5)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
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
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(80, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./iconos/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(110, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./iconos/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(110, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./iconos/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(140, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./iconos/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

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
        self.abonar_ahorro = QPushButton(self.frame)
        self.abonar_ahorro.setObjectName(u"abonar_ahorro")
        self.abonar_ahorro.setGeometry(QRect(430, 30, 141, 31))
        self.abonar_ahorro.setStyleSheet(u"border-style: solid;\n"
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
        self.Retirar.setGeometry(QRect(430, 60, 141, 31))
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
        self.Desarrollo = QFrame(self.contenido)
        self.Desarrollo.setObjectName(u"Desarrollo")
        self.Desarrollo.setGeometry(QRect(40, 100, 1431, 491))
        self.Desarrollo.setFrameShape(QFrame.StyledPanel)
        self.Desarrollo.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.Desarrollo)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(270, 350, 181, 31))
        self.label_41.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_29 = QLabel(self.Desarrollo)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(270, 60, 121, 31))
        self.label_29.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_32 = QLabel(self.Desarrollo)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 170, 791, 31))
        self.label_32.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.label_33 = QLabel(self.Desarrollo)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(270, 320, 791, 31))
        self.label_33.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.Tiempo = QLineEdit(self.Desarrollo)
        self.Tiempo.setObjectName(u"Tiempo")
        self.Tiempo.setGeometry(QRect(450, 230, 221, 31))
        self.Tiempo.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_37 = QLabel(self.Desarrollo)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(670, 200, 181, 31))
        self.label_37.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.Garantia = QLineEdit(self.Desarrollo)
        self.Garantia.setObjectName(u"Garantia")
        self.Garantia.setGeometry(QRect(450, 380, 611, 31))
        self.Garantia.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_19 = QLabel(self.Desarrollo)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 30, 791, 31))
        self.label_19.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.Codeudor = QLineEdit(self.Desarrollo)
        self.Codeudor.setObjectName(u"Codeudor")
        self.Codeudor.setGeometry(QRect(450, 350, 611, 31))
        self.Codeudor.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.Cantidad = QLineEdit(self.Desarrollo)
        self.Cantidad.setObjectName(u"Cantidad")
        self.Cantidad.setGeometry(QRect(450, 200, 221, 31))
        self.Cantidad.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.Guardar = QPushButton(self.Desarrollo)
        self.Guardar.setObjectName(u"Guardar")
        self.Guardar.setGeometry(QRect(750, 440, 91, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.Guardar.setFont(font2)
        self.Guardar.setStyleSheet(u"\n"
"background-color: rgb(116, 170, 80);\n"
"\n"
"")
        self.Borrar = QPushButton(self.Desarrollo)
        self.Borrar.setObjectName(u"Borrar")
        self.Borrar.setGeometry(QRect(570, 440, 91, 31))
        self.Borrar.setFont(font2)
        self.Borrar.setStyleSheet(u"\n"
"background-color: rgb(116, 170, 80);\n"
"\n"
"")
        self.label_36 = QLabel(self.Desarrollo)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(270, 200, 181, 31))
        self.label_36.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.Interes = QLineEdit(self.Desarrollo)
        self.Interes.setObjectName(u"Interes")
        self.Interes.setGeometry(QRect(850, 200, 161, 31))
        self.Interes.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_42 = QLabel(self.Desarrollo)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(270, 380, 181, 31))
        self.label_42.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_3 = QLabel(self.Desarrollo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1010, 200, 51, 31))
        self.label_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_38 = QLabel(self.Desarrollo)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(270, 230, 181, 31))
        self.label_38.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.label_40 = QLabel(self.Desarrollo)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(670, 230, 181, 31))
        self.label_40.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.Frecuencia = QLineEdit(self.Desarrollo)
        self.Frecuencia.setObjectName(u"Frecuencia")
        self.Frecuencia.setGeometry(QRect(850, 230, 211, 31))
        self.Frecuencia.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.cantidad_prestamo = QLabel(self.Desarrollo)
        self.cantidad_prestamo.setObjectName(u"cantidad_prestamo")
        self.cantidad_prestamo.setGeometry(QRect(270, 130, 781, 31))
        self.cantidad_prestamo.setStyleSheet(u"color: rgb(48, 127, 226);")
        self.TextoError = QLabel(self.Desarrollo)
        self.TextoError.setObjectName(u"TextoError")
        self.TextoError.setGeometry(QRect(270, 290, 781, 21))
        self.TextoError.setStyleSheet(u"color: rgb(249, 66, 58);")
        self.plainTextEdit = QPlainTextEdit(self.Desarrollo)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(1070, 60, 41, 31))
        self.nom_cliente = QLabel(self.Desarrollo)
        self.nom_cliente.setObjectName(u"nom_cliente")
        self.nom_cliente.setGeometry(QRect(390, 60, 671, 31))
        self.nom_cliente.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(151, 153, 155);")
        self.TextoError_2 = QLabel(self.Desarrollo)
        self.TextoError_2.setObjectName(u"TextoError_2")
        self.TextoError_2.setGeometry(QRect(450, 420, 601, 21))
        self.TextoError_2.setStyleSheet(u"color: rgb(48, 127, 226);")
        self.Plazo_max = QLabel(self.Desarrollo)
        self.Plazo_max.setObjectName(u"Plazo_max")
        self.Plazo_max.setGeometry(QRect(270, 270, 781, 21))
        self.Plazo_max.setStyleSheet(u"color: rgb(249, 66, 58);")

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
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.Empresa.setText(QCoreApplication.translate("DetailWindow", u"Empresa", None))
        self.Clientes.setText(QCoreApplication.translate("DetailWindow", u"Clientes", None))
        self.Prestamos.setText(QCoreApplication.translate("DetailWindow", u"Prestamos", None))
        self.Ahorros.setText(QCoreApplication.translate("DetailWindow", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("DetailWindow", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("DetailWindow", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("DetailWindow", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("DetailWindow", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("DetailWindow", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("DetailWindow", u"Cheques", None))
        self.label_18.setText("")
        self.IngresaTitulo.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Nuevo prestamo</p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("DetailWindow", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("DetailWindow", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("DetailWindow", u"Mi empresa", None))
        self.abonar_ahorro.setText(QCoreApplication.translate("DetailWindow", u"Abonar ahorro", None))
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
        self.label_41.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Nombre del codeudor</p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("DetailWindow", u"Nombre del cliente", None))
        self.label_32.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Datos del prestamo</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Otros datos</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Tasa de inter\u00e9s anual</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">   Datos del cliente</span></p></body></html>", None))
        self.Codeudor.setPlaceholderText(QCoreApplication.translate("DetailWindow", u"Ingrese el nombre completo del codeudor", None))
        self.Guardar.setText(QCoreApplication.translate("DetailWindow", u"Guardar", None))
        self.Borrar.setText(QCoreApplication.translate("DetailWindow", u"Borrar", None))
        self.label_36.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Cantidad del prestamo</p></body></html>", None))
        self.Interes.setPlaceholderText(QCoreApplication.translate("DetailWindow", u"Ingrese solo n\u00fameros", None))
        self.label_42.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Garantia prestamo</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">%</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Tiempo(a\u00f1os)</p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\">Frecuencia</p></body></html>", None))
        self.cantidad_prestamo.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.TextoError.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.nom_cliente.setToolTip(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nom_cliente.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.TextoError_2.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.Plazo_max.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

