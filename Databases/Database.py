import sqlite3

# Create a connection to our database
# you can also use.connect
connection = sqlite3.Connection("school.db")

# Checks for successful connection
# if connection:
#      print("Connection Successful")
# else:
#     print("Connection error")
# NN -Not null
# PK -Primary key
# AI -Auto increment
# U- Unique

# CRUD-
# C ->Create- inserting a record into a database
# R ->Read/retrieve- Fetching records in a database
# U ->Update- Modify records in a database
# D ->Delete- Delete a record from a database

# Creating a new database
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 

# Check if tables exist
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# Creating a primary key
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Primary key if the table already exists
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")4

# Inserting data into tables
# mycursor = mydb.cursor()

# sql = "INSERT INTO <table name> (Column1, Column2) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit() ->Commits and save info to database
# print(mycursor.rowcount, "record inserted.")

# Another method-
# INSERT INTO [table name] 
#               (column1, column2, column3, column4, column5) 
#               VALUES (value1, value2, value3, value4, value5)

# Inseting multiple values
# sql = "INSERT INTO <Table name> (Column 1, Column2) VALUES (%s, %s)"
# val = [
#   ('Value 1', 'Value 2'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# Display data from a table
# SELECT column(s) FROM table_name

# Update value in tables
# Update table_name SET column = new_value Where id = id_to_update

# Deleting values from table
# DELETE FROM table_name WHERE id=id_to_delete

# Lets select all the students in our database
# connection = sqlite3.Connection("school.db")-created earlier
# Create a connection
# Create a cursor object
# *- means everything eg select everything
cursor = connection.cursor()

# Create the sql/query statement - to fetch all students
# query = "SELECT first_name, last_name FROM students WHERE student_id=3"
query = "SELECT * FROM students"

# Selecting specific columns
# query = "SELECT first_n, email FROM students"

# Execute the query and save results in a variable
results = cursor.execute(query)
# print(results) #-> prints the cursor
# Display the results
students = results.fetchall()
# print(students)


# Print one specific row
# students = results.fetchone()
# print(students)

# Close the database connection
stud = cursor.fetchall()[0]
print(stud)

# get the id of the row you just inserted by asking the cursor object.
# print("1 record inserted, ID:", cursor.lastrowid)



