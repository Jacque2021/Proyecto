# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Diarios_polizas.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_diarios_polizas(object):
    def setupUi(self, diarios_polizas):
        if not diarios_polizas.objectName():
            diarios_polizas.setObjectName(u"diarios_polizas")
        diarios_polizas.resize(636, 490)
        diarios_polizas.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(diarios_polizas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, -1)
        self.central_frame = QFrame(diarios_polizas)
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
        font = QFont()
        font.setPointSize(12)
        self.contenido_frame.setFont(font)
        self.contenido_frame.setStyleSheet(u"background-color: rgb(179, 179, 179)")
        self.contenido_frame.setFrameShape(QFrame.StyledPanel)
        self.contenido_frame.setFrameShadow(QFrame.Raised)
        self.botones_frame = QFrame(self.contenido_frame)
        self.botones_frame.setObjectName(u"botones_frame")
        self.botones_frame.setGeometry(QRect(520, 10, 81, 31))
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
        self.tabla_frame.setGeometry(QRect(10, 50, 591, 381))
        self.tabla_frame.setFrameShape(QFrame.StyledPanel)
        self.tabla_frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.tabla_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 591, 41))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.boton_buscar = QPushButton(self.frame_3)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(510, 10, 71, 31))
        self.boton_buscar.setFont(font)
        self.boton_buscar.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.numero_fin = QLineEdit(self.frame_3)
        self.numero_fin.setObjectName(u"numero_fin")
        self.numero_fin.setGeometry(QRect(320, 10, 71, 22))
        self.numero_fin.setStyleSheet(u"QLineEdit#numero_fin{border: 1px solid rgb(0, 0, 0);}")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 10, 101, 25))
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setFont(font)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(12, 12, 82, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font)
        self.numero_ini = QLineEdit(self.frame_3)
        self.numero_ini.setObjectName(u"numero_ini")
        self.numero_ini.setGeometry(QRect(100, 10, 91, 22))
        self.numero_ini.setStyleSheet(u"QLineEdit#numero_ini{border: 1px solid rgb(0, 0, 0);}")
        self.boton_imprimir = QPushButton(self.tabla_frame)
        self.boton_imprimir.setObjectName(u"boton_imprimir")
        self.boton_imprimir.setGeometry(QRect(510, 330, 75, 31))
        self.boton_imprimir.setFont(font)
        self.boton_imprimir.setStyleSheet(u"background-color: rgb(116, 170, 80);")
        self.tabla_datos = QTableWidget(self.tabla_frame)
        if (self.tabla_datos.rowCount() < 4):
            self.tabla_datos.setRowCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_datos.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_datos.setVerticalHeaderItem(1, __qtablewidgetitem1)
        self.tabla_datos.setObjectName(u"tabla_datos")
        self.tabla_datos.setGeometry(QRect(10, 50, 571, 271))
        self.tabla_datos.setRowCount(4)
        self.tabla_datos.horizontalHeader().setVisible(True)
        self.tabla_datos.horizontalHeader().setHighlightSections(True)
        self.tabla_datos.horizontalHeader().setStretchLastSection(True)
        self.tabla_datos.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.contenido_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(diarios_polizas)

        QMetaObject.connectSlotsByName(diarios_polizas)
    # setupUi

    def retranslateUi(self, diarios_polizas):
        diarios_polizas.setWindowTitle(QCoreApplication.translate("diarios_polizas", u"Form", None))
        self.minimizar.setText(QCoreApplication.translate("diarios_polizas", u"...", None))
        self.maximizar.setText(QCoreApplication.translate("diarios_polizas", u"...", None))
        self.boton_buscar.setText(QCoreApplication.translate("diarios_polizas", u"Buscar", None))
        self.label_8.setText(QCoreApplication.translate("diarios_polizas", u"N\u00famero final:", None))
        self.label_6.setText(QCoreApplication.translate("diarios_polizas", u"N\u00fam inicial:", None))
        self.boton_imprimir.setText(QCoreApplication.translate("diarios_polizas", u"Imprimir", None))
    # retranslateUi

