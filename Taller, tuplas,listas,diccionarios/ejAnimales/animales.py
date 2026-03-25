class Animales:
  def __init__(self, dimension, edad):
    self.dimension = dimension
    self.edad = edad

  def get_dimension(self):
    return self.dimension

  def set_dimension(self, nuevo_dato):
    self.dimension = nuevo_dato

  def crear_animal(self):
    info = f"Animal creado"
    return info

  def ver_info(self):
    print(f"El tamaño es: {self.dimension}")
    print(f"La edad es: {self.edad}")