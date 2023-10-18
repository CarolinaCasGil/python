
#Para una función que toma una lista de números como argumento y devuelve la suma de los números impares en la lista:
print( "Ej 1 ")
def suma_impares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 != 0:
            suma += num
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = suma_impares(numeros)
print(res)


#Para una función que toma una lista de números como argumento y devuelve una nueva lista con elementos únicos de la primera lista:
print( " ")
print("Ej 2 ")
def elementos_unicos(original):
    unicos = list(set(original)) #set elimina numeros duplicados
    return unicos

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
res = elementos_unicos(original)
print(res)


#Para una función que toma una lista y devuelve una nueva lista con elementos únicos de la primera lista, manteniendo el mismo orden:
print( " ")
print( "Ej 3 ")
def unicos(original):
    res = []
    for elemento in original:
        if elemento not in res:
            res.append(elemento)
    return res

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
res = unicos(original)
print(res)



#Para una función que toma una lista y devuelve una nueva lista con elementos únicos de la primera lista, manteniendo el mismo orden:
print( " ")
print( "Ej 4 ")
def impares(origi):
    res = []
    for elemento in origi:
        if elemento not in res:
            res.append(elemento) #append grega un elemento al final de la lista
    return res

origi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res= impares(origi)
print(res)



#Para una función que toma una lista de números como argumento y devuelve una nueva lista con solo los números impares de la lista original:
print( " ")
print( "Ej 5 ")
def impares(lista):
    res = [numero for numero in lista if numero % 2 != 0]
    return res

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = impares(lista)
print(res)


#Para una función que toma una lista de números como argumento y devuelve una nueva lista con solo los números primos de la lista original:
print( " ")
print( "Ej 6 ")
def primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def numeros_primos(lista):
    primos = [numero for numero in lista if primo(numero)]
    return primos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = numeros_primos(lista)
print(res)



#Para una función que toma una lista de números como argumento y devuelve una nueva lista con solo los números palindrómicos de la lista original:
print( " ")
print( "Ej 7 ")
def palindromo(num):
    num_str = str(num)
    return num_str == num_str[::-1] #aqui compara el mismo uemor dado la vuelta

def numeros_palindromicos(lista):
    res = [numero for numero in lista if palindromo(numero)]
    return res

lista = [1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 33, 44, 55, 66, 77, 88, 99, 101, 111, 252, 262, 292, 300, 301]
res = numeros_palindromicos(lista)
print(res)

