# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioSesion.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
from imagenes import res_rc

class InicioSesion(object):
    def setupUi(self, InicioSesion):
        if not InicioSesion.objectName():
            InicioSesion.setObjectName(u"InicioSesion")
        InicioSesion.resize(1345, 685)
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
"	background-color: rgb(255, 255, 255);}")
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
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./iconos/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./iconos/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./iconos/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./iconos/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"QWidget#content_frame\n"
"{border-image: url(:/imagen/c91e5488aa82ea043390cb1462c20f3a.jpg);}")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.content_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.content_frame_2 = QFrame(self.content_frame)
        self.content_frame_2.setObjectName(u"content_frame_2")
        self.content_frame_2.setStyleSheet(u"QWidget#content_frame{\n"
"	border-image: url(:/imagen/c91e5488aa82ea043390cb1462c20f3a.jpg);}")
        self.content_frame_2.setFrameShape(QFrame.StyledPanel)
        self.content_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.content_frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget#frame{background-color:rgba(0,0,0,100);}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_label_3 = QLabel(self.frame_3)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setMinimumSize(QSize(0, 5))
        self.title_label_3.setMaximumSize(QSize(16777215, 7))
        self.title_label_3.setFont(font)
        self.title_label_3.setStyleSheet(u"color: white;")

        self.verticalLayout_3.addWidget(self.title_label_3)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setStyleSheet(u"font: 24pt \"Segoe UI\";")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_17 = QFrame(self.frame_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 80))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(125, 0))
        self.label_10.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setMaximumSize(QSize(70, 16777215))
        self.label_11.setStyleSheet(u"")
        self.label_11.setPixmap(QPixmap(u"./imagenes/login.png"))

        self.horizontalLayout_7.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_7.addWidget(self.label_12)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 130))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(5, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(10, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(240, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.usuario = QLineEdit(self.frame_22)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(10, 0, 225, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.usuario.setFont(font1)
        self.usuario.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(48, 127, 226);\n"
"\n"
"\n"
"border-radius: 5px;")

        self.horizontalLayout_9.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(10, 0))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_24)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(10, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(240, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.contrasena = QLineEdit(self.frame_23)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setGeometry(QRect(10, 10, 225, 40))
        self.contrasena.setFont(font1)
        self.contrasena.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(48, 127, 226);\n"
"\n"
"\n"
"border-radius: 5px;")
        self.contrasena.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_10.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(10, 0))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_25)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 1))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_19)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.texto_error = QLabel(self.frame_19)
        self.texto_error.setObjectName(u"texto_error")
        self.texto_error.setMinimumSize(QSize(250, 0))
        self.texto_error.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 10pt \"Arial\";")

        self.horizontalLayout_2.addWidget(self.texto_error, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_9.addWidget(self.frame_19)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.iniciar_button = QPushButton(self.frame_14)
        self.iniciar_button.setObjectName(u"iniciar_button")
        self.iniciar_button.setMinimumSize(QSize(0, 35))
        self.iniciar_button.setMaximumSize(QSize(16777174, 16777215))
        self.iniciar_button.setStyleSheet(u"QPushButton{background-color: rgb(116, 170, 80);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(44, 148, 44);\n"
"}")

        self.horizontalLayout_8.addWidget(self.iniciar_button)

        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame_15)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.title_label_2 = QLabel(self.frame_3)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 7))
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet(u"color: white;")

        self.verticalLayout_3.addWidget(self.title_label_2)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 0, 181, 131))
        self.label_8.setStyleSheet(u"image: url(:/imagen/logo.png);")
        self.title_label_4 = QLabel(self.frame_10)
        self.title_label_4.setObjectName(u"title_label_4")
        self.title_label_4.setGeometry(QRect(10, 0, 21, 71))
        self.title_label_4.setMinimumSize(QSize(15, 0))
        self.title_label_4.setFont(font)
        self.title_label_4.setStyleSheet(u"color: white;")

        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_11)


        self.horizontalLayout_6.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_7)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_10.addWidget(self.content_frame_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(InicioSesion)

        QMetaObject.connectSlotsByName(InicioSesion)
    # setupUi

    def retranslateUi(self, InicioSesion):
        InicioSesion.setWindowTitle(QCoreApplication.translate("InicioSesion", u"Form", None))
        self.title_label.setText("")
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.title_label_3.setText("")
#if QT_CONFIG(tooltip)
        self.frame_12.setToolTip(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Inicio de sesi\u00f3n</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Inicio de sesi\u00f3n</span></p></body></html>", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
#if QT_CONFIG(whatsthis)
        self.usuario.setWhatsThis(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.usuario.setInputMask("")
        self.usuario.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("InicioSesion", u"          Ingrese su usuario", None))
#if QT_CONFIG(whatsthis)
        self.contrasena.setWhatsThis(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.contrasena.setInputMask("")
        self.contrasena.setText("")
        self.contrasena.setPlaceholderText(QCoreApplication.translate("InicioSesion", u"        Ingrese su contrase\u00f1a", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.texto_error.setToolTip(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.texto_error.setWhatsThis(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.texto_error.setText(QCoreApplication.translate("InicioSesion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_3.setText("")
        self.label_13.setText("")
        self.iniciar_button.setText(QCoreApplication.translate("InicioSesion", u"Iniciar", None))
        self.label_14.setText("")
        self.title_label_2.setText("")
        self.label_8.setText("")
        self.title_label_4.setText("")
    # retranslateUi

