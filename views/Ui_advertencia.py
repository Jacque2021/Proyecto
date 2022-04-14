# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advertencia.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaEmergente(object):
    def setupUi(self, VentanaEmergente):
        if not VentanaEmergente.objectName():
            VentanaEmergente.setObjectName(u"VentanaEmergente")
        VentanaEmergente.resize(400, 300)
        self.verticalLayout = QVBoxLayout(VentanaEmergente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(VentanaEmergente)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget#frame{border-style: solid;\n"
"border-width: 4px;\n"
"border-color: rgb(249, 66, 58);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(249, 66, 58);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 91, 21))

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 265))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 121, 101))
        self.label.setPixmap(QPixmap(u"./imagenes/chi.png"))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 50, 211, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 80, 191, 31))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 120, 191, 31))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 150, 191, 31))
        self.label_6.setFont(font)
        self.Ok = QPushButton(self.frame_3)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(200, 200, 61, 24))
        font1 = QFont()
        font1.setPointSize(12)
        self.Ok.setFont(font1)
        self.Ok.setStyleSheet(u"background-color: rgb(116, 170, 80);")

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(VentanaEmergente)

        QMetaObject.connectSlotsByName(VentanaEmergente)
    # setupUi

    def retranslateUi(self, VentanaEmergente):
        VentanaEmergente.setWindowTitle(QCoreApplication.translate("VentanaEmergente", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("VentanaEmergente", u"<html><head/><body><p><span style=\" font-size:12pt;\">Advertencia</span></p></body></html>", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("VentanaEmergente", u"<html><head/><body><p>No se puede solicitar </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("VentanaEmergente", u"<html><head/><body><p>un nuevo prestamo.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("VentanaEmergente", u"<html><head/><body><p>Favor de realizar los </p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("VentanaEmergente", u"<html><head/><body><p>pagos pendientes.</p></body></html>", None))
        self.Ok.setText(QCoreApplication.translate("VentanaEmergente", u"Ok", None))
    # retranslateUi

