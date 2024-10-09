class PagoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS pagos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    factura_id INTEGER NOT NULL,
                    fecha_pago TEXT DEFAULT CURRENT_TIMESTAMP,
                    monto REAL NOT NULL,
                    metodo_pago TEXT NOT NULL,
                    FOREIGN KEY(factura_id) REFERENCES facturas(id)
                );
            ''')

    def insert(self, pago):
        with self.connection:
            self.connection.execute('''
                INSERT INTO pagos (factura_id, fecha_pago, monto, metodo_pago)
                VALUES (?, ?, ?, ?);
            ''', (pago.factura_id, pago.fecha_pago, pago.monto, pago.metodo_pago))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM pagos')
        return cursor.fetchall()

    def get_by_id(self, pago_id):
        cursor = self.connection.execute('SELECT * FROM pagos WHERE id = ?', (pago_id,))
        return cursor.fetchone()

    def update(self, pago_id, pago):
        with self.connection:
            self.connection.execute('''
                UPDATE pagos
                SET factura_id = ?, fecha_pago = ?, monto = ?, metodo_pago = ?
                WHERE id = ?;
            ''', (pago.factura_id, pago.fecha_pago, pago.monto, pago.metodo_pago, pago_id))

    def delete(self, pago_id):
        with self.connection:
            self.connection.execute('DELETE FROM pagos WHERE id = ?', (pago_id,))
