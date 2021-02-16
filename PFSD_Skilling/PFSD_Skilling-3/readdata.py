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

read_doctor_data = """
SELECT * FROM doctor;
"""

read_patient_data = """
SELECT * FROM patient;
"""

read_medicine_data = """
SELECT * FROM medicine;
"""

connection = create_db_connection("localhost", "root", pw, db)
doctor = read_query(connection, read_doctor_data)

print("\nDoctor Data:")
for result in doctor:
    print(result)

medicine = read_query(connection, read_medicine_data)

print("\nMedicine Data:")
for result in medicine:
    print(result)

patient = read_query(connection, read_patient_data)

print("\nPatient Data:")
for result in patient:
    print(result)
