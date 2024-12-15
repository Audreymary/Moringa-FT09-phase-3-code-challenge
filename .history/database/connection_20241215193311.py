import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    """
    Establishes a connection to the S
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn
