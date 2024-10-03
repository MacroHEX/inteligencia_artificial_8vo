from mods.invoice_items.model.invoice_model import create_invoices_table
from mods.invoices.model.item_model import create_items_table


def setup_database():
    """Sets up the database by creating all the necessary tables."""
    from mods.entities.model.entity_model import create_entities_table

    # Call table creation functions
    create_entities_table()
    create_invoices_table()
    create_items_table()
