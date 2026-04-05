import sqlite3

conn = sqlite3.connect("exam.db", check_same_thread=False)
c = conn.cursor()

def init_db():
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS exams(
        exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher TEXT,
        title TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS questions(
        q_id INTEGER PRIMARY KEY AUTOINCREMENT,
        exam_id INTEGER,
        question TEXT,
        q_type TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        answer TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS results(
        username TEXT,
        exam_id INTEGER,
        score INTEGER
    )""")

    conn.commit()