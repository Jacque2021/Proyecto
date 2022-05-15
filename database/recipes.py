#OPCIONES PARA INTERACTUAR CON LA BASE DE DATOS
"OPCIONES PARA INTERACTUAR CON LA BASE DE DATOS"
#%S= le vamos a dar valores a las filas de la tabla"
import datetime
from mysql import connector
from database.connection import create_conection

#METODO PARA LLENAR TABLA DE CLIENTES EN LA INTERFAZ DE BUSQUEDA
def select_tabal_clientes():
    conn=create_conection()
    sql="""SELECT Id_cliente,nombre,apellidos  FROM clientes"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#METODO PARA LLENAR TABLA DE CLIENTES EN LA INTERFAZ DE BUSQUEDA
def select_tabal_clientes2():
    conn=create_conection()
    sql="""SELECT clientes.Id_cliente,nombre,apellidos  
        FROM clientes
        INNER JOIN prestamos ON prestamos.Id_cliente = clientes.Id_cliente;"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#METODO DE BUSQUEDA DE CLIENTES
def select_by_parameter(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT Id_cliente,nombre, apellidos  FROM clientes
            WHERE Id_cliente LIKE %s OR nombre LIKE %s OR apellidos LIKE %s
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#************   METODO DE BUSQUEDA PARA INGRESAR NOMBRE DEL CLIENTE CON SU ID    ************
def select_by_cliente(_id):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, nombre FROM clientes
            WHERE Id_cliente= {_id}
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()      
#***************************   Almacena ID obtenido de la interfaz de busqueda del cliente    ***************************  
        
def select_cliente(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, CONCAT_WS(' ', nombre, apellidos),puntuacion FROM clientes
            WHERE Id_cliente= %s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()  
#***************************   BUSCAR SI EL CLIENTE TIENE OTRO PRESTAMO PENDIENTE    *************************** 
def condicion(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT clientes.Id_cliente, clientes.puntuacion, prestamos.saldo_insolito, prestamos.cantidad_prestamo
                FROM clientes
                INNER JOIN prestamos ON clientes.Id_cliente=prestamos.Id_cliente
                WHERE clientes.Id_cliente= %s AND prestamos.saldo_insolito>0
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        #cur.close()
        conn.close() 
        
def condicion2(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT nuevo_ahorro.capital
                FROM clientes
                INNER JOIN nuevo_ahorro ON clientes.Id_cliente=nuevo_ahorro.id_cliente
                WHERE clientes.Id_cliente= %s AND nuevo_ahorro.capital
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        #cur.close()
        conn.close()       
"""**************************      INSERTAR DATOS A LA TABLA DE PRESTAMOS       **************************"""
def insert_Prestamos (data):
    conn=create_conection()
    sql="""INSERT INTO prestamos (Id_cliente, cantidad_prestamo, frecuencia, tiempo, periodo, Iva,
                                Iva_div, saldo_insolito, renta, interes, amortizacion, amortizacion_acum,
                                fecha_inicio, fecha_siguiente,nombre_codeudor,Garantia, link)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recipes function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""**************************      LLAMA DATOS A LA TABLA DE PAGOS DE PRESTAMOS       **************************"""
def select_info_cliente_prestamo(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT clientes.Id_cliente, CONCAT_WS(' ', clientes.nombre, clientes.apellidos), 
		prestamos.cantidad_prestamo, prestamos.interes, prestamos.amortizacion, prestamos.renta,prestamos.fecha_siguiente, prestamos.Id_prestamo, prestamos.saldo_insolito, prestamos.Iva_div, prestamos.amortizacion_acum
        FROM clientes
        INNER JOIN prestamos ON clientes.Id_cliente=prestamos.Id_cliente
        WHERE clientes.Id_cliente=%s and saldo_insolito>1
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""**************************      INSERTAR DATOS A LA TABLA DE PAGOS DE PRESTAMOS       **************************"""
def insert_Pagos (data):
    conn=create_conection()
    sql="""INSERT INTO pagos (Id_prestamo, saldo_insolito, interes, amortizacion,amortizacion_acum,
                                limite_time, pago_time, sig_time, moratorio, bandera,link)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recipes function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
"""**************************      EDITA LA TABLA DE PRESTAMOS       **************************"""      
def update_prestamo(_id, data):
    conn=create_conection()
    sql=f"""UPDATE prestamos SET 
                            saldo_insolito=%s,
                            interes=%s,
                            amortizacion=%s,
                            amortizacion_acum=%s,
                            fecha_siguiente=%s
                        WHERE Id_prestamo={_id}
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
"""**************************      MANDAR LLAMAR CAPITAL DE AHORRO       **************************"""  
def capital_ahorro(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT capital, importe
                FROM nuevo_ahorro
                WHERE id_cliente= %s 
                ORDER BY id_ahorro desc
                LIMIT 1
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close()      

"""**************************      PAGAR CON AHORRO       **************************"""    
def pagar_con_ahorro(_id, data):
    conn=create_conection()
    sql=f"""UPDATE nuevo_ahorro SET 
                            capital=%s,
                            importe=%s
                        WHERE id_cliente={_id}
                        ORDER BY id_ahorro desc
                        LIMIT 1
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()   
"""**************************      MANDAR LLAMAR CLIENTES PARA LOS PUNTOS      **************************"""  
def clientes_puntos(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT puntuacion, nombre
                FROM clientes
                WHERE Id_cliente= %s 
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close()      

"""**************************      AUMENTA O DISMINUYE PUNTOS CLIENTES       **************************"""    
def clientes_puntos_mas(_id, data):
    conn=create_conection()
    sql=f"""UPDATE clientes SET 
                            puntuacion=%s,
                            nombre=%s
                        WHERE Id_cliente={_id}
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()   
        
#***************************   CREAR TABLA DE PAGO PRESTAMOS REALIZADO    *************************** 
def vista_cancelaciones():
    conn=create_conection()
    sql="""SELECT pagos.Id_pago,clientes.Id_cliente, clientes.nombre, clientes.apellidos,
		    prestamos.cantidad_prestamo, prestamos.renta, pagos.pago_time
            FROM clientes
            INNER JOIN prestamos ON prestamos.Id_cliente =clientes.Id_cliente
            INNER JOIN pagos ON prestamos.Id_prestamo=pagos.Id_prestamo
            ORDER BY pagos.Id_pago desc
            LIMIT 80"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#***************************   SELECCIONA LOS DATOS DE PAGO    *************************** 
def select_pago_borrar(_id):
    conn=create_conection()
    sql=f"""SELECT * FROM pagos WHERE Id_pago={_id}"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipe=cur.fetchone()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#***************************   BORRA LOS DATOS SELECCIONADOS DE PAGO    ***************************        
def borra_pago(_id):
    conn = create_conection()
    sql = f""" DELETE FROM pagos
            WHERE Id_pago = {_id}                       
            """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#***************************   MANDAR LLAMAR LOS DATOS DE PAGO PRESTAMO    ***************************
def llamar_datos_pago_prestamo(Id_pago):  #Id_pago prestamo
    conn = create_conection()
    sql = f"""SELECT Id_prestamo, saldo_insolito, interes, amortizacion, amortizacion_acum, limite_time, bandera, moratorio, pago_time
                FROM pagos
                WHERE Id_pago= %s 
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_pago,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
#***************************   EDITAR DATOS DE PRESTAMO    ***************************
def editar_prestamo(_id, data):
    conn=create_conection()
    sql=f"""UPDATE prestamos SET 
                            saldo_insolito=%s,
                            interes=%s,
                            amortizacion=%s,
                            amortizacion_acum=%s,
                            fecha_siguiente=%s
                            
                        WHERE Id_prestamo={_id}
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
#***************************   MANDAR LLAMAR LOS DATOS DE PRESTAMOS Y CLIENTES   ***************************
def llamar_datos_prestamo_cliente(Id_prestamo):  #Id_pago prestamo
    conn = create_conection()
    sql = f"""SELECT clientes.puntuacion, clientes.correo, prestamos.renta, prestamos.periodo, clientes.Id_cliente
            FROM clientes
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE prestamos.Id_prestamo= %s 
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_prestamo,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
#***************************   MANDAR LLAMAR LOS DATOS DE AHORRO    ***************************
def llamar_capital(Id_cliente):  #Id_pago prestamo
    conn = create_conection()
    sql = f"""SELECT capital, id_ahorro, importe
            FROM nuevo_ahorro
            WHERE id_cliente= %s 
            ORDER BY id_ahorro desc
            limit 1
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
#***************************   EDITAR DATOS DE AHORRO    ***************************
def editar_capital_ahorro(_id, data):
    conn=create_conection()
    sql=f"""UPDATE nuevo_ahorro SET 
                            capital=%s,
                            importe=%s
                            
                        WHERE id_ahorro={_id}
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
#***************************   EDITAR DATOS DE CLIENTE    ***************************
def editar_puntos_clientes(_id, data):
    conn=create_conection()
    sql=f"""UPDATE clientes SET 
                            puntuacion=%s,
                            correo=%s
                            
                        WHERE Id_cliente={_id}
                        """
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
""" ******************   MANDAR LLAMAR PRESTAMOS *****************"""
def ultimo_prestamo():
    conn = create_conection()
    sql = f"""SELECT Id_cliente,cantidad_prestamo,frecuencia,tiempo,periodo,Iva,Iva_div,saldo_insolito,renta,interes,amortizacion
                FROM prestamos
                ORDER BY Id_prestamo desc
                LIMIT 1
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close() 
""" ******************   MANDAR LLAMAR DATOS DE LA EMPRESA *****************"""
def empresa():
    conn = create_conection()
    sql = f"""SELECT nombre_empresa, ubicacion_emp
                FROM mi_empresa
                LIMIT 1
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close()
""" ******************   MANDAR LLAMAR DATOS DEL CLIENTE *****************"""
def select_clientes(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, CONCAT_WS(' ', nombre, apellidos),telefono,telefono_add,direccion,correo,fecha_nacimiento 
                FROM clientes
            WHERE Id_cliente= %s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#METODO DE BUSQUEDA DE CLIENTES
def select_cancelacion(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT pagos.Id_pago,clientes.Id_cliente, clientes.nombre, clientes.apellidos,
		    prestamos.cantidad_prestamo, prestamos.renta, pagos.pago_time
            FROM clientes
            INNER JOIN prestamos ON prestamos.Id_cliente =clientes.Id_cliente
            INNER JOIN pagos ON prestamos.Id_prestamo=pagos.Id_prestamo
            WHERE clientes.Id_cliente LIKE %s OR clientes.nombre LIKE %s OR clientes.apellidos LIKE %s
            """     
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
"""**************************      LLAMA DATOS PARA CREAR PDF DE PAGO PRESTAMOS       **************************"""
def select_info_pdf_pagos(Id_prestamo):
    conn = create_conection()
    sql = f"""SELECT clientes.Id_cliente, CONCAT_WS(' ', clientes.nombre, clientes.apellidos), clientes.telefono, clientes.telefono_add, clientes.direccion, clientes.correo, clientes.fecha_nacimiento,
		    prestamos.cantidad_prestamo, prestamos.periodo, prestamos.Iva, prestamos.renta, prestamos.fecha_inicio, prestamos.fecha_siguiente, prestamos.saldo_insolito, prestamos.amortizacion
            FROM clientes
            INNER JOIN prestamos ON clientes.Id_cliente=prestamos.Id_cliente
            WHERE prestamos.Id_prestamo=%s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_prestamo,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
"""**************************      LLAMA DATOS PARA CREAR PDF DE PAGO PRESTAMOS       **************************"""
def select_info_pdf_pagos_Matriz(Id_prestamo):
    conn = create_conection()
    sql = f"""SELECT pagos.limite_time, prestamos.renta, pagos.interes, pagos.amortizacion, 
            pagos.amortizacion_acum, pagos.moratorio, pagos.saldo_insolito, pagos.pago_time
            FROM prestamos 
            INNER JOIN pagos ON prestamos.Id_prestamo=pagos.Id_prestamo
            WHERE prestamos.Id_prestamo=%s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_prestamo,))
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close()
"""***************PARA NOTIFICACIONES*******************"""
def conteo(fecha):
    conn = create_conection()
    hoy=datetime.date.today()
    sql = f"""SELECT count(*)fecha_siguiente
            FROM prestamos
            WHERE  fecha_siguiente>={hoy} AND fecha_siguiente<=%s and saldo_insolito>0
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(fecha,))
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        #cur.close()
        conn.close()
"""***************PARA TABLA DE NOTIFICACIONES*******************"""
def tabla_notificacio(fecha):
    conn = create_conection()
    hoy=datetime.date.today()
    sql = f"""SELECT  clientes.Id_cliente, clientes.nombre, clientes.apellidos, prestamos.cantidad_prestamo, prestamos.renta, prestamos.fecha_siguiente
            FROM clientes
            INNER JOIN prestamos ON prestamos.Id_cliente =clientes.Id_cliente
            WHERE  fecha_siguiente>={hoy} AND fecha_siguiente<=%s and saldo_insolito>0
            ORDER BY fecha_siguiente desc
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(fecha,))
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        #cur.close()
        conn.close()
"""***************PARA BUSQUEDA EN TABLA DE NOTIFICACIONES*******************"""    
def busqueda_notificacion(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT clientes.Id_cliente, clientes.nombre, clientes.apellidos, prestamos.cantidad_prestamo, prestamos.renta, prestamos.fecha_siguiente
            FROM clientes
            INNER JOIN prestamos ON prestamos.Id_cliente =clientes.Id_cliente
            WHERE clientes.Id_cliente LIKE %s OR clientes.nombre LIKE %s OR clientes.apellidos LIKE %s
            """     
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


"""*********INSERTAR DATOS A LA TABLA DE MI EMPRESA ************"""
def insertar_empresa(data):
    conn = create_conection()
    sql = """INSERT INTO mi_empresa(RFC, nombre_empresa, ubicacion_emp, inicio_ejercicio, fin_ejercicio,
     tipo_periodo, usuario, contras, host, bd)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)                        
            """
            
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""****************INSERTAR DATOS A LA TABLA RESPALDAR EMPRESA *******************"""
def respladar_empresa(data):
    conn = create_conection()
    sql = """INSERT INTO respaldar_empresa(RFC, nombre_empresa, nombre_respaldo, fecha_respaldo,
             hora_respaldo, ruta)
            VALUES(%s, %s, %s, %s, %s, %s)                        
            """
            
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""*********INSERTAR DATOS A LA TABLA CHEQUES ************"""
def crear_cheque(data):
    conn = create_conection()
    
    sql = """ INSERT INTO cheques(id_cliente, nombre, apellidos, fecha_emision ,
    monto_total, beneficiario, descripcion)
            VALUES(%s, %s, %s, %s, %s, %s, %s)                        
            """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""***************METODO PARA LLENAR TABLA DE CLIENTES tabla cheques*****************"""
def select_cliente_cheque(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, nombre, apellidos FROM clientes
            WHERE Id_cliente= %s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 
  

"""*************** Tabla consulta cheques *****************"""
def select_tabal_cheques():
    conn=create_conection()
    sql="""SELECT Id_cliente,nombre,apellidos, id_cheque, fecha_emision, monto_total,
        beneficiario, descripcion  FROM cheques"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""*************** Tabla consulta retiro ahorro *****************"""
def select_tabal_re_ahorro():
    conn=create_conection()
    sql="""SELECT  id_cliente, nombre, apellidos FROM clientes"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""*********INSERTAR DATOS A LA TABLA NUEVO AHORRO ************"""
def crear_ahorro(data):
    conn = create_conection()
    
    sql = """ INSERT INTO nuevo_ahorro(id_cliente, nombre, apellidos, importe, tea, plazo,
     fecha_vencimiento, fecha_apertura, fecha_inicio, interes, cancelacion, capital)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)                        
            """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""*********Almacena ID obtenido de la interfaz de busqueda del cliente NUEVO AHORRO ************"""
def select_cliente2(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, nombre, apellidos  FROM clientes
            WHERE Id_cliente= %s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close() 


"""*********Tabla consulta retiro ahorro ************"""
def select_tabal_re_ahorro():
        conn=create_conection()
        sql="""SELECT  id_cliente, nombre, apellidos FROM clientes"""
        try:
            cur=conn.cursor()
            cur.execute(sql)
            recipes=cur.fetchall()  #devuelva datos seleccionados
            #conn.commit()    se utiliza cuando se haga cambios en la BD
            return recipes
        except connector.Error as err:
            print(f"Error at select_all function: {err.msg}")
            return False
        finally:
            cur.close()
            conn.close()


"""*********INSERTAR DATOS A LA TABLA RETIRAR AHORRO ************"""
def retirar_ahorro(data):
    conn = create_conection()
    
    sql = """ INSERT INTO retirar_ahorro(id_cliente, nombre, apellidos,capital_ahorrado,
                            total_retiro,capital_actualizado,descripcion, fecha_retiro,hora_retiro)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)                        
            """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#METODO PARA LLENAR TABLA DE EMPRESA
def buscar_empresa():
    conn=create_conection()
    sql="""SELECT RFC, nombre_empresa FROM mi_empresa"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
    
#METODO PARA LLENAR TABLA DE CLIENTES 2
def buscar2c():
    conn=create_conection()
    sql="""SELECT Id_cliente, nombre, apellidos, telefono, 
     telefono_add, direccion, correo, fecha_nacimiento, puntuacion, municipio 
     FROM clientes
     """
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#METODO DE BUSQUEDA DE EMPRESA
def buscar_e(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT RFC,nombre_empresa FROM mi_empresa
            WHERE RFC LIKE %s OR nombre_empresa LIKE %s 
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#METODO DE BUSQUEDA DE CLIENTES 2
def buscarc(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT Id_cliente, nombre, apellidos, telefono, telefono_add, direccion, correo, fecha_nacimiento, 
         puntuacion, municipio FROM clientes WHERE Id_cliente LIKE %s OR nombre LIKE %s 
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#********************************************ALMACENA RFC DE LA EMPRESA PARA SU BUSQUEDA**********#
def select_empresa(RFC_e):
    conn = create_conection()
    sql = f"""SELECT RFC, nombre_empresa FROM mi_empresa
            WHERE RFC= %s
            """
    try:
        cur = conn.cursor()
        cur.execute(sql,(RFC_e,))
        recipes = cur.fetchone()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""****INSERTAR DATOS A LA TABLA DE CLIENTES***"""
def insertar_clientes(data):
    conn = create_conection()
    sql = """INSERT INTO clientes(nombre, apellidos, telefono, 
     telefono_add, direccion, correo, fecha_nacimiento, puntuacion, municipio)
     VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            #VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""****INSERTAR DATOS A LA TABLA DE CATALOGO DE CUENTAS***"""
def insertar_catalogo_cuentas(data):
    conn = create_conection()
    sql = """INSERT INTO catalogo_cuentas(RFC_e, nombre_b, registro, elegircf, codigo_SAT, 
     rubro, digito_fiscal_1, digito_fiscal_2) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""****CONSULTAS PARA EL HISTORIAL DEL CLIENTE***"""
def busqueda_id(Id_cliente):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento, 
            nuevo_ahorro.importe, prestamos.cantidad_prestamo
            FROM clientes 
            INNER JOIN nuevo_ahorro ON clientes.Id_cliente=nuevo_ahorro.Id_cliente 
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.Id_cliente LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
###############################################################
def busqueda_id2(Id_cliente):
    conn = create_conection()
    sql = """SELECT Id_cliente,clientes.nombre,clientes.apellidos
            FROM clientes 
            WHERE Id_cliente LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
###############################################################      
def busqueda_nombre(nombre):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento, 
            nuevo_ahorro.importe, prestamos.cantidad_prestamo
            FROM clientes 
            INNER JOIN nuevo_ahorro ON clientes.Id_cliente=nuevo_ahorro.Id_cliente 
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.nombre LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(nombre,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def busqueda_apellidos(apellidos):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento, 
            nuevo_ahorro.importe, prestamos.cantidad_prestamo 
            FROM clientes 
            INNER JOIN nuevo_ahorro ON clientes.Id_cliente=nuevo_ahorro.Id_cliente 
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.apellidos LIKE %s
            """          
            #
    try:
        cur = conn.cursor()
        cur.execute(sql,(apellidos,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#"""ACTUALIZAR Y ELIMINAR DATOS DEL CLIENTE"""#
def actualizar_cliente(_id, data):
    conn=create_conection()
    #nombre= %s
    sql=f"""UPDATE clientes SET
                            nombre= %s, 
                            apellidos= %s,
                            telefono= %s,
                            telefono_add= %s,
                            direccion= %s,
                            correo= %s,
                            fecha_nacimiento= %s,
                            puntuacion= %s,
                            municipio= %s
                        WHERE Id_cliente={_id}"""
    try:
        cur=conn.cursor()
        cur.execute(sql, data)
        #recipes=cur.fetchall()  #devuelva datos seleccionados
        conn.commit()   # se utiliza cuando se haga cambios en la BD
        return True
    except connector.Error as err:
        print(f"Error at update function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
def eli_cliente(_id):
    conn = create_conection()
    sql = f""" DELETE FROM clientes
            WHERE Id_cliente = {_id}      
            """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()    

#********************************************ALMACENA ID DEL CLIENTE PARA SU BUSQUEDA**********#
def select_cliente3(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, nombre, apellidos, telefono, 
        telefono_add, direccion, correo, fecha_nacimiento, puntuacion, municipio FROM clientes
        WHERE Id_cliente= %s
        """
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipes = cur.fetchone()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#********************************************ALMACENA NOMBRE PARA SU BUSQUEDA**********#
def select_cliente4(nombre):
    conn = create_conection()
    sql = f"""SELECT nombre FROM clientes
        WHERE nombre= %s
        """
    try:
        cur = conn.cursor()
        cur.execute(sql,(nombre,))
        recipes = cur.fetchone()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#********************************************BUSQUEDA DE LISTADO DE POLIZAS**********#
def busqueda_rfc(numero):
    conn = create_conection()
    sql = """SELECT nueva_poliza.numero, nueva_poliza.fecha, nueva_poliza.concepto, movimientos_poliza.cargo, movimientos_poliza.abono
            FROM nueva_poliza
            INNER JOIN movimientos_poliza ON nueva_poliza.cuenta=movimientos_poliza.cuenta
            WHERE nueva_poliza.numero LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(numero,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#********************************************BUSQUEDA DE DIARIOS Y POLIZAS**********#
def filtro_numero(numero_1, numero_2):
    conn=create_conection()
    sql="""SELECT nueva_poliza.fecha, movimientos_poliza.referencia, nueva_poliza.tipo, movimientos_poliza.cuenta,
            nueva_poliza.numero, movimientos_poliza.cuenta, nueva_poliza.concepto, movimientos_poliza.cargo,
            movimientos_poliza.abono
            FROM movimientos_poliza
            INNER JOIN nueva_poliza ON movimientos_poliza.cuenta=nueva_poliza.cuenta
            WHERE nueva_poliza.numero BETWEEN %s AND %s 
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, (numero_1, numero_2))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#********************************************   METODO DE BUSQUEDA DE CUENTA    **********************************            
def select_by_cuenta(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT 
            prestamos.Id_prestamo, clientes.nombre, clientes.apellidos, fecha_inicio, fecha_siguiente, cantidad_prestamo, tiempo
            FROM prestamos INNER JOIN clientes ON prestamos.Id_cliente = clientes.Id_cliente
            WHERE clientes.Id_cliente LIKE %s OR nombre LIKE %s OR apellidos LIKE %s 
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

        
"""**************************      CONSULTA DE FILTRADO DE PAGO      **************************"""    
def filtro_pago(FECHA_1, FECHA_2):
    print("FILTRO PAGO")
    print(FECHA_1)
    print(FECHA_2)
    # FECHA_1 = f"%{FECHA_1}%"
    # FECHA_2 = f"%{FECHA_2}%"
    conn=create_conection()
    sql="""SELECT 
        id_pago,prestamos.Id_prestamo, prestamos.Id_cliente, pagos.saldo_insolito, pagos.interes, pagos.amortizacion, pagos.amortizacion_acum, limite_time,
        pago_time, sig_time, moratorio, bandera 
        FROM prestamos INNER JOIN clientes ON prestamos.Id_cliente = clientes.Id_cliente INNER JOIN pagos
        ON prestamos.Id_prestamo = pagos.id_prestamo
        WHERE limite_time BETWEEN %s  AND %s  

                        """
    # print("SQL")
    # print(sql) 
    try:
        cur = conn.cursor()
        cur.execute(sql, (FECHA_1, FECHA_2))
        #print(cur)
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

    """**************************      CONSULTA DE FILTRADO DE PAGO      **************************"""    
def filtro_pago_fecha_ID(FECHA_1, FECHA_2,ID_1,ID_2):
    print("FILTRO PAGO")
    print(FECHA_1)
    print(FECHA_2)
    print(ID_1)
    print(ID_2)
    # FECHA_1 = f"%{FECHA_1}%"
    # FECHA_2 = f"%{FECHA_2}%"
    # ID_1 = f"%{ID_1}%"
    # ID_2 = f"%{ID_2}%"
    conn=create_conection()
    sql="""SELECT 
        id_pago,prestamos.Id_prestamo, prestamos.Id_cliente, pagos.saldo_insolito, pagos.interes, pagos.amortizacion, pagos.amortizacion_acum, limite_time,
        pago_time, sig_time, moratorio
        FROM prestamos INNER JOIN clientes ON prestamos.Id_cliente = clientes.Id_cliente INNER JOIN pagos
        ON prestamos.Id_prestamo = pagos.id_prestamo
        WHERE limite_time BETWEEN  %s  AND  %s AND prestamos.Id_cliente BETWEEN  %s AND  %s 

                        """
    # print("SQL")
    # print(sql) 
    try:
        cur = conn.cursor()
        cur.execute(sql, (FECHA_1, FECHA_2, ID_1, ID_2))
        #print(cur)
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""**************************      CONSULTA DE FILTRADO DE NUEVO AHORRO POR FECHA      **************************"""    
def filtro_Nuevo_ahorro(FECHA_1, FECHA_2):
    print("FILTRO PAGO")
    print(FECHA_1)
    print(FECHA_2)
    # FECHA_1 = f"%{FECHA_1}%"
    # FECHA_2 = f"%{FECHA_2}%"
    conn=create_conection()
    sql="""SELECT 
            clientes.Id_cliente, nuevo_ahorro.nombre, nuevo_ahorro.apellidos, id_ahorro, importe, tea,
            plazo, capital,
            fecha_apertura, fecha_inicio, fecha_vencimiento
            FROM nuevo_ahorro INNER JOIN clientes ON nuevo_ahorro.nombre = clientes.nombre
            WHERE fecha_vencimiento BETWEEN  %s AND %s
                        """
    # print("SQL")
    # print(sql) 
    try:
        cur = conn.cursor()
        cur.execute(sql, (FECHA_1, FECHA_2))
        #print(cur)
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

    """**************************      CONSULTA DE FILTRADO DE NUEVO AHORRO      **************************"""    
def filtro_Ahorro_fecha_ID(FECHA_1, FECHA_2,ID_1,ID_2):
    print("FILTRO PAGO")
    print(FECHA_1)
    print(FECHA_2)
    print(ID_1)
    print(ID_2)
    # FECHA_1 = f"%{FECHA_1}%"
    # FECHA_2 = f"%{FECHA_2}%"
    # ID_1 = f"%{ID_1}%"
    # ID_2 = f"%{ID_2}%"
    conn=create_conection()
    sql="""SELECT 
            clientes.Id_cliente, nuevo_ahorro.nombre, nuevo_ahorro.apellidos, id_ahorro, importe, tea,
            plazo, capital,
            fecha_apertura, fecha_inicio, fecha_vencimiento
            FROM nuevo_ahorro INNER JOIN clientes ON nuevo_ahorro.nombre = clientes.nombre
            WHERE fecha_vencimiento BETWEEN  %s AND %s
            AND clientes.Id_cliente BETWEEN %s AND %s

                        """
    # print("SQL")
    # print(sql) 
    try:
        cur = conn.cursor()
        cur.execute(sql, (FECHA_1, FECHA_2, ID_1, ID_2))
        #print(cur)
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#************************* BUSQUEDA PARA LLENAR LA TABLA DE LA EMPRESA (EN POLIZAS) *****************************#
def select_tabal_clientes_2():
    conn=create_conection()
    sql="""SELECT RFC_e, nombre_b, codigo_SAT FROM catalogo_cuentas"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#*********************************ALMACENA RFC DE LA EMPRESA PARA SU BUSQUEDA (POLIZAS)************************#
def select_empresa2(RFC):
    conn = create_conection()
    sql = """SELECT RFC_e, nombre_b, codigo_SAT FROM catalogo_cuentas
            WHERE RFC_e= %s
            """
    try:
        cur = conn.cursor()
        cur.execute(sql,(RFC,))
        recipes = cur.fetchone()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


"""******************************INSERTAR DATOS A LA TABLA NUEVA POLIZA*****************************"""
def llena_poliza(data):
    conn = create_conection()
    sql = """INSERT INTO nueva_poliza(cuenta, fecha, tipo, numero, concepto)
            VALUES(%s, %s, %s, %s, %s)                        
            """
            
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#************************* BUSQUEDA PARA LLENAR LA TABLA DE MOVIMIENTOS POLIZA *****************************#
def select_busca_poliza():
    conn=create_conection()
    sql="""SELECT movimiento, cuenta, RFC,
        cargo,abono,referencia 
        FROM movimientos_poliza"""
    try:
        cur=conn.cursor()
        cur.execute(sql)
        recipes=cur.fetchall()  #devuelva datos seleccionados
        #conn.commit()    se utiliza cuando se haga cambios en la BD
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
#METODO DE BUSQUEDA DE CLIENTES
def filtro_pago2(param):
    conn = create_conection()
    param = f"%{param}%"  #cualquier parametro que pongamos puede estar al comienzo o final
    sql = """SELECT Id_cliente,nombre, apellidos  FROM clientes
            WHERE Id_cliente LIKE %s OR nombre LIKE %s OR apellidos LIKE %s
            """
           
    try:
        cur = conn.cursor()
        cur.execute(sql, (param, param, param))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()        

#***************************   Almacena datos de la interfaz ESTADO_CUENTAS     ***************************  
        
def select_cliente_ESTADO_CUENTA(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT Id_cliente, nombre, apellidos FROM clientes
            WHERE Id_cliente= %s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
""""""""""""""""""""""""""
def select_info_cliente_prestamo2(Id_cliente):
    conn = create_conection()
    sql = f"""SELECT pagos.saldo_insolito, prestamos.renta, pagos.interes, pagos.amortizacion, pagos.moratorio, pagos.limite_time, pagos.pago_time
            FROM prestamos INNER JOIN pagos ON prestamos.Id_prestamo= pagos.id_prestamo 
            WHERE prestamos.Id_prestamo=%s
            """       
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipe = cur.fetchall()
        return recipe
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
 #       cur.close()
        conn.close()

#historial Ahorro
def busqueda_id_a(Id_cliente):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento,
            nuevo_ahorro.importe 
            FROM clientes 
            INNER JOIN nuevo_ahorro ON nuevo_ahorro.nombre=clientes.nombre
            WHERE clientes.Id_cliente LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def busqueda_nombre_a(nombre):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento,
            nuevo_ahorro.importe
            FROM clientes 
            INNER JOIN nuevo_ahorro ON nuevo_ahorro.nombre=clientes.nombre
            WHERE clientes.nombre LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(nombre,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def busqueda_apellidos_a(apellidos):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            nuevo_ahorro.fecha_apertura, nuevo_ahorro.fecha_vencimiento, 
            nuevo_ahorro.importe 
            FROM clientes  
            INNER JOIN nuevo_ahorro ON nuevo_ahorro.nombre=clientes.nombre
            WHERE clientes.apellidos LIKE %s
            """          
            #
    try:
        cur = conn.cursor()
        cur.execute(sql,(apellidos,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

#historial Prestamo
def busqueda_id_p(Id_cliente):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            prestamos.cantidad_prestamo
            FROM clientes 
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.Id_cliente LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(Id_cliente,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def busqueda_nombre_p(nombre):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            prestamos.cantidad_prestamo
            FROM clientes 
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.nombre LIKE %s
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(nombre,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def busqueda_apellidos_p(apellidos):
    conn = create_conection()
    sql = """SELECT clientes.Id_cliente,clientes.nombre,clientes.apellidos,
            prestamos.cantidad_prestamo
            FROM clientes  
            INNER JOIN prestamos ON prestamos.Id_cliente=clientes.Id_cliente
            WHERE clientes.apellidos LIKE %s
            """          
            #
    try:
        cur = conn.cursor()
        cur.execute(sql,(apellidos,))
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

"""******************************INSERTAR DATOS A LA TABLA DE MOVIMIENTOS POLIZA*****************************"""
def crear_movimiento(data):
    conn = create_conection()
    sql = """INSERT INTO movimientos_poliza(movimiento, RFC, cuenta, cargo, abono, referencia,
     concepto)
            VALUES(%s, %s, %s, %s, %s, %s, %s)                        
            """
            
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: : {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
"""******************************MANDA LLAMAR CAPITAL*****************************"""
def llama_capital(nombre):
    conn = create_conection()
    sql = """SELECT capital
            FROM nuevo_ahorro
            WHERE id_cliente= %s
            ORDER BY id_ahorro desc
            """ 
    try:
        cur = conn.cursor()
        cur.execute(sql,(nombre,))
        recipes = cur.fetchone()
        return recipes
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
#        cur.close()
        conn.close()
