import sqlite3
import os
print(os.getcwd())
conn = sqlite3.connect("Northwind.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
tables = cursor.fetchall()

table_list = [table[0] for table in tables]

print("\nAvailable Tables:\n")
for i, table in enumerate(table_list, start=1):
    print(f"{i}. {table}")

if len(table_list) == 0:
    print("No tables found in database.")
    conn.close()
    exit()

try:
    choice = int(input("\nEnter the number of the table you want to view: "))

    if choice < 1 or choice > len(table_list):
        print("Invalid choice. Please run again and select a valid number.")
        conn.close()
        exit()

except ValueError:
    print("Invalid input. Please enter a number only.")
    conn.close()
    exit()

selected_table = table_list[choice - 1]

print(f"\nDisplaying data from: {selected_table}\n")

cursor.execute(f"PRAGMA table_info({selected_table});")
columns_info = cursor.fetchall()
column_names = [col[1] for col in columns_info]

print("Row#", *column_names)

cursor.execute(f"SELECT * FROM {selected_table}")
rows = cursor.fetchall()

for index, row in enumerate(rows, start=1):
    print(index, *row)

conn.close()