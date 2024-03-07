import sqlite3

conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# Create tables for each category
cursor.execute('''
CREATE TABLE IF NOT EXISTS Financial_Management (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS DS_3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Data_Analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Database_Management (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS BMGT_3510 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
''')
# Repeat the above create table statement for each category

conn.commit()
conn.close()