from mods.invoice_items.repository.invoice_repository import create_invoice, get_invoice_by_id, get_all_invoices, \
    update_invoice, delete_invoice


# Service to issue an invoice
def issue_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva):
    """
    Issue a new invoice.
    """
    create_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva)


# Service to get an invoice by ID
def get_invoice(invoice_id):
    """
    Retrieve an invoice by its ID.
    """
    return get_invoice_by_id(invoice_id)


# Service to get all invoices
def get_invoices():
    """
    Retrieve all invoices.
    """
    return get_all_invoices()


# Service to update an invoice by ID
def modify_invoice(invoice_id, issuer_id=None, recipient_id=None, timbrado=None, invoice_number=None, issue_date=None,
                   currency=None, iva_10=None, total_iva=None):
    """
    Update an invoice's details by its ID.
    """
    update_invoice(invoice_id, issuer_id=issuer_id, recipient_id=recipient_id, timbrado=timbrado,
                   invoice_number=invoice_number,
                   issue_date=issue_date, currency=currency, iva_10=iva_10, total_iva=total_iva)


# Service to delete an invoice by ID
def remove_invoice(invoice_id):
    """
    Delete an invoice by its ID.
    """
    delete_invoice(invoice_id)
