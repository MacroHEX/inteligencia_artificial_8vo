class TimbradoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS timbrado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_de_documento TEXT NOT NULL,
                    numero_timbrado TEXT NOT NULL,
                    establecimiento TEXT NOT NULL,
                    punto_expedicion TEXT NOT NULL,
                    numero_documento TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL
                );
            ''')

    def insert(self, timbrado):
        with self.connection:
            self.connection.execute('''
                INSERT INTO timbrado (tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion, numero_documento, fecha_inicio)
                VALUES (?, ?, ?, ?, ?, ?);
            ''', (timbrado.tipo_de_documento, timbrado.numero_timbrado, timbrado.establecimiento,
                  timbrado.punto_expedicion, timbrado.numero_documento, timbrado.fecha_inicio))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM timbrado')
        return cursor.fetchall()

    def get_by_id(self, timbrado_id):
        cursor = self.connection.execute('SELECT * FROM timbrado WHERE id = ?', (timbrado_id,))
        return cursor.fetchone()

    def update(self, timbrado_id, timbrado):
        with self.connection:
            self.connection.execute('''
                UPDATE timbrado
                SET tipo_de_documento = ?, numero_timbrado = ?, establecimiento = ?, punto_expedicion = ?, numero_documento = ?, fecha_inicio = ?
                WHERE id = ?;
            ''', (timbrado.tipo_de_documento, timbrado.numero_timbrado, timbrado.establecimiento,
                  timbrado.punto_expedicion, timbrado.numero_documento, timbrado.fecha_inicio, timbrado_id))

    def delete(self, timbrado_id):
        with self.connection:
            self.connection.execute('DELETE FROM timbrado WHERE id = ?', (timbrado_id,))
