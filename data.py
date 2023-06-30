import mysql.connector

# Replace the placeholders with your actual connection details
# connection = mysql.connector.connect(
#     host='localhost',
#     user='madhu',
#     password='2005',
# )


# cursor = connection.cursor()

# database_name = 'my_todo'
# cursor.execute(f"CREATE DATABASE {database_name}")

# connection.commit()

# cursor.close()
# connection.close()


connection = mysql.connector.connect(
    host='localhost',
    user='madhu',
    password='2005',
    database="my_todo"
    
)



cursor = connection.cursor()

create_table_query = '''
CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    due_date DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending'
)
'''

cursor.execute(create_table_query)

connection.commit()

cursor.close()
connection.close()
