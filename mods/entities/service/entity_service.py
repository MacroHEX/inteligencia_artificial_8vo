from mods.entities.repository.entity_repository import create_entity, get_entity_by_id, get_all_entities, update_entity, \
    delete_entity


# Service to register a person with Cédula or RUC
def register_person(name, cedula=None, ruc=None, codigo_verificador=None, email=None, address=None, phone_number=None):
    """
    Register a person with either Cédula or RUC.
    Both cedula and ruc are optional, but at least one should be provided.
    """
    create_entity(name, cedula=cedula, ruc=ruc, codigo_verificador=codigo_verificador, email=email, address=address,
                  phone_number=phone_number)


# Service to register a business with RUC
def register_business(name, ruc, codigo_verificador, email, address, phone_number):
    create_entity(name, ruc=ruc, codigo_verificador=codigo_verificador, email=email, address=address,
                  phone_number=phone_number)


# Service to get an entity by ID
def get_entity(entity_id):
    """
    Retrieve an entity by its ID.
    """
    return get_entity_by_id(entity_id)


# Service to get all entities
def get_entities():
    """
    Retrieve all entities.
    """
    return get_all_entities()


# Service to update an entity by ID
def modify_entity(entity_id, name=None, cedula=None, ruc=None, codigo_verificador=None, email=None, address=None,
                  phone_number=None):
    """
    Update an entity's details by its ID.
    """
    update_entity(entity_id, name=name, cedula=cedula, ruc=ruc, codigo_verificador=codigo_verificador, email=email,
                  address=address, phone_number=phone_number)


# Service to delete an entity by ID
def remove_entity(entity_id):
    """
    Delete an entity by its ID.
    """
    delete_entity(entity_id)
