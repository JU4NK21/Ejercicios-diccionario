from animales import Animales
class Caballo(Animales):
  def __init__(self, dimension, edad, nombre):
    super().__init__(dimension, edad)
    self.nombre = nombre

  def get_nombre(self):
    return self.nombre

  def set_nombre(self, nuevo_dato):
    self.nombre = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"El nombre es: {self.nombre}")