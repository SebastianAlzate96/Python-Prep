"1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es "

# In[1]:
def primo(num):
    es_primo = True
    if num == 2:
        es_primo = True
    elif num % 2 == 0:
        es_primo = False
    else:
        n=3
        while n < num:
            if num % n == 0:
                es_primo = False
                break
            else:
                n += 1
    return es_primo

primo(4)
#%%

"2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista"

# In[2]:
def primos_lista(lista):
    n = 0
    lista_primos = []
    while n < len(lista):
        if primo(lista[n]):
            lista_primos.append(lista[n])
        n += 1
    return lista_primos

a = list(range(2,20))
primos_lista(a)

#%%

"3) Crear una función que al recibir una lista de números,"
"devuelva el que más se repite y cuántas veces lo hace."
"Si hay más de un más repetido, que devuelva cualquiera"
# In[3]:
def rep_lista(lista):
    lista.sort()
    contador = []
    for i in range(0,len(lista)):
        contador.append(lista.count(lista[i]))

    new_lista = [lista[0]]
    new_cont = [contador[0]]
    for i in range(0,len(lista)-1):
        if lista[i] != lista[i+1]:
            new_lista.append(lista[i+1])
            new_cont.append(contador[i+1])

    maximo = max(new_cont)
    indice = new_cont.index(maximo)

    return "el numero " +str(new_lista[indice]) + " se repite " +str(maximo)



a = [3,3,3,3,2,1,1,1,3]
rep_lista(a)
# %%

"4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos."
# In[4]:

def rep_lista(lista, fun_):
    lista.sort()
    contador = []
    for i in range(0,len(lista)):
        contador.append(lista.count(lista[i]))

    new_lista = [lista[0]]
    new_cont = [contador[0]]
    for i in range(0,len(lista)-1):
        if lista[i] != lista[i+1]:
            new_lista.append(lista[i+1])
            new_cont.append(contador[i+1])

    maximo = fun_(new_cont)
    indice = new_cont.index(maximo)

    return "el numero " +str(new_lista[indice]) + " se repite " +str(maximo)



a = [3,3,3,3,2,1,1,1]
rep_lista(a, min)

# %%
