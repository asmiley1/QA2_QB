import sqlite3

def create_table(cursor, table_name):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        );
    ''')
    print(f"Table '{table_name}' created successfully.")

def main():
    table_name = 'NewTable'

    with sqlite3.connect('QuizBowl.db') as conn:
        cursor = conn.cursor()
        create_table(cursor, table_name)

if __name__ == "__main__":
    main()