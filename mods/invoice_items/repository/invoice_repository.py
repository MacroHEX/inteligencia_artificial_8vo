from lib.db_connection import connect


# Create a new invoice
def create_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO invoices (issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva))

    conn.commit()
    conn.close()


# Read an invoice by ID
def get_invoice_by_id(invoice_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM invoices WHERE id = ?', (invoice_id,))
    invoice = cursor.fetchone()

    conn.close()
    return invoice


# Read all invoices
def get_all_invoices():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM invoices')
    invoices = cursor.fetchall()

    conn.close()
    return invoices


# Update an invoice by ID
def update_invoice(invoice_id, issuer_id=None, recipient_id=None, timbrado=None, invoice_number=None, issue_date=None,
                   currency=None, iva_10=None, total_iva=None):
    conn = connect()
    cursor = conn.cursor()

    # Build the update query dynamically based on which fields are provided
    update_fields = []
    update_values = []

    if issuer_id:
        update_fields.append("issuer_id = ?")
        update_values.append(issuer_id)
    if recipient_id:
        update_fields.append("recipient_id = ?")
        update_values.append(recipient_id)
    if timbrado:
        update_fields.append("timbrado = ?")
        update_values.append(timbrado)
    if invoice_number:
        update_fields.append("invoice_number = ?")
        update_values.append(invoice_number)
    if issue_date:
        update_fields.append("issue_date = ?")
        update_values.append(issue_date)
    if currency:
        update_fields.append("currency = ?")
        update_values.append(currency)
    if iva_10:
        update_fields.append("iva_10 = ?")
        update_values.append(iva_10)
    if total_iva:
        update_fields.append("total_iva = ?")
        update_values.append(total_iva)

    update_query = f"UPDATE invoices SET {', '.join(update_fields)} WHERE id = ?"
    update_values.append(invoice_id)

    cursor.execute(update_query, tuple(update_values))

    conn.commit()
    conn.close()


# Delete an invoice by ID
def delete_invoice(invoice_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM invoices WHERE id = ?', (invoice_id,))

    conn.commit()
    conn.close()
