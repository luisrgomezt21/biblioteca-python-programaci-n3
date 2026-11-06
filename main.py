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
            opcion = int(input("Seleccione una opción (1-7): "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido del 1 al 7.")
            continue

        if opcion == 1:
            logica.registrar_libro()
        
        elif opcion == 2:
            logica.listar_libros()
        
        elif opcion == 3:
            logica.buscar_libro(titulo)
        
        elif opcion == 4:
            logica.modificar_estado_libro(5)
        
        elif opcion == 5:
            titulo = input("Ingrese el título del libro a eliminar: ")
            confirmacion = input("¿Está seguro? (s/n): ").lower()
            if confirmacion == 's':
                logica.eliminar_libro()
            else:
                print("Operación cancelada.")
        
        elif opcion == 6:
            logica.reporte_libros_prestados()
        
        elif opcion == 7:
            print("👋 ¡Gracias por usar el sistema de biblioteca. Hasta luego!")
            break
        
        else:
            print("⚠️ Error: Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
