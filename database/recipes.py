#OPCIONES PARA INTERACTUAR CON LA BASE DE DATOS
"OPCIONES PARA INTERACTUAR CON LA BASE DE DATOS"
#%S= le vamos a dar valores a las filas de la tabla"
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
"""**************************      INSERTAR DATOS A LA TABLA DE PRESTAMOS       **************************"""
def insert_Prestamos (data):
    conn=create_conection()
    sql="""INSERT INTO prestamos (Id_cliente, cantidad_prestamo, frecuencia, tiempo, periodo, Iva,
                                Iva_div, saldo_insolito, renta, interes, amortizacion, amortizacion_acum,
                                fecha_inicio, fecha_siguiente,nombre_codeudor,Garantia)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
        WHERE clientes.Id_cliente=%s and saldo_insolito>0
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
                                limite_time, pago_time, sig_time, moratorio, bandera)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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
    sql = f"""SELECT capital, Importe
                FROM ahorro
                WHERE Id_cliente= %s 
                ORDER BY Id_ahorro desc
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
    sql=f"""UPDATE ahorro SET 
                            capital=%s,
                            Importe=%s
                        WHERE Id_cliente={_id}
                        ORDER BY Id_ahorro desc
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
    sql = f"""SELECT capital, Id_ahorro, Importe
            FROM ahorro
            WHERE Id_cliente= %s 
            ORDER BY Id_ahorro desc
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
    sql=f"""UPDATE ahorro SET 
                            capital=%s,
                            Importe=%s
                            
                        WHERE Id_ahorro={_id}
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
