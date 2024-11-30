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

    def actualizar_emisiones(self, nuevas_emisiones):
        self.emisiones_reducidas = nuevas_emisiones

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_info(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Ubicación: {self.ubicacion}, " \
               f"Responsable: {self.responsable}, Emisiones Reducidas: {self.emisiones_reducidas} T, " \
               f"Energía Generada: {self.energia_generada} kWh, Estado: {self.estado}"
