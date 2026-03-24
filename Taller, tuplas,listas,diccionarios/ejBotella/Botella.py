class Botella:
    def __init__(self, material, forma):
        self.material = material
        self.forma = forma

    def get_material(self):
        return self.material

    def set_material(self, nuevo_dato):
        self.material = nuevo_dato

    def crear_botella(self):
        info = f"Botella creada"
        return info

    def ver_info(self):
        print(f"material es : {self.material}")
        print(f"la forma es : {self.forma}")