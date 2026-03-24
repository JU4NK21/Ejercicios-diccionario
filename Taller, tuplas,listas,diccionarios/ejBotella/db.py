from Botella import Botella
from plastico import Plastico
from vidrio import Vidrio

class Base_datos:
    def __init__(self):
        self.almacen = []
        
    def agregar(self, objeto):
        self.almacen.append(objeto)
        print("Objeto agregado correctamente")
        
    def consultar(self, indice):
        return self.almacen[indice]
    
    def actualizar(self, indice, objeto_nuevo):
        self.almacen[indice] = objeto_nuevo
        print("Objeto actualizado correctamente")
        
    def eliminar(self, indice):
        self.almacen.pop(indice)
        print("Objeto eleminado correctamente")
        
    def imprimir_todo(self):
        for objeto in self.almacen:
            objeto.ver_info()
            print("----")