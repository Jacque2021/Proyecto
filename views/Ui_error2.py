# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error2.ui'
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
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)
from imagenes import res_rc

class Ui_Error(object):
    def setupUi(self, InicioSesion):
        if not InicioSesion.objectName():
            InicioSesion.setObjectName(u"InicioSesion")
        InicioSesion.resize(290, 230)
        InicioSesion.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(InicioSesion)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(InicioSesion)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(5, 5, 5, 5)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"QWidget#background_frame{\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"\n"
"	border-color: rgb(249, 66, 58);\n"
"}")
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
        self.top_bar_frame.setStyleSheet(u"background-color: rgb(249, 66, 58);")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(130, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimizar = QToolButton(self.buttons_holder_frame)
        self.minimizar.setObjectName(u"minimizar")
        self.minimizar.setGeometry(QRect(50, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./iconos/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizar.setIcon(icon)
        self.minimizar.setIconSize(QSize(25, 25))
        self.maximizar = QToolButton(self.buttons_holder_frame)
        self.maximizar.setObjectName(u"maximizar")
        self.maximizar.setGeometry(QRect(90, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./iconos/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizar.setIcon(icon1)
        self.maximizar.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"QWidget#content_frame{\n"
"	border-image: url(:/imagen/logobueno_preview_rev_1.png);\n"
"}")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget#frame{background-color:rgba(151, 153, 155,240);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 70, 191, 21))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 15pt \"Arial Black\";\n"
"")
        self.regresar_button = QPushButton(self.frame)
        self.regresar_button.setObjectName(u"regresar_button")
        self.regresar_button.setGeometry(QRect(100, 100, 61, 31))
        self.regresar_button.setStyleSheet(u"QPushButton#regresar_button{\n"
"background-color: #74AA50;\n"
"color: white;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton::hover#regresar_button{background-color: #ffc13b};\n"
"")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 40, 191, 21))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 15pt \"Arial\";\n"
"\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 191, 21))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 15pt \"Arial\";\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(InicioSesion)

        QMetaObject.connectSlotsByName(InicioSesion)
    # setupUi

    def retranslateUi(self, InicioSesion):
        InicioSesion.setWindowTitle(QCoreApplication.translate("InicioSesion", u"Form", None))
        self.title_label.setText("")
        self.minimizar.setText("")
        self.maximizar.setText("")
        self.label_4.setText(QCoreApplication.translate("InicioSesion", u"Intente de nuevo.", None))
        self.regresar_button.setText(QCoreApplication.translate("InicioSesion", u"Regresar", None))
        self.label_3.setText(QCoreApplication.translate("InicioSesion", u"no son correctos!!", None))
        self.label.setText(QCoreApplication.translate("InicioSesion", u"Los datos ingresados", None))
    # retranslateUi

