import random
import sqlite3

# ANSI escape codes for colored output
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def get_table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    table_names = cursor.fetchall()
    return [table[0] for table in table_names]

def choose_category(cursor):
    available_tables = get_table_names(cursor)
    print("Available Tables:")
    for idx, table in enumerate(available_tables, start=1):
        print(f"{idx}. {table}")

    table_index = int(input("Select a table (enter the corresponding number): ")) - 1
    return available_tables[table_index]

def fetch_all_questions(cursor, category):
    cursor.execute(f'SELECT * FROM {category};')
    return cursor.fetchall()

def display_question(questions, asked_questions):
    remaining_questions = [q for q in questions if q not in asked_questions]
    if not remaining_questions:
        return None  # All questions asked

    question = random.choice(remaining_questions)
    asked_questions.append(question)
    return question

def main():
    play_again = True

    while play_again:
        with sqlite3.connect('QuizBowl.db') as conn:
            cursor = conn.cursor()

            category = choose_category(cursor)
            print(f"Category: {category}")

            all_questions = fetch_all_questions(cursor, category)
            asked_questions = []

            while True:
                question = display_question(all_questions, asked_questions)

                if question is None:
                    print("All questions from this category have been asked.")
                    break

                print(f"Question: {question[1]}")
                user_answer = input("Your Answer: ").lower()

                if user_answer == question[2].lower():
                    print(GREEN + "Correct! Well done." + RESET)
                else:
                    print(RED + f"Sorry, the correct answer is: {question[2]}" + RESET)

            play_again_input = input("Do you want to play again? (yes/no): ").lower()
            play_again = play_again_input == "yes"

if __name__ == "__main__":
    main()