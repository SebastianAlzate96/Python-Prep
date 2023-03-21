"1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1"
# In[1]:
lista = []
a = -1   # numero mayor
b = -15  # numero menor

for i in range(0,a-b+1):
    lista.append(b+i)
print(lista)
#%%

"2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?"
# In[2]:
n = 0
while n < len(list):
    if list[n] % 2 == 0:
        print(list[n])
    n += 1
# %%

"3) Resolver el punto anterior sin utilizar un ciclo while"
# In[3]:
for i in range(0,len(list)):
    if list[i] % 2 == 0:
        print(list[i])

#%%

"4) Utilizar el iterable para recorrer sólo los primeros 3 elementos"
# In[4]:
n = 0
while n < 3:
    elemento = list[n]
    print(elemento)
    n += 1
#%%

"5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento"
# In[5]:
for i, e in enumerate(list):
    print(i, e)
# %%

"6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]"
# In[6]:
lista = [1,2,5,7,8,10,13,14,15,17,20]
for i in range(0,lista[len(lista)-1]):
    if lista[i] == i+1:
        continue
    else:
        lista.insert(i,i+1)
print(lista)
# %%

"7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>"
"n<sub>0</sub> = 0<br>"
"n<sub>1</sub> = 1<br>"
"n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>"
"Crear una lista con los primeros treinta números de la sucesión.<br>"
# In[7]:
fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)
#%%

"8) Realizar la suma de todos elementos de la lista del punto anterior"
sum(fibo)

"9"
primeros = 15
n = primeros - 5
while(n < primeros):
    print(fibo[n]/fibo[n-1])
    n += 1

"10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra"
# In[10]:
frase = "Hola Mundo nn"
contador = 0
for i in frase:
    if i == "o":
        contador = contador + 1
print(contador)
#%%

"11) Crear un diccionario e imprimir sus claves utilizando un iterador"
# In[11]:
dicc = {  'Ciudad': ['Buenos Aires','Caracas','Bogotá','Lisboa','Roma'], 
'País': ['Argentina','Venezuela','Colombia','Portugal','Italia'], 
'Continente' : ['América','América','América','Europa','Europa']}
for i in dicc:
    print(i)

#%%

"12) Convertir en una lista la variable cadena del punto 10 y luego recorrerla con un iterador"
# In[12]:
frase = "Hola Mundo nn"
print(iter(list(frase)))
for elem in list(frase):
    print(elem)
#%%

"13) Crear dos listas y unirlas en una tupla utilizando la función zip"
# In[13]:
lista_1 = list(range(0,5))
lista_2 = list(range(5,10))

lista_3 = tuple(zip(lista_1,lista_2))
print(lista_3)
# %%

"14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>"
# In[14]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
divi_7 = []
for i in range(0,len(lis)):
    if lis[i] % 7 == 0:
        divi_7.append(lis[i])
print(divi_7)
#%%

"15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>"
"lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]"
# In[15]:
contador = 0
for i in range(0,len(lis)):
    if (type(lis[i])==list):
        contador = contador + len(lis[i])
    else:
        contador += 1

print(contador)
#%%

"16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es"

# In[16]:
for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)

print(lis)
#%%


