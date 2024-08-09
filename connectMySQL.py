import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host, user, password, database):
    try:
        # Conectar a la base de datos MySQL
        connection = mysql.connector.connect(
            host='195.179.238.58',
            user='u927419088_admin',
            password='#Admin12345#',
            database='u927419088_testing_sql'
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record[0]}")

            # Aquí puedes agregar más operaciones de base de datos

            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada.")

# Ejemplo de uso:
host = 'localhost'
user = 'tu_usuario'
password = 'tu_contraseña'
database = 'tu_base_de_datos'

connection = connect_to_mysql(host, user, password, database)

# Si necesitas realizar operaciones, aquí es donde lo harías

# Cerrar la conexión al finalizar
close_connection(connection)