'''
1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera 
arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero 
¿qué pasa si se envía otro tipo de dato?
'''

# In[1]:

import sys

sys.path.append(r'/C:/Users/sebas/Documents/Henry/Python-Prep/07 - Clases & OOP/Herramientas.py')

import herramientas as h

#h1 = h.Herramientas('Hola')

h1 = h.Herramientas([2,3,5,6,2])
# %%

'''
2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, 
de no serlo, informar cuáles son los valores esperados.
'''
# In[2]
import importlib
importlib.reload(h)

h1 = h.Herramientas([2,3,5,6,2])
h1.conversion_grados(1,2)
h1.conversion_grados('celsius','farenheit')
# %%

'''
3) Importar el modulo "unittest" y crear los siguientes casos de pruebas 
sobre la clase utilizada en el punto 2<br>
Creacion del objeto incorrecta<br>
Creacion correcta del objeto<br>
Metodo valor_modal()<br>
'''

# In[3]:

import unittest

class ProbandoMiClase(unittest.TestCase):
    
    def test_crear_objeto1(self):
        param = 'hola'
        self.assertRaises(ValueError, h.Herramientas, param)
        #self.failUnlessRaises(ValueError, h.Herramientas, param)

    def test_crear_objeto2(self):
        param = [1,2,2,5]
        h1 = h.Herramientas(param)
        self.assertEqual(h1.lista, param)

    def test_valor_modal(self):
        lis = [1,2,1,3]
        h1 = h.Herramientas(lis)
        moda, veces = h1.valor_modal(False)
        moda = [moda]
        moda.append(veces)
        resultado = [1, 2]
        self.assertEqual(moda, resultado)

unittest.main(argv=[''], verbosity=2, exit=False)
# %%

'''
4) Probar una creación incorrecta y visualizar la salida del "raise"
'''
# In[4]:

h2 = h.Herramientas('algo')
# %%

'''
6) Agregar casos de pruebas para el método verifica_primos() realizando el 
cambio en la clase, para que devuelva una lista de True o False en función 
de que el elemento en la posisicón sea o no primo
'''
# In[6]:

class ProbandoMiClase2(unittest.TestCase):

    def test_verifica_primos1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        primos = h1.verifica_primo()
        primos_esperado = [True, True, False, False, True]
        self.assertEqual(primos, primos_esperado)

importlib.reload(h)

unittest.main(argv=[''], verbosity=2, exit=False)
# %%

'''
7) Agregar casos de pruebas para el método conversion_grados()
'''

# In[7]:

class ProbandoMiClase3(unittest.TestCase):

    def test_verifica_conversion1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        grados = h1.conversion_grados('celsius','farenheit')
        grados_esperado = [35.6, 37.4, 46.4, 50.0, 55.4]
        self.assertEqual(grados, grados_esperado)

importlib.reload(h)

unittest.main(argv=[''], verbosity=2, exit=False)
# %%

'''
8) Agregar casos de pruebas para el método factorial()
'''

# In[8]:

class ProbandoMiClase4(unittest.TestCase):

    def test_verifica_factorial(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        factorial = h1.factorial()
        factorial_esperado = [2, 6, 40320, 3628800, 6227020800]
        self.assertEqual(factorial, factorial_esperado)

importlib.reload(h)

unittest.main(argv=[''], verbosity=2, exit=False)
# %%
