#Se importan todas las Clases 
from animales import Animales
from caballo import Caballo
from caiman import Caiman
from escarabajo import Escarabajo
from pez import Pez
from pato import Pato
from db import Basededatos

#Se crea la base de datos
db = Basededatos()

#Se crean los datos de los objetos 

print("===AGREGANDO OBJETOS===")
animal1= Animales("grande", "5 años")
animal2= Caballo("mediano", "4 años", "Vicente")
animal3= Caiman("pequeño", "1 año", "carnivoro")
animal4= Escarabajo("pequeño", "6 meses", "selva tropical")
animal5= Pez("grande", "1 año", "multicolor")
animal6= Pato("mediano", "2 años", "omnivoro")

db.agregar(animal1)
db.agregar(animal2)
db.agregar(animal3)
db.agregar(animal4)
db.agregar(animal5)
db.agregar(animal6)

#Mostrar el objeto que esta en la posicion 0
print("\n===CONSULTANDO OBJETO QUE ESTA EN LA POSICION 0===")
objeto = db.consultar(0)
objeto.ver_info()

#Se actualizan el objeto que esta en la posicion 0
print("\n===ACTUALIZANDO OBJETO EN LA POSICION 0===")
animal_nuevo = Animales("grande", "10 años")
db.actualizar(0, animal_nuevo)

#Se elemina el objeto en la posicion 4
print("\n===ELEMINANDO OBJETO EN LA POSICION 4===")
db.eleminar(4)

#Se imprimen todos los objetos
print("\n===TODOS LOS OBJETOS DE LA BASE DE DATOS===")
db.imprimir_todo()