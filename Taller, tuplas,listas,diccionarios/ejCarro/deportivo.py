from carro import Carro
class Deportivo(Carro):
  def __init__(self,modelo,color,numero_puertas):
    super().__init__(modelo, color)
    self.numero_puertas = numero_puertas

  def get_numeropuertas(self):
    return self.numero_puertas

  def set_numeropuertas(self,nuevo_dato):
    self.numero_puertas = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"El numero de puertas son: {self.numero_puertas}")