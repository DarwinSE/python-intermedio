# Ejercicios con Tipos de Errores

# SyntaxError

#print 'Hola Mundo!' # Esto es un error de syntax
print('Hola Mundo!')


# NameError

# print(name) # Esto es un error de name por no estar declarada la variable
name = 'Lawi'
print(name)


# IndexError

my_list = ['Python', 'Java', 'C#']
# print(my_list[3]) El index esta fuera de rango
print(my_list[-1])


# ModuleNotFoundError
# import maths # Error al importar
import math

print(math.pi)


# AttributeError
# print(math.PI) # Error al llamar el atributo de pi
print(math.pi)


# KeyError

my_dict = {'Nombre': 'Darwin', 'Apellido': 'Guerra', 'Edad': 24}
print(my_dict['Edad'])
# print(my_dict['Eda']) # Error al llamar la clave


# TypeError

# print(my_list['Java']) # Error al llamar un atributo de una lista debido a que no soporta str
print(my_list[1])


# ImportError

# from math import PI # Error al llamar el modulo
from math import pi

print(pi)


# ValueError

my_int = int('10')
# my_int = int('10 años') # No se puede transformar a int
print(type(my_int))


# ZeroDivisionError

# print(10 / 0) # No se puede dividir entre 0
print(18 / 3)