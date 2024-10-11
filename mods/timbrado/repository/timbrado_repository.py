class TimbradoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS timbrado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_de_documento_med TEXT NOT NULL,
                    numero_timbrado_med TEXT NOT NULL,
                    establecimiento_med TEXT NOT NULL,
                    punto_expedicion_med TEXT NOT NULL,
                    numero_documento_med INTEGER NOT NULL,
                    fecha_inicio_med TEXT NOT NULL
                );
            ''')

    def insert(self, timbrado):
        with self.connection:
            self.connection.execute('''
                INSERT INTO timbrado (tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med, numero_documento_med, fecha_inicio_med)
                VALUES (?, ?, ?, ?, ?, ?);
            ''', (
                timbrado.tipo_de_documento_med,  # Ensure this is a string
                timbrado.numero_timbrado_med,  # Ensure this is a string
                timbrado.establecimiento_med,  # Ensure this is a string
                timbrado.punto_expedicion_med,  # Ensure this is a string
                timbrado.numero_documento_med,  # Ensure this is handled correctly (string or int based on type)
                timbrado.fecha_inicio_med  # Ensure this is a string representing the date
            ))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM timbrado')
        return cursor.fetchall()

    def get_by_id(self, timbrado_id_med):
        cursor = self.connection.execute('SELECT * FROM timbrado WHERE id = ?', (timbrado_id_med,))
        return cursor.fetchone()

    def update(self, timbrado_id_med, tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med,
               numero_documento_med, fecha_inicio_med):
        with self.connection:
            self.connection.execute('''
                UPDATE timbrado
                SET tipo_de_documento_med = ?, numero_timbrado_med = ?, establecimiento_med = ?, punto_expedicion_med = ?, numero_documento_med = ?, fecha_inicio_med = ?
                WHERE id = ?;
            ''', (tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med, numero_documento_med, fecha_inicio_med,
                  timbrado_id_med))

    def delete(self, timbrado_id_med):
        with self.connection:
            self.connection.execute('DELETE FROM timbrado WHERE id = ?', (timbrado_id_med,))
