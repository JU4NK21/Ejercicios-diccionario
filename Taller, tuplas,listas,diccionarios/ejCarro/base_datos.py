from carro import Carro
from deportivo import Deportivo
from van import Van
from camion import Camion 

class Base_Datos:
    def __init__(self):
        self.lista = []

    def agregar(self, objeto):
        self.lista.append(objeto)
        print("Objeto agregado correctamente")

    def consultar(self, indice):
        return self.lista[indice]

    def actualizar(self, indice, objeto_nuevo):
        self.lista[indice] = objeto_nuevo
        print("Objeto actualizado correctamente")

    def eliminar(self, indice):
        self.lista.pop(indice)
        print("Objeto eliminado correctamente")

    def imprimir_todo(self):
        for objeto in self.lista:
            objeto.ver_info()
            print("---")