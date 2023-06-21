'''
Encontrar elnúmero que falta en una matriz significa encontrar los números que faltan en la matriz de acuerso con el rango de valores dentro de la matriz, la mayoria dde las veces, la pregunta que obtinene en base a ente problema es como:
    - Dada una matriz que contienen un rango de números de 0 a n con un número pedido, encuentre el número que falta en la matriz de entrada.
Para encontrar el número que falta en una matriz, necesitamos iterar sobre la matriz de entrada y almacenar los números en otra matriz que no encontramos en la matriz de entrada mientras iteramos sobre ella, 
'''

def encontrar_nemro(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

lista_numeros = [1,2,3,4,6,7,8,9,11,14,16]
print(encontrar_nemro(lista_numeros)) # [5, 10, 12, 13, 15]