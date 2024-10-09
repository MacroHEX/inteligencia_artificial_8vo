class FacturaRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS facturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha_emision TEXT DEFAULT CURRENT_TIMESTAMP,
                    entidad_id INTEGER,
                    timbrado_id INTEGER,
                    total REAL NOT NULL,
                    estado TEXT NOT NULL,
                    FOREIGN KEY(entidad_id) REFERENCES entidades(id),
                    FOREIGN KEY(timbrado_id) REFERENCES timbrado(id)
                );
            ''')

    def insert(self, factura):
        with self.connection:
            self.connection.execute('''
                INSERT INTO facturas (fecha_emision, entidad_id, timbrado_id, total, estado)
                VALUES (?, ?, ?, ?, ?);
            ''', (factura.fecha_emision, factura.entidad_id, factura.timbrado_id, factura.total, factura.estado))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM facturas')
        return cursor.fetchall()

    def get_by_id(self, factura_id):
        cursor = self.connection.execute('SELECT * FROM facturas WHERE id = ?', (factura_id,))
        return cursor.fetchone()

    def update(self, factura_id, factura):
        with self.connection:
            self.connection.execute('''
                UPDATE facturas
                SET fecha_emision = ?, entidad_id = ?, timbrado_id = ?, total = ?, estado = ?
                WHERE id = ?;
            ''', (
            factura.fecha_emision, factura.entidad_id, factura.timbrado_id, factura.total, factura.estado, factura_id))

    def delete(self, factura_id):
        with self.connection:
            self.connection.execute('DELETE FROM facturas WHERE id = ?', (factura_id,))
