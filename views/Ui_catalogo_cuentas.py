# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catalogo_cuentas.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Catalogo_cuentas(object):
    def setupUi(self, Catalogo_cuentas):
        if not Catalogo_cuentas.objectName():
            Catalogo_cuentas.setObjectName(u"Catalogo_cuentas")
        Catalogo_cuentas.resize(1350, 693)
        Catalogo_cuentas.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(Catalogo_cuentas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(Catalogo_cuentas)
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
        self.restore_button.setGeometry(QRect(110, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./../pys6-recipes-organizer-master/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon)
        self.restore_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(150, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./../pys6-recipes-organizer-master/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(107, 0, 31, 22))
        icon2 = QIcon()
        icon2.addFile(u"./../pys6-recipes-organizer-master/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(70, 0, 22, 22))
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
        self.IngresaTitulo.setGeometry(QRect(240, 20, 841, 61))
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
        self.Desarrollo.setGeometry(QRect(10, 100, 1431, 491))
        self.Desarrollo.setMinimumSize(QSize(1350, 0))
        self.Desarrollo.setFrameShape(QFrame.StyledPanel)
        self.Desarrollo.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.Desarrollo)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(219, 130, 651, 71))
        self.frame_5.setMaximumSize(QSize(1000, 90))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 10, 631, 25))
        self.label_28.setMaximumSize(QSize(1000, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 40, 231, 20))
        self.label_30.setMaximumSize(QSize(270, 20))
        self.label_30.setFont(font2)
        self.codigo_SAT = QComboBox(self.frame_5)
        self.codigo_SAT.setObjectName(u"codigo_SAT")
        self.codigo_SAT.setGeometry(QRect(250, 40, 391, 25))
        self.codigo_SAT.setMaximumSize(QSize(500, 25))
        self.codigo_SAT.setFont(font2)
        self.codigo_SAT.setStyleSheet(u"QComboBox#codigo_SAT{border: 1px solid rgb(0, 0, 0);}")
        self.elegir_c_f = QComboBox(self.Desarrollo)
        self.elegir_c_f.setObjectName(u"elegir_c_f")
        self.elegir_c_f.setGeometry(QRect(220, 90, 150, 25))
        self.elegir_c_f.setMaximumSize(QSize(150, 25))
        self.elegir_c_f.setFont(font2)
        self.elegir_c_f.setStyleSheet(u"QComboBox#elegir_c_f{border: 1px solid rgb(0, 0, 0);}")
        self.frame_6 = QFrame(self.Desarrollo)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(220, 200, 651, 61))
        self.frame_6.setMaximumSize(QSize(1000, 120))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_33 = QLabel(self.frame_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 631, 25))
        self.label_33.setMaximumSize(QSize(1000, 25))
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.rubro = QLineEdit(self.frame_6)
        self.rubro.setObjectName(u"rubro")
        self.rubro.setGeometry(QRect(70, 40, 121, 20))
        self.rubro.setMaximumSize(QSize(16777215, 20))
        self.rubro.setFont(font2)
        self.rubro.setStyleSheet(u"QLineEdit#rubro{border: 1px solid rgb(0, 0, 0);}")
        self.label_37 = QLabel(self.frame_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 40, 51, 20))
        self.label_37.setMaximumSize(QSize(100, 20))
        self.label_37.setFont(font2)
        self.frame_7 = QFrame(self.Desarrollo)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(220, 270, 651, 101))
        self.frame_7.setMaximumSize(QSize(1000, 250))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 10, 631, 25))
        self.label_38.setMaximumSize(QSize(1000, 25))
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.label_41 = QLabel(self.frame_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(9, 72, 100, 20))
        self.label_41.setMaximumSize(QSize(100, 20))
        self.label_41.setFont(font2)
        self.digito_fis = QLineEdit(self.frame_7)
        self.digito_fis.setObjectName(u"digito_fis")
        self.digito_fis.setGeometry(QRect(109, 72, 121, 20))
        self.digito_fis.setMaximumSize(QSize(16777215, 20))
        self.digito_fis.setFont(font2)
        self.digito_fis.setStyleSheet(u"QLineEdit#digito_fis{border: 1px solid rgb(0, 0, 0);}")
        self.label_39 = QLabel(self.frame_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 40, 100, 20))
        self.label_39.setMaximumSize(QSize(100, 20))
        self.label_39.setFont(font2)
        self.digito_fiscal = QLineEdit(self.frame_7)
        self.digito_fiscal.setObjectName(u"digito_fiscal")
        self.digito_fiscal.setGeometry(QRect(109, 42, 121, 20))
        self.digito_fiscal.setMaximumSize(QSize(16777215, 20))
        self.digito_fiscal.setFont(font2)
        self.digito_fiscal.setStyleSheet(u"QLineEdit#digito_fiscal{border: 1px solid rgb(0, 0, 0);}")
        self.frame_3 = QFrame(self.Desarrollo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(220, 20, 651, 61))
        self.frame_3.setMaximumSize(QSize(1000, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.clave_e = QLineEdit(self.frame_3)
        self.clave_e.setObjectName(u"clave_e")
        self.clave_e.setGeometry(QRect(50, 10, 401, 20))
        self.clave_e.setMaximumSize(QSize(16777215, 20))
        self.clave_e.setFont(font2)
        self.clave_e.setStyleSheet(u"QLineEdit#clave_e{border: 1px solid rgb(0, 0, 0);}")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 10, 31, 20))
        self.label_21.setMaximumSize(QSize(70, 20))
        self.label_21.setFont(font2)
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(460, 10, 70, 20))
        self.label_29.setMaximumSize(QSize(70, 20))
        self.label_29.setFont(font2)
        self.registro = QDateEdit(self.frame_3)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(530, 10, 111, 20))
        self.registro.setMaximumSize(QSize(16777215, 20))
        self.registro.setFont(font2)
        self.registro.setStyleSheet(u"QDateEdit#registro{border: 1px solid rgb(0, 0, 0);}")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 40, 121, 20))
        self.label_22.setMaximumSize(QSize(150, 20))
        self.label_22.setFont(font2)
        self.nombre_b = QLineEdit(self.frame_3)
        self.nombre_b.setObjectName(u"nombre_b")
        self.nombre_b.setGeometry(QRect(70, 40, 381, 20))
        self.nombre_b.setMaximumSize(QSize(16777215, 20))
        self.nombre_b.setFont(font2)
        self.nombre_b.setStyleSheet(u"QLineEdit#nombre_b{border: 1px solid rgb(0, 0, 0);}")
        self.boton_borrar = QPushButton(self.Desarrollo)
        self.boton_borrar.setObjectName(u"boton_borrar")
        self.boton_borrar.setGeometry(QRect(550, 400, 75, 25))
        self.boton_borrar.setMaximumSize(QSize(16777215, 25))
        self.boton_borrar.setFont(font2)
        self.boton_borrar.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.boton_guardar_1 = QPushButton(self.Desarrollo)
        self.boton_guardar_1.setObjectName(u"boton_guardar_1")
        self.boton_guardar_1.setGeometry(QRect(440, 400, 75, 25))
        self.boton_guardar_1.setMaximumSize(QSize(16777215, 25))
        self.boton_guardar_1.setFont(font2)
        self.boton_guardar_1.setStyleSheet(u"background-color: rgb(116, 170, 80);")

        self.verticalLayout_3.addWidget(self.contenido)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(Catalogo_cuentas)

        QMetaObject.connectSlotsByName(Catalogo_cuentas)
    # setupUi

    def retranslateUi(self, Catalogo_cuentas):
        Catalogo_cuentas.setWindowTitle(QCoreApplication.translate("Catalogo_cuentas", u"Form", None))
        self.title_label.setText("")
        self.restore_button.setText("")
        self.close_button.setText("")
        self.maximize_button.setText("")
        self.minimize_button.setText("")
        self.Empresa.setText(QCoreApplication.translate("Catalogo_cuentas", u"Empresa", None))
        self.Clientes.setText(QCoreApplication.translate("Catalogo_cuentas", u"Clientes", None))
        self.Prestamos.setText(QCoreApplication.translate("Catalogo_cuentas", u"Prestamos", None))
        self.Ahorros.setText(QCoreApplication.translate("Catalogo_cuentas", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("Catalogo_cuentas", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("Catalogo_cuentas", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("Catalogo_cuentas", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("Catalogo_cuentas", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("Catalogo_cuentas", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("Catalogo_cuentas", u"Cheques", None))
        self.notify.setText(QCoreApplication.translate("Catalogo_cuentas", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_18.setText("")
        self.IngresaTitulo.setText(QCoreApplication.translate("Catalogo_cuentas", u"<html><head/><body><p align=\"center\">Cat\u00e1logo de cuentas</p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("Catalogo_cuentas", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("Catalogo_cuentas", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("Catalogo_cuentas", u"Mi empresa", None))
        self.Ahorro.setText(QCoreApplication.translate("Catalogo_cuentas", u"Nuevo ahorro", None))
        self.abonar.setText(QCoreApplication.translate("Catalogo_cuentas", u"Abonar pago", None))
        self.Reportes.setText(QCoreApplication.translate("Catalogo_cuentas", u"Emitir reporte", None))
        self.Polizas.setText(QCoreApplication.translate("Catalogo_cuentas", u"Nueva poliza", None))
        self.Historial.setText(QCoreApplication.translate("Catalogo_cuentas", u"Historial del cliente", None))
        self.Estado.setText(QCoreApplication.translate("Catalogo_cuentas", u"Estado de cuentas", None))
        self.cancelar.setText(QCoreApplication.translate("Catalogo_cuentas", u"Cancelar pago", None))
        self.Cliente.setText(QCoreApplication.translate("Catalogo_cuentas", u"Agregar nuevo cliente", None))
        self.Retirar.setText(QCoreApplication.translate("Catalogo_cuentas", u"Retirar ahorro", None))
        self.Cheques.setText(QCoreApplication.translate("Catalogo_cuentas", u"Cheques", None))
        self.Consulta_cheque.setText(QCoreApplication.translate("Catalogo_cuentas", u"Consultar cheques", None))
        self.Listado.setText(QCoreApplication.translate("Catalogo_cuentas", u"Listado de polizas", None))
        self.prestamo.setText(QCoreApplication.translate("Catalogo_cuentas", u"Nuevo prestamo", None))
        self.Reportes_2.setText(QCoreApplication.translate("Catalogo_cuentas", u"Emitir reporte \n"
"de prestamos", None))
        self.label_28.setText(QCoreApplication.translate("Catalogo_cuentas", u"Contabilidad en medios electr\u00f3nicos", None))
        self.label_30.setText(QCoreApplication.translate("Catalogo_cuentas", u"C\u00f3digo agrupador de cuentas del SAT:", None))
        self.label_33.setText(QCoreApplication.translate("Catalogo_cuentas", u"Normas de informaci\u00f3n financiera (NIF)", None))
        self.label_37.setText(QCoreApplication.translate("Catalogo_cuentas", u"Rubro:", None))
        self.label_38.setText(QCoreApplication.translate("Catalogo_cuentas", u"Normas de informaci\u00f3n financiera (NIF)", None))
        self.label_41.setText(QCoreApplication.translate("Catalogo_cuentas", u"Digito fiscal 2:", None))
        self.label_39.setText(QCoreApplication.translate("Catalogo_cuentas", u"Digito fiscal 1:", None))
        self.clave_e.setText("")
        self.label_21.setText(QCoreApplication.translate("Catalogo_cuentas", u"RFC:", None))
        self.label_29.setText(QCoreApplication.translate("Catalogo_cuentas", u"Registro:", None))
        self.label_22.setText(QCoreApplication.translate("Catalogo_cuentas", u"Nombre:", None))
        self.nombre_b.setText("")
        self.boton_borrar.setText(QCoreApplication.translate("Catalogo_cuentas", u"Borrar", None))
        self.boton_guardar_1.setText(QCoreApplication.translate("Catalogo_cuentas", u"Guardar", None))
    # retranslateUi

