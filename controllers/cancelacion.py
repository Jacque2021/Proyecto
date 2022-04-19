from string import punctuation
from views.Ui_borrar_prestamo import Ui_consulta_cliente
from decimal import Decimal
#from views.Ui_consulta_cliente import Ui_consulta_cliente
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from views import components
from controllers.cancelado import mensaje
import datetime 
from database import recipes
class Error(QWidget, Ui_consulta_cliente):
    def __init__(self, parent=None): #capturar instancia de mainwindows
        super().__init__(parent)
        self.setupUi(self) #1
        self.setWindowFlag(Qt.Window)
        self.config_table() #medidas de la tabla
        self.set_table_data()
        self.ingre_nombre.returnPressed.connect(self.search)  #returnPressed= al dar enter hace la accion
        self.ingre_nombre.textChanged.connect(self.restore_table_data)

        
    """*********************  DISEÑAR LA TABLA   ***************************"""  
    def populate_table(self, data): #crea tabla
        self.tabla_clientes.setRowCount(len(data)) #cantidad de filas que va tener
        for(index_row, row) in enumerate(data):   #index_row contiene indice de la fila y row contiene el dato de la fila
            #enumerate(data) retorna el indice y los datos
            for(index_cell, cell) in enumerate(row): #idex de cada celda   enumerate(row)= por cada fila
                self.tabla_clientes.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
            self.tabla_clientes.setCellWidget(
                index_row, 7, self.build_action_buttons()
            )
                
    def  config_table(self): #MEDIDAS DE LA TABLA
        column_labels=("","ID", "NOMBRE", "APELLIDOS", "PRESTAMO", "PAGO", "FECHA REGISTRO DE PAGO", "CANCELAR")
        #self.tabla_clientes.setAlternatingRowColors(True) #color alterno
        self.tabla_clientes.setColumnCount(len(column_labels)) 
        self.tabla_clientes.setHorizontalHeaderLabels(column_labels)
        self.tabla_clientes.setColumnWidth(0, 1)
        self.tabla_clientes.setColumnWidth(1, 30) #ancho de la tabla en la celda ID
        self.tabla_clientes.setColumnWidth(2, 100) #ancho de la celda Nombre
        self.tabla_clientes.setColumnWidth(3, 140) #ancho de la celda Apellidos
        self.tabla_clientes.setColumnWidth(4, 80) #ancho prestamo
        self.tabla_clientes.setColumnWidth(5, 70) #ancho pago 
        self.tabla_clientes.setColumnWidth(6, 180) #ancho fecha 
        self.tabla_clientes.setColumnWidth(7, 30)
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(30) #tamaño de las filas 
        self.tabla_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)#selecciona la selda completa
        self.tabla_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)#deshabilita la edicion
        
    def set_table_data(self):
        data=recipes.vista_cancelaciones()  
        self.populate_table(data)  
    """*********************  AGREGAR BOTON DE BORRAR   ***************************"""  
    def build_action_buttons(self):

        delete_button= components.Button("delete")
        
        buttons_layout=QHBoxLayout()
        buttons_layout.addWidget(delete_button)
        #Los layout deben estar dentro de un frame
        buttons_frame=QFrame()
        buttons_frame.setLayout(buttons_layout)
        
        delete_button.clicked.connect(self.delete_recipe)
        return buttons_frame
    """*********************  BUSQUEDA DE PAGO PRESTAMO   ***************************"""
    #Metodo de buscar
    def search(self):
        param = self.ingre_nombre.text()
        if param != "":
            data = recipes.select_cancelacion(param)
            self.populate_table(data)
    #METODO DE REGRESAR TODOS LOS PARAMETROS DESPUES DE BUSCAR
    def restore_table_data(self):
        param = self.ingre_nombre.text()
        if param == "":
            self.set_table_data()
    """*********************  OBTIENE EL ID DEL PAGO PRESTAMO   ***************************"""             
    def get_recipe_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        recipe_id = table.model().data(cell_id_index)
        return recipe_id
    """*********************  FUNCION DE BORRAR O CANCELAR PAGO PRESTAMO   ***************************"""  
    def delete_recipe(self):
        button = self.sender()
        table = self.tabla_clientes
        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            pago=recipes.llamar_datos_pago_prestamo(recipe_id) #id_pago_prestamo
            id_prestamo=int(pago[0])
            saldo=Decimal(pago[1])
            interes=Decimal(pago[2])
            amortizacion=Decimal(pago[3])
            aumuluado=Decimal(pago[4])
            fecha=datetime.datetime.strptime(pago[5],'%Y-%m-%d %H:%M:%S.%f')
            moratorio=Decimal(pago[7])
            bandera=int(pago[6]) #para saber si pago en efectivo o con ahorro 
            datos=recipes.llamar_datos_prestamo_cliente(id_prestamo)
            punctuacion=int(datos[0])
            correo=str(datos[1])
            renta=Decimal(datos[2])
            periodo=datos[3]
            id_cliente=int(datos[4])
            if moratorio>0 and bandera==1:
                ahorro=recipes.llamar_capital(id_cliente)
                capital=Decimal(ahorro[0])
                importe=Decimal(ahorro[2])
                id_ahorro=ahorro[1]
                puntos=punctuacion+1
                s=renta+moratorio
                cap=capital+s
                correo2=correo
                importe2=importe
                bu=(puntos, correo2)
                if recipes.editar_puntos_clientes(id_cliente, bu):
                 print("Editada la puntuacion")
                na=(cap,importe2)
                if recipes.editar_capital_ahorro(id_ahorro, na):
                     print("Editada capital")
            elif moratorio==0 and bandera==1:
                ahorro=recipes.llamar_capital(id_cliente)
                capital=Decimal(ahorro[0])
                importe=Decimal(ahorro[2])
                id_ahorro=int(ahorro[1])
                puntos=punctuacion
                cap=capital+renta
                correo2=correo
                importe2=importe
                bu=(puntos, correo2)
                na=(cap,importe2)
                if recipes.editar_capital_ahorro(id_ahorro, na):
                     print("Editada capital")
                if recipes.editar_puntos_clientes(id_cliente, bu):
                 print("Editada la puntuacion")
            elif bandera==0 and moratorio==0:
                puntos=punctuacion-1
                correo2=correo
                bu=(puntos, correo2)
                if recipes.editar_puntos_clientes(id_cliente, bu):
                 print("Editada la puntuacion")
            elif bandera==0 and moratorio>0:
                puntos=punctuacion
                correo2=correo
                bu=(puntos, correo2)
                if recipes.editar_puntos_clientes(id_cliente, bu):
                 print("Editada la puntuacion")
            else: None
            """REALIZA CAMBIOS DEL PRESTAMO"""
            saldo_insolito=saldo+amortizacion
            interes2=interes
            amortizacion2=amortizacion
            acum=aumuluado-amortizacion
            fecha_lim=fecha
            nuevo=(saldo_insolito, interes2,amortizacion2,acum,str(fecha_lim))
            if recipes.editar_prestamo(id_prestamo, nuevo):
                 print("editado el prestamo")
            if recipes.borra_pago(recipe_id):
                self.set_table_data()
                print("dato borrado")
            self.Open_emergente()
    """ABRIR VENTANA EMERGENTE"""
    def Open_emergente(self):
        self.window=mensaje(self)
        self.window.show()
    