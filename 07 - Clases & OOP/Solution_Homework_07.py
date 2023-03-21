'''
1) Crear la clase vehículo que contenga los atributos:<br>
Color<br>
Si es moto, auto, camioneta ó camión<br>
Cilindrada del motor
'''

# In[1]:
class vehiculo:

    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje

'''
2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
Acelerar<br>
Frenar<br>
Doblar<br>
'''

# In[2]:

class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados

# %%

'''
3) Instanciar 3 objetos de la clase vehículo y 
ejecutar sus métodos, probar luego el resultado'''
# In[3]:

a1 = vehiculo('rojo', 'auto', 2)
a2 = vehiculo('blanco', 'camioneta', 3.6)
a3 = vehiculo('negro', 'moto', 1)

print(a3)

a1.Acelerar(40)
a2.Acelerar(60)
a3.Acelerar(30)
a1.Doblar(30)
a3.Doblar(-30)
a2.Frenar(-50)

print(a3)
# %%

'''
4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. 
Y otro método que muestre color, tipo y cilindrada
'''
# In[4]:

class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados

    def Estado(self):
        return "El vehiculo es de color: " +str(self.color)+ " y es de tipo: " +str(self.tipo)+ " y con cilindraje: " +str(self.cilindrada)
    
a = vehiculo("rojo", "camioneta", 12)
print(a.Estado())
# %%

'''
5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
Verificar Primo<br>
Valor modal<br>
Conversión grados<br>
Factorial<br>
'''
# In[5]:
class varios:

    def __init__(self) -> None:
        pass

    def primo(self, num):
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
    
    def rep_lista(self, lista, fun_):
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

        return new_lista[indice], maximo
    
    def conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero
    
"6) Probar las funciones incorporadas en la clase del punto 5"

v = varios()

v.primo(6)
v.factorial(6)

listado = [1,8,2,5,4,8,10,7]
v.rep_lista(listado, max)

v.conversion_grados(10, 'celsius', 'kelvin')
# %%

'''
7) Es necesario que la clase creada en el punto 5 contenga una lista, 
sobre la cual se aplquen las funciones incorporadas
'''

# In[7]:

class varios:

    def __init__(self, lista):
        self.lista = lista

    def __primo(self, num):
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
    
    def primo(self):
        lista2 = []
        for i in self.lista:
            if self.__primo(self.lista[i]):
                lista2.append(self.lista[i])
        return lista2
    
    def rep_lista(self, fun_):
        self.lista.sort()
        contador = []
        for i in range(0,len(self.lista)):
            contador.append(self.lista.count(self.lista[i]))

        new_lista = [self.lista[0]]
        new_cont = [contador[0]]
        for i in range(0,len(self.lista)-1):
            if self.lista[i] != self.lista[i+1]:
                new_lista.append(self.lista[i+1])
                new_cont.append(contador[i+1])

        maximo = fun_(new_cont)
        indice = new_cont.index(maximo)

        return new_lista[indice], maximo
    
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados de',origen, "son", 
                  self._conversion_grados(self.lista[i],origen,destino), 
                  "en", destino)

    
    def _conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def factorial(self):
        for i in self.lista:
            print("el factorial de "+str(self.lista[i])+" es "+str(self._factorial(self.lista[i])))

    def _factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self._factorial(numero - 1)
        return numero

lis = list(range(0,20))
v = varios(lis)
v.primo()
v.rep_lista(max)
v.conversion_grados('celsius','farenheit')
v.factorial()

# %%

'''
8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. 
\Luego realizar la importación del módulo y probar alguna de sus funciones
'''
# In[8]:

from varios import *
