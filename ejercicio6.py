class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                return
        print("El producto no se encontró en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)


# Crear un objeto Inventario
inventario = Inventario()

# Agregar productos al inventario
producto1 = Producto("001", "Camiseta", 15.99)
producto2 = Producto("002", "Pantalones", 29.99)
producto3 = Producto("003", "Zapatos", 49.99)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar el inventario
inventario.mostrar_inventario()

# Eliminar un producto del inventario
inventario.eliminar_producto("002")

# Mostrar el inventario actualizado
inventario.mostrar_inventario()
