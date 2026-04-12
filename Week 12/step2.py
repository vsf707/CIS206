import sqlite3

conn = sqlite3.connect("Northwind.db")
cursor = conn.cursor()

allowed_tables = ["Customers", "Employees", "Products"]

print("\nChoose a table:")
for i, table in enumerate(allowed_tables, start=1):
    print(f"{i}. {table}")

table_choice = int(input("\nEnter table number: "))
selected_table = allowed_tables[table_choice - 1]

print("\nChoose an operation:")
print("I - Insert")
print("U - Update")
print("D - Delete")

action = input("Enter choice (I/U/D): ").upper()

if action == "I":
    cursor.execute(f"PRAGMA table_info({selected_table})")
    columns = [col[1] for col in cursor.fetchall()]

    print("\nEnter values for the new record:")

    values = []
    for col in columns:
        val = input(f"{col}: ")
        values.append(val)

    placeholders = ",".join(["?"] * len(values))
    col_names = ",".join(columns)

    cursor.execute(
        f"INSERT INTO {selected_table} ({col_names}) VALUES ({placeholders})",
        values
    )

    conn.commit()
    print("Record inserted successfully!")

elif action == "U":
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()

    print("\nRecords:")
    for i, row in enumerate(rows, start=1):
        print(i, row)

    row_choice = int(input("\nSelect row number to update: "))
    selected_row = rows[row_choice - 1]

    cursor.execute(f"PRAGMA table_info({selected_table})")
    columns = [col[1] for col in cursor.fetchall()]

    print("\nColumns:")
    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    col_choice = int(input("\nSelect column number to update: "))
    new_value = input("Enter new value: ")

    pk_column = columns[0]  # assumes first column is ID
    pk_value = selected_row[0]

    cursor.execute(
        f"UPDATE {selected_table} SET {columns[col_choice - 1]} = ? WHERE {pk_column} = ?",
        (new_value, pk_value)
    )

    conn.commit()
    print("Record updated successfully!")

elif action == "D":
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()

    print("\nRecords:")
    for i, row in enumerate(rows, start=1):
        print(i, row)

    row_choice = int(input("\nSelect row number to delete: "))
    selected_row = rows[row_choice - 1]

    cursor.execute(f"PRAGMA table_info({selected_table})")
    columns = [col[1] for col in cursor.fetchall()]

    pk_column = columns[0]
    pk_value = selected_row[0]

    cursor.execute(
        f"DELETE FROM {selected_table} WHERE {pk_column} = ?",
        (pk_value,)
    )

    conn.commit()
    print("Record deleted successfully!")

else:
    print("Invalid choice.")

conn.close()