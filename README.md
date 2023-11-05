# BigQuery

Gestión de Biblioteca.
Una biblioteca está interesada en automatizar la gestión de préstamos, para esto se pide realizar lo siguiente:

Estudiante 1:
Diseñar el procesamiento de los PRÉSTAMOS:
●Diseñar las Altas de Préstamos con los siguientes atributos: ID (código único), fecha de préstamo, fecha de devolución, y estado (por ejemplo: activo, devuelto, vencido).
●Diseñar las Bajas de Préstamos.
●Diseñar las Modificaciones de Préstamos.
●Diseñar las Consultas de Préstamos.
Tenga en cuenta las Relaciones:
●Un préstamo está asociado a un usuario, pero un usuario puede tener varios préstamos activos.
●Un préstamo se realiza en una sucursal, pero una sucursal puede tener varios préstamos activos.
●Un préstamo puede involucrar varios libros, y un libro puede estar involucrado en varios préstamos.
●Un préstamo es realizado por un empleado, pero un empleado puede realizar varios préstamos.
●Un evento puede tener varios préstamos asociados, y un préstamo puede estar relacionado con un evento (por ejemplo, eventos de promoción de lectura). Estudiante 2:
Diseñar el procesamiento de los USUARIOS:
●Diseñar las Altas de Usuarios con los siguientes atributos: ID (código único), nombre, dirección y correo electrónico.
●Diseñar las Bajas de Usuarios.
●Diseñar las Modificaciones de Usuarios.
●Diseñar las Consultas de Usuarios.
Tenga en cuenta las Relaciones:
● Un préstamo está asociado a un usuario, pero un usuario puede tener
varios préstamos activos.
● Un usuario es afiliado a una membresía, y a una membresía pueden
afiliarse muchos usuarios.
Estudiante 3:
Diseñar el procesamiento de los EMPLEADOS:
● Diseñar las Altas de Empleados con los siguientes atributos: ID (código
único), nombre, cargo y fecha de contratación.
● Diseñar las Bajas de Empleados.
● Diseñar las Modificaciones de Empleados.
● Diseñar las Consultas de Empleados.
Tenga en cuenta las Relaciones:
● Un préstamo es realizado por un empleado, pero un empleado puede
realizar varios préstamos.
● Un evento es organizado por un empleado, y un empleado puede
organizar varios eventos.
Todos:
● Elaborar el Diseño de Altas, Bajas, Modificaciones y Consultas de la
Biblioteca. Asimismo, deben integrar las tres partes para obtener un diseño
único.
● Elaborar el Programa para la Gestión de la Biblioteca según lo diseñado.
Además de Préstamos, Usuarios y Empleados, intervienen las siguientes entidades:
• LIBROS que incluye los atributos: ISBN (código único), título, año de publicación
y cantidad disponible.
• AUTORES con los atributos: ID (código único), nombre y nacionalidad.
• CATEGORÍAS de libros con atributos: ID (código único) y nombre de la
categoría.
• IDIOMAS con los atributos: ID (código único) y nombre del idioma.
• SUCURSALES con los atributos: ID (código único), nombre y ubicación.
• EDITORIALES con los atributos: ID (código único), nombre y país.
• MEMBRESÍAS de usuarios con los atributos: ID (código único), tipo de
membresía y fecha de vencimiento.
• EVENTOS de la biblioteca con los atributos: ID (código único), nombre del
evento, fecha y lugar.
Notas:
Un "evento" representa una actividad o reunión planificada que tiene lugar en la biblioteca.
Estos eventos pueden variar en naturaleza y propósito, y pueden incluir actividades como
charlas de autores, clubes de lectura, talleres educativos, ferias del libro y otras iniciativas
para fomentar la participación de la comunidad y promover la cultura de la lectura.
Una "categoría" representa una clasificación o etiqueta que se asigna a los libros para
organizarlos y facilitar su búsqueda y selección por parte de los usuarios. Por ejemplo, en
una biblioteca, los libros pueden clasificarse en diversas categorías como "Ficción", "No
Ficción", "Ciencia Ficción", "Historia", "Biografía", etc. Cada categoría proporciona una
manera de agrupar y organizar los libros según su temática o género.
Asuma todo lo que crea conveniente; puede agregar otros atributos en las entidades de ser
necesario.
