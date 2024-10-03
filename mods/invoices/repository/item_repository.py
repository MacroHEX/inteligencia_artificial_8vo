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


# Read an invoice item by ID
def get_invoice_item_by_id(item_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM invoice_items WHERE id = ?', (item_id,))
    item = cursor.fetchone()

    conn.close()
    return item


# Read all items for a specific invoice
def get_items_by_invoice_id(invoice_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM invoice_items WHERE invoice_id = ?', (invoice_id,))
    items = cursor.fetchall()

    conn.close()
    return items


# Update an invoice item by ID
def update_invoice_item(item_id, description=None, quantity=None, unit_price=None):
    conn = connect()
    cursor = conn.cursor()

    # Build the update query dynamically based on which fields are provided
    update_fields = []
    update_values = []

    if description:
        update_fields.append("description = ?")
        update_values.append(description)
    if quantity:
        update_fields.append("quantity = ?")
        update_values.append(quantity)
    if unit_price:
        update_fields.append("unit_price = ?")
        update_values.append(unit_price)
        update_fields.append("total_price = quantity * ?")  # Update total price
        update_values.append(unit_price)

    update_query = f"UPDATE invoice_items SET {', '.join(update_fields)} WHERE id = ?"
    update_values.append(item_id)

    cursor.execute(update_query, tuple(update_values))

    conn.commit()
    conn.close()


# Delete an invoice item by ID
def delete_invoice_item(item_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM invoice_items WHERE id = ?', (item_id,))

    conn.commit()
    conn.close()
