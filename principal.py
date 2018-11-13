
from metodos import *
e = EstPrecencial()
e.agregar_nombre("Luis")
e.agregar_apellido("Banitez")
e.agregar_ciclo(10)
e.agregar_id(10002)
e.agregar_num_creditos(100)
c1= Ciudad()
c1.agregar_nombre("Loja")
c1.agregar_poblacion(" 2000000")
e.agregarCiudad(c1)
print (e.presentar_datos())
