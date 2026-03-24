from Botella import Botella
class Plastico(Botella):
  def __init__(self,material,forma,tapa):
    super().__init__(material, forma)
    self.tapa = tapa

  def get_tapa(self):
    return self.tapa

  def set_tapa(self,nuevo_dato):
    self.tapa = nuevo_dato

  def ver_info(self):
    super().ver_info()
    print(f"la tapa es: {self.tapa}")