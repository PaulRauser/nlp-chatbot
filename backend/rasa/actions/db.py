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


def get_image(name:  str) -> str:
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT url FROM images WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            print(f"URL for '{name}': {result[0]}")
            return result[0]
        else:
            print(f"No URL found for name: {name}")
            return "Nothing to be seen here"

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
        return ""
    finally:
        conn.close()

def get_car_details(name:  str) -> str:
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT details FROM car_data WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            print(f"No details found for name: {name}")
            return "Nothing to be seen here"

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
        return ""
    finally:
        conn.close()

def get_team_details(name:  str) -> str:
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT details FROM team_data WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            print(f"No details found for name: {name}")
            return "Nothing to be seen here"

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
        return ""
    finally:
        conn.close()

def get_car_link(name:  str):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT link FROM car_links WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            return {'name': name, 'result': result[0]}
        else:
            print(f"No link found for name: {name}")
            return "Nothing to be seen here"

    except sqlite3.Error as e:
        print(f"An error occured: {e}")
        return ""
    finally:
        conn.close()
