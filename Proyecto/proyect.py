class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones_reducidas, energia_generada, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones_reducidas = emisiones_reducidas
        self.energia_generada = energia_generada
        self.estado = estado

    def mostrar_informacion(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Responsable: {self.responsable}")
        print(f"Emisiones Reducidas: {self.emisiones_reducidas} toneladas")
        print(f"Energía Generada: {self.energia_generada} MW")
        print(f"Estado: {self.estado}")
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Estado del proyecto {self.nombre} actualizado a: {self.estado}")

class Responsable:
    def __init__(self, dni, nombre, apellido, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")

class Organizacion:
    def __init__(self, nombre, responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print(f"Proyecto {proyecto.nombre} agregado a la organización {self.nombre}.")

    def eliminar_proyecto(self, proyecto_id):
        self.proyectos = [p for p in self.proyectos if p.id != proyecto_id]
        print(f"Proyecto con ID {proyecto_id} eliminado de la organización {self.nombre}.")

    def ordenar_proyectos_por_emisiones(self):
        self.proyectos.sort(key=lambda p: p.emisiones_reducidas, reverse=True)
        print("Proyectos ordenados por emisiones reducidas.")

    def mostrar_proyectos(self):
        if not self.proyectos:
            print("No hay proyectos disponibles.")
        else:
            for proyecto in self.proyectos:
                proyecto.mostrar_informacion()

    def contar_proyectos_completados(self):
        completados = [p for p in self.proyectos if p.estado == "completado"]
        return len(completados)
