# Ejercicios con Lambda

sum_two_numbers = lambda first_number, second_number: first_number + second_number
print(sum_two_numbers(5, 10))

multiply_two_numbers = lambda first_number, second_number: first_number * second_number
print(multiply_two_numbers(2, 13))

def sum_three_values(value):
    return lambda first_number, second_number: first_number + second_number + value

print(sum_three_values(2)(3,5))