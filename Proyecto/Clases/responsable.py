class Responsable:
    def __init__(self, dni, nombre, apellido, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_info(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"
