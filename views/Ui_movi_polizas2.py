# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movi_polizas.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
    QLineEdit, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Mov_polizas_2(object):
    def setupUi(self, Mov_polizas):
        if not Mov_polizas.objectName():
            Mov_polizas.setObjectName(u"Mov_polizas")
        Mov_polizas.resize(800, 500)
        self.central_frame = QFrame(Mov_polizas)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setGeometry(QRect(-10, -10, 821, 511))
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contenido_frame = QFrame(self.background_frame)
        self.contenido_frame.setObjectName(u"contenido_frame")
        self.contenido_frame.setFrameShape(QFrame.StyledPanel)
        self.contenido_frame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.contenido_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 781, 42))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.boton_salir1 = QToolButton(self.frame)
        self.boton_salir1.setObjectName(u"boton_salir1")
        self.boton_salir1.setStyleSheet(u"background-color: rgb(249, 66, 58);")
        icon = QIcon()
        icon.addFile(u"./assets/Iconos/X.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_salir1.setIcon(icon)
        self.boton_salir1.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.boton_salir1)

        self.boton_guardar_2 = QToolButton(self.contenido_frame)
        self.boton_guardar_2.setObjectName(u"boton_guardar_2")
        self.boton_guardar_2.setGeometry(QRect(20, 70, 71, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.boton_guardar_2.setFont(font1)
        self.boton_guardar_2.setStyleSheet(u"background-color: rgb(116,170,80);")
        self.boton_guardar_3 = QToolButton(self.contenido_frame)
        self.boton_guardar_3.setObjectName(u"boton_guardar_3")
        self.boton_guardar_3.setGeometry(QRect(110, 70, 71, 21))
        self.boton_guardar_3.setFont(font1)
        self.boton_guardar_3.setStyleSheet(u"background-color: rgb(116,170,80);")
        self.boton_guardar_4 = QToolButton(self.contenido_frame)
        self.boton_guardar_4.setObjectName(u"boton_guardar_4")
        self.boton_guardar_4.setGeometry(QRect(200, 70, 71, 21))
        self.boton_guardar_4.setFont(font1)
        self.boton_guardar_4.setStyleSheet(u"background-color: rgb(116,170,80);")
        self.linea_datosg_6 = QFrame(self.contenido_frame)
        self.linea_datosg_6.setObjectName(u"linea_datosg_6")
        self.linea_datosg_6.setGeometry(QRect(20, 170, 91, 20))
        self.linea_datosg_6.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.linea_datosg_6.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_6.setFrameShadow(QFrame.Raised)
        self.datos_cliente_7 = QLabel(self.linea_datosg_6)
        self.datos_cliente_7.setObjectName(u"datos_cliente_7")
        self.datos_cliente_7.setGeometry(QRect(0, 0, 61, 16))
        self.datos_cliente_7.setFont(font1)
        self.linea_datosg_7 = QFrame(self.contenido_frame)
        self.linea_datosg_7.setObjectName(u"linea_datosg_7")
        self.linea_datosg_7.setGeometry(QRect(20, 240, 91, 20))
        self.linea_datosg_7.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.linea_datosg_7.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_7.setFrameShadow(QFrame.Raised)
        self.datos_cliente_8 = QLabel(self.linea_datosg_7)
        self.datos_cliente_8.setObjectName(u"datos_cliente_8")
        self.datos_cliente_8.setGeometry(QRect(0, 0, 61, 16))
        self.datos_cliente_8.setFont(font1)
        self.linea_datosg_8 = QFrame(self.contenido_frame)
        self.linea_datosg_8.setObjectName(u"linea_datosg_8")
        self.linea_datosg_8.setGeometry(QRect(20, 290, 91, 20))
        self.linea_datosg_8.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.linea_datosg_8.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_8.setFrameShadow(QFrame.Raised)
        self.datos_cliente_9 = QLabel(self.linea_datosg_8)
        self.datos_cliente_9.setObjectName(u"datos_cliente_9")
        self.datos_cliente_9.setGeometry(QRect(0, 0, 61, 16))
        self.datos_cliente_9.setFont(font1)
        self.linea_datosg_9 = QFrame(self.contenido_frame)
        self.linea_datosg_9.setObjectName(u"linea_datosg_9")
        self.linea_datosg_9.setGeometry(QRect(20, 360, 91, 20))
        self.linea_datosg_9.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.linea_datosg_9.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_9.setFrameShadow(QFrame.Raised)
        self.datos_cliente_10 = QLabel(self.linea_datosg_9)
        self.datos_cliente_10.setObjectName(u"datos_cliente_10")
        self.datos_cliente_10.setGeometry(QRect(0, 0, 71, 16))
        self.datos_cliente_10.setFont(font1)
        self.linea_datosg_10 = QFrame(self.contenido_frame)
        self.linea_datosg_10.setObjectName(u"linea_datosg_10")
        self.linea_datosg_10.setGeometry(QRect(20, 420, 91, 20))
        self.linea_datosg_10.setStyleSheet(u"background-color: rgb(151,153,155);\n"
"")
        self.linea_datosg_10.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_10.setFrameShadow(QFrame.Raised)
        self.datos_cliente_11 = QLabel(self.linea_datosg_10)
        self.datos_cliente_11.setObjectName(u"datos_cliente_11")
        self.datos_cliente_11.setGeometry(QRect(0, 0, 71, 16))
        self.datos_cliente_11.setFont(font1)
        self.linea_datosg_11 = QFrame(self.contenido_frame)
        self.linea_datosg_11.setObjectName(u"linea_datosg_11")
        self.linea_datosg_11.setGeometry(QRect(20, 130, 751, 20))
        self.linea_datosg_11.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"")
        self.linea_datosg_11.setFrameShape(QFrame.StyledPanel)
        self.linea_datosg_11.setFrameShadow(QFrame.Raised)
        self.datos_cliente_12 = QLabel(self.linea_datosg_11)
        self.datos_cliente_12.setObjectName(u"datos_cliente_12")
        self.datos_cliente_12.setGeometry(QRect(0, 0, 91, 16))
        self.datos_cliente_12.setFont(font1)
        self.caja_rfc_7 = QLineEdit(self.linea_datosg_11)
        self.caja_rfc_7.setObjectName(u"caja_rfc_7")
        self.caja_rfc_7.setGeometry(QRect(100, 0, 111, 20))
        self.caja_rfc_8 = QLineEdit(self.contenido_frame)
        self.caja_rfc_8.setObjectName(u"caja_rfc_8")
        self.caja_rfc_8.setGeometry(QRect(120, 170, 191, 20))
        self.caja_rfc_9 = QLineEdit(self.contenido_frame)
        self.caja_rfc_9.setObjectName(u"caja_rfc_9")
        self.caja_rfc_9.setGeometry(QRect(120, 190, 331, 20))
        self.caja_rfc_10 = QLineEdit(self.contenido_frame)
        self.caja_rfc_10.setObjectName(u"caja_rfc_10")
        self.caja_rfc_10.setGeometry(QRect(120, 240, 331, 20))
        self.caja_rfc_11 = QLineEdit(self.contenido_frame)
        self.caja_rfc_11.setObjectName(u"caja_rfc_11")
        self.caja_rfc_11.setGeometry(QRect(120, 290, 331, 20))
        self.caja_rfc_12 = QLineEdit(self.contenido_frame)
        self.caja_rfc_12.setObjectName(u"caja_rfc_12")
        self.caja_rfc_12.setGeometry(QRect(120, 360, 601, 41))
        self.caja_rfc_13 = QLineEdit(self.contenido_frame)
        self.caja_rfc_13.setObjectName(u"caja_rfc_13")
        self.caja_rfc_13.setGeometry(QRect(120, 420, 601, 41))

        self.verticalLayout_3.addWidget(self.contenido_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.retranslateUi(Mov_polizas)

        QMetaObject.connectSlotsByName(Mov_polizas)
    # setupUi

    def retranslateUi(self, Mov_polizas):
        Mov_polizas.setWindowTitle(QCoreApplication.translate("Mov_polizas", u"Form", None))
        self.label.setText(QCoreApplication.translate("Mov_polizas", u"Diarios y polizas", None))
        self.boton_salir1.setText(QCoreApplication.translate("Mov_polizas", u"X", None))
        self.boton_guardar_2.setText(QCoreApplication.translate("Mov_polizas", u"Guardar", None))
        self.boton_guardar_3.setText(QCoreApplication.translate("Mov_polizas", u"Nuevo", None))
        self.boton_guardar_4.setText(QCoreApplication.translate("Mov_polizas", u"Borrar", None))
        self.datos_cliente_7.setText(QCoreApplication.translate("Mov_polizas", u"Cuenta", None))
        self.datos_cliente_8.setText(QCoreApplication.translate("Mov_polizas", u"Cargo", None))
        self.datos_cliente_9.setText(QCoreApplication.translate("Mov_polizas", u"Abono", None))
        self.datos_cliente_10.setText(QCoreApplication.translate("Mov_polizas", u"Referencia", None))
        self.datos_cliente_11.setText(QCoreApplication.translate("Mov_polizas", u"Concepto", None))
        self.datos_cliente_12.setText(QCoreApplication.translate("Mov_polizas", u"Movimiento", None))
    # retranslateUi

