# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# # Utilizar reduce con la función definida dentro del argumento lambda
# result = reduce(lambda acc, x: acc + x**2, numbers, 0)
# print(result)


# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Utilizar reduce para calcular el producto de los números pares
# result = reduce(lambda acc, x: acc * x if x % 2 == 0 else acc, numbers, 1)
# print(result)  # Salida esperada: 3840


# from functools import reduce

# words = ['Hello', ' ', 'World', '!']
# # Utilizar reduce para concatenar las cadenas
# result = reduce(lambda acc, x: acc + x, words, '')
# print(result)  # Salida esperada: 'Hello World!'


# from functools import reduce

# numbers = [10, 5, 8, 15, 3]
# # Utilizar reduce para encontrar el elemento máximo
# result = reduce(lambda acc, x: x if x > acc else acc, numbers)
# print(result)  # Salida esperada: 15


# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# # Utilizar reduce con una función de acumulador lambda para concatenar cadenas
# result = reduce(lambda acc, x: acc + str(x), numbers, '')
# print(result)  # Salida esperada: '12345'


# from functools import reduce

# def factorial(n):
#     # Use reduce to calculate the factorial of n
#     result = reduce(lambda x, y: x * y, range(1, n + 1), 1)
#     return result

# print(factorial(5))  # Expected output: 120


from functools import reduce

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Utilizar reduce para aplanar las listas anidadas
result = reduce(lambda acc, x: acc + x, nested_lists, [])
print(result)  # Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8]
