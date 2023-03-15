"1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla"
name_city = ["Bogota","Caracas","Buenos aires", "Salvador", "Brazilia"]
print(name_city)

"2) Imprimir por pantalla el segundo elemento de la lista"
print(name_city[1])

"3) Imprimir por pantalla del segundo al cuarto elemento"
print(name_city[1:4])

"4) Visualizar el tipo de dato de la lista"
print(type(name_city))

"5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento"
print(name_city[2:])

"6) Visualizar los primeros 4 elementos de la lista"
print(name_city[:4])

"7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?"
name_city.append("Quito")
name_city.append("Bogota")

"8) Agregar otra ciudad, pero en la cuarta posición"
name_city.insert(4, "Lima")

"9) Concatenar otra lista a la ya creada"
name_country = ["Colombia", "venezuela", "Peru"]

name_city.extend(name_country)
print(name_city)

"10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?"
print(name_city.index("Bogota"))

"11) ¿Qué pasa si se busca un elemento que no existe?"
#print(name_city.index("New York"))

"12) Eliminar un elemento de la lista"
print(name_city.remove('Caracas'))


"13) ¿Qué pasa si el elemento a eliminar no existe?"
#print(name_city.remove("New York"))

"14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo"
eliminado = name_city.pop()
print(eliminado)

"15) Mostrar la lista multiplicada por 4"
print(name_city*4)

"16) Crear una tupla que contenga los números enteros del 1 al 20"
mi_tupla = list(range(1,21))
print(tuple(mi_tupla))

"17) Imprimir desde el índice 10 al 15 de la tupla"
print(mi_tupla[10:16])

"18) Evaluar si los números 20 y 30 están dentro de la tupla"
print(20 in mi_tupla)
print(30 in mi_tupla)

"19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido."
# In[1]:

city = "Bogota"
if (city in name_city):
    print(city, "esta en la lista de ciudades")
else:
    name_city.append(city)
    print(city, "Ha sido agregado a la lista de ciudades")

elemento = 'París'
if (not(elemento in name_city)):
    name_city.append(elemento)
    print('Se insertó el elemento', elemento)
else:
    print('El elemento', elemento, 'ya existía')

# %%

"20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista"
print(name_city.count("Bogota"))
print(mi_tupla.count(1))

"21) Convertir la tupla en una lista"
print(list(mi_tupla))

"22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables"
v1, v2, v3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = mi_tupla
print(v1)
print(v2)
print(v3)

"23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave ciudad. Agregar tambien otras claves, como puede ser Pais y Continente."

mi_diccionario = { "Ciudades": name_city,
                  "paises": name_country,
                  "Continente": ["America","Asia"]}

"24) Imprimir las claves del diccionario"
print(mi_diccionario.keys())

"25) Imprimir las ciudades a través de su clave"
print(mi_diccionario["Ciudades"])













# %%
