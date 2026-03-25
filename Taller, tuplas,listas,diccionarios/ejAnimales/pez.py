from animales import Animales
class Pez(Animales):
  def __init__(self, dimension, edad, color):
    super().__init__(dimension, edad)
    self.color = color

  def get_color(self):
    return self.color

  def set_color(self, nuevo_dato):
    self.color = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"Su color es: {self.color}")