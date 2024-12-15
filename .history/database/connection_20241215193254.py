import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    """
    E
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn
