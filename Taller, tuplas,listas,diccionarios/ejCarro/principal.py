#Se importan todas las clases
from carro import Carro
from deportivo import Deportivo
from van import Van
from camion import Camion 
from base_datos import Base_Datos

#Se Crea la base de datos
db = Base_Datos()

#Se crea los datos
print("===AGREGANDO OBJETOS===")
carro1 = Carro("2008","azul")
carro2 = Deportivo("2024","negro","2 puertas")
carro3 = Van("2018","blanco","hibrido")
carro4 = Camion("2005","marron","diesel")

db.agregar(carro1)
db.agregar(carro2)
db.agregar(carro3)
db.agregar(carro4)

#Mostrar datos en las posicion 0

objeto = db.consultar(0)
objeto.ver_info()

#Se actualizan los datos del objeto en la posicion 0
print("\n===ACTUALIZANDO OBJETO EN LA POSICION 0===")
carro_nuevo = Carro("2026","rojo")
db.actualizar(0, carro_nuevo)

#Se elemina el objeto en la posicion 2 
print ("\n===ELEMINANDO OBJETO EN LA POSICION 2===")
db.eliminar(2)

#Se imprimen todos los datos
print("\n===TODOS LOS OBJETOS DE LA BASE DE DATOS===")
db.imprimir_todo()