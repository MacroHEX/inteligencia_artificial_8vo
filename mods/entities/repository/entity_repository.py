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

# Additional CRUD operations can go here (read, update, delete)
