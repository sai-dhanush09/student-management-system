import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chinnu@123",
            database="student_db"
        )
        return conn
    except Exception as e:
        print("Database Connection Error:", e)