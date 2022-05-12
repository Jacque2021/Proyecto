# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo_ahorro.ui'
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
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)
#import res_rc

class NuevoAhorro(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(1350, 685)
        DetailWindow.setStyleSheet(u"QWidget#DetailWindow{border-radius: 5px}")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
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
        icon4.addFile(u"../assets/Iconos/house.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.Desarrollo.setGeometry(QRect(20, 120, 1401, 471))
        self.Desarrollo.setFrameShape(QFrame.StyledPanel)
        self.Desarrollo.setFrameShadow(QFrame.Raised)
        self.advertencia = QLabel(self.Desarrollo)
        self.advertencia.setObjectName(u"advertencia")
        self.advertencia.setGeometry(QRect(580, 260, 471, 20))
        self.advertencia.setStyleSheet(u"color: rgb(249, 66, 58);")
        self.cuenta = QLabel(self.Desarrollo)
        self.cuenta.setObjectName(u"cuenta")
        self.cuenta.setGeometry(QRect(360, 100, 81, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.cuenta.setFont(font2)
        self.fecha = QLabel(self.Desarrollo)
        self.fecha.setObjectName(u"fecha")
        self.fecha.setGeometry(QRect(700, 410, 131, 20))
        self.fecha.setStyleSheet(u"color: rgb(116, 170, 80);")
        self.fecha_limite = QLabel(self.Desarrollo)
        self.fecha_limite.setObjectName(u"fecha_limite")
        self.fecha_limite.setGeometry(QRect(730, 190, 131, 31))
        self.fecha_limite.setFont(font2)
        self.nombre = QLabel(self.Desarrollo)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(590, 100, 281, 31))
        self.nombre.setFont(font2)
        self.fecha_registro = QLabel(self.Desarrollo)
        self.fecha_registro.setObjectName(u"fecha_registro")
        self.fecha_registro.setGeometry(QRect(760, 220, 131, 31))
        self.fecha_registro.setFont(font2)
        self.fecha_sig = QLabel(self.Desarrollo)
        self.fecha_sig.setObjectName(u"fecha_sig")
        self.fecha_sig.setGeometry(QRect(550, 410, 131, 20))
        self.fecha_sig.setStyleSheet(u"color: rgb(116, 170, 80);")
        self.total_pag = QLabel(self.Desarrollo)
        self.total_pag.setObjectName(u"total_pag")
        self.total_pag.setGeometry(QRect(660, 290, 131, 31))
        self.total_pag.setFont(font2)
        self.realizo_pago = QLabel(self.Desarrollo)
        self.realizo_pago.setObjectName(u"realizo_pago")
        self.realizo_pago.setGeometry(QRect(290, 380, 551, 20))
        self.realizo_pago.setStyleSheet(u"color: rgb(116, 170, 80);")
        self.primera_linea_3 = QFrame(self.Desarrollo)
        self.primera_linea_3.setObjectName(u"primera_linea_3")
        self.primera_linea_3.setGeometry(QRect(90, 10, 681, 21))
        self.primera_linea_3.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.primera_linea_3.setFrameShape(QFrame.StyledPanel)
        self.primera_linea_3.setFrameShadow(QFrame.Raised)
        self.datos_cliente_3 = QLabel(self.primera_linea_3)
        self.datos_cliente_3.setObjectName(u"datos_cliente_3")
        self.datos_cliente_3.setGeometry(QRect(0, 0, 111, 16))
        self.datos_cliente_3.setFont(font)
        self.frame_contenidoC = QFrame(self.Desarrollo)
        self.frame_contenidoC.setObjectName(u"frame_contenidoC")
        self.frame_contenidoC.setGeometry(QRect(90, 30, 681, 521))
        self.frame_contenidoC.setFrameShape(QFrame.StyledPanel)
        self.frame_contenidoC.setFrameShadow(QFrame.Raised)
        self.primera_linea_6 = QFrame(self.frame_contenidoC)
        self.primera_linea_6.setObjectName(u"primera_linea_6")
        self.primera_linea_6.setGeometry(QRect(0, 120, 701, 21))
        self.primera_linea_6.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.primera_linea_6.setFrameShape(QFrame.StyledPanel)
        self.primera_linea_6.setFrameShadow(QFrame.Raised)
        self.datos_cliente_6 = QLabel(self.primera_linea_6)
        self.datos_cliente_6.setObjectName(u"datos_cliente_6")
        self.datos_cliente_6.setGeometry(QRect(10, 0, 171, 16))
        self.datos_cliente_6.setFont(font)
        self.titulo_importe = QLabel(self.frame_contenidoC)
        self.titulo_importe.setObjectName(u"titulo_importe")
        self.titulo_importe.setGeometry(QRect(10, 150, 61, 16))
        font3 = QFont()
        font3.setPointSize(10)
        self.titulo_importe.setFont(font3)
        self.caja_importe = QLineEdit(self.frame_contenidoC)
        self.caja_importe.setObjectName(u"caja_importe")
        self.caja_importe.setGeometry(QRect(100, 150, 171, 20))
        self.caja_importe.setStyleSheet(u"QLineEdit#caja_importe{border: 1px solid rgb(0,0,0);}")
        self.titulo_tea = QLabel(self.frame_contenidoC)
        self.titulo_tea.setObjectName(u"titulo_tea")
        self.titulo_tea.setGeometry(QRect(10, 230, 51, 16))
        self.titulo_tea.setFont(font3)
        self.titulo_fecapert = QLabel(self.frame_contenidoC)
        self.titulo_fecapert.setObjectName(u"titulo_fecapert")
        self.titulo_fecapert.setGeometry(QRect(10, 190, 101, 16))
        self.titulo_fecapert.setFont(font3)
        self.label_48 = QLabel(self.frame_contenidoC)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 280, 71, 16))
        self.label_48.setFont(font3)
        self.label_49 = QLabel(self.frame_contenidoC)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(380, 150, 101, 16))
        self.label_49.setFont(font3)
        self.label_50 = QLabel(self.frame_contenidoC)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(330, 190, 141, 16))
        self.label_50.setFont(font3)
        self.fecha_venc = QDateEdit(self.frame_contenidoC)
        self.fecha_venc.setObjectName(u"fecha_venc")
        self.fecha_venc.setGeometry(QRect(480, 190, 171, 22))
        self.fecha_venc.setStyleSheet(u"QDateEdit#fecha_venc{border: 1px solid rgb(0,0,0);}")
        self.label_51 = QLabel(self.frame_contenidoC)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(350, 240, 101, 16))
        self.label_51.setFont(font3)
        self.label_53 = QLabel(self.frame_contenidoC)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(380, 280, 101, 16))
        self.label_53.setFont(font3)
        self.frame_botones = QFrame(self.frame_contenidoC)
        self.frame_botones.setObjectName(u"frame_botones")
        self.frame_botones.setGeometry(QRect(80, 400, 521, 31))
        self.frame_botones.setFrameShape(QFrame.StyledPanel)
        self.frame_botones.setFrameShadow(QFrame.Raised)
        self.label_55 = QLabel(self.frame_contenidoC)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 30, 21, 16))
        self.label_55.setFont(font3)
        self.id_c = QLineEdit(self.frame_contenidoC)
        self.id_c.setObjectName(u"id_c")
        self.id_c.setGeometry(QRect(40, 30, 61, 20))
        self.id_c.setStyleSheet(u"QLineEdit#id_c{border: 1px solid rgb(0,0,0);}")
        self.label_56 = QLabel(self.frame_contenidoC)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(130, 30, 61, 16))
        self.label_56.setFont(font3)
        self.nombre_c = QLineEdit(self.frame_contenidoC)
        self.nombre_c.setObjectName(u"nombre_c")
        self.nombre_c.setGeometry(QRect(190, 30, 141, 20))
        self.nombre_c.setStyleSheet(u"QLineEdit#nombre_c{border: 1px solid rgb(0,0,0);}")
        self.label_57 = QLabel(self.frame_contenidoC)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(360, 30, 61, 16))
        self.label_57.setFont(font3)
        self.apellidos_c = QLineEdit(self.frame_contenidoC)
        self.apellidos_c.setObjectName(u"apellidos_c")
        self.apellidos_c.setGeometry(QRect(450, 30, 231, 20))
        self.apellidos_c.setStyleSheet(u"QLineEdit#apellidos_c{border: 1px solid rgb(0,0,0);}")
        self.plazo = QTextBrowser(self.frame_contenidoC)
        self.plazo.setObjectName(u"plazo")
        self.plazo.setGeometry(QRect(110, 280, 61, 31))
        self.plazo.setStyleSheet(u"QTextBrowser#plazo{border: 1px solid rgb(0,0,0);}")
        self.interes_c = QLabel(self.frame_contenidoC)
        self.interes_c.setObjectName(u"interes_c")
        self.interes_c.setGeometry(QRect(480, 230, 250, 32))
        self.interes_c.setMinimumSize(QSize(250, 0))
        self.interes_c.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"QLabel#interes_c{border: 1px solid rgb(0,0,0);}")
        self.cancelacion = QLabel(self.frame_contenidoC)
        self.cancelacion.setObjectName(u"cancelacion")
        self.cancelacion.setGeometry(QRect(480, 270, 250, 32))
        self.cancelacion.setMinimumSize(QSize(250, 0))
        self.cancelacion.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 10pt \"Arial\";\n"
"QLabel#interes_c{border: 1px solid rgb(0,0,0);}")
        self.texto_error = QLabel(self.frame_contenidoC)
        self.texto_error.setObjectName(u"texto_error")
        self.texto_error.setGeometry(QRect(20, 340, 421, 32))
        self.texto_error.setMinimumSize(QSize(250, 0))
        self.texto_error.setStyleSheet(u"color: rgb(48, 127, 226);\n"
"font: 10pt \"Arial\";")
        self.caja_tea = QLineEdit(self.frame_contenidoC)
        self.caja_tea.setObjectName(u"caja_tea")
        self.caja_tea.setGeometry(QRect(110, 230, 61, 20))
        self.caja_tea.setStyleSheet(u"QLineEdit#caja_tea{border: 1px solid rgb(0,0,0);}")
        self.label = QLabel(self.frame_contenidoC)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 230, 47, 13))
        self.horan = QLabel(self.frame_contenidoC)
        self.horan.setObjectName(u"horan")
        self.horan.setGeometry(QRect(110, 190, 161, 21))
        self.horan.setStyleSheet(u"QLabel#horan{border: 1px solid rgb(0,0,0);}")
        self.horan_2 = QLabel(self.frame_contenidoC)
        self.horan_2.setObjectName(u"horan_2")
        self.horan_2.setGeometry(QRect(480, 150, 171, 21))
        self.horan_2.setStyleSheet(u"QLabel#horan_2{border: 1px solid rgb(0,0,0);}")
        self.boton_procesar = QToolButton(self.frame_contenidoC)
        self.boton_procesar.setObjectName(u"boton_procesar")
        self.boton_procesar.setGeometry(QRect(350, 390, 71, 21))
        self.boton_procesar.setFont(font)
        self.boton_procesar.setStyleSheet(u"background-color: rgb(116,170,80);")
        self.frame_2 = QFrame(self.Desarrollo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(900, 10, 291, 341))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.textBrowser_3 = QTextBrowser(self.frame_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(60, 0, 51, 31))
        self.textBrowser_3.setStyleSheet(u"QTextBrowser#textBrowser_3{border: 1px solid rgb(0,0,0);};\n"
"")
        self.textBrowser_4 = QTextBrowser(self.frame_2)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(110, 0, 151, 31))
        self.textBrowser_4.setStyleSheet(u"QTextBrowser#textBrowser_4{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia1 = QTextBrowser(self.frame_2)
        self.dia1.setObjectName(u"dia1")
        self.dia1.setGeometry(QRect(60, 30, 51, 31))
        self.dia1.setStyleSheet(u"QTextBrowser#dia1{border: 1px solid rgb(0,0,0);};\n"
"")
        self.textBrowser_7 = QTextBrowser(self.frame_2)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(60, 180, 51, 31))
        self.textBrowser_7.setStyleSheet(u"QTextBrowser#textBrowser_7{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia5 = QTextBrowser(self.frame_2)
        self.dia5.setObjectName(u"dia5")
        self.dia5.setGeometry(QRect(60, 150, 51, 31))
        self.dia5.setStyleSheet(u"QTextBrowser#dia5{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia4 = QTextBrowser(self.frame_2)
        self.dia4.setObjectName(u"dia4")
        self.dia4.setGeometry(QRect(60, 120, 51, 31))
        self.dia4.setStyleSheet(u"QTextBrowser#dia4{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia3 = QTextBrowser(self.frame_2)
        self.dia3.setObjectName(u"dia3")
        self.dia3.setGeometry(QRect(60, 90, 51, 31))
        self.dia3.setStyleSheet(u"QTextBrowser#dia3{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia2 = QTextBrowser(self.frame_2)
        self.dia2.setObjectName(u"dia2")
        self.dia2.setGeometry(QRect(60, 60, 51, 31))
        self.dia2.setStyleSheet(u"QTextBrowser#dia2{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia360 = QTextBrowser(self.frame_2)
        self.dia360.setObjectName(u"dia360")
        self.dia360.setGeometry(QRect(60, 240, 51, 31))
        self.dia360.setStyleSheet(u"QTextBrowser#dia360{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1 = QTextBrowser(self.frame_2)
        self.interes1.setObjectName(u"interes1")
        self.interes1.setGeometry(QRect(110, 30, 151, 31))
        self.interes1.setStyleSheet(u"QTextBrowser#interes1{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_2 = QTextBrowser(self.frame_2)
        self.interes1_2.setObjectName(u"interes1_2")
        self.interes1_2.setGeometry(QRect(110, 60, 151, 31))
        self.interes1_2.setStyleSheet(u"QTextBrowser#interes1_2{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_3 = QTextBrowser(self.frame_2)
        self.interes1_3.setObjectName(u"interes1_3")
        self.interes1_3.setGeometry(QRect(110, 90, 151, 31))
        self.interes1_3.setStyleSheet(u"QTextBrowser#interes1_3{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_4 = QTextBrowser(self.frame_2)
        self.interes1_4.setObjectName(u"interes1_4")
        self.interes1_4.setGeometry(QRect(110, 120, 151, 31))
        self.interes1_4.setStyleSheet(u"QTextBrowser#interes1_4{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_5 = QTextBrowser(self.frame_2)
        self.interes1_5.setObjectName(u"interes1_5")
        self.interes1_5.setGeometry(QRect(110, 150, 151, 31))
        self.interes1_5.setStyleSheet(u"QTextBrowser#interes1_5{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_359 = QTextBrowser(self.frame_2)
        self.interes1_359.setObjectName(u"interes1_359")
        self.interes1_359.setGeometry(QRect(110, 210, 151, 31))
        self.interes1_359.setStyleSheet(u"QTextBrowser#interes1_359{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_360 = QTextBrowser(self.frame_2)
        self.interes1_360.setObjectName(u"interes1_360")
        self.interes1_360.setGeometry(QRect(110, 240, 151, 31))
        self.interes1_360.setStyleSheet(u"QTextBrowser#interes1_360{border: 1px solid rgb(0,0,0);};\n"
"")
        self.interes1_total = QTextBrowser(self.frame_2)
        self.interes1_total.setObjectName(u"interes1_total")
        self.interes1_total.setGeometry(QRect(110, 270, 151, 31))
        self.interes1_total.setStyleSheet(u"QTextBrowser#interes1_total{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dias1_13 = QTextBrowser(self.frame_2)
        self.dias1_13.setObjectName(u"dias1_13")
        self.dias1_13.setGeometry(QRect(60, 270, 51, 31))
        self.dias1_13.setStyleSheet(u"QTextBrowser#dias1_13{border: 1px solid rgb(0,0,0);};\n"
"")
        self.dia359 = QTextBrowser(self.frame_2)
        self.dia359.setObjectName(u"dia359")
        self.dia359.setGeometry(QRect(60, 210, 51, 31))
        self.dia359.setStyleSheet(u"QTextBrowser#dia359{border: 1px solid rgb(0,0,0);};\n"
"")

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
        self.Prestamos.setText(QCoreApplication.translate("DetailWindow", u"Prestamos", None))
        self.Ahorros.setText(QCoreApplication.translate("DetailWindow", u"Ahorros", None))
        self.Consultas.setText(QCoreApplication.translate("DetailWindow", u"Consultas", None))
        self.Ayuda.setText(QCoreApplication.translate("DetailWindow", u"Ayuda", None))
        self.Salir.setText(QCoreApplication.translate("DetailWindow", u"Salir", None))
        self.Notificaciones.setText(QCoreApplication.translate("DetailWindow", u"Notificaciones", None))
        self.PolizaS.setText(QCoreApplication.translate("DetailWindow", u"Polizas", None))
        self.ChequeS.setText(QCoreApplication.translate("DetailWindow", u"Cheques", None))
        self.notify.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_18.setText("")
        self.IngresaTitulo.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Nuevo ahorro</span></p></body></html>", None))
        self.label_10.setText("")
        self.Catalogo.setText(QCoreApplication.translate("DetailWindow", u"Cat\u00e1logo de cuentas", None))
        self.Respaldo.setText(QCoreApplication.translate("DetailWindow", u"Respaldar empresa", None))
        self.Mi_Empresa.setText(QCoreApplication.translate("DetailWindow", u"Mi empresa", None))
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
        self.Reportes_2.setText(QCoreApplication.translate("DetailWindow", u"Emitir reporte \n"
"de prestamos", None))
        self.advertencia.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.cuenta.setText("")
        self.fecha.setText("")
        self.fecha_limite.setText("")
        self.nombre.setText("")
        self.fecha_registro.setText("")
        self.fecha_sig.setText("")
        self.total_pag.setText("")
        self.realizo_pago.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.datos_cliente_3.setText(QCoreApplication.translate("DetailWindow", u"Datos del cliente", None))
        self.datos_cliente_6.setText(QCoreApplication.translate("DetailWindow", u"Datos del ahorro", None))
        self.titulo_importe.setText(QCoreApplication.translate("DetailWindow", u"Importe:", None))
        self.titulo_tea.setText(QCoreApplication.translate("DetailWindow", u"T.E.A:", None))
        self.titulo_fecapert.setText(QCoreApplication.translate("DetailWindow", u"Fecha apertura:", None))
        self.label_48.setText(QCoreApplication.translate("DetailWindow", u"Plazo:", None))
        self.label_49.setText(QCoreApplication.translate("DetailWindow", u"Fecha inicio:", None))
        self.label_50.setText(QCoreApplication.translate("DetailWindow", u"Fecha de vencimiento:", None))
        self.label_51.setText(QCoreApplication.translate("DetailWindow", u"Inter\u00e9s calculado:", None))
        self.label_53.setText(QCoreApplication.translate("DetailWindow", u"Cancelaci\u00f3n:", None))
        self.label_55.setText(QCoreApplication.translate("DetailWindow", u"Id:", None))
        self.label_56.setText(QCoreApplication.translate("DetailWindow", u"Nombre:", None))
        self.label_57.setText(QCoreApplication.translate("DetailWindow", u"Apellidos:", None))
        self.plazo.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">360 dias</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.interes_c.setToolTip(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.interes_c.setWhatsThis(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.interes_c.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cancelacion.setToolTip(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cancelacion.setWhatsThis(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.cancelacion.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.texto_error.setToolTip(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.texto_error.setWhatsThis(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.texto_error.setText(QCoreApplication.translate("DetailWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"%", None))
        self.horan.setText("")
        self.horan_2.setText("")
        self.boton_procesar.setText(QCoreApplication.translate("DetailWindow", u"Guardar", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">DIAS </span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">INTERES CALC.</span></p></body></html>", None))
        self.dia1.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">1</span></p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">.</span></p></body></html>", None))
        self.dia5.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">5</span></p></body></html>", None))
        self.dia4.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">4</span></p></body></html>", None))
        self.dia3.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">3</span></p></body></html>", None))
        self.dia2.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">2</span></p></body></html>", None))
        self.dia360.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">360</span></p></body></html>", None))
        self.interes1.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_2.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_3.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_4.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_5.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_359.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_360.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.interes1_total.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.dias1_13.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">TOTAL</span></p></body></html>", None))
        self.dia359.setHtml(QCoreApplication.translate("DetailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600;\">359</span></p></body></html>", None))
    # retranslateUi

