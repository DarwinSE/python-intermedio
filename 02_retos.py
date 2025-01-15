# Retos de Python

"""
FIZZ BUZZ
Escribe un programa que muestre con un print los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion),
sustituyendo los siguientes:
- Multiplos de 3 por la palabra 'fizz'
- Multiplos de 5 por la palabra 'buzz'
- Multiplos de 3 y 5 a la vez por la palabra 'fizzbuzz'
"""

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 5 == 0:
            print('buzz')
        else:
            print(number)    

fizzbuzz()


"""
ANAGRAMA
Escribe una funcion que reciba dos palabras (string) y retorne verdadero o falso segun sean o no anagramas
- Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial
- No hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagramas
"""

def anagram(firts_word, second_word):
    if firts_word.lower() == second_word.lower():
        return False
    elif sorted(firts_word.lower()) == sorted(second_word.lower()):
        return True
    else:
        return 'No es un Anagrama'
    
print(anagram('Amor', 'amoR'))
print(anagram('Amor', 'Roma'))


"""
SUCESION DE FIBONACCI
Escribe un programa que imprima los 50 primeros numeros de la sucesion de Fibonaccio empezando en 0
- La serie Fibonacci se compone por una sucesion de numeros en la que 
  el siguiente siempre es la suma de los dos anteriores 0, 1, 1, 2, 3, 5, 8, 13
"""

def fibonacci():
    prev = 0
    next = 1
    for i in range(50):
        number = prev + next
        prev = next
        next = number

        print(number)

fibonacci()


"""
NUMEROS PRIMOS
Escribe un programa que se encargue de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 100
"""

def prime_number():
    for number in range(1, 101):
        if number >= 2:
            divisible = False

            for i in range(2, number):
                if number % i == 0:
                    divisible = True
                    break
            
            if not divisible:
                print(number)

prime_number()


"""
DAR VUELTA A STRING
Crea un programa que invierta el orden de una cadena de texto sin usar fucniones propias del lenguaje
que lo hagan de forma automatica.
- Si le pasamos 'Hola Mundo', nos retornaria 'odnuM aloH'
"""

def reverse_string(str):
    str_len = len(str)
    reversed = ''

    for i in range(0, str_len):
        reversed += str[(str_len - 1) - i]

    return reversed

print(reverse_string('Hola Mundo'))