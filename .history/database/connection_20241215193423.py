import sqlite3

DATABASE_NAME = './database/magazine.db'
class Connection 
def get_db_connection():
    """
    Establishes a connection to the SQLite database .
    Configures the connection to return rows a dictionaries .
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn