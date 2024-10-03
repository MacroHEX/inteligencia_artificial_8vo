from mods.invoices.repository.item_repository import create_invoice_item


# Service to add an item to an invoice
def add_invoice_item(invoice_id, description, quantity, unit_price):
    """Add an item to an invoice."""
    create_invoice_item(invoice_id, description, quantity, unit_price)
