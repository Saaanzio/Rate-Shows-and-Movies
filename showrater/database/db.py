import sqlite3

DB_NAME = "reviews.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        rating INTEGER
    )
    """)

    conn.commit()
    conn.close()

def execute(query, params: tuple = ()) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_all(query: str, params: tuple = ()) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()
    return rows


def fetch_one(query: str, params: tuple = ()) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchone()

    conn.close()
    return rows
