import sqlite3

# Function to create a SQLite database file
def create_database():
    conn = sqlite3.connect('timetable.db')
    conn.close()

# Function to create tables for login/register system
def create_login_register_tables():
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            is_admin INTEGER DEFAULT 0 -- 0 for regular users, 1 for admin
        )
    ''')

    conn.commit()
    conn.close()

# Function to create tables for university timetable scheduling system
def create_timetable_tables():
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            subject_id INTEGER PRIMARY KEY,
            subject_name TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Labs (
            lab_id INTEGER PRIMARY KEY,
            lab_name TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Faculty (
            faculty_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
    ''')

    # Add initial subjects and labs
    initial_subjects = ['COA', 'OS', 'EM1', 'AT', 'CNND']
    for subject in initial_subjects:
        cursor.execute('INSERT OR IGNORE INTO Subjects (subject_name) VALUES (?)', (subject,))
    
    initial_labs = ['MPL', 'NL', 'PythonL', 'UNIX']
    for lab in initial_labs:
        cursor.execute('INSERT OR IGNORE INTO Labs (lab_name) VALUES (?)', (lab,))

    conn.commit()
    conn.close()

# Function to add a new subject by the admin
def add_subject(subject_name):
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO Subjects (subject_name) VALUES (?)', (subject_name,))
    conn.commit()
    conn.close()

# Function to add a new lab by the admin
def add_lab(lab_name):
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO Labs (lab_name) VALUES (?)', (lab_name,))
    conn.commit()
    conn.close()

# Function to get a list of faculty for dropdown menu
def get_faculty_for_dropdown():
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM Faculty')
    faculty = cursor.fetchall()
    conn.close()
    return faculty

# Create the database and tables
create_database()
create_login_register_tables()
create_timetable_tables()

print("Database and tables created successfully.")

# Get list of faculty for dropdown menu
faculty = get_faculty_for_dropdown()
print("List of faculty for dropdown menu:", faculty)
