class CrisMorris:
    def __init__(self, idusuario):
        self.idusuario = idusuario
        self.coraje = 0
        self.afecto = 0
        self.alimento = 100
        self.inventario = []

    def agregar_item(self, item):
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario:
            print("Inventario Vacio")
        else:
            print("Inventario")
            for i, item in enumerate(self.inventario, 1):
                print(f"{i}. {item}")

    def modificar_coraje(self, cantidad):
        self.coraje += cantidad

    def modificar_afecto(self, cantidad):
        self.afecto += cantidad

    def mostrar_estado(self):
        print(f"Coraje: {self.coraje}")
        print(f"Afecto: {self.afecto}")
        print(f"Alimento: {self.alimento}")
        self.mostrar_inventario()
