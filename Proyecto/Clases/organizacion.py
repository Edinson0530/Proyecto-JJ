from clases.proyecto import Proyecto

class Organizacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def agregar_proyecto(self, proyecto: Proyecto):
        self.proyectos.append(proyecto)

    def eliminar_proyecto(self, id_proyecto):
        self.proyectos = [p for p in self.proyectos if p.id != id_proyecto]

    def ordenar_por_emisiones(self):
        self.proyectos.sort(key=lambda p: p.emisiones_reducidas, reverse=True)

    def calcular_emisiones_totales(self):
        return sum(p.emisiones_reducidas for p in self.proyectos)

    def proyectos_completados(self):
        return len([p for p in self.proyectos if p.estado.lower() == "completado"])

    def mostrar_proyectos(self):
        return [p.mostrar_info() for p in self.proyectos]
