import sqlite3

def connect_db():
    # Connects to Northwind database
    conn = sqlite3.connect("Northwind.db")
    return conn

def get_columns(cursor, table):
    # Returns list of column names for a table
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [col[1] for col in cursor.fetchall()]
    return columns

def insert_record(cursor, conn, table):

    columns = get_columns(cursor, table)

    print("\nEnter values for new record:")

    values = []
    for col in columns:
        val = input(f"{col}: ")
        values.append(val)

    placeholders = ",".join(["?"] * len(values))
    col_names = ",".join(columns)

    cursor.execute(
        f"INSERT INTO {table} ({col_names}) VALUES ({placeholders})",
        values
    )

    conn.commit()
    print("Record inserted successfully!")

def update_record(cursor, conn, table):

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    if not rows:
        print("No records found.")
        return

    print("\nRecords:")
    for i, row in enumerate(rows, start=1):
        print(i, row)

    try:
        row_choice = int(input("\nSelect row number to update: "))
        if row_choice < 1 or row_choice > len(rows):
            print("Invalid row selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_row = rows[row_choice - 1]

    columns = get_columns(cursor, table)

    print("\nColumns:")
    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    try:
        col_choice = int(input("\nSelect column number to update: "))
        if col_choice < 1 or col_choice > len(columns):
            print("Invalid column selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    new_value = input("Enter new value: ")

    pk_column = columns[0]
    pk_value = selected_row[0]

    cursor.execute(
        f"UPDATE {table} SET {columns[col_choice - 1]} = ? WHERE {pk_column} = ?",
        (new_value, pk_value)
    )

    conn.commit()
    print("Record updated successfully!")

def delete_record(cursor, conn, table):

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    if not rows:
        print("No records found.")
        return

    print("\nRecords:")
    for i, row in enumerate(rows, start=1):
        print(i, row)

    try:
        row_choice = int(input("\nSelect row number to delete: "))
        if row_choice < 1 or row_choice > len(rows):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_row = rows[row_choice - 1]

    columns = get_columns(cursor, table)
    pk_column = columns[0]
    pk_value = selected_row[0]

    cursor.execute(
        f"DELETE FROM {table} WHERE {pk_column} = ?",
        (pk_value,)
    )

    conn.commit()
    print("Record deleted successfully!")

def main():
    conn = connect_db()
    cursor = conn.cursor()

    allowed_tables = ["Customers", "Employees", "Products"]

    print("\nChoose a table:")
    for i, table in enumerate(allowed_tables, start=1):
        print(f"{i}. {table}")

    try:
        table_choice = int(input("\nEnter table number: "))
        if table_choice < 1 or table_choice > len(allowed_tables):
            print("Invalid table selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_table = allowed_tables[table_choice - 1]

    print("\nChoose an operation:")
    print("I - Insert")
    print("U - Update")
    print("D - Delete")

    action = input("Enter choice (I/U/D): ").upper()

    if action == "I":
        insert_record(cursor, conn, selected_table)
    elif action == "U":
        update_record(cursor, conn, selected_table)
    elif action == "D":
        delete_record(cursor, conn, selected_table)
    else:
        print("Invalid option.")

    conn.close()

main()