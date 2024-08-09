import mysql.connector
from mysql.connector import Error


def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',
            user='u927419088_admin',
            password='#Admin12345#',
            database='u927419088_testing_sql'
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def update_record(connection, query, data):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()  # Confirmar los cambios en la base de datos
        print("Registro modificado exitosamente")
    except Error as e:
        print(f"Error al insertar el registro: {e}")
        connection.rollback()  # Deshacer los cambios en caso de error


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada.")


# Ejemplo de uso:
host = '195.179.238.58',
user = 'u927419088_admin',
password = '#Admin12345#',
database = 'u927419088_testing_sql'

# Conectar a la base de datos
connection = connect_to_mysql(host, user, password, database)

if connection:
    # Definir la consulta SQL para insertar un registro
    query = "UPDATE asignatura SET nombre = %s WHERE idAsignatura = %s"

    # Datos del nuevo registro
    data = ('ÁLGEBRA LINEAL', 'AS001')

    # Modificar el registro en la base de datos
    update_record(connection, query, data)

    # Cerrar la conexión a la base de datos
    close_connection(connection)