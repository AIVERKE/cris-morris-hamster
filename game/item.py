class Item:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"


# Ejemplo de uso

"""
from game.item import Item

# Crear un item:
llave = Item(1, "Llave Dorada", "Abre la puerta del jardín secreto.")

# Agregarlo al inventario:
cris = ChrisMorris(idusuario=1)
cris.agregar_item(llave)

cris.mostrar_inventario()

"""
