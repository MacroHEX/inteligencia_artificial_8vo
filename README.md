# Aplicación de Facturación Generada por IAGen

Este proyecto es una aplicación de facturación simple desarrollada utilizando SQLite como base de datos y con una
interfaz gráfica de usuario (GUI) completamente funcional. La aplicación permite la gestión de entidades (personas o
empresas), la creación de facturas y la asignación de ítems a dichas facturas. Está diseñada para almacenar información
relevante de las entidades, emitir facturas y detallar los productos o servicios facturados. Todas las pantallas de la
GUI incluyen el nombre completo del alumno en la esquina superior derecha, conforme a los criterios de evaluación.

La implementación de la Inteligencia Artificial Generativa (IAGen) en este proyecto sigue la línea de investigaciones
recientes que demuestran su capacidad para automatizar tareas repetitivas en el desarrollo de software, como la
generación de bases de datos y operaciones CRUD. En particular, Zhang et al. (2023), en el Journal of Software
Engineering, explican cómo los modelos generativos han mostrado una mejora en la productividad de los desarrolladores al
reducir la cantidad de código manual que deben escribir.

## Características

- **Gestión de entidades:** Almacena información de personas o empresas, incluyendo cédula, RUC, dirección, correo
  electrónico y número de teléfono, con los campos terminando en las tres primeras letras de mi apellido.
- **Creación de facturas:**  Permite crear facturas vinculadas a emisores (entidades) y receptores, con detalles como
  fecha de emisión, número de timbrado y valores de IVA.
- **Ítems en facturas:** Cada factura puede incluir múltiples ítems, con su descripción, cantidad, precio unitario y
  precio total.
- **Interfaz gráfica (GUI):** La interfaz gráfica permite al usuario interactuar con la aplicación de manera sencilla y
  visual, facilitando la gestión de entidades, facturas e ítems sin necesidad de trabajar directamente con el código.

La base de datos utilizada es SQLite, una elección adecuada para proyectos pequeños y medianos debido a su eficiencia y
simplicidad. La documentación oficial de SQLite (2023) la describe como una de las bases de datos más usadas a nivel
mundial, especialmente en proyectos donde la integración directa en el código es esencial.

## Estructura de la base de datos

La base de datos está compuesta por las siguientes entidades:

1. **Entidad:** Almacena las entidades (personas o negocios).

    - **nombre_med:** Nombre de la entidad.
    - **tipo_med:** Tipo de entidad, que puede ser "Persona Física", "Persona Jurídica" o "No Contribuyente".
    - **ruc_med:** RUC de la entidad (opcional).
    - **direccion_med:** Dirección de la entidad (opcional).
    - **telefono_med:** Número de teléfono de la entidad (opcional).
    - **email_med:** Correo electrónico de la entidad (opcional).
    - **cedula_med:** Cédula de la persona (opcional).

2. **Factura:** Almacena las facturas emitidas.

    - **fecha_emision_med:** Fecha de emisión de la factura.
    - **entidad_id_med:** ID de la entidad que emite la factura.
    - **timbrado_id_med:** ID del timbrado asociado.
    - **total_med:** Total de la factura.
    - **estado_med:** Estado de la factura.

3. **Producto:** Almacena los productos ofrecidos.

    - **codigo_interno_med:** Código interno del producto.
    - **nombre_med:** Nombre del producto.
    - **descripcion_med:** Descripción del producto.
    - **precio_med:** Precio del producto.
    - **stock_med:** Cantidad disponible en stock.

4. **DetalleFactura:** Almacena los ítems dentro de las facturas.

    - **factura_id_med:** ID de la factura a la que pertenece el ítem.
    - **producto_id_med:** ID del producto facturado.
    - **cantidad_med:** Cantidad de productos facturados.
    - **precio_unitario_med:** Precio unitario del producto.
    - **subtotal_med:** Subtotal calculado para este ítem.
    -
5. **Timbrado:** Almacena la información del timbrado.

    - **tipo_de_documento_med:** Tipo de documento emitido.
    - **numero_timbrado_med:** Número de timbrado.
    - **establecimiento_med:** Establecimiento del emisor.
    - **punto_expedicion_med:** Punto de expedición del documento.
    - **numero_documento_med:** Número de documento asociado.
    - **fecha_inicio_med:** Fecha de inicio del timbrado.

## Funciones principales

El archivo `main.py` se encarga de inicializar la base de datos y ejecutar la interfaz gráfica.

- **setup_database():** Configura la base de datos creando las tablas necesarias.
- **create_entity():** Permite crear una nueva entidad, ya sea una persona o una empresa.
- **create_invoice():** Permite crear una nueva factura.
- **create_invoice_item():** Permite agregar ítems a una factura existente.

En el `main.py`, los servicios asociados a cada entidad (entidad, timbrado, producto, factura y detalle de factura) se
inicializan al establecer la conexión con la base de datos y se pasan a la interfaz gráfica principal (`MainWindow`),
que gestiona las operaciones del usuario.

La manipulación de imágenes en la interfaz gráfica se realiza mediante Pillow, una biblioteca de procesamiento de
imágenes en Python que ha demostrado ser extremadamente versátil y fácil de integrar con Tkinter. Según la documentación
oficial de Pillow (2023), es una de las bibliotecas más usadas para la manipulación de imágenes en proyectos de Python
que requieren interfaces gráficas.

## Conclusiones y recomendaciones

Este proyecto demuestra la efectividad del uso de la IAGen para generar código de aplicaciones de facturación simples.
Aunque el código generado requiere ajustes manuales menores, es una herramienta valiosa para automatizar partes del
proceso de desarrollo, especialmente en la creación de bases de datos y CRUD. Recomendamos continuar explorando
estrategias de prompting para optimizar los resultados y aplicar la IAGen en proyectos más complejos.

## Requisitos

- Python 3.x
- SQLite3 (incluido por defecto en Python)
- **Pillow** (para la manipulación de imágenes en la interfaz gráfica)

## Instrucciones de instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Instala las dependencias necesarias ejecutando el siguiente comando:

   ```bash
   pip install pillow
   ```

4. Ejecuta el script para crear la base de datos e iniciar la interfaz.

## Licencia

Este proyecto está bajo la Licencia [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).