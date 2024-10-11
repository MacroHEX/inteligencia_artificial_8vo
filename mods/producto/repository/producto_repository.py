class ProductoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo_interno_med TEXT NOT NULL,
                    nombre_med TEXT NOT NULL,
                    descripcion_med TEXT,
                    precio_med REAL NOT NULL,
                    stock_med INTEGER NOT NULL
                );
            ''')

    def insert(self, producto):
        with self.connection:
            self.connection.execute('''
                INSERT INTO productos (codigo_interno_med, nombre_med, descripcion_med, precio_med, stock_med)
                VALUES (?, ?, ?, ?, ?);
            ''', (producto.codigo_interno_med, producto.nombre_med, producto.descripcion_med, producto.precio_med, producto.stock_med))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM productos')
        return cursor.fetchall()

    def get_by_id(self, producto_id_med):
        cursor = self.connection.execute('SELECT * FROM productos WHERE id = ?', (producto_id_med,))
        return cursor.fetchone()

    def update(self, producto_id_med, producto):
        with self.connection:
            self.connection.execute('''
                UPDATE productos
                SET codigo_interno_med = ?, nombre_med = ?, descripcion_med = ?, precio_med = ?, stock_med = ?
                WHERE id = ?;
            ''', (producto.codigo_interno_med, producto.nombre_med, producto.descripcion_med, producto.precio_med, producto.stock_med,
                  producto_id_med))

    def delete(self, producto_id_med):
        with self.connection:
            self.connection.execute('DELETE FROM productos WHERE id = ?', (producto_id_med,))
