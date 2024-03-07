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
    
    if not available_tables:
        print("No available tables.")
        return None
    
    print("Available Tables:")
    for idx, table in enumerate(available_tables, start=1):
        print(f"{idx}. {table}")

    try:
        table_index = int(input("Select a table (enter the corresponding number): ")) - 1
        return available_tables[table_index]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return None

def fetch_all_questions(cursor, category):
    cursor.execute(f'SELECT * FROM {category} LIMIT 10;')  # Limit to 10 questions
    return cursor.fetchall()

def display_question(questions):
    for question in questions:
        print(f"Question: {question[1]}")
        user_answer = input("Your Answer: ").lower()

        if user_answer == question[2].lower():
            print(GREEN + "Correct! Well done." + RESET)
        else:
            print(RED + f"Sorry, the correct answer is: {question[2]}" + RESET)

def play_again():
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    return play_again_input == "yes"

def main():
    while True:
        with sqlite3.connect('QuizBowl.db') as conn:
            cursor = conn.cursor()

            category = choose_category(cursor)

            if category is not None:
                print(f"Category: {category}")

                all_questions = fetch_all_questions(cursor, category)
                display_question(all_questions)

        if not play_again():
            break

if __name__ == "__main__":
    main()