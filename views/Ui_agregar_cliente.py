# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
from imagenes import res_rc

class Ui_Agregar_cliente(object):
    def setupUi(self, Agregar_cliente):
        if not Agregar_cliente.objectName():
            Agregar_cliente.setObjectName(u"Agregar_cliente")
        Agregar_cliente.resize(1410, 685)
        Agregar_cliente.setMinimumSize(QSize(1350, 0))
        Agregar_cliente.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(Agregar_cliente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(Agregar_cliente)
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
        self.buttons_holder_frame_2 = QFrame(self.buttons_holder_frame)
        self.buttons_holder_frame_2.setObjectName(u"buttons_holder_frame_2")
        self.buttons_holder_frame_2.setGeometry(QRect(-30, 0, 180, 30))
        self.buttons_holder_frame_2.setMinimumSize(QSize(180, 30))
        self.buttons_holder_frame_2.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame_2.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame_2.setFrameShadow(QFrame.Raised)
        self.close_button = QToolButton(self.buttons_holder_frame_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(150, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./iconos/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame_2)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(110, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./../pys6-recipes-organizer-master/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.minimize_button = QToolButton(self.buttons_holder_frame_2)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(70, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./../pys6-recipes-organizer-master/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon2)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame_2)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(110, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./../pys6-recipes-organizer-master/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon3)
        self.maximize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(1350, 0))
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
        self.Desarrollo.setGeometry(QRect(0, 100, 1431, 491))
        self.Desarrollo.setMinimumSize(QSize(1350, 0))
        self.Desarrollo.setFrameShape(QFrame.StyledPanel)
        self.Desarrollo.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.Desarrollo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 20, 1011, 251))
        self.frame_3.setMaximumSize(QSize(3000, 3000))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.codigo_cliente = QLineEdit(self.frame_3)
        self.codigo_cliente.setObjectName(u"codigo_cliente")
        self.codigo_cliente.setGeometry(QRect(280, 50, 191, 25))
        self.codigo_cliente.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setPointSize(12)
        self.codigo_cliente.setFont(font2)
        self.codigo_cliente.setStyleSheet(u"QLineEdit#codigo_cliente{border: 1px solid rgb(0, 0, 0);}")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(172, 50, 101, 25))
        self.label_20.setMaximumSize(QSize(1100, 25))
        self.label_20.setFont(font2)
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 10, 791, 31))
        self.label_19.setStyleSheet(u"background-color: rgb(151, 153, 155);")
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(480, 50, 71, 25))
        self.label_29.setMaximumSize(QSize(200, 25))
        self.label_29.setFont(font2)
        self.nombre = QLineEdit(self.frame_3)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(560, 50, 401, 25))
        self.nombre.setMaximumSize(QSize(16777215, 25))
        self.nombre.setFont(font2)
        self.nombre.setStyleSheet(u"QLineEdit#nombre{border: 1px solid rgb(0, 0, 0);}")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(170, 90, 60, 25))
        self.label_21.setMaximumSize(QSize(60, 25))
        self.label_21.setFont(font2)
        self.telefono = QLineEdit(self.frame_3)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setGeometry(QRect(240, 90, 231, 25))
        self.telefono.setMaximumSize(QSize(16777215, 25))
        self.telefono.setFont(font2)
        self.telefono.setStyleSheet(u"QLineEdit#telefono{border: 1px solid rgb(0, 0, 0);}")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(480, 90, 71, 21))
        self.label_22.setMaximumSize(QSize(200, 25))
        self.label_22.setFont(font2)
        self.apellidos = QLineEdit(self.frame_3)
        self.apellidos.setObjectName(u"apellidos")
        self.apellidos.setGeometry(QRect(560, 90, 401, 25))
        self.apellidos.setMaximumSize(QSize(16777215, 25))
        self.apellidos.setFont(font2)
        self.apellidos.setStyleSheet(u"QLineEdit#apellidos{border: 1px solid rgb(0, 0, 0);}")
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(170, 130, 71, 25))
        self.label_28.setMaximumSize(QSize(100, 25))
        self.label_28.setFont(font2)
        self.direccion = QLineEdit(self.frame_3)
        self.direccion.setObjectName(u"direccion")
        self.direccion.setGeometry(QRect(250, 130, 291, 25))
        self.direccion.setMaximumSize(QSize(16777215, 25))
        self.direccion.setFont(font2)
        self.direccion.setStyleSheet(u"QLineEdit#direccion{border: 1px solid rgb(0, 0, 0);}")
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(550, 130, 131, 25))
        self.label_31.setMaximumSize(QSize(200, 25))
        self.label_31.setFont(font2)
        self.telefono_adicional = QLineEdit(self.frame_3)
        self.telefono_adicional.setObjectName(u"telefono_adicional")
        self.telefono_adicional.setGeometry(QRect(680, 130, 281, 25))
        self.telefono_adicional.setMaximumSize(QSize(16777215, 25))
        self.telefono_adicional.setFont(font2)
        self.telefono_adicional.setStyleSheet(u"QLineEdit#telefono_adicional{border: 1px solid rgb(0, 0, 0);}")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(170, 170, 141, 25))
        self.label_34.setMaximumSize(QSize(200, 25))
        self.label_34.setFont(font2)
        self.correo_elec = QLineEdit(self.frame_3)
        self.correo_elec.setObjectName(u"correo_elec")
        self.correo_elec.setGeometry(QRect(310, 170, 371, 25))
        self.correo_elec.setMaximumSize(QSize(16777215, 25))
        self.correo_elec.setFont(font2)
        self.correo_elec.setStyleSheet(u"QLineEdit#correo_elec{border: 1px solid rgb(0, 0, 0);}")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(690, 170, 151, 25))
        self.label_36.setMaximumSize(QSize(200, 25))
        self.label_36.setFont(font2)
        self.fecha_de_nacimiento = QDateEdit(self.frame_3)
        self.fecha_de_nacimiento.setObjectName(u"fecha_de_nacimiento")
        self.fecha_de_nacimiento.setGeometry(QRect(840, 170, 121, 25))
        self.fecha_de_nacimiento.setMaximumSize(QSize(16777215, 25))
        self.fecha_de_nacimiento.setFont(font2)
        self.fecha_de_nacimiento.setStyleSheet(u"QDateEdit#fecha_de_nacimiento{border: 1px solid rgb(0, 0, 0);}")
        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(550, 210, 81, 25))
        self.label_37.setMaximumSize(QSize(120, 25))
        self.label_37.setFont(font2)
        self.puntuacion = QLineEdit(self.frame_3)
        self.puntuacion.setObjectName(u"puntuacion")
        self.puntuacion.setGeometry(QRect(270, 210, 271, 25))
        self.puntuacion.setMaximumSize(QSize(16777215, 25))
        self.puntuacion.setFont(font2)
        self.puntuacion.setStyleSheet(u"QLineEdit#puntuacion{border: 1px solid rgb(0, 0, 0);}")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(170, 210, 91, 25))
        self.label_35.setMaximumSize(QSize(120, 25))
        self.label_35.setFont(font2)
        self.municipio = QLineEdit(self.frame_3)
        self.municipio.setObjectName(u"municipio")
        self.municipio.setGeometry(QRect(630, 210, 331, 25))
        self.municipio.setMaximumSize(QSize(16777215, 25))
        self.municipio.setFont(font2)
        self.municipio.setStyleSheet(u"QLineEdit#municipio{border: 1px solid rgb(0, 0, 0);}")
        self.boton_buscar = QPushButton(self.Desarrollo)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(670, 320, 75, 31))
        self.boton_buscar.setFont(font2)
        self.boton_buscar.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.boton_guardar = QPushButton(self.Desarrollo)
        self.boton_guardar.setObjectName(u"boton_guardar")
        self.boton_guardar.setGeometry(QRect(570, 320, 75, 31))
        self.boton_guardar.setFont(font2)
        self.boton_guardar.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.mensaje = QLabel(self.Desarrollo)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(240, 270, 771, 31))
        self.mensaje.setStyleSheet(u"color: rgb(249, 66, 58);")

        self.verticalLayout_3.addWidget(self.contenido)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(Agregar_cliente)

        QMetaObject.connectSlotsByName(Agregar_cliente)
    # setupUi

    def retranslateUi(self, Agregar_cliente):
        Agregar_cliente.setWindowTitle(QCoreApplication.translate("Agregar_cliente", u"Form", None))
        self.title_label.setText("")
        self.close_button.setText("")
        self.restore_button.setText("")
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.Empresa.setText(QCoreApplication.translate("Agregar_cliente", u"Empresa", None))
        self.Clientes.setText(QCoreApplication.translate("Agregar_cliente", u"Clientes", None))
        self.Prestamos.setText(QCoreApplication.translate("Agregar_cliente", u"Prestamos", None))
        self.Ahorros.setText(QCoreApplication.translate("Agregar_cliente", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("Agregar_cliente", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("Agregar_cliente", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("Agregar_cliente", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("Agregar_cliente", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("Agregar_cliente", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("Agregar_cliente", u"Cheques", None))
        self.notify.setText("")
        self.label_18.setText("")
        self.label_17.setText(QCoreApplication.translate("Agregar_cliente", u"<html><head/><body><p align=\"center\">Agregar cliente</p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("Agregar_cliente", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("Agregar_cliente", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("Agregar_cliente", u"Mi empresa", None))
        self.Ahorro.setText(QCoreApplication.translate("Agregar_cliente", u"Nuevo ahorro", None))
        self.abonar.setText(QCoreApplication.translate("Agregar_cliente", u"Abonar pago", None))
        self.Reportes.setText(QCoreApplication.translate("Agregar_cliente", u"Emitir reporte de ahorro", None))
        self.Polizas.setText(QCoreApplication.translate("Agregar_cliente", u"Nueva poliza", None))
        self.Historial.setText(QCoreApplication.translate("Agregar_cliente", u"Historial del cliente", None))
        self.Estado.setText(QCoreApplication.translate("Agregar_cliente", u"Estado de cuentas", None))
        self.cancelar.setText(QCoreApplication.translate("Agregar_cliente", u"Cancelar pago", None))
        self.Cliente.setText(QCoreApplication.translate("Agregar_cliente", u"Agregar nuevo cliente", None))
        self.Retirar.setText(QCoreApplication.translate("Agregar_cliente", u"Retirar ahorro", None))
        self.Cheques.setText(QCoreApplication.translate("Agregar_cliente", u"Cheques", None))
        self.Consulta_cheque.setText(QCoreApplication.translate("Agregar_cliente", u"Consultar cheques", None))
        self.Listado.setText(QCoreApplication.translate("Agregar_cliente", u"Listado de polizas", None))
        self.prestamo.setText(QCoreApplication.translate("Agregar_cliente", u"Nuevo prestamo", None))
        self.Reportes_2.setText(QCoreApplication.translate("Agregar_cliente", u"Emitir reporte \n"
"de prestamos", None))
        self.label_20.setText(QCoreApplication.translate("Agregar_cliente", u"ID del cliente:", None))
        self.label_19.setText(QCoreApplication.translate("Agregar_cliente", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">   Datos del cliente</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("Agregar_cliente", u"Nombre:", None))
        self.nombre.setText("")
        self.label_21.setText(QCoreApplication.translate("Agregar_cliente", u"Tel\u00e9fono:", None))
        self.telefono.setText("")
        self.label_22.setText(QCoreApplication.translate("Agregar_cliente", u"Apellidos:", None))
        self.apellidos.setText("")
        self.label_28.setText(QCoreApplication.translate("Agregar_cliente", u"Direcci\u00f3n:", None))
        self.direccion.setText("")
        self.label_31.setText(QCoreApplication.translate("Agregar_cliente", u"Telefono adicional:", None))
        self.telefono_adicional.setText("")
        self.label_34.setText(QCoreApplication.translate("Agregar_cliente", u"Correo electr\u00f3nico:", None))
        self.correo_elec.setText("")
        self.label_36.setText(QCoreApplication.translate("Agregar_cliente", u"Fecha de nacimiento:", None))
        self.label_37.setText(QCoreApplication.translate("Agregar_cliente", u"Municipio:", None))
        self.puntuacion.setText("")
        self.label_35.setText(QCoreApplication.translate("Agregar_cliente", u"Puntuaci\u00f3n:", None))
        self.municipio.setText("")
        self.boton_buscar.setText(QCoreApplication.translate("Agregar_cliente", u"Buscar", None))
        self.boton_guardar.setText(QCoreApplication.translate("Agregar_cliente", u"Guardar", None))
        self.mensaje.setText(QCoreApplication.translate("Agregar_cliente", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

