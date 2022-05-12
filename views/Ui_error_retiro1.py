# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_retiro1.ui'
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
#import res_rc

class Ui_error_1(object):
    def setupUi(self, error_cliente):
        if not error_cliente.objectName():
            error_cliente.setObjectName(u"error_cliente")
        error_cliente.resize(254, 170)
        self.verticalLayout = QVBoxLayout(error_cliente)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(error_cliente)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget#frame{background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 4px;\n"
"border-color: rgb(249, 66, 58);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 0, 251, 21))
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(249, 66, 58);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 30, 161, 41))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 50, 161, 41))
        self.Ok = QPushButton(self.frame)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(110, 120, 41, 24))
        font = QFont()
        font.setPointSize(12)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 80, 161, 41))

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(error_cliente)

        QMetaObject.connectSlotsByName(error_cliente)
    # setupUi

    def retranslateUi(self, error_cliente):
        error_cliente.setWindowTitle(QCoreApplication.translate("error_cliente", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("error_cliente", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u00a1Error!</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("error_cliente", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El retiro no puede ser</span></p></body></html>", None))
        self.Ok.setText(QCoreApplication.translate("error_cliente", u"Ok", None))
        self.label_4.setText(QCoreApplication.translate("error_cliente", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">mayor que el capital.</span></p></body></html>", None))
    # retranslateUi

