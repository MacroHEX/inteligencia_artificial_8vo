class DetalleFacturaRepository:
    def __init__(self, connection):
        self.connection = connection

    def crear_tabla(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS detalles_factura (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    factura_id_med INTEGER NOT NULL,
                    producto_id_med INTEGER NOT NULL,
                    cantidad_med INTEGER NOT NULL,
                    precio_unitario_med REAL NOT NULL,
                    subtotal_med REAL NOT NULL,
                    FOREIGN KEY(factura_id_med) REFERENCES facturas(id),
                    FOREIGN KEY(producto_id_med) REFERENCES productos(id)
                );
            ''')

    def insertar(self, detalle_factura):
        with self.connection:
            self.connection.execute('''
                INSERT INTO detalles_factura (factura_id_med, producto_id_med, cantidad_med, precio_unitario_med, subtotal_med)
                VALUES (?, ?, ?, ?, ?);
            ''', (detalle_factura.factura_id_med, detalle_factura.producto_id_med, detalle_factura.cantidad_med,
                  detalle_factura.precio_unitario_med, detalle_factura.subtotal_med))

    def listar_detalles(self):
        cursor = self.connection.execute('SELECT * FROM detalles_factura')
        return cursor.fetchall()

    def listar_detalle_por_id(self, detalle_id):
        cursor = self.connection.execute('SELECT * FROM detalles_factura WHERE id = ?', (detalle_id,))
        return cursor.fetchone()

    def actualizar_detalle_factura(self, detalle_id, detalle_factura):
        with self.connection:
            self.connection.execute('''
                UPDATE detalles_factura
                SET factura_id_med = ?, producto_id_med = ?, cantidad_med = ?, precio_unitario_med = ?, subtotal_med = ?
                WHERE id = ?;
            ''', (detalle_factura.factura_id_med, detalle_factura.producto_id_med, detalle_factura.cantidad_med,
                  detalle_factura.precio_unitario_med, detalle_factura.subtotal_med, detalle_id))

    def eliminar_detalle_factura(self, detalle_id):
        with self.connection:
            self.connection.execute('DELETE FROM detalles_factura WHERE id = ?', (detalle_id,))
