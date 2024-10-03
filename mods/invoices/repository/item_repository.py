from lib.db_connection import connect

# Create a new invoice item
def create_invoice_item(invoice_id, description, quantity, unit_price):
    conn = connect()
    cursor = conn.cursor()

    total_price = quantity * unit_price

    cursor.execute('''INSERT INTO invoice_items (invoice_id, description, quantity, unit_price, total_price)
                      VALUES (?, ?, ?, ?, ?)''',
                   (invoice_id, description, quantity, unit_price, total_price))

    conn.commit()
    conn.close()

# Additional CRUD operations can go here (read, update, delete)
