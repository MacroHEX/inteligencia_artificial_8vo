class EntidadRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS entidades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    ruc TEXT UNIQUE,
                    direccion TEXT,
                    telefono TEXT,
                    email TEXT,
                    cedula TEXT UNIQUE
                );
            ''')

    def insert(self, entidad):
        with self.connection:
            self.connection.execute('''
                INSERT INTO entidades (nombre, tipo, ruc, direccion, telefono, email, cedula)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            ''', (entidad.nombre, entidad.tipo, entidad.ruc, entidad.direccion, entidad.telefono, entidad.email,
                  entidad.cedula))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM entidades')
        return cursor.fetchall()

    def get_by_id(self, entidad_id):
        cursor = self.connection.execute('SELECT * FROM entidades WHERE id = ?', (entidad_id,))
        return cursor.fetchone()

    def update(self, entidad_id, entidad):
        with self.connection:
            self.connection.execute('''
                UPDATE entidades
                SET nombre = ?, tipo = ?, ruc = ?, direccion = ?, telefono = ?, email = ?, cedula = ?
                WHERE id = ?;
            ''', (entidad.nombre, entidad.tipo, entidad.ruc, entidad.direccion, entidad.telefono, entidad.email,
                  entidad.cedula, entidad_id))

    def delete(self, entidad_id):
        with self.connection:
            self.connection.execute('DELETE FROM entidades WHERE id = ?', (entidad_id,))
