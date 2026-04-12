import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='devuser',
        password='123456',
        database='zoologico',
        auth_plugin='mysql_native_password'
    )
