from carro import Carro
class Van(Carro):
  def __init__(self,modelo,color,motor):
    super().__init__(modelo, color)
    self.motor = motor

  def get_motor(self):
    return self.motor

  def set_motor(self,nuevo_dato):
    self.motor = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"El motor es: {self.motor}")