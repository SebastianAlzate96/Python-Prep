"1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero"
num = 0
if (num > 0):
    print(num," es positivo")
elif (num < 0):
    print(num, " es negativo")
else:
    print(num, " es igual a cero")

"2) Crear dos variables y un condicional que informe si son del mismo tipo de dato"
var_1 = True
var_2 = True

if type(var_1) == type(var_2):
    print("las variables son del mismo tipo")
    print('Las variables ' + str(var_1) + ' y ' + str(var_2) + ' son del mismo tipo de dato')
else:
    print("las variables no son del mismo tipo")

"3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar"
a= -2
if a % 2 == 0:
    print("El numero " + str(a) + " es par")
else:
    print("El numero " + str(a) + " es impar")

n=1
while n < 21:
    if n % 2 == 0:
        print("El numero " + str(n) + " es par")
    else:
        print("El numero " + str(n) + " es impar")
    n = n + 1

"4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3"
for i in range(0,6):
    print("El numero " + str(i) + " elevado a la 3 es igual a " + str(i**3))

"5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos"
n = 2
for i in range(0, n):
    print(i)

"6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0"
n = 5
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n > 2):
            n = n - 1
            factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')

numero = 5
factorial = 1
i = 1

while i <= numero:
    factorial *= i
    i += 1

print("El factorial de", numero, "es", factorial)

"7) Crear un ciclo for dentro de un ciclo while"

while n < 10:
    for i in range(0,n):
        a = i+a
    print(a)
    n += 1

n = 0
while(n < 5):
    for i in range(0,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))
    n += 1

"8) Crear un ciclo while dentro de un ciclo for"
for i in range(0,5):
    print("ciclo for #: ", i)
    n = i
    while n < 5:
        print("ciclo while #: ", n)
        n += 1

"9) Imprimir los números primos existentes entre 0 y 30"
ciclos_sin_break = 0
i=2
primo = True
tope = 100
while i < tope:
    n = 2
    while n < i:
        ciclos_sin_break += 1
        if (i % n == 0):
            primo  = False
        n += 1
    if (primo):
        print(i)
    else:
        primo = True
    i +=1

print('Cantidad de ciclos: ' + str(ciclos_sin_break))

"10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin"
ciclos_con_break = 0
i=2
primo = True
while i < tope:
    n = 2
    while n < i:
        ciclos_con_break += 1
        if (i % n == 0):
            primo  = False
            break
        n += 1
    if (primo):
        print(i)
    else:
        primo = True
    i +=1

print('Cantidad de ciclos: ' + str(ciclos_con_break))


"11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?"
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')

"12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?"
# Yes

"13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300"
# In[1]:
n=99
while n < 301:
    n += 1
    if (n % 12 != 0):
        continue
    print(n, "es divisible por 12")
# %%

"14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente"
# In[2]:
num = input("ingresar el numero: ")
num = int(num)

ciclos_con_break = 0
sigue = 1
primo = True
m=1

while (sigue == 1):
    n=2
    while n < num:
        ciclos_con_break += 1
        if (num % n == 0):
            #print(num, "no es primo")
            primo = False
            break
        n += 1
    if (primo):
        print(num, "es primo")
        print(input("desea encontrar el siguiente primo: "))
        if (input() != "1"):
            print("Gracias")
            break
    else:
        primo=True
    num += 1

# %%


"15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6"

# In[3]:
n=99
while (n < 301):
    n += 1
    if (n % 3 != 0):
        continue
    elif (n % 6 != 0):
        continue
    else:
        print(n, "es divisible por 3 y multiplo de 6")
        break

# %%
