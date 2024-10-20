import mysql.connector # type: ignore
from mysql.connector import errorcode # type: ignore

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL server host
            user="root",       # Replace with your MySQL username
            password="Immamanu1234!"  # Replace with your MySQL password
        )
        cursor = conn.cursor()

        # Create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
        
        # Close cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

if __name__ == "__main__":
    create_database()
