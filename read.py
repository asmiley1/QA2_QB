import sqlite3

def get_table_names_and_data(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Get a list of all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    # Store table names and corresponding data
    tables_data = {}

    # Fetch all data from each table
    for table in table_names:
        table_name = table[0]
        cursor.execute(f'SELECT * FROM {table_name};')
        table_data = cursor.fetchall()
        tables_data[table_name] = table_data

    conn.close()
    return tables_data

if __name__ == "__main__":
    database_name = 'QuizBowl.db'
    all_tables_data = get_table_names_and_data(database_name)

    # Display table names and data
    for table_name, data in all_tables_data.items():
        print(f"Table: {table_name}")
        print("Data:")
        for row in data:
            print(row)
        print("-" * 20)