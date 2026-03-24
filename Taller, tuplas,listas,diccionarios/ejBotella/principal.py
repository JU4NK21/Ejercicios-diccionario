from Botella import Botella
from plastico import Plastico
from vidrio import Vidrio
from db import Base_datos

#CODIGO PRINCIPAL

#CREAR LA BASE DE DATOS
db = Base_datos()

print("Agregando objetos")
botella1 = Botella("plastico", "cilindrica")
botella2 = Vidrio("vidrio", "cuadrada", "1L")
botella3 = Plastico("plastico", "ovalada", "roja")

db.agregar(botella1)
db.agregar(botella2)
db.agregar(botella3)

print("\nConsultando objeto en posicion 0")
objeto = db.consultar(0)
objeto.ver_info()

# Paso 5 - UPDATE
print("\n=== ACTUALIZANDO OBJETO EN POSICION 0 ===")
botella_nueva = Botella("aluminio", "rectangular")
db.actualizar(0, botella_nueva)

# Paso 6 - DELETE
print("\n=== ELIMINANDO OBJETO EN POSICION 2 ===")
db.eliminar(2)

# Paso 7 - IMPRIMIR TODO
print("\n=== TODOS LOS OBJETOS EN LA BASE DE DATOS ===")
db.imprimir_todo()