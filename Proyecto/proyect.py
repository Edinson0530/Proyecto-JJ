class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones_reducidas=0, energia_generada=0, estado='En progreso'):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones_reducidas = emisiones_reducidas
        self.energia_generada = energia_generada
        self.estado = estado