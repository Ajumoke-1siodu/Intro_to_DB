import mysql.connector
from mysql.connector import Error

def create_database():
    try:
# Connect to MySQL server (adjust user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # add your MySQL root password here if needed
                                                        
        )
        if connection.is_connected():
            cursor = connection.cursor()
                                                                        try:
                                                                            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                                                                            print("Database 'alx_book_store' created successfully!")
            except Error as err:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()
                connection.close()
        except Error as err:
            print(f"Error: Could not connect to MySQL server. {err}")
if __name__ == '__main__':
    create_database()
