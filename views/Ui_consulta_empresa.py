# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consulta_empresa.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_consulta_empresa(object):
    def setupUi(self, consulta_empresa):
        if not consulta_empresa.objectName():
            consulta_empresa.setObjectName(u"consulta_empresa")
        consulta_empresa.resize(547, 298)
        consulta_empresa.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(consulta_empresa)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, -1)
        self.central_frame = QFrame(consulta_empresa)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"QWidget#central_frame{border: 1px solid rgb(249,66,58);}")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(151, 153, 155);\n"
"\n"
"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contenido_frame = QFrame(self.background_frame)
        self.contenido_frame.setObjectName(u"contenido_frame")
        self.contenido_frame.setStyleSheet(u"background-color: rgb(179, 179, 179)")
        self.contenido_frame.setFrameShape(QFrame.StyledPanel)
        self.contenido_frame.setFrameShadow(QFrame.Raised)
        self.botones_frame = QFrame(self.contenido_frame)
        self.botones_frame.setObjectName(u"botones_frame")
        self.botones_frame.setGeometry(QRect(440, 10, 81, 31))
        self.botones_frame.setFrameShape(QFrame.StyledPanel)
        self.botones_frame.setFrameShadow(QFrame.Raised)
        self.minimizar = QToolButton(self.botones_frame)
        self.minimizar.setObjectName(u"minimizar")
        self.minimizar.setGeometry(QRect(30, 0, 21, 20))
        self.minimizar.setStyleSheet(u"border-style: solid;\n"
"border-with 0px;")
        icon = QIcon()
        icon.addFile(u"./iconos/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizar.setIcon(icon)
        self.minimizar.setIconSize(QSize(25, 25))
        self.maximizar = QToolButton(self.botones_frame)
        self.maximizar.setObjectName(u"maximizar")
        self.maximizar.setGeometry(QRect(50, 0, 25, 19))
        self.maximizar.setStyleSheet(u"border-style: solid;\n"
"border-with 0px;")
        icon1 = QIcon()
        icon1.addFile(u"./iconos/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizar.setIcon(icon1)
        self.maximizar.setIconSize(QSize(25, 25))
        self.tabla_frame = QFrame(self.contenido_frame)
        self.tabla_frame.setObjectName(u"tabla_frame")
        self.tabla_frame.setGeometry(QRect(10, 50, 491, 211))
        self.tabla_frame.setFrameShape(QFrame.StyledPanel)
        self.tabla_frame.setFrameShadow(QFrame.Raised)
        self.titulo_cliente = QLabel(self.tabla_frame)
        self.titulo_cliente.setObjectName(u"titulo_cliente")
        self.titulo_cliente.setGeometry(QRect(10, 10, 141, 16))
        font = QFont()
        font.setPointSize(10)
        self.titulo_cliente.setFont(font)
        self.ingre_nombre = QLineEdit(self.tabla_frame)
        self.ingre_nombre.setObjectName(u"ingre_nombre")
        self.ingre_nombre.setGeometry(QRect(160, 10, 181, 20))
        self.ingre_nombre.setStyleSheet(u"background-color:white\n"
"")
        self.tabla_empresa = QTableWidget(self.tabla_frame)
        if (self.tabla_empresa.rowCount() < 4):
            self.tabla_empresa.setRowCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_empresa.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_empresa.setVerticalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_empresa.setObjectName(u"tabla_empresa")
        self.tabla_empresa.setGeometry(QRect(20, 40, 461, 161))
        self.tabla_empresa.setRowCount(4)
        self.tabla_empresa.horizontalHeader().setVisible(True)
        self.tabla_empresa.horizontalHeader().setHighlightSections(True)
        self.tabla_empresa.horizontalHeader().setStretchLastSection(True)
        self.tabla_empresa.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.contenido_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(consulta_empresa)

        QMetaObject.connectSlotsByName(consulta_empresa)
    # setupUi

    def retranslateUi(self, consulta_empresa):
        consulta_empresa.setWindowTitle(QCoreApplication.translate("consulta_empresa", u"Form", None))
        self.minimizar.setText(QCoreApplication.translate("consulta_empresa", u"...", None))
        self.maximizar.setText(QCoreApplication.translate("consulta_empresa", u"...", None))
        self.titulo_cliente.setText(QCoreApplication.translate("consulta_empresa", u"Nombre de la empresa:", None))
    # retranslateUi
