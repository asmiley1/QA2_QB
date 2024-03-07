# QA2_QB
Quarterly Assessment over Quiz Bowl

# Quiz Bowl Application

Welcome to the Quiz Bowl application! This project aims to create an engaging quiz experience with different categories of questions. Below, you'll find instructions on how to use the application and the organization of files within the repository.

## How to Run the Application

1. Clone the repository to your local machine.
2. Navigate to the repository folder in your terminal.
3. Execute the app file (`app.py`) to play the Quiz Bowl.

(The `app.py` file is the only file necessary to run to play the game.)



## Files in the Repository

### 1. Create File (`create.py`)

This file serves two purposes: creating new tables and adding data to those tables. It is intended to be used as a one-time setup to populate the database with questions and answers.

#### Creating a New Table:
- Run the script to create a new table. Adjust the script to add tables as needed.

#### Adding Data to the Table:
- After creating a table, run the script to add questions and answers to the specified table.

### 2. Read File (`read.py`)

This file allows you to pull a list of all table names from your database and fetch all data from each table.

#### Fetching Table Names:
- Run the script to get a list of all table names in the connected database.

#### Fetching All Data:
- Use the script to retrieve all data from each table in the database.

### 3. App File (`app.py`)

This is the main application file where users can play the Quiz Bowl. When grading the project, this is the only file you need to run.

#### Running the Application:
- Execute `app.py` to start the Quiz Bowl application.
- Select a category, answer questions, and enjoy the quiz experience.

### 4. README.md

This file provides essential information about the project, its structure, and instructions for running the application.