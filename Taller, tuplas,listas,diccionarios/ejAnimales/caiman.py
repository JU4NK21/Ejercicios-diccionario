from animales import Animales
class Caiman(Animales):
  def __init__(self, dimension, edad, dieta):
    super().__init__(dimension, edad)
    self.dieta = dieta

  def get_dieta(self):
    return self.dieta

  def set_dieta(self, nuevo_dato):
    self.dieta = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"Su dieta es: {self.dieta}")