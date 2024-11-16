import sqlite3
import os

def connect_db():
    # Resolve the absolute path for debugging
    db_path = os.path.abspath('../../database/chatbot.db')
    print(f"Attempting to connect to database at: {db_path}")
    
    # Check if the file exists
    if not os.path.exists(db_path):
        print(f"Database file not found at {db_path}")
        raise FileNotFoundError(f"Database file not found at {db_path}")

    print("Database file found. Attempting to connect...")
    return sqlite3.connect(db_path)


def insert_user_input(user_input:  str) -> None:
    conn = connect_db()
    cursor = conn.cursor()

    try:
        print(user_input)
        cursor.execute("INSERT INTO user_input (user_input) VALUES(?)", (user_input,))
        conn.commit()

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        conn.close()
