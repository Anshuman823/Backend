<<<<<<< HEAD


from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(dotenv_path=".env")


db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=3306,
    use_pure=True
)



cur = db.cursor()

def insert(data):
    
    table_name = data['table'].strip(';')
    print("Table Name:", table_name)

   
    values_dict = data['values']
    print("Values Dictionary:", values_dict)

    
    column_names = []
    for column in values_dict.keys():
        column_names.append(column)
    print("Columns to insert:", column_names)

    
    columns_string = ', '.join(column_names)
    print("Columns string:", columns_string)

    
    values_list = []
    for value in values_dict.values():
        values_list.append(value)
    print("Values to insert:", values_list)

    
    placeholders = []
    for _ in values_list:
        placeholders.append('%s')
    placeholders_string = ', '.join(placeholders)
    print("Placeholders:", placeholders_string)

   
    sql_query = f"INSERT INTO {table_name} ({columns_string}) VALUES ({placeholders_string})"
    print("Final SQL Query:", sql_query)

    
    cur.execute(sql_query, tuple(values_list))

    
    db.commit()

    
    print("Data inserted successfully into", table_name)


def get(table_name):
    table_name = table_name.rstrip(';')
    sql = f"SELECT * FROM {table_name}"
    cur.execute(sql)
    rows = cur.fetchall()
    print(f"\nData in table '{table_name}':")
    for row in rows:
        print(row)

def delete_data(table_name):
    table_name = table_name.rstrip(';')
    column_name = input("Enter the column name to delete by: ").strip()
    value = input(f"Enter the value of {column_name} to delete: ").strip()
    sql = f"DELETE FROM {table_name} WHERE {column_name} = %s"
    cur.execute(sql, (value,))
    db.commit()
    print(f"Deleted record(s) from {table_name} where {column_name} = {value}")
    get(table_name)


table_name = input("Enter table name: ")

columns_input = input("Enter column names by comma separated: ")
columns = [col.strip() for col in columns_input.split(',')]

values = {}
for col in columns:
    val = input(f"Enter value for {col}: ")
    if val.isdigit():
        val = int(val)
    values[col] = val

args = {
    'table': table_name,
    'values': values
}

insert(args)
get(table_name)

delete_choice = input("\nDo you want to delete a record? (yes/no): ").lower()
if delete_choice == 'yes':
    delete_data(table_name)


=======


from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(dotenv_path=".env")


db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=3306,
    use_pure=True
)



cur = db.cursor()

def insert(data):
    
    table_name = data['table'].strip(';')
    print("Table Name:", table_name)

   
    values_dict = data['values']
    print("Values Dictionary:", values_dict)

    
    column_names = []
    for column in values_dict.keys():
        column_names.append(column)
    print("Columns to insert:", column_names)

    
    columns_string = ', '.join(column_names)
    print("Columns string:", columns_string)

    
    values_list = []
    for value in values_dict.values():
        values_list.append(value)
    print("Values to insert:", values_list)

    
    placeholders = []
    for _ in values_list:
        placeholders.append('%s')
    placeholders_string = ', '.join(placeholders)
    print("Placeholders:", placeholders_string)

   
    sql_query = f"INSERT INTO {table_name} ({columns_string}) VALUES ({placeholders_string})"
    print("Final SQL Query:", sql_query)

    
    cur.execute(sql_query, tuple(values_list))

    
    db.commit()

    
    print("Data inserted successfully into", table_name)


def get(table_name):
    table_name = table_name.rstrip(';')
    sql = f"SELECT * FROM {table_name}"
    cur.execute(sql)
    rows = cur.fetchall()
    print(f"\nData in table '{table_name}':")
    for row in rows:
        print(row)

def delete_data(table_name):
    table_name = table_name.rstrip(';')
    column_name = input("Enter the column name to delete by: ").strip()
    value = input(f"Enter the value of {column_name} to delete: ").strip()
    sql = f"DELETE FROM {table_name} WHERE {column_name} = %s"
    cur.execute(sql, (value,))
    db.commit()
    print(f"Deleted record(s) from {table_name} where {column_name} = {value}")
    get(table_name)


table_name = input("Enter table name: ")

columns_input = input("Enter column names by comma separated: ")
columns = [col.strip() for col in columns_input.split(',')]

values = {}
for col in columns:
    val = input(f"Enter value for {col}: ")
    if val.isdigit():
        val = int(val)
    values[col] = val

args = {
    'table': table_name,
    'values': values
}

insert(args)
get(table_name)

delete_choice = input("\nDo you want to delete a record? (yes/no): ").lower()
if delete_choice == 'yes':
    delete_data(table_name)


>>>>>>> 74da55a4cda22045181359bf439ec72c681f887c
