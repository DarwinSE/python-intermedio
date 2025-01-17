# Ejercicios con Expresiones Regulares

import re

# match

my_string = 'Esta es la leccion numero 7: Leccion Expresiones Regulares!'
my_other_string = 'Esta no es la leccion numero 6: Manejo de Ficheros!'

matched = re.match('Esta es la leccion', my_string, re.I)
print(matched)
print(matched.span())

start, end = matched.span()
print(my_string[start:end])

print(re.match('Expresiones', my_string))
print(re.match('Esta es la leccion', my_other_string))


# findall

finded = re.findall('numero (\d+)', my_string)
print(finded)

print(re.findall('numero (\d+)', my_other_string))

finded_all = re.findall('leccion', my_string, re.I)
print(finded_all)

# search

searched = re.search('numero', my_string, re.I)
print(searched)
start, end = searched.span()
print(my_string[start:end])


# split

print(re.split(':', my_string))


# sub

print(re.sub('leccion|Leccion', 'LECCION', my_string))
print(re.sub('[l|L]eccion', 'LECCION', my_string))


# Patrones

pattern = r'[a-f]'
print(re.findall(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].'
print(re.findall(pattern, my_string))

# Patron complejo

email = 'darwin@guerra.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))