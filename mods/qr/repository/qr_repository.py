class QRCodeRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS qr_codes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    factura_id INTEGER NOT NULL,
                    qr_url TEXT NOT NULL,
                    FOREIGN KEY(factura_id) REFERENCES facturas(id)
                );
            ''')

    def insert(self, qr_code):
        with self.connection:
            self.connection.execute('''
                INSERT INTO qr_codes (factura_id, qr_url)
                VALUES (?, ?);
            ''', (qr_code.factura_id, qr_code.qr_url))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM qr_codes')
        return cursor.fetchall()

    def get_by_id(self, qr_code_id):
        cursor = self.connection.execute('SELECT * FROM qr_codes WHERE id = ?', (qr_code_id,))
        return cursor.fetchone()

    def update(self, qr_code_id, qr_code):
        with self.connection:
            self.connection.execute('''
                UPDATE qr_codes
                SET factura_id = ?, qr_url = ?
                WHERE id = ?;
            ''', (qr_code.factura_id, qr_code.qr_url, qr_code_id))

    def delete(self, qr_code_id):
        with self.connection:
            self.connection.execute('DELETE FROM qr_codes WHERE id = ?', (qr_code_id,))
