import pymysql

def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="engr@580H",
        db="tornado_crud",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
