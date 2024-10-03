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

# Additional CRUD operations can go here (read, update, delete)
