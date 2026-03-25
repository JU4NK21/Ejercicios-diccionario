from carro import Carro
class Camion(Carro):
  def __init__(self,modelo,color,combustible):
    super().__init__(modelo, color)
    self.combustible = combustible

  def get_combustible(self):
    return self.combustible

  def set_combustible(self,nuevo_dato):
    self.combustible = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"El tipo de combustible es: {self.combustible}")
