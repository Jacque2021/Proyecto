import sys

from PySide6 import QtCore, QtGui, QtWidgets


class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.baja_id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.baja_id.setGeometry(QtCore.QRect(320, 480, 211, 41))
        self.baja_id.setReadOnly(True)
        self.lista_clientes = QtWidgets.QTableWidget(self.centralwidget)
        self.lista_clientes.setGeometry(QtCore.QRect(45, 41, 701, 371))
        self.lista_clientes.setColumnCount(2)
        self.lista_clientes.setRowCount(2)

        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista_clientes.setItem(1, 1, item)
        item = self.lista_clientes.verticalHeaderItem(0)
        item.setText("1")
        item = self.lista_clientes.verticalHeaderItem(1)
        item.setText("2")
        item = self.lista_clientes.horizontalHeaderItem(0)
        item.setText("Id.")
        item = self.lista_clientes.horizontalHeaderItem(1)
        item.setText("Nombre")
        item = self.lista_clientes.item(0, 0)
        item.setText("1")
        item = self.lista_clientes.item(0, 1)
        item.setText("Luís Enrique")
        item = self.lista_clientes.item(1, 0)
        item.setText("5")
        item = self.lista_clientes.item(1, 1)
        item.setText("Luciana Altamira")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 480, 81, 41))
        self.setCentralWidget(self.centralwidget)
        self.label.setText("Ide. Cliente")

        self.lista_clientes.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.lista_clientes.itemSelectionChanged.connect(self.on_selec_change)



    
    #@QtCore.pyqtSlot() 
    def on_selec_change(self):
        row = self.lista_clientes.currentRow()
        item = self.lista_clientes.item(row, 0)
        if item is not None:
            self.baja_id.setPlainText(item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    app.exec()