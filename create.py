import sqlite3

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        );
    ''')
    print("Table '{table_name}' created successfully.")

def insert_question_answer(cursor, question, answer):
    cursor.execute("INSERT INTO {table_name} (question, answer) VALUES (?, ?);", (question, answer))
    print("Question and answer inserted successfully.")

def main():
    with sqlite3.connect('QuizBowl.db') as conn:
        cursor = conn.cursor()

        # Part 1: Create Financial Management Table
        create_table(cursor)

        # Part 2: Add Questions and Answers
        questions_and_answers = [
            ("Question1", "Awnser1"),
            ("Question2", "Awnser2"),
            # Add more questions and answers as needed
        ]

        for question, answer in questions_and_answers:
            insert_question_answer(cursor, question, answer)

if __name__ == "__main__":
    main()