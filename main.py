from logica import (
    registrar_libro,
    listar_libros,
    buscar_libro,
    modificar_libro,
    eliminar_libro,
    reporte_libros_prestados
)

def mostrar_menu():
    print("\n=====================================")
    print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=====================================")
    print("1. Registrar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Modificar libro")
    print("5. Eliminar libro")
    print("6. Reporte de libros prestados")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción (1-7): "))
            
            if opcion == 1:
                registrar_libro()
            elif opcion == 2:
                listar_libros()
            elif opcion == 3:
                buscar_libro()
            elif opcion == 4:
                modificar_libro()
            elif opcion == 5:
                eliminar_libro()
            elif opcion == 6:
                reporte_libros_prestados()
            elif opcion == 7:
                print("\nSaliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Error: Opción inválida. Elija un número del 1 al 7.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()