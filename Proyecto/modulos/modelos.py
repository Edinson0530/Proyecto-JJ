class ProductoAlimento:
    def __init__(self, nombre, precio, descripcion, fecha_expiracion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.fecha_expiracion = fecha_expiracion

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - {self.descripcion} - Expira: {self.fecha_expiracion}"


class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre_producto):
        return self.productos.get(nombre_producto, None)

    def eliminar_producto(self, nombre_producto):
        if nombre_producto in self.productos:
            del self.productos[nombre_producto]

    def listar_productos(self):
        return [str(producto) for producto in self.productos.values()]


class Almacen:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.secciones = {}

    def agregar_seccion(self, nombre_seccion):
        self.secciones[nombre_seccion] = Seccion(nombre_seccion)

    def eliminar_seccion(self, nombre_seccion):
        if nombre_seccion in self.secciones:
            del self.secciones[nombre_seccion]

    def buscar_seccion(self, nombre_seccion):
        return self.secciones.get(nombre_seccion, None)

    def listar_secciones(self):
        return list(self.secciones.keys())

    def mover_producto(self, nombre_producto, seccion_origen, almacen_destino, seccion_destino):
        origen = self.buscar_seccion(seccion_origen)
        if not origen:
            return f"Error: La sección '{seccion_origen}' no existe en el almacén '{self.nombre}'."

        producto = origen.buscar_producto(nombre_producto)
        if not producto:
            return f"Error: El producto '{nombre_producto}' no está en la sección '{seccion_origen}'."

        destino = almacen_destino.buscar_seccion(seccion_destino)
        if not destino:
            return f"Error: La sección '{seccion_destino}' no existe en el almacén '{almacen_destino.nombre}'."

        origen.eliminar_producto(nombre_producto)
        destino.agregar_producto(producto)
        return f"El producto '{nombre_producto}' fue movido del almacén '{self.nombre}' al almacén '{almacen_destino.nombre}'."
