from lib.db_connection import connect


# Function to create the 'invoice_items' table
def create_items_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS invoice_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,
        description TEXT NOT NULL,
        quantity REAL NOT NULL,
        unit_price REAL NOT NULL,
        total_price REAL NOT NULL,
        FOREIGN KEY (invoice_id) REFERENCES invoices(id)
    )''')

    conn.commit()
    conn.close()
