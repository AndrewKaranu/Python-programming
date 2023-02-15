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

# Inserting data into tables
# INSERT INTO [table name] 
#               (column1, column2, column3, column4, column5) 
#               VALUES (value1, value2, value3, value4, value5)
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
query = "SELECT first_name, last_name FROM students WHERE student_id=3"
# query = "SELECT * FROM students"
# Execute the query and save results in a variable
results = cursor.execute(query)
print(results) #-> prints the cursor
# Display the results
students = results.fetchall()
print(students)

# Close the database connection



