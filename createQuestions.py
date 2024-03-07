import sqlite3

def insert_question_answer(cursor, table_name, question, answer):
    cursor.execute(f"INSERT INTO {table_name} (question, answer) VALUES (?, ?);", (question, answer))
    print("Question and answer inserted successfully.")

def main():
    table_name = 'NewTable'

    with sqlite3.connect('QuizBowl.db') as conn:
        cursor = conn.cursor()

        # Add Questions and Answers
        questions_and_answers = [
            ("Question 1", "Answer 1"),
            ("Question 2", "Answer 2"),
            # Add more questions and answers as needed
        ]

        for question, answer in questions_and_answers:
            insert_question_answer(cursor, table_name, question, answer)

if __name__ == "__main__":
    main()