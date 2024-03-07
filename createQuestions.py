import sqlite3

conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# Define questions and answers for each category
Financial_Management = [("What does FV stand for?", "future value"),
    ("What does A stand for in A=L+SE.", "asset"),
    ("What does L stand for in A=L+SE?", "liability"),
    ("Is cash a current asset Y/N?", "y"),
    ("Define leverage.", "debt"),
    ("What is the risk free rate?", "10 year treasury bill return"),
    ("Diverse group of assets.", "portfolio"),
    ("What is a budget?", "financial plan"),
    ("With higher risk you expect higher _____.", "return"),
    ("What does SE stand for in A=L+SE?", "shareholders equity"),
]


BMGT_3510 = [("What is the purpose of human resource management in an organization?", "staffing"),
    ("what does ROI mean?", "return on invesment"),
    ("What does SWOT stand for?", "strengths weaknesses opportunities threats"),
    ("What do Key Performance Indicators (KPIs) measure in an organization?", "performance"),
    ("In business, what role does Customer Relationship Management (CRM) play?", "customer relationships"),
    ("What is the acronym for Human Resource Management", "hrm"),
    ("What does CEO stand for?", "chief executive officer"),
    ("What does SOP stand for?", "standard operating procedures"),
    ("What is the acronym for Enterprise Resource Planning.", "erp"),
    ("In a business-to-business (B2B) context, what entities are involved?", "businesses"),
    
    
]

Database_Managment = [("What is the purpose of a database in computing?", "Storage"),
    ("Explain the role of SQL in managing relational databases.", "Queries"),
    ("How does normalization contribute to database design?", "Efficiency"),
    ("Define the concept of data integrity in a database system.", "Consistency"),
    ("What is the significance of indexing in database performance?", "Efficiency"),
    ("Explain the role of a database administrator (DBA) in an organization.", "Management"),
    ("How do transactions ensure data consistency in a database?", "Atomicity"),
    ("Define the term 'database schema' in the context of database management.", "Structure"),
    ("What is the purpose of database views in relational databases?", "Abstraction"),
    ("Explain the role of triggers in a database system.", "Automation"),
]
   


DS_3850 = [("What does .py stand for?", "python"),
    ("What does .db stand for?", "database"),
    ("What function converts integers to a string?", "str"),
    ("What function converts text to integers", "int"),
    ("What do you write to import a module?", "import"),
    ("What other language did I use to create the database", "sqlite"),
    ("What software are we currently using to code?", "vscode"),
    ("What website do we use to commit changes", "github"),
    ("What is the acronym for a Graphical User Interface?", "gui"),
    ("What do you use to define a function?", "def")
     
]

Data_Analytics = [("True or False: Data analytics involves extracting insights from data.", "true"),
    ("In data analytics, what is correlation used to measure?", "relationships"),
    ("True or False: Clustering is a technique in supervised machine learning.", "false"),
    ("What does the term 'data cleansing' refer to in analytics?", "cleaning"),
    ("True or False: Descriptive analytics focuses on predicting future outcomes.", "false"),
    ("What statistical measure describes the spread of data values?", "variability"),
    ("True or False: Regression analysis is used to classify data into groups.", "false"),
    ("In data analytics, what is 'ANOVA' an acronym for?", "analysis of variance"),
    ("True or False: Data sampling involves analyzing the entire dataset.", "false"),
    ("What is the square root of the variance of a data set?", "standard deviation"),
]

# Insert data into tables
cursor.executemany('INSERT INTO Financial_Management (question, answer) VALUES (?, ?)', Financial_Management)
cursor.executemany('INSERT INTO BMGT_3510 (question, answer) VALUES (?, ?)', BMGT_3510)
cursor.executemany('INSERT INTO Database_Managment (question, answer) VALUES (?, ?)', Database_Managment)
cursor.executemany('INSERT INTO DS_3850 (question, answer) VALUES (?, ?)', DS_3850)
cursor.executemany('INSERT INTO Data_Analytics (question, answer) VALUES (?, ?)', Data_Analytics)

conn.commit()
conn.close()