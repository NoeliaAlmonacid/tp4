def separar(lista):
    
    pares = []
    impares = []

    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    pares.sort()
    impares.sort()

    return pares, impares

# Ejemplo de lista para probar la funcion:
numeros = [3, 7, 1, 9, 2, 8]
pares, impares = separar(numeros)
print("Números pares:", pares)
print("Números impares:", impares)
