from modelos import ProductoAlimento, Almacen

# Diccionario global de almacenes
almacenes = {
    "A": Almacen("Almacén A", "Calle 1"),
    "B": Almacen("Almacén B", "Calle 2")
}

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
