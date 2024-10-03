from lib.db_connection import connect


# Create a new entity (person or business)
def create_entity(name, cedula=None, ruc=None, codigo_verificador=None, email=None, address=None, phone_number=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO entities (name, cedula, ruc, codigo_verificador, email, address, phone_number)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (name, cedula, ruc, codigo_verificador, email, address, phone_number))

    conn.commit()
    conn.close()


# Read an entity by ID
def get_entity_by_id(entity_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM entities WHERE id = ?', (entity_id,))
    entity = cursor.fetchone()

    conn.close()
    return entity


# Read all entities
def get_all_entities():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM entities')
    entities = cursor.fetchall()

    conn.close()
    return entities


# Update an entity by ID
def update_entity(entity_id, name=None, cedula=None, ruc=None, codigo_verificador=None, email=None, address=None,
                  phone_number=None):
    conn = connect()
    cursor = conn.cursor()

    # Build the update query dynamically based on which fields are provided
    update_fields = []
    update_values = []

    if name:
        update_fields.append("name = ?")
        update_values.append(name)
    if cedula:
        update_fields.append("cedula = ?")
        update_values.append(cedula)
    if ruc:
        update_fields.append("ruc = ?")
        update_values.append(ruc)
    if codigo_verificador:
        update_fields.append("codigo_verificador = ?")
        update_values.append(codigo_verificador)
    if email:
        update_fields.append("email = ?")
        update_values.append(email)
    if address:
        update_fields.append("address = ?")
        update_values.append(address)
    if phone_number:
        update_fields.append("phone_number = ?")
        update_values.append(phone_number)

    update_query = f"UPDATE entities SET {', '.join(update_fields)} WHERE id = ?"
    update_values.append(entity_id)

    cursor.execute(update_query, tuple(update_values))

    conn.commit()
    conn.close()


# Delete an entity by ID
def delete_entity(entity_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM entities WHERE id = ?', (entity_id,))

    conn.commit()
    conn.close()
