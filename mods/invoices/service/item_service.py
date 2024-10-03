from mods.invoices.repository.item_repository import create_invoice_item, get_invoice_item_by_id, \
    get_items_by_invoice_id, update_invoice_item, delete_invoice_item


# Service to add an item to an invoice
def add_invoice_item(invoice_id, description, quantity, unit_price):
    """
    Add an item to an invoice.
    """
    create_invoice_item(invoice_id, description, quantity, unit_price)


# Service to get an invoice item by ID
def get_invoice_item(item_id):
    """
    Retrieve an invoice item by its ID.
    """
    return get_invoice_item_by_id(item_id)


# Service to get all items for a specific invoice
def get_items_for_invoice(invoice_id):
    """
    Retrieve all items for a specific invoice by its ID.
    """
    return get_items_by_invoice_id(invoice_id)


# Service to update an invoice item by ID
def modify_invoice_item(item_id, description=None, quantity=None, unit_price=None):
    """
    Update an invoice item's details by its ID.
    """
    update_invoice_item(item_id, description=description, quantity=quantity, unit_price=unit_price)


# Service to delete an invoice item by ID
def remove_invoice_item(item_id):
    """
    Delete an invoice item by its ID.
    """
    delete_invoice_item(item_id)
