# Clases principales
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

# Diccionario global de almacenes
almacenes = {
    "A": Almacen("Almacén A", "Calle 1"),
    "B": Almacen("Almacén B", "Calle 2")
}

# Funciones auxiliares
def listar_secciones():
    nombre_almacen = input("Ingrese el almacén (A o B u otro): ").upper()
    almacen = almacenes.get(nombre_almacen)
    if almacen:
        print(f"Secciones en {almacen.nombre}: {almacen.listar_secciones()}")
    else:
        print("Almacén no encontrado.")

def agregar_seccion():
    nombre_almacen = input("Ingrese el almacén (A o B u otro): ").upper()
    nombre_seccion = input("Ingrese el nombre de la nueva sección: ")
    almacen = almacenes.get(nombre_almacen)
    if almacen:
        almacen.agregar_seccion(nombre_seccion)
        print(f"Sección '{nombre_seccion}' agregada al {almacen.nombre}.")
    else:
        print("Almacén no encontrado.")

def agregar_producto():
    nombre_almacen = input("Ingrese el almacén (A o B u otro): ").upper()
    nombre_seccion = input("Ingrese la sección: ")
    nombre_producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    descripcion = input("Descripción del producto: ")
    fecha_expiracion = input("Fecha de expiración (AAAA-MM-DD): ")

    almacen = almacenes.get(nombre_almacen)
    if almacen:
        seccion = almacen.buscar_seccion(nombre_seccion)
        if seccion:
            producto = ProductoAlimento(nombre_producto, precio, descripcion, fecha_expiracion)
            seccion.agregar_producto(producto)
            print(f"Producto '{nombre_producto}' agregado a la sección '{nombre_seccion}' en el {almacen.nombre}.")
        else:
            print(f"La sección '{nombre_seccion}' no existe en el {almacen.nombre}.")
    else:
        print("Almacén no encontrado.")

def mover_producto():
    origen = input("Almacén origen (A o B u otro): ").upper()
    destino = input("Almacén destino (A o B u otro): ").upper()
    seccion_origen = input("Sección origen: ")
    seccion_destino = input("Sección destino: ")
    nombre_producto = input("Nombre del producto: ")

    almacen_origen = almacenes.get(origen)
    almacen_destino = almacenes.get(destino)
    if almacen_origen and almacen_destino:
        resultado = almacen_origen.mover_producto(
            nombre_producto, seccion_origen, almacen_destino, seccion_destino
        )
        print(resultado)
    else:
        print("Uno de los almacenes especificados no existe.")

def agregar_almacen():
    nombre_almacen = input("Ingrese la letra o código del nuevo almacén: ").upper()
    nombre = input("Nombre del almacén: ")
    direccion = input("Dirección del almacén: ")

    if nombre_almacen in almacenes:
        print(f"El almacén con código '{nombre_almacen}' ya existe.")
    else:
        almacenes[nombre_almacen] = Almacen(nombre, direccion)
        print(f"Almacén '{nombre}' agregado con el código '{nombre_almacen}'.")

# Menú principal
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

# Ejecutar el menú interactivo
menu()
