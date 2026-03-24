from Botella import Botella
class Vidrio(Botella):
    def __init__(self, material, forma, cantidad):
        super().__init__(material, forma)
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nuevo_dato):
        self.cantidad = nuevo_dato

    def ver_info(self):
        super().ver_info()
        print(f"cantidad es : {self.cantidad}")
