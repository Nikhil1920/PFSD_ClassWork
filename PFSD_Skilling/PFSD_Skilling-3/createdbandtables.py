import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


pw = "nikhil4u"
db = "hospital"

connection = create_server_connection("localhost", "root", pw)

create_database_query = "CREATE DATABASE hospital"

create_database(connection, create_database_query)


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


create_doctor_table = """
CREATE TABLE doctor (
  doctor_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  dob DATE,
  specality VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20)
  );
 """

create_patient_table = """
CREATE TABLE patient (
  patient_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  dob DATE,
  phone_no VARCHAR(20)
  );
 """

create_medicine_table = """
CREATE TABLE medicine (
  medicine_id INT PRIMARY KEY,
  medicine_name VARCHAR(40) NOT NULL,
  medicine_stock INT NULL DEFAULT 0,
  manufactured DATE NOT NULL,
  expiry DATE NOT NULL
  );
 """


connection = create_db_connection(
    "localhost", "root", pw, db)

execute_query(connection, create_doctor_table)

execute_query(connection, create_patient_table)

execute_query(connection, create_medicine_table)

populate_doctor_table = """
INSERT INTO doctor VALUES
(1,  'James', 'Smith', '1985-04-20', 'heart', '91774553676'),
(2, 'Stefanie',  'Martin', '1970-02-17', 'brain', '91234567890'), 
(3, 'Steve', 'Wang', '1990-11-12', 'teeth','97840921333'),
(4, 'Friederike',  'Muller', '1987-07-07',  'bones', '92345678901'),
(5, 'Isobel', 'Ivanova', '1963-05-30',  'stomach', '91772635467'),
(6, 'Niamh', 'Murphy', '1995-09-08',  'brain', '91231231232');
"""

populate_patient_table = """
INSERT INTO patient VALUES
(1, 'Andrea', 'Duerr', 'New York', '1996-06-16', '9166448524'),
(2, 'Harry', 'Potter', 'Hogwarts', '1998-07-18', '8647951322'),
(3, 'Heiko', 'Fleischer', 'Anakapalli', '1999-11-12', '8521474571'),
(4, 'Marina', 'Berg','vijayawada', '2001-03-22', '9645874466');
"""

populate_medicine_table = """
INSERT INTO medicine VALUES
(1, 'benadryl', 8, '2021-01-01', '2023-01-01'),
(2, 'aspirin', 10, '2021-01-01', '2023-01-01'),
(3, 'azofaram', 18, '2021-01-01', '2023-01-01'),
(4, 'covishield', 16, '2021-01-01', '2023-01-01'),
(5, 'chloroform', 12, '2021-01-01', '2023-01-01'),
(6, 'dulcoflex', 14, '2021-01-01', '2023-01-01');
"""

connection = create_db_connection("localhost", "root", pw, db)

execute_query(connection, populate_doctor_table)

execute_query(connection, populate_patient_table)

execute_query(connection, populate_medicine_table)
