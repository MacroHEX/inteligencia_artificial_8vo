from lib.db_connection import connect


# Function to create the 'entities' table
def create_entities_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS entities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cedula TEXT,
        ruc TEXT,
        codigo_verificador TEXT,
        email TEXT,
        address TEXT,
        phone_number TEXT
    )''')

    conn.commit()
    conn.close()
