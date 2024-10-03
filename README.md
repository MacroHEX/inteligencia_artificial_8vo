# Aplicación de Facturación

Este proyecto es una aplicación de facturación simple desarrollada utilizando SQLite como base de datos, y próximamente
contará con una interfaz gráfica de usuario (GUI). La aplicación permite la gestión de entidades (personas o empresas),
la creación de facturas y la asignación de ítems a dichas facturas. Está diseñada para almacenar información relevante
de las entidades, emitir facturas y detallar los productos o servicios facturados.

## Características

- **Gestión de entidades:** Almacena información de personas o empresas, incluyendo cédula, RUC, dirección, email y
  número de teléfono.
- **Creación de facturas:** Permite crear facturas vinculadas a emisores (entidades) y receptores, con detalles como
  fecha de emisión, número de timbrado y valores de IVA.
- **Ítems en facturas:** Cada factura puede incluir múltiples ítems, con su descripción, cantidad, precio unitario y
  precio total.
- **Interfaz gráfica (GUI):** Se añadirá una interfaz gráfica para facilitar el uso de la aplicación, permitiendo al
  usuario interactuar de manera más amigable sin necesidad de trabajar directamente con el código.

## Estructura de la base de datos

La base de datos está compuesta por las siguientes tablas:

1. entities: Almacena las entidades (personas o negocios).

    - `id`: Identificador único.
    - `name`: Nombre de la entidad.
    - `cedula`: Cédula de la persona (opcional).
    - `ruc`: RUC de la entidad (opcional).
    - `codigo_verificador`: Código verificador del RUC (opcional).
    - `email`: Correo electrónico de la entidad.
    - `address`: Dirección de la entidad.
    - `phone_number`: Número de teléfono de la entidad.

2. invoices: Almacena las facturas emitidas.

    - `id`: Identificador único.
    - `issuer_id`: ID del emisor (entidad que emite la factura).
    - `recipient_id`: ID del receptor (entidad que recibe la factura).
    - `timbrado`: Número de timbrado de la factura.
    - `invoice_number`: Número de la factura.
    - `issue_date`: Fecha de emisión.
    - `currency`: Moneda en que se emite la factura.
    - `iva_10`: Monto de IVA al 10%.
    - `total_iva`: Monto total del IVA.

3. `invoice_items`: Almacena los ítems dentro de las facturas.

    - `id`: Identificador único.
    - `invoice_id`: ID de la factura a la que pertenece el ítem.
    - `description`: Descripción del producto o servicio.
    - `quantity`: Cantidad del producto o servicio.
    - `unit_price`: Precio unitario.
    - `total_price`: Precio total (cantidad * precio unitario).

## Funciones principales

- **setup_database():** Configura la base de datos creando las tablas necesarias.
- **create_entity():** Permite crear una nueva entidad, ya sea una persona o una empresa.
- **create_invoice():** Permite crear una nueva factura.
- **create_invoice_item():** Permite agregar ítems a una factura existente.

## Ejemplo de Uso

```python
if __name__ == '__main__':
    setup_database()

    # Crear una entidad (persona con cédula)
    create_entity('Martin Medina', cedula='123456', email='micorreo@gmail.com', address='1234 Address St',
                  phone_number='0981234567')

    # Crear una entidad (empresa con RUC)
    create_entity('Banco SA', ruc='80019270', codigo_verificador='2', email='banco@baco.com',
                  address='MCAL. 3233', phone_number='0216274000')

    # Crear una factura con el emisor y receptor
    create_invoice(
        issuer_id=2,  # Banco SA (Empresa)
        recipient_id=1,  # Martin Medina (Persona)
        timbrado='15710667',
        invoice_number='001-001-8111605',
        issue_date='2024-09-26 12:00:00',
        currency='PYG',
        iva_10=79.0,
        total_iva=79.0
    )

    # Crear un ítem en la factura
    create_invoice_item(
        invoice_id=1,
        description='Compras Exterior-20120508214',
        quantity=1,
        unit_price=866.0
    )

    print("¡Factura e ítems creados con éxito!")

```

## Créditos

Este proyecto fue desarrollado 100% con herramientas de inteligencia artificial, con algunas correcciones manuales, para
la clase **Inteligencia Artificial y Sistemas Expertos**, impartida por el profesor **Miguel Duarte** y realizado por *
*Martín Medina**.

## Requisitos

- Python 3.x
- SQLite3 (incluido por defecto en Python)

## Instrucciones de instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Ejecuta el script para crear la base de datos y agregar algunas entidades y facturas de ejemplo.

## Próximos pasos

Se desarrollará una interfaz gráfica (GUI) para mejorar la experiencia del usuario, permitiendo un manejo más fácil y
visual de la aplicación sin necesidad de interactuar directamente con el código.

Licencia
Este proyecto está bajo la Licencia [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).