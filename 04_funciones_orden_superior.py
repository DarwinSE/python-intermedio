# Ejercicios de Funciones de Orden Superior

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_numbers_and_add_value(first_number, second_number, f_sum):
    return f_sum(first_number + second_number)

print(sum_two_numbers_and_add_value(7, 1, sum_one))
print(sum_two_numbers_and_add_value(7, 1, sum_five))


# Closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(1))
print(sum_ten()(2))


# Funciones de Orden Superior Pre-existentes
numbers = [2, 3, 5, 7, 11, 13, 0, 17]

# Map
print(list(map(lambda number: number * 2, numbers)))
print(list(map(sum_five, numbers)))

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
from functools import reduce

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))