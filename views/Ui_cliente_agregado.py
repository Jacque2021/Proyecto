# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_agregado.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
    
class Ui_cliente_agregado(object):
    def setupUi(self, cliente_agregado):
        if not cliente_agregado.objectName():
            cliente_agregado.setObjectName(u"cliente_agregado")
        cliente_agregado.resize(235, 170)
        self.verticalLayout = QVBoxLayout(cliente_agregado)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(cliente_agregado)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget#frame{background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 4px;\n"
"border-color: rgb(48, 127, 226);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 0, 251, 21))
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(48, 127, 226);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 30, 121, 41))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 60, 111, 41))
        self.Ok = QPushButton(self.frame)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(90, 110, 41, 24))
        font = QFont()
        font.setPointSize(12)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet(u"background-color: rgb(116, 170, 80);")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(cliente_agregado)

        QMetaObject.connectSlotsByName(cliente_agregado)
    # setupUi

    def retranslateUi(self, cliente_agregado):
        cliente_agregado.setWindowTitle(QCoreApplication.translate("cliente_agregado", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("cliente_agregado", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cliente agregado</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("cliente_agregado", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">exitosamente</span></p></body></html>", None))
        self.Ok.setText(QCoreApplication.translate("cliente_agregado", u"Ok", None))
    # retranslateUi

