from clases.proyecto import Proyecto
from clases.organizacion import Organizacion

def menu():
    organizacion = Organizacion("GreenTech Global")
    while True:
        print("\n--- Menú de Gestión de Proyectos ---")
        print("1. Crear un nuevo proyecto")
        print("2. Mostrar información de todos los proyectos")
        print("3. Actualizar el estado de un proyecto")
        print("4. Ordenar proyectos por impacto (emisiones reducidas)")
        print("5. Calcular el total de emisiones reducidas")
        print("6. Determinar cuántos proyectos han sido completados")
        print("7. Eliminar un proyecto")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID del proyecto: "))
            nombre = input("Nombre del proyecto: ")
            tipo = input("Tipo de energía (Solar, Eólica, etc.): ")
            ubicacion = input("Ubicación: ")
            responsable = input("Responsable del proyecto: ")
            emisiones = float(input("Emisiones reducidas (en toneladas): "))
            energia = float(input("Energía generada (en kWh): "))
            estado = input("Estado (En Proceso, Completado, etc.): ")
            proyecto = Proyecto(id, nombre, tipo, ubicacion, responsable, emisiones, energia, estado)
            organizacion.agregar_proyecto(proyecto)
            print("Proyecto agregado exitosamente.")

        elif opcion == "2":
            print("\n--- Información de Proyectos ---")
            for info in organizacion.mostrar_proyectos():
                print(info)

        elif opcion == "3":
            id = int(input("ID del proyecto a actualizar: "))
            nuevo_estado = input("Nuevo estado: ")
            for proyecto in organizacion.proyectos:
                if proyecto.id == id:
                    proyecto.cambiar_estado(nuevo_estado)
                    print("Estado actualizado exitosamente.")
                    break
            else:
                print("Proyecto no encontrado.")

        elif opcion == "4":
            organizacion.ordenar_por_emisiones()
            print("Proyectos ordenados por emisiones reducidas.")

        elif opcion == "5":
            total_emisiones = organizacion.calcular_emisiones_totales()
            print(f"Total de emisiones reducidas: {total_emisiones} T")

        elif opcion == "6":
            completados = organizacion.proyectos_completados()
            print(f"Proyectos completados: {completados}")

        elif opcion == "7":
            id = int(input("ID del proyecto a eliminar: "))
            organizacion.eliminar_proyecto(id)
            print("Proyecto eliminado exitosamente.")

        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
