class ImpuestoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS impuestos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    porcentaje REAL NOT NULL
                );
            ''')

    def insert(self, impuesto):
        with self.connection:
            self.connection.execute('''
                INSERT INTO impuestos (nombre, porcentaje)
                VALUES (?, ?);
            ''', (impuesto.nombre, impuesto.porcentaje))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM impuestos')
        return cursor.fetchall()

    def get_by_id(self, impuesto_id):
        cursor = self.connection.execute('SELECT * FROM impuestos WHERE id = ?', (impuesto_id,))
        return cursor.fetchone()

    def update(self, impuesto_id, impuesto):
        with self.connection:
            self.connection.execute('''
                UPDATE impuestos
                SET nombre = ?, porcentaje = ?
                WHERE id = ?;
            ''', (impuesto.nombre, impuesto.porcentaje, impuesto_id))

    def delete(self, impuesto_id):
        with self.connection:
            self.connection.execute('DELETE FROM impuestos WHERE id = ?', (impuesto_id,))
