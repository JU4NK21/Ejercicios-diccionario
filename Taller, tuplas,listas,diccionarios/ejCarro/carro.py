class Carro:
  def __init__(self, modelo, color):
    self.modelo = modelo
    self.color = color

  def get_modelo(self):
    return self.modelo

  def set_modelo(self, nuevo_dato):
    self.modelo = nuevo_dato

  def crear_botella(self):
    info = f"Carro creado"
    return info

  def ver_info(self):
    print(f"El modelo es: {self.modelo}")
    print(f"El color es: {self.color}")
