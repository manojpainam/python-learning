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
sql = "INSERT INTO customers (username, name, email) VALUES(%s, %s, %s)"

#inserting single row
#val = ("manoj", "Manoj", "manoj.painam1@gmail.com")

#inseerting multiple rows
val = [
    ("manoj1", "Manoj1", "manoj.painam1@gmail.com"),
    ("manoj2", "Manoj2", "manoj.painam2@gmail.com"),
]
cursor_.executemany(sql, val)

db.commit()
print(cursor_.rowcount, "record inserted")
