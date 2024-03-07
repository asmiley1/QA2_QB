import sqlite3

conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# Define questions and answers for each category
financial_management_data = [
    ("What is the time value of money?", "The concept that a sum of money has a different value today compared to its value in the future."),
    ("Define working capital.", "The difference between a company's current assets and current liabilities."),
    # Add more questions...
]

business_management_data = [
    ("What is organizational culture?", "The shared values, beliefs, and practices that shape an organization's identity."),
    ("Define SWOT analysis.", "An evaluation of a company's Strengths, Weaknesses, Opportunities, and Threats."),
    # Add more questions...
]

database_management_data = [
    ("What is a database?", "A structured collection of data organized in a way that a computer program can quickly select and retrieve specific pieces of data."),
    ("Define SQL.", "Structured Query Language, a domain-specific language used to manage and manipulate relational databases."),
    # Add more questions...
]

applications_development_data = [
    ("What is the software development life cycle (SDLC)?", "A process for planning, creating, testing, and deploying software."),
    ("Define object-oriented programming (OOP).", "A programming paradigm based on the concept of objects, which can contain data in the form of attributes and code in the form of procedures."),
    # Add more questions...
]

data_analytics_data = [
    ("What is data cleansing?", "The process of identifying and correcting errors or inconsistencies in datasets."),
    ("Define correlation.", "A statistical measure that describes the extent to which two variables change together."),
    # Add more questions...
]

# Insert data into tables
cursor.executemany('INSERT INTO Financial_Management (question, answer) VALUES (?, ?)', financial_management_data)
cursor.executemany('INSERT INTO Business_Management (question, answer) VALUES (?, ?)', business_management_data)
cursor.executemany('INSERT INTO Database_Management (question, answer) VALUES (?, ?)', database_management_data)
cursor.executemany('INSERT INTO Applications_Development (question, answer) VALUES (?, ?)', applications_development_data)
cursor.executemany('INSERT INTO Data_Analytics (question, answer) VALUES (?, ?)', data_analytics_data)

conn.commit()
conn.close()