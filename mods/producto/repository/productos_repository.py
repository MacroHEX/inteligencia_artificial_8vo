class ProductoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo_interno TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL
                );
            ''')

    def insert(self, producto):
        with self.connection:
            self.connection.execute('''
                INSERT INTO productos (codigo_interno, nombre, descripcion, precio, stock)
                VALUES (?, ?, ?, ?, ?);
            ''', (producto.codigo_interno, producto.nombre, producto.descripcion, producto.precio, producto.stock))

    def get_all(self):
        cursor = self.connection.execute('SELECT * FROM productos')
        return cursor.fetchall()

    def get_by_id(self, producto_id):
        cursor = self.connection.execute('SELECT * FROM productos WHERE id = ?', (producto_id,))
        return cursor.fetchone()

    def update(self, producto_id, producto):
        with self.connection:
            self.connection.execute('''
                UPDATE productos
                SET codigo_interno = ?, nombre = ?, descripcion = ?, precio = ?, stock = ?
                WHERE id = ?;
            ''', (producto.codigo_interno, producto.nombre, producto.descripcion, producto.precio, producto.stock,
                  producto_id))

    def delete(self, producto_id):
        with self.connection:
            self.connection.execute('DELETE FROM productos WHERE id = ?', (producto_id,))
