# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mensaje_error.ui'
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
from imagenes import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(257, 174)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(249, 66, 58);\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rojo = QFrame(Form)
        self.rojo.setObjectName(u"rojo")
        self.rojo.setStyleSheet(u"QWidget#rojo{background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 4px;\n"
"border-color: rgb(249, 66, 58);}")
        self.rojo.setFrameShape(QFrame.StyledPanel)
        self.rojo.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.rojo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 0, 261, 21))
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(249, 66, 58);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.mensaje = QLabel(self.rojo)
        self.mensaje.setObjectName(u"mensaje")
        self.mensaje.setGeometry(QRect(20, 30, 221, 91))
        self.mensaje.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Ok = QPushButton(self.rojo)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(110, 130, 41, 24))
        font = QFont()
        font.setPointSize(12)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet(u"background-color: rgb(116, 170, 80);")

        self.verticalLayout.addWidget(self.rojo)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mensaje.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.Ok.setText(QCoreApplication.translate("Form", u"Ok", None))
    # retranslateUi

