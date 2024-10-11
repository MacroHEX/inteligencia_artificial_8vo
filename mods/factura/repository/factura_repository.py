class FacturaRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS facturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha_emision_med TEXT DEFAULT CURRENT_TIMESTAMP,
                    entidad_id_med INTEGER,
                    timbrado_id_med INTEGER,
                    total_med REAL NOT NULL,
                    estado_med TEXT NOT NULL,
                    FOREIGN KEY(entidad_id_med) REFERENCES entidades(id),
                    FOREIGN KEY(timbrado_id_med) REFERENCES timbrado(id)
                );
            ''')

    def insert(self, factura):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('''
                   INSERT INTO facturas (fecha_emision_med, entidad_id_med, timbrado_id_med, total_med, estado_med)
                   VALUES (?, ?, ?, ?, ?);
               ''', (factura.fecha_emision_med, factura.entidad_id_med, factura.timbrado_id_med, factura.total_med, factura.estado_med))

            # Return the generated factura_id_med (last inserted row ID)
            return cursor.lastrowid

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM facturas')
        return cursor.fetchall()

    def get_by_id(self, factura_id_med):
        cursor = self.connection.execute('SELECT * FROM facturas WHERE id = ?', (factura_id_med,))
        return cursor.fetchone()

    def update(self, factura_id_med, factura):
        with self.connection:
            self.connection.execute('''
                UPDATE facturas
                SET fecha_emision_med = ?, entidad_id_med = ?, timbrado_id_med = ?, total_med = ?, estado_med = ?
                WHERE id = ?;
            ''', (
                factura.fecha_emision_med, factura.entidad_id_med, factura.timbrado_id_med, factura.total_med, factura.estado_med,
                factura_id_med))

    def delete(self, factura_id_med):
        with self.connection:
            self.connection.execute('DELETE FROM facturas WHERE id = ?', (factura_id_med,))
