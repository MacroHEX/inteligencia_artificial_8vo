class EntidadRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS entidades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_med TEXT NOT NULL,
                    tipo_med TEXT NOT NULL,
                    ruc_med TEXT UNIQUE,
                    direccion_med TEXT,
                    telefono_med TEXT,
                    email_med TEXT,
                    cedula_med TEXT UNIQUE
                );
            ''')

    def insert(self, entidad):
        with self.connection:
            self.connection.execute('''
                INSERT INTO entidades (nombre_med, tipo_med, ruc_med, direccion_med, telefono_med, email_med, cedula_med)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            ''', (entidad.nombre_med, entidad.tipo_med, entidad.ruc_med, entidad.direccion_med, entidad.telefono_med, entidad.email_med,
                  entidad.cedula_med))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM entidades')
        return cursor.fetchall()

    def get_by_id(self, entidad_id_med):
        cursor = self.connection.execute('SELECT * FROM entidades WHERE id = ?', (entidad_id_med,))
        return cursor.fetchone()

    def update(self, entidad_id_med, entidad):
        with self.connection:
            self.connection.execute('''
                UPDATE entidades
                SET nombre_med = ?, tipo_med = ?, ruc_med = ?, direccion_med = ?, telefono_med = ?, email_med = ?, cedula_med = ?
                WHERE id = ?;
            ''', (entidad.nombre_med, entidad.tipo_med, entidad.ruc_med, entidad.direccion_med, entidad.telefono_med, entidad.email_med,
                  entidad.cedula_med, entidad_id_med))

    def delete(self, entidad_id_med):
        with self.connection:
            self.connection.execute('DELETE FROM entidades WHERE id = ?', (entidad_id_med,))
