from mods.entities.repository.entity_repository import create_entity


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
