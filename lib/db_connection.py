import sqlite3


def connect():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect('invoice_app.db')
