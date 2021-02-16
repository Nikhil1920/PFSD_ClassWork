import mysql.connector
import pandas as pd
from mysql.connector import Error


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


pw = "nikhil4u"
db = "hospital"

read_medicine_data = """
SELECT * FROM medicine;
"""

connection = create_db_connection("localhost", "root", pw, db)
medicine = read_query(connection, read_medicine_data)

print("\nMedicine Data before updating:")
for result in medicine:
    print(result)

update = """
UPDATE medicine 
SET medicine_stock = 8
WHERE medicine_id = 4;
"""

execute_query(connection, update)

medicine = read_query(connection, read_medicine_data)

print("\nMedicine Data after updating:")
for result in medicine:
    print(result)
