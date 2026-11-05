import logica

def mostrar_menu():
    print("\n" + "="*40)
    print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚")
    print("="*40)
    print("1. Registrar un nuevo libro")
    print("2. Listar todos los libros")
    print("3. Buscar libro por título")
    print("4. Modificar estado (Disponible / Prestado)")
    print("5. Eliminar un libro")
    print("6. Reporte de libros prestados")
    print("7. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("👉 Seleccione una opción (1-7): "))
        except ValueError:
            print("⚠️ Error: Por favor, ingrese un número válido del 1 al 7.")
            continue

        if opcion == 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            print(logica.registrar_libro(titulo, autor))
        
        elif opcion == 2:
            print(logica.listar_libros())
        
        elif opcion == 3:
            titulo = input("Ingrese el título (o parte de él) a buscar: ")
            print(logica.buscar_libro(titulo))
        
        elif opcion == 4:
            titulo = input("Ingrese el título del libro a modificar: ")
            print("Estados válidos: 'Disponible' o 'Prestado'")
            nuevo_estado = input("Ingrese el nuevo estado: ").strip().capitalize()
            if nuevo_estado in ["Disponible", "Prestado"]:
                print(logica.modificar_estado_libro(titulo, nuevo_estado))
            else:
                print("❌ Error: Estado no válido. Use 'Disponible' o 'Prestado'.")
        
        elif opcion == 5:
            titulo = input("Ingrese el título del libro a eliminar: ")
            confirmacion = input("¿Está seguro? (s/n): ").lower()
            if confirmacion == 's':
                print(logica.eliminar_libro(titulo))
            else:
                print("Operación cancelada.")
        
        elif opcion == 6:
            print(logica.reporte_libros_prestados())
        
        elif opcion == 7:
            print("👋 ¡Gracias por usar el sistema de biblioteca. Hasta luego!")
            break
        
        else:
            print("⚠️ Error: Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
