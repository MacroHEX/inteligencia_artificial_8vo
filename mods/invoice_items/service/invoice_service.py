from mods.invoice_items.repository.invoice_repository import create_invoice


# Service to issue an invoice
def issue_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva):
    """Issue a new invoice."""
    create_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, total_iva)
