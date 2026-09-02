import mysql.connector
import os


#connect to mysql db
db = mysql.connector.connect(
    host="localhost",
    #currently we are reading it from the .zshrc file
    user=os.environ.get("DB_USERNAME", "root"),
    password=os.environ.get("DB_PASSWORD"),
    database="py_db"
)

#ceate database using cursor object
cursor_ = db.cursor()

#if db already exists it will throw an error.
#cursor_.execute("CREATE DATABASE py_db")
#cursor_.execute("SHOW DATABASES")

#print databases
# for database in cursor_:
#     print(database)

#create table
#cursor_.execute("CREATE TABLE customers(username VARCHAR(30), name VARCHAR(256), email VARCHAR(100))")
#cursor_.execute("SHOW TABLES")

#access tables avaible in studio
# for i in cursor_:
#     print(i)

#alter table data
#cursor_.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# sql = "INSERT INTO customers (username, name, email) VALUES(%s, %s, %s)"

# #inserting single row
# #val = ("manoj", "Manoj", "manoj.painam1@gmail.com")

# #inseerting multiple rows
# val = [
#     ("manoj1", "Manoj1", "manoj.painam1@gmail.com"),
#     ("manoj2", "Manoj2", "manoj.painam2@gmail.com"),
# ]
# cursor_.executemany(sql, val)

# db.commit()

def fetch_all_customers():
    cursor_.execute("SELECT * FROM customers")
    print_customers(cursor_.fetchall())

def fetch_single_customer():
    cursor_.execute("SELECT * FROM customers")
    print_customers(cursor_.fetchone())


def fetch_customer_using_where():
    cursor_.execute("SELECT * FROM customers WHERE username='manoj'")
    print_customers(cursor_.fetchall())

def fetch_customer_using_placeholders():
    sql = "SELECT * FROM customers where username = %s"
    username = ("manoj",)
    cursor_.execute(sql, username)
    print_customers(cursor_.fetchall())

def fetch_customers_using_order_by():
    cursor_.execute("SELECT * FROM customers ORDER BY id DESC")
    print_customers(cursor_.fetchall())

def print_customers(customers):
    for customer in customers:
        print("customer details : {}".format(customer))

def delete_record(username):
    cursor_.execute("DELETE FROM customers WHERE username=%s", (username,))
    print("Deleted user with username".format(username))

    fetch_all_customers()

def drop_table():
    cursor_.execute("DROP TABLE IF EXISTS user_details")

def update_record():
    sql = "UPDATE customers SET email=%s WHERE username=%s"
    values = ("manoj.painam@outlook.com", "manoj1")
    cursor_.execute(sql, values)

    db.commit()
    print(cursor_.rowcount, "record(s) effected")


# fetch_all_customers()
# fetch_single_customer()
#fetch_customer_using_where()
#fetch_customer_using_placeholders()
# fetch_customers_using_order_by()
# delete_record(username="manoj2")
# drop_table()
update_record()
