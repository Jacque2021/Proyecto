# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuenta_agregada.ui'
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

class Ui_cuenta_agregada(object):
    def setupUi(self, cuenta_agregada):
        if not cuenta_agregada.objectName():
            cuenta_agregada.setObjectName(u"cuenta_agregada")
        cuenta_agregada.resize(225, 170)
        self.verticalLayout = QVBoxLayout(cuenta_agregada)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(cuenta_agregada)
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
        self.label_2.setGeometry(QRect(50, 40, 121, 41))
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


        self.retranslateUi(cuenta_agregada)

        QMetaObject.connectSlotsByName(cuenta_agregada)
    # setupUi

    def retranslateUi(self, cuenta_agregada):
        cuenta_agregada.setWindowTitle(QCoreApplication.translate("cuenta_agregada", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("cuenta_agregada", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cuenta agregada</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("cuenta_agregada", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">exitosamente</span></p></body></html>", None))
        self.Ok.setText(QCoreApplication.translate("cuenta_agregada", u"Ok", None))
    # retranslateUi

