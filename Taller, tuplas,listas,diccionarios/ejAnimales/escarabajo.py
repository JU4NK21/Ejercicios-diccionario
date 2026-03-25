from animales import Animales
class Escarabajo(Animales):
  def __init__(self, dimension, edad, habitat):
    super().__init__(dimension, edad)
    self.habitat = habitat

  def get_habitat(self):
    return self.habitat

  def set_habitat(self, nuevo_dato):
    self.habitat = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"Su habitat es: {self.habitat}")