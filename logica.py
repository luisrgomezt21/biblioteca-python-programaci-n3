from persistencia import cargar_datos, guardar_datos

def registrar_libro():
    libros = cargar_datos()
    print("\n--- Registrar Nuevo Libro ---")
    
    titulo = input("Ingrese el título del libro: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.")
        return

    autor = input("Ingrese el autor del libro: ").strip()
    if not autor:
        print("Error: El autor no puede estar vacío.")
        return

    print("Estado del libro:")
    print("1. disponible")
    print("2. prestado")
    opcion_estado = input("Seleccione el estado (1 o 2): ").strip()
    
    if opcion_estado == "1":
        estado = "disponible"
    elif opcion_estado == "2":
        estado = "prestado"
    else:
        print("Opción inválida. Se asignará 'disponible' por defecto.")
        estado = "disponible"

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "estado": estado
    }

    libros.append(nuevo_libro)
    guardar_datos(libros)
    print("¡Libro registrado exitosamente!")

def listar_libros():
    libros = cargar_datos()
    if not libros:
        print("\nNo hay libros registrados en la biblioteca.")
        return

    print("\n--- Lista de Libros ---")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. Título: {libro['titulo']} | Autor: {libro['autor']} | Estado: {libro['estado']}")

def buscar_libro():
    libros = cargar_datos()
    if not libros:
        print("\nNo hay libros registrados para buscar.")
        return

    criterio = input("\nIngrese el título del libro a buscar: ").strip().lower()
    if not criterio:
        print("Error: El campo de búsqueda no puede estar vacío.")
        return

    encontrados = [l for l in libros if criterio in l['titulo'].lower()]

    if not encontrados:
        print("No se encontraron libros con ese título.")
        return

    print("\n--- Resultados de la Búsqueda ---")
    for libro in encontrados:
        print(f"- Título: {libro['titulo']} | Autor: {libro['autor']} | Estado: {libro['estado']}")

def modificar_libro():
    libros = cargar_datos()
    if not libros:
        print("\nNo hay libros registrados para modificar.")
        return

    listar_libros()
    try:
        indice = int(input("\nIngrese el número del libro que desea modificar: ")) - 1
        if indice < 0 or indice >= len(libros):
            print("Error: Número de libro inválido.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    libro = libros[indice]
    print(f"\nModificando libro: {libro['titulo']}")
    
    nuevo_titulo = input(f"Nuevo título (dejar en blanco para mantener '{libro['titulo']}'): ").strip()
    nuevo_autor = input(f"Nuevo autor (dejar en blanco para mantener '{libro['autor']}'): ").strip()
    
    print(f"Estado actual: {libro['estado']}")
    print("1. disponible")
    print("2. prestado")
    nuevo_estado_op = input("Seleccione nuevo estado (o presione Enter para mantener): ").strip()

    if nuevo_titulo:
        libro['titulo'] = nuevo_titulo
    if nuevo_autor:
        libro['autor'] = nuevo_autor
    
    if nuevo_estado_op == "1":
        libro['estado'] = "disponible"
    elif nuevo_estado_op == "2":
        libro['estado'] = "prestado"
    elif nuevo_estado_op != "":
        print("Opción inválida, se mantiene el estado anterior.")

    guardar_datos(libros)
    print("¡Libro modificado exitosamente!")

def eliminar_libro():
    libros = cargar_datos()
    if not libros:
        print("\nNo hay libros registrados para eliminar.")
        return

    listar_libros()
    try:
        indice = int(input("\nIngrese el número del libro que desea eliminar: ")) - 1
        if indice < 0 or indice >= len(libros):
            print("Error: Número de libro inválido.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    libro_eliminado = libros.pop(indice)
    guardar_datos(libros)
    print(f"Libro '{libro_eliminado['titulo']}' eliminado exitosamente.")

def reporte_libros_prestados():
    libros = cargar_datos()
    prestados = [l for l in libros if l['estado'] == "prestado"]

    print("\n--- Reporte: Libros Prestados ---")
    if not prestados:
        print("No hay libros prestados actualmente.")
        return

    for i, libro in enumerate(prestados, 1):
        print(f"{i}. Título: {libro['titulo']} | Autor: {libro['autor']}")
    print(f"\nTotal de libros prestados: {len(prestados)}")