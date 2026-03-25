from animales import Animales
from caballo import Caballo 
from caiman import Caiman 
from pez import Pez
from escarabajo import Escarabajo
from pato import Pato

class Basededatos:
    def __init__(self):
        self.lista = []
        
    def agregar(self, objeto):
        self.lista.append(objeto)
        print("Objeto agregado correctamente")
        
    def consultar(self,indice):
        return self.lista[indice]
    
    def actualizar(self, indice, objeto_nuevo):
        self.lista[indice] = objeto_nuevo
        print("Objeto actualizado correctamente")
    
    def eleminar(self, indice):
        self.lista.pop(indice)
        print("Objeto eleminado correctamente")
        
    def imprimir_todo(self):
        for objeto in self.lista:
            objeto.ver_info()
            print("----")