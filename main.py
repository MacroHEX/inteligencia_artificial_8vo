import sqlite3


# Set up the SQLite database and create tables
def setup_database():
    conn = sqlite3.connect('invoice_app.db')
    cursor = conn.cursor()

    # Create table for storing entities (can be a person or business)
    cursor.execute('''CREATE TABLE IF NOT EXISTS entities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,  -- Name of the entity
        cedula TEXT,  -- Cédula of the person (nullable)
        ruc TEXT,  -- RUC of the entity (nullable)
        codigo_verificador TEXT,  -- Verification code for RUC (nullable)
        email TEXT,
        address TEXT,
        phone_number TEXT
    )''')

    # Create table for storing invoices
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issuer_id INTEGER,  -- Foreign key to entities (issuer)
        recipient_id INTEGER,  -- Foreign key to entities (recipient)
        timbrado TEXT NOT NULL,
        invoice_number TEXT NOT NULL,
        issue_date TEXT NOT NULL,
        currency TEXT NOT NULL,
        iva_10 REAL,
        total_iva REAL,
        FOREIGN KEY (issuer_id) REFERENCES entities(id),
        FOREIGN KEY (recipient_id) REFERENCES entities(id)
    )''')

    # Create table for storing invoice items
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoice_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,  -- Foreign key to invoices
        description TEXT NOT NULL,  -- Description of the product or service
        quantity REAL NOT NULL,  -- Quantity of the item
        unit_price REAL NOT NULL,  -- Price per unit
        total_price REAL NOT NULL,  -- Total price (quantity * unit_price)
        FOREIGN KEY (invoice_id) REFERENCES invoices(id)
    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


# Function to create a new entity (person or business)
def create_entity(name, cedula=None, ruc=None, codigo_verificador=None, email=None, address=None, phone_number=None):
    conn = sqlite3.connect('invoice_app.db')
    cursor = conn.cursor()

    # Insert a new entity into the 'entities' table
    cursor.execute('''INSERT INTO entities (name, cedula, ruc, codigo_verificador, email, address, phone_number)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (name, cedula, ruc, codigo_verificador, email, address, phone_number))

    conn.commit()
    conn.close()


# Function to create a new invoice
def create_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva):
    conn = sqlite3.connect('invoice_app.db')
    cursor = conn.cursor()

    # Insert a new invoice into the 'invoices' table
    cursor.execute('''INSERT INTO invoices (issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva))

    conn.commit()
    conn.close()


# Function to create invoice items
def create_invoice_item(invoice_id, description, quantity, unit_price):
    conn = sqlite3.connect('invoice_app.db')
    cursor = conn.cursor()

    total_price = quantity * unit_price

    # Insert a new item into the 'invoice_items' table
    cursor.execute('''INSERT INTO invoice_items (invoice_id, description, quantity, unit_price, total_price)
                      VALUES (?, ?, ?, ?, ?)''',
                   (invoice_id, description, quantity, unit_price, total_price))

    conn.commit()
    conn.close()


# Example usage to test:
if __name__ == '__main__':
    setup_database()

    # Example entity creation (person with Cédula)
    create_entity('Martin Aveiro', cedula='4264956', email='martin18py@gmail.com', address='1234 Address St',
                  phone_number='0981234567')

    # Example entity creation (business with RUC and verification code)
    create_entity('Banco Continental SA', ruc='80019270', codigo_verificador='2', email='banco@continental.com',
                  address='MCAL. LOPEZ 3233', phone_number='0216274000')

    # Example invoice creation with issuer and recipient
    create_invoice(
        issuer_id=2,  # Banco Continental SA (Business)
        recipient_id=1,  # Martin Aveiro (Person)
        timbrado='15710667',
        invoice_number='001-001-8111605',
        issue_date='2024-09-26 12:00:00',
        currency='PYG',
        iva_10=79.0,
        total_iva=79.0
    )

    # Example invoice item creation
    create_invoice_item(
        invoice_id=1,
        description='Compras Exterior-20120508214',
        quantity=1,
        unit_price=866.0
    )

    print("Invoice and items created successfully!")
