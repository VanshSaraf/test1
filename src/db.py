import sqlite3  

def get_connection(db_path):
    return sqlite3.connect(db_path)

def create_users_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()

def insert_user(conn, username, password_hash):
    # Bug: wrong column name — 'passwd_hash' doesn't exist
    conn.execute(
        "INSERT INTO users (username, passwd_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    conn.commit()
