class DetalleFacturaRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS detalles_factura (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    factura_id INTEGER NOT NULL,
                    producto_id INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    subtotal REAL NOT NULL,
                    FOREIGN KEY(factura_id) REFERENCES facturas(id),
                    FOREIGN KEY(producto_id) REFERENCES productos(id)
                );
            ''')

    def insert(self, detalle_factura):
        with self.connection:
            self.connection.execute('''
                INSERT INTO detalles_factura (factura_id, producto_id, cantidad, precio_unitario, subtotal)
                VALUES (?, ?, ?, ?, ?);
            ''', (detalle_factura.factura_id, detalle_factura.producto_id, detalle_factura.cantidad,
                  detalle_factura.precio_unitario, detalle_factura.subtotal))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM detalles_factura')
        return cursor.fetchall()

    def get_by_id(self, detalle_id):
        cursor = self.connection.execute('SELECT * FROM detalles_factura WHERE id = ?', (detalle_id,))
        return cursor.fetchone()

    def update(self, detalle_id, detalle_factura):
        with self.connection:
            self.connection.execute('''
                UPDATE detalles_factura
                SET factura_id = ?, producto_id = ?, cantidad = ?, precio_unitario = ?, subtotal = ?
                WHERE id = ?;
            ''', (detalle_factura.factura_id, detalle_factura.producto_id, detalle_factura.cantidad,
                  detalle_factura.precio_unitario, detalle_factura.subtotal, detalle_id))

    def delete(self, detalle_id):
        with self.connection:
            self.connection.execute('DELETE FROM detalles_factura WHERE id = ?', (detalle_id,))
