from lib.db_connection import connect

# Function to create the 'invoices' table
def create_invoices_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issuer_id INTEGER,
        recipient_id INTEGER,
        timbrado TEXT NOT NULL,
        invoice_number TEXT NOT NULL,
        issue_date TEXT NOT NULL,
        currency TEXT NOT NULL,
        iva_10 REAL,
        total_iva REAL,
        FOREIGN KEY (issuer_id) REFERENCES entities(id),
        FOREIGN KEY (recipient_id) REFERENCES entities(id)
    )''')

    conn.commit()
    conn.close()
