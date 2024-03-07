import sqlite3

conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# Create tables for each category
cursor.execute('''
CREATE TABLE IF NOT EXISTS {Newtable} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')



Newtable = [("Question", "answer"),]


cursor.executemany('INSERT INTO Newtable (question, answer) VALUES (?, ?)', Newtable)