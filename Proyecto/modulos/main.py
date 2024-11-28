from funciones import (
    listar_secciones,
    agregar_seccion,
    agregar_producto,
    mover_producto,
    agregar_almacen,
)

def menu():
    while True:
        print("\n=== Sistema de Gestión de Almacenes ===")
        print("1. Listar secciones de un almacén")
        print("2. Agregar sección a un almacén")
        print("3. Agregar producto a una sección")
        print("4. Mover producto entre almacenes")
        print("5. Agregar nuevo almacén")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_secciones()
        elif opcion == "2":
            agregar_seccion()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            mover_producto()
        elif opcion == "5":
            agregar_almacen()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
menu()
